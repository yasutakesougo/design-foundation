from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable, Mapping, Sequence

MAX_BYTES = 512 * 1024
ALLOWED_OWNER = "yasutakesougo"
ALLOWED_REPO = "design-foundation"
ALLOWED_REPOSITORY = f"{ALLOWED_OWNER}/{ALLOWED_REPO}"
ALLOWED_HOSTS = {"api.github.com", "raw.githubusercontent.com"}
DERIVED_PACKET_FIELDS = {"ReviewId", "IdempotencyKey", "PacketSHA256"}
PACKET_REQUIRED = {
    "Workstream",
    "LifecycleIssue",
    "ReviewType",
    "ReviewedRepository",
    "ReviewedArtifactIdentity",
    "ReviewedBaselineOrHEAD",
    "DefinitionIdentity",
    "LockedScopeIdentity",
    "AcceptanceCriteriaIdentity",
    "AllowedInputs",
    "ExcludedInputs",
    "DeclaredAmbientContext",
    "ExpectedFindingsVisibility",
    "MutationAuthority",
    "CreatedFromReadback",
}
OUTPUT_REQUIRED = {
    "ReviewId",
    "PacketSHA256",
    "ReviewedArtifactIdentity",
    "ReviewedBaselineOrHEAD",
    "ObservedAmbientContext",
    "EvidenceUsed",
    "Findings",
    "P0",
    "P1",
    "P2",
    "UnsupportedOrUnverifiedItems",
    "Verdict",
    "Contamination",
    "ExcludedItemIntentionallyRetrieved",
    "ExcludedItemObserved",
    "MutationAttempted",
    "HumanGateInferredOrConsumed",
}
VERDICTS = {"PASS", "CORRECTION", "HOLD", "FAIL"}
CONTAMINATION = {"NONE", "POSSIBLE", "PRESENT", "UNKNOWN"}
TRI = {"YES", "NO", "UNKNOWN"}
POSITIVE_RECONCILIATION = "REVIEW_PREDICATE_SATISFIED__REEVALUATE_EXISTING_AUTHORITY"


class FRAError(RuntimeError):
    pass


class HoldError(FRAError):
    pass


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def packet_payload(packet: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in packet.items() if key not in DERIVED_PACKET_FIELDS}


def packet_sha256(packet: Mapping[str, Any]) -> str:
    return sha256_hex(canonical_json_bytes(packet_payload(packet)))


def _idempotency_preimage(payload: Mapping[str, Any], packet_hash: str) -> dict[str, Any]:
    return {
        "Workstream": payload["Workstream"],
        "ReviewType": payload["ReviewType"],
        "ReviewedArtifactIdentity": payload["ReviewedArtifactIdentity"],
        "ReviewedBaselineOrHEAD": payload["ReviewedBaselineOrHEAD"],
        "DefinitionIdentity": payload["DefinitionIdentity"],
        "LockedScopeIdentity": payload["LockedScopeIdentity"],
        "PacketSHA256": packet_hash,
    }


def idempotency_key(payload: Mapping[str, Any], packet_hash: str) -> str:
    return sha256_hex(canonical_json_bytes(_idempotency_preimage(payload, packet_hash)))


def review_id_from_key(key: str) -> str:
    return f"fra-{key[:24]}"


def validate_packet_shape(payload: Mapping[str, Any]) -> None:
    missing = sorted(PACKET_REQUIRED.difference(payload))
    if missing:
        raise HoldError(f"MISSING_PACKET_FIELDS:{','.join(missing)}")
    if payload.get("ReviewedRepository") != ALLOWED_REPOSITORY:
        raise HoldError("REPOSITORY_NOT_ALLOWED")
    if payload.get("ExpectedFindingsVisibility") != "HIDDEN":
        raise HoldError("EXPECTED_FINDINGS_VISIBILITY_MUST_BE_HIDDEN")
    if payload.get("MutationAuthority") != "NONE":
        raise HoldError("MUTATION_AUTHORITY_MUST_BE_NONE")
    if not payload.get("ReviewedBaselineOrHEAD"):
        raise HoldError("MISSING_REVIEWED_BASELINE_OR_HEAD")
    for field in ("DefinitionIdentity", "LockedScopeIdentity", "AcceptanceCriteriaIdentity"):
        if not payload.get(field):
            raise HoldError(f"MISSING_REQUIRED_EVIDENCE_IDENTITY:{field}")
    if not isinstance(payload.get("AllowedInputs"), list) or not isinstance(payload.get("ExcludedInputs"), list):
        raise HoldError("INPUT_BOUNDARIES_MUST_BE_ARRAYS")


def _validate_repo_url(url: str) -> urllib.parse.SplitResult:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https":
        raise HoldError("HTTPS_REQUIRED")
    if parsed.hostname not in ALLOWED_HOSTS:
        raise HoldError("HOST_NOT_ALLOWED")
    if parsed.username or parsed.password or parsed.port not in (None, 443):
        raise HoldError("URL_AUTH_OR_PORT_NOT_ALLOWED")
    parts = [urllib.parse.unquote(p) for p in parsed.path.split("/") if p]
    if parsed.hostname == "api.github.com":
        if len(parts) < 3 or parts[0] != "repos" or parts[1] != ALLOWED_OWNER or parts[2] != ALLOWED_REPO:
            raise HoldError("REPOSITORY_PATH_NOT_ALLOWED")
    elif parsed.hostname == "raw.githubusercontent.com":
        if len(parts) < 3 or parts[0] != ALLOWED_OWNER or parts[1] != ALLOWED_REPO:
            raise HoldError("REPOSITORY_PATH_NOT_ALLOWED")
    return parsed


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req: Any, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> None:
        return None


class FreshGitHubReader:
    def __init__(self, opener: Any | None = None):
        self._opener = opener or urllib.request.build_opener(_NoRedirect())

    def get(self, url: str) -> bytes:
        _validate_repo_url(url)
        request = urllib.request.Request(url, method="GET", headers={"Accept": "application/vnd.github+json"})
        try:
            response = self._opener.open(request, timeout=30)
        except urllib.error.HTTPError as exc:
            if 300 <= exc.code < 400:
                raise HoldError("REDIRECT_NOT_ALLOWED") from exc
            raise HoldError(f"GITHUB_READ_FAILED:{exc.code}") from exc
        status = getattr(response, "status", getattr(response, "code", 200))
        if 300 <= int(status) < 400:
            raise HoldError("REDIRECT_NOT_ALLOWED")
        if int(status) != 200:
            raise HoldError(f"GITHUB_READ_FAILED:{status}")
        return response.read(MAX_BYTES + 1)


def extract_readback_identity(raw: bytes) -> str:
    if len(raw) > MAX_BYTES:
        raise HoldError("READBACK_TOO_LARGE")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise HoldError("READBACK_MALFORMED") from exc
    candidates = [
        data.get("sha") if isinstance(data, dict) else None,
        data.get("commit", {}).get("sha") if isinstance(data, dict) and isinstance(data.get("commit"), dict) else None,
        data.get("head", {}).get("sha") if isinstance(data, dict) and isinstance(data.get("head"), dict) else None,
    ]
    for candidate in candidates:
        if isinstance(candidate, str) and candidate:
            return candidate
    raise HoldError("READBACK_IDENTITY_NOT_FOUND")


def build_packet(payload: Mapping[str, Any], read_url: str, reader: Any | None = None) -> dict[str, Any]:
    material = dict(payload)
    for derived in DERIVED_PACKET_FIELDS:
        material.pop(derived, None)
    validate_packet_shape(material)
    reader = reader or FreshGitHubReader()
    observed = extract_readback_identity(reader.get(read_url))
    if observed != material["ReviewedBaselineOrHEAD"]:
        raise HoldError("BASELINE_OR_HEAD_MISMATCH")
    material["CreatedFromReadback"] = dict(material.get("CreatedFromReadback") or {})
    material["CreatedFromReadback"]["ObservedIdentity"] = observed
    material["CreatedFromReadback"]["ReadURL"] = read_url
    payload_bytes = canonical_json_bytes(material)
    if len(payload_bytes) > MAX_BYTES:
        raise HoldError("PACKET_TOO_LARGE")
    packet_hash = sha256_hex(payload_bytes)
    key = idempotency_key(material, packet_hash)
    final = dict(material)
    final["ReviewId"] = review_id_from_key(key)
    final["IdempotencyKey"] = key
    final["PacketSHA256"] = packet_hash
    verify_packet(final)
    return final


def verify_packet(packet: Mapping[str, Any]) -> None:
    validate_packet_shape(packet)
    expected = packet_sha256(packet)
    if packet.get("PacketSHA256") != expected:
        raise HoldError("PACKET_SHA256_MISMATCH")
    expected_key = idempotency_key(packet_payload(packet), expected)
    if packet.get("IdempotencyKey") != expected_key:
        raise HoldError("IDEMPOTENCY_KEY_MISMATCH")
    if packet.get("ReviewId") != review_id_from_key(expected_key):
        raise HoldError("REVIEW_ID_DERIVATION_MISMATCH")
    if len(canonical_json_bytes(dict(packet))) > MAX_BYTES:
        raise HoldError("PACKET_TOO_LARGE")


def _require_int_count(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise HoldError(f"MALFORMED_SEVERITY_COUNT:{name}")
    return value


@dataclass(frozen=True)
class ValidatedReviewerOutput:
    parsed: dict[str, Any]
    raw: bytes
    sha256: str


def validate_reviewer_output(raw: bytes, packet: Mapping[str, Any], independence_required: bool = True) -> ValidatedReviewerOutput:
    verify_packet(packet)
    if len(raw) > MAX_BYTES:
        raise HoldError("REVIEWER_OUTPUT_TOO_LARGE")
    try:
        parsed = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise HoldError("MALFORMED_REVIEWER_OUTPUT") from exc
    if not isinstance(parsed, dict):
        raise HoldError("REVIEWER_OUTPUT_MUST_BE_OBJECT")
    missing = sorted(OUTPUT_REQUIRED.difference(parsed))
    if missing:
        raise HoldError(f"MISSING_OUTPUT_FIELDS:{','.join(missing)}")
    if parsed["ReviewId"] != packet["ReviewId"]:
        raise HoldError("REVIEW_ID_MISMATCH")
    if parsed["PacketSHA256"] != packet["PacketSHA256"]:
        raise HoldError("PACKET_SHA256_MISMATCH")
    if parsed["ReviewedArtifactIdentity"] != packet["ReviewedArtifactIdentity"]:
        raise HoldError("REVIEWED_ARTIFACT_IDENTITY_MISMATCH")
    if parsed["ReviewedBaselineOrHEAD"] != packet["ReviewedBaselineOrHEAD"]:
        raise HoldError("REVIEWED_BASELINE_OR_HEAD_MISMATCH")
    p0 = _require_int_count(parsed["P0"], "P0")
    p1 = _require_int_count(parsed["P1"], "P1")
    _require_int_count(parsed["P2"], "P2")
    if parsed["Verdict"] not in VERDICTS:
        raise HoldError("INVALID_VERDICT")
    if parsed["Contamination"] not in CONTAMINATION:
        raise HoldError("INVALID_CONTAMINATION")
    if parsed["ExcludedItemIntentionallyRetrieved"] not in TRI:
        raise HoldError("INVALID_EXCLUDED_RETRIEVAL")
    if parsed["ExcludedItemObserved"] not in TRI:
        raise HoldError("INVALID_EXCLUDED_OBSERVED")
    if parsed["MutationAttempted"] not in {"YES", "NO"}:
        raise HoldError("INVALID_MUTATION_ATTEMPTED")
    if parsed["HumanGateInferredOrConsumed"] not in {"YES", "NO"}:
        raise HoldError("INVALID_HUMAN_GATE_FIELD")
    if parsed["MutationAttempted"] != "NO":
        raise HoldError("MUTATION_ATTEMPTED")
    if parsed["HumanGateInferredOrConsumed"] != "NO":
        raise HoldError("HUMAN_GATE_INFERRED_OR_CONSUMED")
    if parsed["Contamination"] == "PRESENT":
        raise HoldError("CONTAMINATION_PRESENT")
    if parsed["Verdict"] == "PASS":
        if p0 > 0 or p1 > 0:
            raise HoldError("PASS_WITH_BLOCKING_FINDINGS")
        if parsed["ExcludedItemIntentionallyRetrieved"] != "NO":
            raise HoldError("PASS_WITH_EXCLUDED_RETRIEVAL")
        if independence_required:
            if parsed["Contamination"] != "NONE":
                raise HoldError("INDEPENDENT_PASS_REQUIRES_CONTAMINATION_NONE")
            if parsed["ExcludedItemObserved"] != "NO":
                raise HoldError("INDEPENDENT_PASS_REQUIRES_EXCLUDED_OBSERVED_NO")
    return ValidatedReviewerOutput(parsed=parsed, raw=raw, sha256=sha256_hex(raw))


def build_relay_envelope(
    packet: Mapping[str, Any],
    validated: ValidatedReviewerOutput,
    target_evidence_location: str,
    created_at: str | None = None,
) -> dict[str, Any]:
    verify_packet(packet)
    if sha256_hex(validated.raw) != validated.sha256:
        raise HoldError("REVIEWER_OUTPUT_HASH_MISMATCH")
    encoded = base64.b64encode(validated.raw).decode("ascii")
    envelope = {
        "ReviewId": packet["ReviewId"],
        "PacketSHA256": packet["PacketSHA256"],
        "ReviewerOutputSHA256": validated.sha256,
        "TargetEvidenceLocation": target_evidence_location,
        "ReviewedBaselineOrHEAD": packet["ReviewedBaselineOrHEAD"],
        "ReviewerOutputEncoding": "base64",
        "ReviewerOutputBytes": encoded,
        "RelayCreatedAt": created_at or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "RelayMutationAuthority": "NONE",
    }
    decoded = base64.b64decode(envelope["ReviewerOutputBytes"], validate=True)
    if decoded != validated.raw or sha256_hex(decoded) != envelope["ReviewerOutputSHA256"]:
        raise HoldError("RELAY_ROUNDTRIP_FAILED")
    return envelope


def _child_environment(packet: Mapping[str, Any], additional_names: Sequence[str] = ()) -> dict[str, str]:
    allowed = {"PATH", "HOME", "TMPDIR", "TEMP", "LANG", "LC_ALL"}.union(additional_names)
    env = {key: os.environ[key] for key in allowed if key in os.environ}
    env["FRA_REVIEWER_CONTEXT"] = "1"
    env["FRA_REVIEW_ID"] = str(packet["ReviewId"])
    env["FRA_PACKET_SHA256"] = str(packet["PacketSHA256"])
    return env


class ReviewerCoordinator:
    def __init__(self, state_dir: str | os.PathLike[str] | None = None):
        self._lock = threading.Lock()
        self._active_key: str | None = None
        self._completed: dict[str, dict[str, Any]] = {}
        self._state_dir = pathlib.Path(state_dir) if state_dir else None
        if self._state_dir:
            self._state_dir.mkdir(parents=True, exist_ok=True)

    def invoke(
        self,
        packet: Mapping[str, Any],
        argv: Sequence[str],
        *,
        timeout_seconds: float = 1200,
        additional_env: Sequence[str] = (),
        independence_required: bool = True,
    ) -> dict[str, Any]:
        verify_packet(packet)
        if os.environ.get("FRA_DISABLE") == "1":
            raise HoldError("FRA_DISABLE")
        if os.environ.get("FRA_REVIEWER_CONTEXT") == "1":
            raise HoldError("NESTED_REVIEWER_INVOCATION_PROHIBITED")
        if not argv:
            raise HoldError("REVIEWER_ARGV_REQUIRED")
        if timeout_seconds <= 0 or timeout_seconds > 1200:
            raise HoldError("TIMEOUT_OUT_OF_RANGE")
        key = str(packet["IdempotencyKey"])
        with self._lock:
            if key in self._completed:
                return dict(self._completed[key])
            if self._active_key == key:
                raise HoldError("DUPLICATE")
            if self._active_key is not None:
                raise HoldError("BUSY")
            self._active_key = key
        try:
            env = _child_environment(packet, additional_env)
            proc = subprocess.Popen(
                list(argv),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=False,
                env=env,
            )
            packet_bytes = canonical_json_bytes(dict(packet))
            try:
                stdout, stderr = proc.communicate(packet_bytes, timeout=timeout_seconds)
            except subprocess.TimeoutExpired as exc:
                proc.kill()
                proc.communicate()
                raise HoldError("REVIEWER_TIMEOUT") from exc
            if len(stdout) > MAX_BYTES:
                raise HoldError("REVIEWER_OUTPUT_TOO_LARGE")
            if proc.returncode != 0:
                diagnostic = stderr.decode("utf-8", errors="replace")[:1000]
                raise HoldError(f"REVIEWER_NONZERO_EXIT:{proc.returncode}:{diagnostic}")
            validated = validate_reviewer_output(stdout, packet, independence_required=independence_required)
            result = {
                "RunIdentity": packet["ReviewId"],
                "ReviewerOutputSHA256": validated.sha256,
                "Validated": validated,
            }
            with self._lock:
                self._completed[key] = result
            if self._state_dir:
                state = {
                    "RunIdentity": packet["ReviewId"],
                    "IdempotencyKey": key,
                    "ReviewerOutputSHA256": validated.sha256,
                }
                (self._state_dir / f"{key}.json").write_bytes(canonical_json_bytes(state))
            return dict(result)
        finally:
            with self._lock:
                if self._active_key == key:
                    self._active_key = None


def reconcile(
    packet: Mapping[str, Any],
    validated: ValidatedReviewerOutput,
    read_url: str,
    *,
    current_scope_identity: str,
    required_human_authority_identity: str | None,
    supplied_human_authority_identity: str | None,
    reader: Any | None = None,
) -> str:
    verify_packet(packet)
    if packet.get("LockedScopeIdentity") != current_scope_identity:
        raise HoldError("CURRENT_SCOPE_IDENTITY_MISMATCH")
    if required_human_authority_identity is not None:
        if supplied_human_authority_identity != required_human_authority_identity:
            raise HoldError("HUMAN_AUTHORITY_IDENTITY_MISMATCH")
    if sha256_hex(validated.raw) != validated.sha256:
        raise HoldError("REVIEWER_OUTPUT_HASH_MISMATCH")
    parsed = validated.parsed
    validate_reviewer_output(validated.raw, packet, independence_required=True)
    if parsed["Verdict"] != "PASS" or parsed["P0"] != 0 or parsed["P1"] != 0:
        raise HoldError("REVIEW_PREDICATE_NOT_SATISFIED")
    reader = reader or FreshGitHubReader()
    observed = extract_readback_identity(reader.get(read_url))
    if observed != packet["ReviewedBaselineOrHEAD"]:
        raise HoldError("FRESH_READ_MISMATCH")
    return POSITIVE_RECONCILIATION


def _read_json(path: str) -> Any:
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))


def _write_json(value: Any, path: str | None) -> None:
    data = canonical_json_bytes(value) + b"\n"
    if path:
        pathlib.Path(path).write_bytes(data)
    else:
        sys.stdout.buffer.write(data)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="fresh-review-automation-v1")
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build-packet")
    build.add_argument("--payload", required=True)
    build.add_argument("--read-url", required=True)
    build.add_argument("--output")

    validate = sub.add_parser("validate-output")
    validate.add_argument("--packet", required=True)
    validate.add_argument("--reviewer-output", required=True)
    validate.add_argument("--output")

    relay = sub.add_parser("build-relay")
    relay.add_argument("--packet", required=True)
    relay.add_argument("--reviewer-output", required=True)
    relay.add_argument("--target-evidence-location", required=True)
    relay.add_argument("--output")

    args = parser.parse_args(argv)
    try:
        if args.command == "build-packet":
            packet = build_packet(_read_json(args.payload), args.read_url)
            _write_json(packet, args.output)
        elif args.command == "validate-output":
            packet = _read_json(args.packet)
            raw = pathlib.Path(args.reviewer_output).read_bytes()
            result = validate_reviewer_output(raw, packet)
            _write_json({"ReviewerOutputSHA256": result.sha256, "Verdict": result.parsed["Verdict"]}, args.output)
        elif args.command == "build-relay":
            packet = _read_json(args.packet)
            raw = pathlib.Path(args.reviewer_output).read_bytes()
            validated = validate_reviewer_output(raw, packet)
            envelope = build_relay_envelope(packet, validated, args.target_evidence_location)
            _write_json(envelope, args.output)
        return 0
    except FRAError as exc:
        sys.stderr.write(f"HOLD: {exc}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

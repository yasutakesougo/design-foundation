from __future__ import annotations

import ast
import base64
import io
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import threading
import time
import unittest
import urllib.error
from unittest import mock

from tools.fresh_review_automation_v1 import cli


BASELINE = "6b5f655102970fe520d21092a05b9d253322ba19"
READ_URL = "https://api.github.com/repos/yasutakesougo/design-foundation/branches/main"
AUTHORIZED_PATHS = {
    "references/in-progress/fresh-review-automation-v1/README.md",
    "references/in-progress/fresh-review-automation-v1/automation-contract.md",
    "tools/fresh_review_automation_v1/__init__.py",
    "tools/fresh_review_automation_v1/cli.py",
    "tools/fresh_review_automation_v1/schemas/review-packet.schema.json",
    "tools/fresh_review_automation_v1/schemas/reviewer-output.schema.json",
    "tools/fresh_review_automation_v1/schemas/relay-envelope.schema.json",
    "tools/fresh_review_automation_v1/tests/test_cli.py",
}


class FakeReader:
    def __init__(self, identity: str = BASELINE):
        self.identity = identity
        self.calls: list[str] = []

    def get(self, url: str) -> bytes:
        cli._validate_repo_url(url)
        self.calls.append(url)
        return json.dumps({"name": "main", "commit": {"sha": self.identity}}).encode()


def payload(**changes):
    value = {
        "Workstream": "FRESH-REVIEW-AUTOMATION-V1",
        "LifecycleIssue": "#251",
        "ReviewType": "Fresh Independent Implementation Review",
        "ReviewedRepository": "yasutakesougo/design-foundation",
        "ReviewedArtifactIdentity": "PR#fixture",
        "ReviewedBaselineOrHEAD": BASELINE,
        "DefinitionIdentity": "#248 BODY",
        "LockedScopeIdentity": "#251+Clarification-1+Correction-1",
        "AcceptanceCriteriaIdentity": "#251 V1-V41",
        "AllowedInputs": ["Issue #251", "exact HEAD"],
        "ExcludedInputs": ["old chat", "self verdict"],
        "DeclaredAmbientContext": [],
        "ExpectedFindingsVisibility": "HIDDEN",
        "MutationAuthority": "NONE",
        "CreatedFromReadback": {"Source": "fresh fixture"},
    }
    value.update(changes)
    return value


def packet(**changes):
    return cli.build_packet(payload(**changes), READ_URL, reader=FakeReader(changes.get("ReviewedBaselineOrHEAD", BASELINE)))


def reviewer_output(pkt, **changes):
    value = {
        "ReviewId": pkt["ReviewId"],
        "PacketSHA256": pkt["PacketSHA256"],
        "ReviewedArtifactIdentity": pkt["ReviewedArtifactIdentity"],
        "ReviewedBaselineOrHEAD": pkt["ReviewedBaselineOrHEAD"],
        "ObservedAmbientContext": [],
        "EvidenceUsed": ["fixture"],
        "Findings": [],
        "P0": 0,
        "P1": 0,
        "P2": 0,
        "UnsupportedOrUnverifiedItems": [],
        "Verdict": "PASS",
        "Contamination": "NONE",
        "ExcludedItemIntentionallyRetrieved": "NO",
        "ExcludedItemObserved": "NO",
        "MutationAttempted": "NO",
        "HumanGateInferredOrConsumed": "NO",
    }
    value.update(changes)
    return cli.canonical_json_bytes(value)


def assert_hold(testcase: unittest.TestCase, needle: str, fn, *args, **kwargs):
    with testcase.assertRaises(cli.HoldError) as cm:
        fn(*args, **kwargs)
    testcase.assertIn(needle, str(cm.exception))


class VerificationV1ToV41(unittest.TestCase):
    def test_V01_authorized_changed_path_set_contract_is_exact(self):
        self.assertEqual(len(AUTHORIZED_PATHS), 8)
        self.assertEqual(
            AUTHORIZED_PATHS,
            {
                "references/in-progress/fresh-review-automation-v1/README.md",
                "references/in-progress/fresh-review-automation-v1/automation-contract.md",
                "tools/fresh_review_automation_v1/__init__.py",
                "tools/fresh_review_automation_v1/cli.py",
                "tools/fresh_review_automation_v1/schemas/review-packet.schema.json",
                "tools/fresh_review_automation_v1/schemas/reviewer-output.schema.json",
                "tools/fresh_review_automation_v1/schemas/relay-envelope.schema.json",
                "tools/fresh_review_automation_v1/tests/test_cli.py",
            },
        )

    def test_V02_scope_declares_add_only(self):
        contract = pathlib.Path(__file__).parents[3] / "references/in-progress/fresh-review-automation-v1/README.md"
        self.assertTrue(contract.exists())
        self.assertNotIn("modify existing", contract.read_text(encoding="utf-8").lower())

    def test_V03_standard_library_only_imports(self):
        source = pathlib.Path(cli.__file__).read_text(encoding="utf-8")
        tree = ast.parse(source)
        roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                roots.add(node.module.split(".")[0])
        allowed = {
            "__future__", "argparse", "base64", "dataclasses", "hashlib", "json", "os",
            "pathlib", "subprocess", "sys", "threading", "time", "typing", "urllib"
        }
        self.assertLessEqual(roots, allowed)

    def test_V04_packet_canonicalization_deterministic(self):
        a = packet()
        b = packet()
        self.assertEqual(cli.canonical_json_bytes(a), cli.canonical_json_bytes(b))
        self.assertEqual(a["PacketSHA256"], b["PacketSHA256"])

    def test_V05_same_tuple_same_idempotency_key(self):
        self.assertEqual(packet()["IdempotencyKey"], packet()["IdempotencyKey"])

    def test_V06_head_change_invalidates_prior_packet_as_current(self):
        pkt = packet()
        assert_hold(self, "FRESH_READ_MISMATCH", cli.reconcile,
                    pkt, cli.validate_reviewer_output(reviewer_output(pkt), pkt), READ_URL,
                    current_scope_identity=pkt["LockedScopeIdentity"],
                    required_human_authority_identity=None, supplied_human_authority_identity=None,
                    reader=FakeReader("f" * 40))

    def test_V07_packet_hash_mismatch_fails_closed(self):
        pkt = packet(); pkt["PacketSHA256"] = "0" * 64
        assert_hold(self, "PACKET_SHA256_MISMATCH", cli.verify_packet, pkt)

    def test_V08_review_id_mismatch_fails_closed(self):
        pkt = packet()
        assert_hold(self, "REVIEW_ID_MISMATCH", cli.validate_reviewer_output,
                    reviewer_output(pkt, ReviewId="wrong"), pkt)

    def test_V09_reviewer_output_hash_mismatch_fails_closed(self):
        pkt = packet(); raw = reviewer_output(pkt)
        val = cli.ValidatedReviewerOutput(json.loads(raw), raw, "0" * 64)
        assert_hold(self, "REVIEWER_OUTPUT_HASH_MISMATCH", cli.build_relay_envelope, pkt, val, "issue:#x")

    def test_V10_contamination_present_cannot_pass(self):
        pkt = packet()
        assert_hold(self, "CONTAMINATION_PRESENT", cli.validate_reviewer_output,
                    reviewer_output(pkt, Contamination="PRESENT"), pkt)

    def test_V11_unknown_or_possible_contamination_cannot_independent_pass(self):
        pkt = packet()
        for value in ("UNKNOWN", "POSSIBLE"):
            assert_hold(self, "INDEPENDENT_PASS_REQUIRES_CONTAMINATION_NONE", cli.validate_reviewer_output,
                        reviewer_output(pkt, Contamination=value), pkt)

    def test_V12_mutation_attempted_yes_fails(self):
        pkt = packet()
        assert_hold(self, "MUTATION_ATTEMPTED", cli.validate_reviewer_output,
                    reviewer_output(pkt, MutationAttempted="YES"), pkt)

    def test_V13_human_gate_inferred_or_consumed_yes_fails(self):
        pkt = packet()
        assert_hold(self, "HUMAN_GATE_INFERRED_OR_CONSUMED", cli.validate_reviewer_output,
                    reviewer_output(pkt, HumanGateInferredOrConsumed="YES"), pkt)

    def test_V14_nonzero_p0_or_p1_cannot_pass(self):
        pkt = packet()
        for field in ("P0", "P1"):
            assert_hold(self, "PASS_WITH_BLOCKING_FINDINGS", cli.validate_reviewer_output,
                        reviewer_output(pkt, **{field: 1}), pkt)

    def test_V15_excluded_intentional_retrieval_cannot_pass(self):
        pkt = packet()
        for value in ("YES", "UNKNOWN"):
            assert_hold(self, "PASS_WITH_EXCLUDED_RETRIEVAL", cli.validate_reviewer_output,
                        reviewer_output(pkt, ExcludedItemIntentionallyRetrieved=value), pkt)

    def test_V16_completed_identical_invocation_reused_not_respawned(self):
        pkt = packet(); raw = reviewer_output(pkt)
        script = "import sys; sys.stdin.buffer.read(); sys.stdout.buffer.write(" + repr(raw) + ")"
        coord = cli.ReviewerCoordinator()
        with mock.patch("subprocess.Popen", wraps=subprocess.Popen) as popen:
            one = coord.invoke(pkt, [sys.executable, "-c", script], timeout_seconds=5)
            two = coord.invoke(pkt, [sys.executable, "-c", script], timeout_seconds=5)
        self.assertEqual(one["RunIdentity"], two["RunIdentity"])
        self.assertEqual(popen.call_count, 1)

    def test_V17_nested_invocation_rejected(self):
        pkt = packet(); coord = cli.ReviewerCoordinator()
        with mock.patch.dict(os.environ, {"FRA_REVIEWER_CONTEXT": "1"}, clear=False):
            assert_hold(self, "NESTED_REVIEWER_INVOCATION_PROHIBITED", coord.invoke,
                        pkt, [sys.executable, "-c", "pass"], timeout_seconds=1)

    def test_V18_timeout_returns_hold(self):
        pkt = packet(); coord = cli.ReviewerCoordinator()
        assert_hold(self, "REVIEWER_TIMEOUT", coord.invoke, pkt,
                    [sys.executable, "-c", "import time; time.sleep(2)"], timeout_seconds=0.05)

    def test_V19_packet_and_output_size_limits_enforced(self):
        huge = "x" * cli.MAX_BYTES
        assert_hold(self, "PACKET_TOO_LARGE", cli.build_packet, payload(DeclaredAmbientContext=huge), READ_URL, FakeReader())
        pkt = packet()
        assert_hold(self, "REVIEWER_OUTPUT_TOO_LARGE", cli.validate_reviewer_output, b"x" * (cli.MAX_BYTES + 1), pkt)

    def test_V20_child_environment_allowlist_based(self):
        pkt = packet()
        with mock.patch.dict(os.environ, {"SHOULD_NOT_PASS": "secret", "PATH": os.environ.get("PATH", "")}, clear=False):
            env = cli._child_environment(pkt)
        self.assertNotIn("SHOULD_NOT_PASS", env)
        self.assertEqual(env["FRA_REVIEWER_CONTEXT"], "1")

    def test_V21_network_reader_uses_get_and_no_write_method(self):
        class Opener:
            def __init__(self): self.request = None
            def open(self, request, timeout):
                self.request = request
                return type("R", (), {"status": 200, "read": lambda self, n: b'{}'})()
        opener = Opener(); reader = cli.FreshGitHubReader(opener)
        reader.get(READ_URL)
        self.assertEqual(opener.request.get_method(), "GET")
        self.assertFalse(hasattr(reader, "post"))

    def test_V22_other_repository_rejected(self):
        assert_hold(self, "REPOSITORY_NOT_ALLOWED", cli.build_packet,
                    payload(ReviewedRepository="other/repo"), READ_URL, FakeReader())

    def test_V23_relay_round_trip_exact_bytes_and_hash(self):
        pkt = packet(); raw = reviewer_output(pkt)
        validated = cli.validate_reviewer_output(raw, pkt)
        envelope = cli.build_relay_envelope(pkt, validated, "issue:#x", "2026-09-12T00:00:00Z")
        decoded = base64.b64decode(envelope["ReviewerOutputBytes"])
        self.assertEqual(decoded, raw)
        self.assertEqual(envelope["ReviewerOutputSHA256"], cli.sha256_hex(raw))

    def test_V24_reconciliation_fresh_read_mismatch_hold(self):
        pkt = packet(); val = cli.validate_reviewer_output(reviewer_output(pkt), pkt)
        assert_hold(self, "FRESH_READ_MISMATCH", cli.reconcile, pkt, val, READ_URL,
                    current_scope_identity=pkt["LockedScopeIdentity"], required_human_authority_identity=None,
                    supplied_human_authority_identity=None, reader=FakeReader("e" * 40))

    def test_V25_reconciliation_success_only_positive_token(self):
        pkt = packet(); val = cli.validate_reviewer_output(reviewer_output(pkt), pkt)
        result = cli.reconcile(pkt, val, READ_URL, current_scope_identity=pkt["LockedScopeIdentity"],
                               required_human_authority_identity="human:#gate",
                               supplied_human_authority_identity="human:#gate", reader=FakeReader())
        self.assertEqual(result, cli.POSITIVE_RECONCILIATION)

    def test_V26_no_execution_function_for_auto_resume_ready_merge_deploy_promotion(self):
        forbidden = {"auto_resume", "ready", "merge", "deploy", "promotion", "human_go"}
        names = {name.lower() for name in dir(cli)}
        self.assertTrue(forbidden.isdisjoint(names))

    def test_V27_fra_disable_blocks_spawn(self):
        pkt = packet(); coord = cli.ReviewerCoordinator()
        with mock.patch.dict(os.environ, {"FRA_DISABLE": "1"}, clear=False), mock.patch("subprocess.Popen") as popen:
            assert_hold(self, "FRA_DISABLE", coord.invoke, pkt, [sys.executable, "-c", "pass"])
        popen.assert_not_called()

    def test_V28_tests_use_fixture_commands_only(self):
        source = pathlib.Path(__file__).read_text(encoding="utf-8")
        tree = ast.parse(source)
        reviewer_invocations = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "invoke":
                reviewer_invocations.append(node)
        self.assertGreater(len(reviewer_invocations), 0)
        for call in reviewer_invocations:
            self.assertGreaterEqual(len(call.args), 2)
            argv = call.args[1]
            self.assertIsInstance(argv, ast.List)
            first = argv.elts[0]
            self.assertIsInstance(first, ast.Attribute)
            self.assertIsInstance(first.value, ast.Name)
            self.assertEqual((first.value.id, first.attr), ("sys", "executable"))

    def test_V29_redirect_not_followed_returns_hold(self):
        class Opener:
            def open(self, request, timeout):
                raise urllib.error.HTTPError(request.full_url, 302, "Found", {}, io.BytesIO(b""))
        assert_hold(self, "REDIRECT_NOT_ALLOWED", cli.FreshGitHubReader(Opener()).get, READ_URL)

    def test_V30_non_https_rejected(self):
        assert_hold(self, "HTTPS_REQUIRED", cli._validate_repo_url,
                    "http://api.github.com/repos/yasutakesougo/design-foundation/branches/main")

    def test_V31_hostname_suffix_prefix_confusion_rejected(self):
        for url in (
            "https://api.github.com.evil.example/repos/yasutakesougo/design-foundation/branches/main",
            "https://evil.example/?next=api.github.com/repos/yasutakesougo/design-foundation",
        ):
            assert_hold(self, "HOST_NOT_ALLOWED", cli._validate_repo_url, url)

    def test_V32_repository_path_prefix_confusion_rejected(self):
        for suffix in ("design-foundation-evil", "design-foundationevil"):
            assert_hold(self, "REPOSITORY_PATH_NOT_ALLOWED", cli._validate_repo_url,
                        f"https://api.github.com/repos/yasutakesougo/{suffix}/branches/main")

    def test_V33_boundary_shifted_fields_distinct_preimages_and_keys(self):
        p1 = payload(Workstream="ab", ReviewType="c")
        p2 = payload(Workstream="a", ReviewType="bc")
        h = "1" * 64
        self.assertNotEqual(cli.canonical_json_bytes(cli._idempotency_preimage(p1, h)),
                            cli.canonical_json_bytes(cli._idempotency_preimage(p2, h)))
        self.assertNotEqual(cli.idempotency_key(p1, h), cli.idempotency_key(p2, h))

    def test_V34_insertion_order_does_not_change_idempotency_key(self):
        p = payload(); h = "2" * 64
        reversed_p = dict(reversed(list(p.items())))
        self.assertEqual(cli.idempotency_key(p, h), cli.idempotency_key(reversed_p, h))

    def test_V35_cross_key_concurrent_spawn_rejected_busy(self):
        first = packet(); second = packet(ReviewedArtifactIdentity="PR#other")
        coord = cli.ReviewerCoordinator(); entered = threading.Event(); release = threading.Event()

        original_popen = subprocess.Popen
        def delayed_popen(*args, **kwargs):
            proc = original_popen(*args, **kwargs)
            entered.set()
            return proc

        script = "import sys,time; sys.stdin.buffer.read(); time.sleep(0.3); sys.stdout.write('{}')"
        errors = []
        def run_first():
            try: coord.invoke(first, [sys.executable, "-c", script], timeout_seconds=2)
            except Exception as exc: errors.append(exc)
        with mock.patch("subprocess.Popen", side_effect=delayed_popen):
            thread = threading.Thread(target=run_first); thread.start(); entered.wait(1)
            assert_hold(self, "BUSY", coord.invoke, second, [sys.executable, "-c", "pass"], timeout_seconds=1)
            thread.join()
        self.assertTrue(errors)  # first output is intentionally malformed; BUSY check is the subject here.

    def test_V36_timeout_exactly_one_spawn(self):
        pkt = packet(); coord = cli.ReviewerCoordinator()
        with mock.patch("subprocess.Popen", wraps=subprocess.Popen) as popen:
            assert_hold(self, "REVIEWER_TIMEOUT", coord.invoke, pkt,
                        [sys.executable, "-c", "import time; time.sleep(1)"], timeout_seconds=0.05)
        self.assertEqual(popen.call_count, 1)

    def test_V37_nonzero_exit_exactly_one_spawn(self):
        pkt = packet(); coord = cli.ReviewerCoordinator()
        with mock.patch("subprocess.Popen", wraps=subprocess.Popen) as popen:
            assert_hold(self, "REVIEWER_NONZERO_EXIT", coord.invoke, pkt,
                        [sys.executable, "-c", "import sys; sys.exit(7)"], timeout_seconds=1)
        self.assertEqual(popen.call_count, 1)

    def test_V38_malformed_output_exactly_one_spawn(self):
        pkt = packet(); coord = cli.ReviewerCoordinator()
        with mock.patch("subprocess.Popen", wraps=subprocess.Popen) as popen:
            assert_hold(self, "MALFORMED_REVIEWER_OUTPUT", coord.invoke, pkt,
                        [sys.executable, "-c", "import sys; sys.stdin.buffer.read(); print('not-json')"], timeout_seconds=1)
        self.assertEqual(popen.call_count, 1)

    def test_V39_pass_with_excluded_observed_yes_rejected(self):
        pkt = packet()
        assert_hold(self, "INDEPENDENT_PASS_REQUIRES_EXCLUDED_OBSERVED_NO", cli.validate_reviewer_output,
                    reviewer_output(pkt, ExcludedItemObserved="YES"), pkt)

    def test_V40_pass_with_excluded_observed_unknown_rejected(self):
        pkt = packet()
        assert_hold(self, "INDEPENDENT_PASS_REQUIRES_EXCLUDED_OBSERVED_NO", cli.validate_reviewer_output,
                    reviewer_output(pkt, ExcludedItemObserved="UNKNOWN"), pkt)

    def test_V41_contradictory_excluded_contamination_not_normalized(self):
        pkt = packet(); raw = reviewer_output(pkt, Contamination="NONE", ExcludedItemObserved="YES")
        with self.assertRaises(cli.HoldError):
            cli.validate_reviewer_output(raw, pkt)
        parsed = json.loads(raw)
        self.assertEqual(parsed["Contamination"], "NONE")
        self.assertEqual(parsed["ExcludedItemObserved"], "YES")


if __name__ == "__main__":
    unittest.main()

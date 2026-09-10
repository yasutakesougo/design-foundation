from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
import sys
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "backend_selection_gate.py"
spec = importlib.util.spec_from_file_location("backend_selection_gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = gate
assert spec.loader is not None
spec.loader.exec_module(gate)


class BackendSelectionGateTests(unittest.TestCase):
    def attempt(self, mode: str, ok: bool, failure: str | None = None):
        return gate.Attempt(mode=mode, label=gate.MODE_LABELS[mode], ok=ok, failure_class=failure)

    def test_primary_success_never_uses_fallback(self):
        calls = []
        def runner(mode):
            calls.append(mode)
            return self.attempt(mode, True)
        result, used, attempts = gate.resolve_with_runner(runner, allow_fallback=True)
        self.assertEqual(result, "SOURCE-GUIDED")
        self.assertFalse(used)
        self.assertEqual(calls, [gate.PRIMARY_MODE])
        self.assertEqual(len(attempts), 1)

    def test_primary_failure_is_fail_closed_without_explicit_fallback(self):
        calls = []
        def runner(mode):
            calls.append(mode)
            return self.attempt(mode, False, "simulated")
        result, used, attempts = gate.resolve_with_runner(runner, allow_fallback=False)
        self.assertEqual(result, "HOLD")
        self.assertFalse(used)
        self.assertEqual(calls, [gate.PRIMARY_MODE])
        self.assertEqual(len(attempts), 1)

    def test_explicit_fallback_records_join_continuity(self):
        calls = []
        def runner(mode):
            calls.append(mode)
            if mode == gate.PRIMARY_MODE:
                return self.attempt(mode, False, "simulated-primary-failure")
            return self.attempt(mode, True)
        result, used, attempts = gate.resolve_with_runner(runner, allow_fallback=True)
        self.assertEqual(result, "JOIN-CONTINUITY")
        self.assertTrue(used)
        self.assertEqual(calls, [gate.PRIMARY_MODE, gate.FALLBACK_MODE])
        self.assertEqual(attempts[0].failure_class, "simulated-primary-failure")

    def test_both_fail_remains_hold(self):
        def runner(mode):
            return self.attempt(mode, False, "simulated")
        result, used, attempts = gate.resolve_with_runner(runner, allow_fallback=True)
        self.assertEqual(result, "HOLD")
        self.assertTrue(used)
        self.assertEqual(len(attempts), 2)

    def test_validation_rejects_nonfinite_path_coordinate(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            svg = td / "bad.svg"
            metrics = td / "m.json"
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><g fill="none" stroke="currentColor" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><path d="M 0 0 C nan 1 2 3 4 5"/></g></svg>')
            metrics.write_text(json.dumps({
                "path_count": 1, "source_path_count": 1, "segment_count": 1,
                "correction3_refined_path_count": 1,
                "centerline_deviation_mean_source_px": 0.1,
                "centerline_deviation_max_source_px": 0.2,
            }))
            errors, _ = gate.validate_candidate(svg, metrics)
            self.assertIn("nonfinite-path-coordinate", errors)

    def test_validation_rejects_path_count_topology_mismatch(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            svg = td / "bad.svg"
            metrics = td / "m.json"
            svg.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><g fill="none" stroke="currentColor" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><path d="M 0 0 L 1 1"/></g></svg>')
            metrics.write_text(json.dumps({
                "path_count": 1, "source_path_count": 2, "segment_count": 1,
                "correction3_refined_path_count": 0,
                "centerline_deviation_mean_source_px": 0.1,
                "centerline_deviation_max_source_px": 0.2,
            }))
            errors, _ = gate.validate_candidate(svg, metrics)
            self.assertIn("path-count-vs-source-topology-mismatch", errors)

    def _fake_vectorizer(self, directory: Path) -> Path:
        script = directory / "fake_vectorizer.py"
        script.write_text(
            """#!/usr/bin/env python3
import json, sys
from pathlib import Path
args=sys.argv[1:]
mode=args[args.index('--curve-mode')+1]
out=Path(args[1]); metrics=Path(args[args.index('--metrics')+1])
if mode == 'curvature-aware-source-guided':
    print('simulated source-guided execution failure', file=sys.stderr)
    raise SystemExit(9)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text('<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 512 512\"><g fill=\"none\" stroke=\"currentColor\" stroke-width=\"8\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M 0 0 L 1 1\"/></g></svg>')
metrics.write_text(json.dumps({'path_count':1,'source_path_count':1,'segment_count':1,'correction3_refined_path_count':0,'centerline_deviation_mean_source_px':0.1,'centerline_deviation_max_source_px':0.2}))
""",
            encoding="utf-8",
        )
        return script

    def test_cli_explicit_fallback_is_recorded(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            inp = td / "input.bin"; inp.write_bytes(b"fixture")
            vectorizer = self._fake_vectorizer(td)
            out = td / "out"; report = td / "report.json"
            proc = subprocess.run([sys.executable, str(SCRIPT), str(inp), str(out), "--vectorizer", str(vectorizer), "--allow-fallback", "--json", str(report)], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0)
            data = json.loads(report.read_text())
            self.assertEqual(data["result"], "JOIN-CONTINUITY")
            self.assertTrue(data["fallback_used"])
            self.assertEqual(len(data["attempts"]), 2)
            self.assertEqual(data["attempts"][0]["failure_class"], "backend-execution-failed")
            self.assertTrue(data["attempts"][1]["ok"])

    def test_cli_primary_failure_without_fallback_is_hold(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            inp = td / "input.bin"; inp.write_bytes(b"fixture")
            vectorizer = self._fake_vectorizer(td)
            out = td / "out"; report = td / "report.json"
            proc = subprocess.run([sys.executable, str(SCRIPT), str(inp), str(out), "--vectorizer", str(vectorizer), "--json", str(report)], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2)
            data = json.loads(report.read_text())
            self.assertEqual(data["result"], "HOLD")
            self.assertFalse(data["fallback_used"])
            self.assertEqual(len(data["attempts"]), 1)


if __name__ == "__main__":
    unittest.main()

"""Exercise review isolation/cleanup and decision-log output without live services."""
from __future__ import annotations

import csv
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "plugins/vstack/skills/adversarial-review/scripts/run_adversarial_review.sh"
LOG = ROOT / "plugins/vstack/skills/show-me-your-work/scripts/log.sh"


class ReviewIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "source with spaces"
        self.repo.mkdir()
        self.scratch = self.root / "scratch"
        self.scratch.mkdir()
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.test")
        self.git("config", "commit.gpgsign", "false")
        (self.repo / "data.txt").write_text("before\n")
        self.git("add", "data.txt")
        self.git("commit", "-qm", "Base")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("branch", "fixture-base")
        (self.repo / "data.txt").write_text("after\n")
        self.git("commit", "-qam", "Change")
        self.head = self.git("rev-parse", "HEAD").stdout.strip()
        self.runner = self.root / "fake reviewer"
        self.runner.write_text("""#!/usr/bin/env bash
set -eu
printf '%s\\n' "$@" > "$FIXTURE_OUTPUT/arguments"
pwd > "$FIXTURE_OUTPUT/working-directory"
cat > "$FIXTURE_OUTPUT/prompt"
git rev-parse HEAD > "$FIXTURE_OUTPUT/head"
git show refs/review/base:data.txt > "$FIXTURE_OUTPUT/base-data"
printf 'reviewer edit\\n' > data.txt
exit "${FIXTURE_EXIT:-0}"
""")
        self.runner.chmod(0o755)
        self.env = dict(os.environ, TMPDIR=str(self.scratch),
                        CLAUDE_BIN=str(self.runner), FIXTURE_OUTPUT=str(self.root),
                        ADVERSARIAL_REVIEW_MODEL="", FIXTURE_EXIT="0")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, text=True,
                              capture_output=True, check=True)

    def review(self, *args, code=0):
        result = subprocess.run(
            ["bash", str(REVIEW), "--base", "fixture-base", *args],
            cwd=self.repo, env=self.env, text=True, capture_output=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return result

    def test_pins_local_base_isolates_edits_and_cleans_success(self):
        self.review("--model", "fixture-model")
        self.assertEqual((self.root / "arguments").read_text(),
                         "-p\n--model\nfixture-model\n")
        self.assertEqual((self.root / "head").read_text().strip(), self.head)
        self.assertEqual((self.root / "base-data").read_text(), "before\n")
        self.assertEqual((self.repo / "data.txt").read_text(), "after\n")
        self.assertEqual(self.git("status", "--porcelain").stdout, "")
        self.assertIn(self.base, (self.root / "prompt").read_text())
        self.assertEqual(list(self.scratch.iterdir()), [])

    def test_cleans_failure_and_preserves_exit_status(self):
        self.env["FIXTURE_EXIT"] = "7"
        self.review(code=7)
        self.assertEqual(list(self.scratch.iterdir()), [])
        self.assertEqual((self.repo / "data.txt").read_text(), "after\n")

    def test_keep_retains_clone_and_uses_configured_runner_default(self):
        self.review("--keep")
        clone = Path((self.root / "working-directory").read_text().strip())
        self.assertTrue(clone.is_dir())
        self.assertEqual((self.root / "arguments").read_text(), "-p\n")

    def test_dry_run_never_invokes_reviewer(self):
        result = self.review("--dry-run")
        self.assertIn("Dry run only", result.stderr)
        self.assertFalse((self.root / "arguments").exists())
        self.assertEqual(list(self.scratch.iterdir()), [])

    def test_refuses_staged_unstaged_and_untracked_work(self):
        for kind in ("unstaged", "staged", "untracked"):
            with self.subTest(kind=kind):
                target = self.repo / ("extra.txt" if kind == "untracked" else "data.txt")
                target.write_text("unreviewed\n")
                if kind == "staged":
                    self.git("add", "data.txt")
                result = self.review(code=1)
                self.assertIn("clean worktree", result.stderr)
                self.assertFalse((self.root / "arguments").exists())
                self.assertEqual(list(self.scratch.iterdir()), [])
                if kind == "untracked":
                    target.unlink()
                else:
                    self.git("restore", "--source=HEAD", "--staged", "--worktree", "data.txt")

    def test_invalid_base_does_not_run_or_leak_clone(self):
        self.review("--base", "absent-ref", code=128)
        self.assertFalse((self.root / "arguments").exists())
        self.assertEqual(list(self.scratch.iterdir()), [])

    def test_extra_prompt_path_with_spaces(self):
        prompt = self.root / "extra context.md"
        prompt.write_text("Check the transaction boundary.\n")
        self.review("--prompt", str(prompt))
        self.assertIn(prompt.read_text(), (self.root / "prompt").read_text())


class DecisionLogIntegrationTests(unittest.TestCase):
    def test_rows_remain_tsv_and_formula_cells_are_escaped(self):
        with tempfile.TemporaryDirectory() as temp:
            log = Path(temp) / "nested folder" / "decisions.tsv"
            args = ["bash", str(LOG), str(log), "=phase", "line\nbreak",
                    "tab\there", "@evidence", "+result"]
            subprocess.run(args, check=True)
            subprocess.run(args, check=True)
            with log.open(newline="") as handle:
                rows = list(csv.reader(handle, delimiter="\t"))
            self.assertEqual(rows[0], ["ts", "phase", "decision", "why", "evidence", "result"])
            self.assertEqual(len(rows), 3)
            for row in rows[1:]:
                self.assertEqual(row[1:], ["'=phase", "line break", "tab here",
                                          "'@evidence", "'+result"])


if __name__ == "__main__":
    unittest.main()

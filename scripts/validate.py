#!/usr/bin/env python3
"""Validate the portable Vishaal skills marketplace."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "vishaal"
SKILLS = PLUGIN / "skills"
EXPECTED_SKILLS = {
    "adversarial-review",
    "check-ci",
    "cli-creator",
    "deslop",
    "grab",
    "grill-me",
    "meaningful-contribution",
    "resolve-conflicts",
    "tdd",
    "trace-request-flow",
    "yeet",
}
FORBIDDEN_TEXT = (
    "pedestal",
    "platform-demo",
    "wayfair",
    "/users/yalamanchali",
    "[todo:",
)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise AssertionError(f"Invalid JSON at {path.relative_to(ROOT)}: {exc}") from exc


def validate_manifests() -> None:
    codex_marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    codex_plugin = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    claude_plugin = load_json(PLUGIN / ".claude-plugin" / "plugin.json")

    assert codex_marketplace["name"] == "vishaal-skills"
    assert claude_marketplace["name"] == "vishaal-skills"
    assert codex_marketplace["plugins"][0]["name"] == "vishaal"
    assert codex_marketplace["plugins"][0]["source"]["path"] == "./plugins/vishaal"
    assert claude_marketplace["plugins"][0]["name"] == "vishaal"
    assert claude_marketplace["plugins"][0]["source"] == "./plugins/vishaal"
    assert codex_plugin["name"] == "vishaal"
    assert claude_plugin["name"] == "vishaal"


def validate_skills() -> None:
    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    assert actual == EXPECTED_SKILLS, (
        f"Skill set mismatch: missing={sorted(EXPECTED_SKILLS - actual)}, "
        f"unexpected={sorted(actual - EXPECTED_SKILLS)}"
    )

    for skill_name in sorted(EXPECTED_SKILLS):
        skill_file = SKILLS / skill_name / "SKILL.md"
        text = skill_file.read_text()
        frontmatter = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        assert frontmatter, f"Missing YAML frontmatter: {skill_file.relative_to(ROOT)}"
        name_match = re.search(r"^name:\s*[\"']?([^\"'\n]+)", frontmatter.group(1), re.MULTILINE)
        assert name_match, f"Missing skill name: {skill_file.relative_to(ROOT)}"
        assert name_match.group(1).strip() == skill_name, (
            f"Skill name mismatch in {skill_file.relative_to(ROOT)}"
        )


def validate_portability() -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".ico"}:
            continue
        try:
            text = path.read_text().lower()
        except UnicodeDecodeError:
            continue
        for forbidden in FORBIDDEN_TEXT:
            assert forbidden not in text, (
                f"Forbidden text {forbidden!r} in {path.relative_to(ROOT)}"
            )


def main() -> int:
    try:
        validate_manifests()
        validate_skills()
        validate_portability()
    except (AssertionError, KeyError, OSError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"validated {len(EXPECTED_SKILLS)} portable skills and both marketplaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

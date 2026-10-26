#!/usr/bin/env python3
"""Validate vstack's manifests, skills, references, and published inventory."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "vstack"
SKILLS = PLUGIN / "skills"
REPOSITORY = "https://github.com/drkm-hq/vstack"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def validate_manifests() -> None:
    codex = load_json(ROOT / ".agents/plugins/marketplace.json")
    claude = load_json(ROOT / ".claude-plugin/marketplace.json")
    for marketplace in (codex, claude):
        assert marketplace["name"] == "vstack"
        assert len(marketplace["plugins"]) == 1
        assert marketplace["plugins"][0]["name"] == "vstack"
    assert codex["plugins"][0]["source"] == {
        "source": "local", "path": "./plugins/vstack"
    }
    assert claude["plugins"][0]["source"] == "./plugins/vstack"
    versions = set()
    for engine in ("codex", "claude"):
        manifest = load_json(PLUGIN / f".{engine}-plugin/plugin.json")
        assert manifest["name"] == "vstack"
        assert manifest["repository"] == REPOSITORY
        assert manifest["homepage"] == REPOSITORY
        versions.add(manifest["version"])
    assert len(versions) == 1, "Plugin versions disagree"
    assert load_json(PLUGIN / ".codex-plugin/plugin.json")["skills"] == "./skills/"


def validate_skills() -> set[str]:
    names = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    assert names, "No skills found"
    for name in sorted(names):
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) < 64, name
        path = SKILLS / name / "SKILL.md"
        text = path.read_text()
        match = re.match(r"^---\n(.*?)\n---\n(.+)", text, re.DOTALL)
        assert match, f"Missing frontmatter or body: {path}"
        frontmatter = yaml.safe_load(match[1])
        assert isinstance(frontmatter, dict), f"Invalid frontmatter: {path}"
        assert frontmatter["name"] == name, f"Skill name mismatch: {path}"
        description = frontmatter.get("description")
        assert isinstance(description, str) and description.strip(), f"Missing description: {path}"
        assert len(description) <= 1024, f"Description too long: {path}"
        assert "[TODO:" not in text, f"Unfinished scaffold: {path}"
        ui = path.parent / "agents/openai.yaml"
        if ui.exists():
            metadata = yaml.safe_load(ui.read_text())
            interface = metadata["interface"]
            assert isinstance(interface["display_name"], str)
            short = interface["short_description"]
            assert isinstance(short, str) and 25 <= len(short) <= 64, ui
            if "default_prompt" in interface:
                assert f"$" + name in interface["default_prompt"], ui
    return names


def validate_links() -> None:
    for path in [ROOT / "README.md", ROOT / "SOURCES.md", *SKILLS.rglob("*.md")]:
        text = path.read_text()
        # Example templates in code fences are not actual package dependencies.
        prose = re.sub(r"(?ms)^[ \t]*```.*?^[ \t]*```[^\n]*$", "", text)
        for destination in re.findall(r"\]\(([^)\s]+)\)", prose):
            parsed = urlsplit(destination.strip("<>"))
            if parsed.scheme or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            assert target.is_relative_to(ROOT), f"Reference escapes package: {path}: {destination}"
            assert target.exists(), f"Broken reference: {path}: {destination}"
    for path in SKILLS.rglob("*"):
        assert not path.is_symlink(), f"Nonportable symlink: {path}"
        if path.is_file():
            text = path.read_text()
            assert not re.search(r"/(?:Users|home)/[a-zA-Z0-9_.-]+/", text), f"Machine path: {path}"


def main() -> int:
    try:
        validate_manifests()
        names = validate_skills()
        validate_links()
        catalog = set(re.findall(
            r"\| \`([a-z0-9-]+)\` \|", (ROOT / "README.md").read_text()
        ))
        assert names == catalog, f"README inventory mismatch: {names ^ catalog}"
    except (AssertionError, KeyError, TypeError, ValueError, OSError, yaml.YAMLError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"validated {len(names)} skills, local references, and both vstack marketplaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

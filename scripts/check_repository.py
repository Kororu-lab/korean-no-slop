#!/usr/bin/env python3
"""Validate the portable skill and evaluation bundle using Python stdlib."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/korean-no-slop"


def main():
    errors = []
    required = ["SKILL.md", "references/ui.md", "references/slides.md",
                "references/prose.md", "agents/openai.yaml"]
    for name in required:
        if not (SKILL / name).is_file():
            errors.append("Missing skill file: " + name)
    if errors:
        print("\n".join(errors))
        return 1
    entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not entry.startswith("---\nname: korean-no-slop\ndescription: "):
        errors.append("Unexpected skill frontmatter")
    if "\n---\n" not in entry[4:]:
        errors.append("Unclosed skill frontmatter")
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".local", "dist"} for part in path.parts):
            continue
        content = path.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in link or link.startswith("#"):
                continue
            target = link.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                errors.append("Broken reference in {}: {}".format(path.relative_to(ROOT), target))
    cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "evals/rubric.json").read_text(encoding="utf-8"))
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate case IDs")
    if set(ids) != set(rubric):
        errors.append("Cases and rubric do not match")
    for case in cases:
        if not isinstance(case.get("request"), str) or not case["request"].strip():
            errors.append("Missing request: " + case["id"])
        rule = rubric.get(case["id"], {})
        if not rule.get("review"):
            errors.append("Missing semantic review criterion: " + case["id"])
        for field in ("required", "forbidden"):
            if not isinstance(rule.get(field), list) or not all(isinstance(x, str) for x in rule[field]):
                errors.append("Invalid {}: {}".format(field, case["id"]))
    if errors:
        print("\n".join(errors))
        return 1
    print("Repository checks pass; {} evaluation cases; local references resolve.".format(len(cases)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("Invalid repository data: {}".format(exc), file=sys.stderr)
        sys.exit(2)

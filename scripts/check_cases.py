#!/usr/bin/env python3
"""Check observable invariants in recorded skill outputs; no model calls."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def check(path):
    rubric = json.loads((ROOT / "evals/rubric.json").read_text(encoding="utf-8"))
    run = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    outputs = run["outputs"]
    if not isinstance(outputs, dict):
        raise ValueError("outputs must be an object")
    failures = []
    for extra in sorted(set(outputs) - set(rubric)):
        failures.append((extra, "unknown case"))
    passed = 0
    for case_id, rules in rubric.items():
        value = outputs.get(case_id)
        errors = []
        if not isinstance(value, str):
            errors.append("missing output or non-string output")
        else:
            for phrase in rules["required"]:
                if phrase not in value:
                    errors.append("missing: " + phrase)
            for phrase in rules["forbidden"]:
                if phrase in value:
                    errors.append("unexpected: " + phrase)
            if "exact" in rules and value.strip() != rules["exact"]:
                errors.append("preserved text differs")
        failures.extend((case_id, error) for error in errors)
        if not errors:
            passed += 1
    for case_id, error in failures:
        print("FAIL {}: {}".format(case_id, error))
    print("Observable checks: {}/{} cases pass".format(passed, len(rubric)))
    print("Semantic review and rendered-artifact QA are separate.")
    return not failures


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/check_cases.py RUN.json", file=sys.stderr)
        return 2
    try:
        return 0 if check(Path(sys.argv[1])) else 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print("Invalid evaluation data: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

from __future__ import annotations

import json
from pathlib import Path


CASES = Path(__file__).with_name("cases.jsonl")


def main() -> None:
    ids = set()
    count = 0
    for line_number, line in enumerate(CASES.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        case = json.loads(line)
        required = {"id", "route"}
        if case.get("route", "").startswith("publish"):
            required.add("expected_decision")
        missing = required - case.keys()
        if missing:
            raise SystemExit(f"line {line_number}: missing {sorted(missing)}")
        if case["id"] in ids:
            raise SystemExit(f"line {line_number}: duplicate id {case['id']}")
        ids.add(case["id"])
        count += 1
    print(f"Validated {count} eval cases")


if __name__ == "__main__":
    main()

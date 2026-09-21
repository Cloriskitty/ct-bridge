from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skill"
STANDALONE_SKILLS = ("cn-crypto-publish", "en-crypto-decode")


def package_skill(name: str, output_dir: Path) -> Path:
    source = SKILL_ROOT / name
    if not source.is_dir():
        raise SystemExit(f"Skill directory not found: {source}")

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / f"{name}.zip"
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, Path(name) / path.relative_to(source))
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description="Package standalone CT Bridge skills")
    parser.add_argument("--output-dir", type=Path, default=REPO_ROOT / "dist")
    parser.add_argument("--skill", choices=(*STANDALONE_SKILLS, "all"), default="all")
    args = parser.parse_args()

    names = STANDALONE_SKILLS if args.skill == "all" else (args.skill,)
    for name in names:
        print(package_skill(name, args.output_dir.expanduser().resolve()))


if __name__ == "__main__":
    main()

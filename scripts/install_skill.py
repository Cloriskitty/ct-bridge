from __future__ import annotations

import argparse
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("ct-bridge", "cn-crypto-publish")


def main() -> None:
    parser = argparse.ArgumentParser(description="Install the CT Bridge skill locally")
    parser.add_argument(
        "--skills-dir",
        type=Path,
        required=True,
        help="Agent skills directory, for example $CODEX_HOME/skills",
    )
    parser.add_argument(
        "--skill",
        choices=SKILLS,
        default="ct-bridge",
        help="Skill to install (default: ct-bridge)",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace an existing skill directory",
    )
    args = parser.parse_args()

    source = REPO_ROOT / "skill" / args.skill
    destination = args.skills_dir.expanduser().resolve() / args.skill
    if destination.exists():
        if not args.replace:
            raise SystemExit(f"{destination} already exists; rerun with --replace")
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    print(f"Installed {args.skill} to {destination}")


if __name__ == "__main__":
    main()

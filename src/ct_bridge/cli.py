from __future__ import annotations

import argparse
import json
import sys
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

from . import __version__


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def read_input(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
        paragraphs = []
        for paragraph in root.iter(f"{{{W_NS}}}p"):
            text = "".join(node.text or "" for node in paragraph.iter(f"{{{W_NS}}}t"))
            if text.strip():
                paragraphs.append(text)
        return "\n\n".join(paragraphs)
    return path.read_text(encoding="utf-8")


def build_prompt(args: argparse.Namespace) -> str:
    content = read_input(args.input)
    if args.action == "decode":
        instruction = (
            "Use $ct-bridge in Decode mode. Explain the content in Chinese. "
            "Separate direct meaning, tone or subtext, necessary cultural background, "
            "and uncertainty. Keep the first answer concise."
        )
    else:
        instruction = (
            f"Use $ct-bridge in Publish mode with the {args.mode} boundary. "
            "Preserve the author's claims and voice. Return polished English and identify "
            "only decisions that materially affect meaning, culture, or register."
        )
        if args.source:
            source = read_input(args.source)
            content = f"CHINESE SOURCE:\n{source}\n\nENGLISH DRAFT:\n{content}"
    return f"{instruction}\n\nCONTENT:\n{content}\n"


def write_feedback(args: argparse.Namespace) -> int:
    event = {
        "event_id": str(uuid.uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "schema_version": "1.0",
        "client": "ct-bridge-cli",
        "client_version": __version__,
        "consent_level": args.consent,
        "mode": args.mode,
        "concept": args.concept,
        "choice": args.choice,
        "rating": args.rating,
        "reason": args.reason,
        "platform": args.platform,
        "audience": args.audience,
    }
    if args.snippet:
        if args.consent not in {"snippet", "full-example"}:
            raise SystemExit("--snippet requires --consent snippet or full-example")
        event["snippet"] = args.snippet
    payload = json.dumps(event, ensure_ascii=False, indent=2)
    print(payload)
    if args.output:
        with args.output.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, ensure_ascii=False) + "\n")
        print(f"Saved locally to {args.output}", file=sys.stderr)
    else:
        print("Preview only. Nothing was saved or uploaded.", file=sys.stderr)
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="ct-bridge")
    root.add_argument("--version", action="version", version=__version__)
    commands = root.add_subparsers(dest="command", required=True)

    prompt = commands.add_parser("prompt", help="Create a local model-ready task packet")
    prompt.add_argument("action", choices=["decode", "publish"])
    prompt.add_argument("input", type=Path)
    prompt.add_argument("--source", type=Path, help="Chinese source for bilingual review")
    prompt.add_argument(
        "--mode",
        choices=["faithful", "ct-native", "editorial"],
        default="faithful",
    )

    feedback = commands.add_parser("feedback", help="Preview or save an opt-in feedback event")
    feedback.add_argument("--concept", required=True)
    feedback.add_argument("--choice", required=True)
    feedback.add_argument("--rating", choices=["useful", "wrong", "missing-context"], required=True)
    feedback.add_argument("--reason")
    feedback.add_argument("--mode", default="publish-faithful")
    feedback.add_argument("--platform")
    feedback.add_argument("--audience")
    feedback.add_argument("--consent", choices=["metadata", "snippet", "full-example"], default="metadata")
    feedback.add_argument("--snippet")
    feedback.add_argument("--output", type=Path, help="Append JSONL locally; no network submission")
    return root


def main() -> int:
    args = parser().parse_args()
    if args.command == "prompt":
        print(build_prompt(args))
        return 0
    return write_feedback(args)

from __future__ import annotations

import argparse
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from ct_bridge.cli import build_prompt, read_input, write_feedback


class CliTests(unittest.TestCase):
    def test_read_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("probably nothing", encoding="utf-8")
            self.assertEqual(read_input(path), "probably nothing")

    def test_read_minimal_docx(self) -> None:
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
          <w:body><w:p><w:r><w:t>exit liquidity</w:t></w:r></w:p></w:body>
        </w:document>"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", xml)
            self.assertEqual(read_input(path), "exit liquidity")

    def test_decode_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("we are so back", encoding="utf-8")
            args = argparse.Namespace(action="decode", input=path, mode="faithful", source=None)
            prompt = build_prompt(args)
            self.assertIn("Decode mode", prompt)
            self.assertIn("we are so back", prompt)

    def test_feedback_preview_does_not_write(self) -> None:
        args = argparse.Namespace(
            concept="接盘",
            choice="become exit liquidity",
            rating="useful",
            consent="metadata",
            mode="publish-faithful",
            reason=None,
            platform=None,
            audience=None,
            snippet=None,
            output=None,
        )
        self.assertEqual(write_feedback(args), 0)

    def test_snippet_requires_consent(self) -> None:
        args = argparse.Namespace(
            concept="接盘",
            choice="become exit liquidity",
            rating="useful",
            consent="metadata",
            mode="publish-faithful",
            reason=None,
            platform=None,
            audience=None,
            snippet="private text",
            output=None,
        )
        with self.assertRaises(SystemExit):
            write_feedback(args)

    def test_saved_feedback_is_jsonl(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "feedback.jsonl"
            args = argparse.Namespace(
                concept="probably nothing",
                choice="ironic",
                rating="useful",
                consent="metadata",
                mode="decode-context",
                reason="Needed cultural context",
                platform="x",
                audience="advanced",
                snippet=None,
                output=output,
            )
            write_feedback(args)
            event = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(event["consent_level"], "metadata")
            self.assertNotIn("snippet", event)


if __name__ == "__main__":
    unittest.main()

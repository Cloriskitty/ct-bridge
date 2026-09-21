from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InstallTests(unittest.TestCase):
    def test_installs_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "install_skill.py"),
                    "--skills-dir",
                    directory,
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            installed = Path(directory) / "ct-bridge"
            self.assertTrue((installed / "SKILL.md").exists())
            self.assertTrue((installed / "agents" / "openai.yaml").exists())

    def test_refuses_to_overwrite_without_replace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "ct-bridge"
            destination.mkdir()
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "install_skill.py"),
                    "--skills-dir",
                    directory,
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("already exists", result.stderr + result.stdout)

    def test_installs_publish_only_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "install_skill.py"),
                    "--skills-dir",
                    directory,
                    "--skill",
                    "cn-crypto-publish",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            installed = Path(directory) / "cn-crypto-publish"
            self.assertTrue((installed / "SKILL.md").exists())
            self.assertTrue((installed / "references" / "editorial-boundaries.md").exists())

    def test_installs_decode_only_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "install_skill.py"),
                    "--skills-dir",
                    directory,
                    "--skill",
                    "en-crypto-decode",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            installed = Path(directory) / "en-crypto-decode"
            self.assertTrue((installed / "SKILL.md").exists())
            self.assertTrue((installed / "references" / "context-cards.md").exists())


if __name__ == "__main__":
    unittest.main()

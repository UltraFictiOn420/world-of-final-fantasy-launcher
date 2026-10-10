"""Non-launching checks. Never starts/stops or changes an installed game."""
import hashlib
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import build_release


class SourceTests(unittest.TestCase):
    def test_success_exits_without_wait_or_pause(self):
        source = (ROOT / "Launch-WoFF.bat").read_text(encoding="ascii")
        success = source.split("\n:missingGame")[0]
        commands = [line.strip().lower() for line in success.splitlines()
                    if line.strip() and not line.strip().lower().startswith("rem ")]
        self.assertIn('start "" "woff.exe"', commands)
        self.assertIn("exit /b 0", commands)
        self.assertFalse(any("/wait" in line or line == "pause" for line in commands))
        self.assertIn('set "__compat_layer=runasinvoker win7rtm"', commands)

    def test_no_hidden_or_downloaded_code(self):
        source = (ROOT / "Launch-WoFF.bat").read_text(encoding="ascii").lower()
        for forbidden in ("encodedcommand", "executionpolicy", "invoke-webrequest",
                          "downloadstring", "reg add", "reg delete", "icacls",
                          "taskkill", "set-mppreference", "schtasks", "runas.exe"):
            self.assertNotIn(forbidden, source)
        self.assertEqual((ROOT / "steam_appid.txt").read_text().strip(), "552700")

    def test_release_inventory_and_checksums(self):
        archive = build_release.build()
        first = archive.read_bytes()
        self.assertEqual(build_release.build().read_bytes(), first)
        with zipfile.ZipFile(archive) as bundle:
            self.assertEqual(set(bundle.namelist()),
                             set(build_release.FILES) | {"CHECKSUMS.sha256"})
            for line in bundle.read("CHECKSUMS.sha256").decode().splitlines():
                expected, path = line.split("  ", 1)
                self.assertEqual(hashlib.sha256(bundle.read(path)).hexdigest(), expected)
            batch = bundle.read("Launch-WoFF.bat")
            self.assertNotIn(b"\n", batch.replace(b"\r\n", b""))


@unittest.skipUnless(os.name == "nt", "Windows batch checks")
class RefusalTests(unittest.TestCase):
    def run_launcher(self, folder):
        # All folders are synthetic and lack at least one required file.
        result = subprocess.run(
            [str(ROOT / "Launch-WoFF.bat"), str(folder)],
            shell=True, input="", text=True, capture_output=True, timeout=20,
        )
        return result

    def test_missing_game_with_spaces(self):
        with tempfile.TemporaryDirectory(prefix="WoFF test ") as folder:
            self.assertEqual(self.run_launcher(folder).returncode, 2)

    def test_missing_resources(self):
        with tempfile.TemporaryDirectory(prefix="WoFF test ") as folder:
            Path(folder, "WOFF.exe").touch()
            self.assertEqual(self.run_launcher(folder).returncode, 3)

    def test_missing_app_id(self):
        with tempfile.TemporaryDirectory(prefix="WoFF test ") as folder:
            Path(folder, "WOFF.exe").touch()
            Path(folder, "resource").mkdir()
            self.assertEqual(self.run_launcher(folder).returncode, 4)


if __name__ == "__main__":
    unittest.main()

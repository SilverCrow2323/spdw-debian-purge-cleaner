"""Regression tests for deletion and scanning around symbolic links."""
import os
import tempfile
import threading
import unittest
from pathlib import Path

from spdw_purge import core, finder


class SymlinkSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.scan_root = self.root / "scan"
        self.outside = self.root / "outside"
        self.scan_root.mkdir()
        self.outside.mkdir()
        core.DRY.clear()

    def tearDown(self):
        core.DRY.clear()
        self.temp.cleanup()

    def write(self, path: Path, payload: bytes = b"protected target"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)

    def test_destroy_file_symlink_unlinks_only_the_link(self):
        target = self.outside / "important.bin"
        self.write(target)
        link = self.scan_root / "shortcut"
        link.symlink_to(target)
        freed = core.destroy(str(link), False, lambda *_args: None)
        self.assertGreaterEqual(freed, 0)
        self.assertFalse(link.exists())
        self.assertTrue(target.is_file())
        self.assertEqual(target.read_bytes(), b"protected target")

    def test_destroy_directory_does_not_follow_linked_directory(self):
        target = self.outside / "keep.txt"
        self.write(target, b"outside data")
        nested = self.scan_root / "nested"
        nested.mkdir()
        (nested / "outside-link").symlink_to(self.outside, target_is_directory=True)
        core.destroy(str(nested), False, lambda *_args: None)
        self.assertFalse(nested.exists())
        self.assertTrue(target.is_file())
        self.assertEqual(target.read_bytes(), b"outside data")

    def test_scan_tree_does_not_descend_into_linked_directory(self):
        self.write(self.scan_root / "local.bin", b"local")
        self.write(self.outside / "secret.bin", b"outside secret")
        (self.scan_root / "external").symlink_to(self.outside, target_is_directory=True)
        result = core.scan_tree(str(self.scan_root), lambda *_args: None, threading.Event())
        self.assertIsNotNone(result)
        self.assertNotIn(str(self.outside), result.sizes)
        self.assertNotIn(str(self.outside / "secret.bin"), [row[1] for row in result.top])

    def test_duplicate_finder_does_not_hash_symlink_targets(self):
        payload = b"same content" * 10000
        self.write(self.scan_root / "real.bin", payload)
        (self.scan_root / "alias.bin").symlink_to(self.scan_root / "real.bin")
        self.write(self.outside / "copy.bin", payload)
        results = finder.find_duplicates(str(self.scan_root), 1, threading.Event())
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()

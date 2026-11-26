"""Regression tests for deletion and scanning around symbolic links."""
import threading
import tempfile
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

    def test_duplicate_finder_ignores_symlinks_but_finds_real_copies(self):
        payload = b"same content" * 10000
        real = self.scan_root / "real.bin"
        copy = self.scan_root / "copy.bin"
        alias = self.scan_root / "alias.bin"
        self.write(real, payload)
        self.write(copy, payload)
        alias.symlink_to(real)
        results = finder.find_duplicates(str(self.scan_root), 1, threading.Event())
        self.assertEqual(len(results), 1)
        self.assertEqual(set(results[0][1]), {str(real), str(copy)})
        self.assertNotIn(str(alias), results[0][1])

if __name__ == "__main__":
    unittest.main()

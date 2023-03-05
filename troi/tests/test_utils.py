import unittest

from troi.utils import discover_patches
from troi.patch import Patch


class TestPatches(unittest.TestCase):

    def test_discover_patches(self):
        patches = discover_patches()

        assert "daily-jams" in patches
        assert "area-random-recordings" in patches
        assert "weekly-flashback-jams" in patches
        assert "playlist-from-mbids" in patches
        assert "world-trip" in patches
        assert "recs-to-playlist" in patches
        assert "transfer-playlist" in patches
        assert "new-jams" in patches

        for p in patches:
            assert issubclass(patches[p], Patch)

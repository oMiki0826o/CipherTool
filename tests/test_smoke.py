"""Verify the minimum executable CipherTool foundation."""

import unittest

from cipher_tool import main


class CipherToolSmokeTest(unittest.TestCase):
    """Check that the public application entry point is importable."""

    def test_main_entry_point_is_callable(self) -> None:
        """The package exposes a callable application entry point."""
        self.assertTrue(callable(main))


if __name__ == "__main__":
    unittest.main()

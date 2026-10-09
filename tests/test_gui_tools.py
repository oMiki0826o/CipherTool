"""Test the GUI's display-name to tool-id mapping."""

import unittest

from cipher_tool.gui import tool_id_from_name


class GuiToolTest(unittest.TestCase):
    """Verify the GUI can dispatch display names to registry identifiers."""

    def test_resolves_registered_display_name(self) -> None:
        """A user-facing name resolves to the corresponding internal ID."""
        self.assertEqual(tool_id_from_name("Caesar Cipher"), "caesar")


if __name__ == "__main__":
    unittest.main()

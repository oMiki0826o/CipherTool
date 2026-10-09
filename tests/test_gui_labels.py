"""Test human-friendly GUI parameter labels."""

import unittest

from cipher_tool.gui import PARAMETER_LABELS


class GuiLabelTest(unittest.TestCase):
    """Verify key parameters have user-facing Chinese labels."""

    def test_key_parameter_labels_are_friendly(self) -> None:
        """Technical field names map to clear Chinese labels."""
        self.assertEqual(PARAMETER_LABELS["key"], "密鑰")
        self.assertEqual(PARAMETER_LABELS["shift"], "位移量")
        self.assertEqual(PARAMETER_LABELS["from_base"], "來源進位")


if __name__ == "__main__":
    unittest.main()

"""Test number-base and text conversion modules."""

import unittest

from cipher_tool.conversion import number_base, text


class NumberBaseTest(unittest.TestCase):
    """Verify generic integer base conversion."""

    def test_convert_between_common_bases(self) -> None:
        """Decimal, binary, octal, and hexadecimal interoperate."""
        self.assertEqual(number_base.convert_base("255", 10, 16), "FF")
        self.assertEqual(number_base.convert_base("FF", 16, 2), "11111111")
        self.assertEqual(number_base.convert_base("-10", 10, 2), "-1010")

    def test_invalid_base_or_digit_is_rejected(self) -> None:
        """Invalid source bases and digits produce value errors."""
        with self.assertRaises(ValueError):
            number_base.convert_base("2", 2, 10)
        with self.assertRaises(ValueError):
            number_base.convert_base("10", 1, 10)


class TextConversionTest(unittest.TestCase):
    """Verify byte and character text conversions."""

    def test_utf8_binary_and_hex_round_trip(self) -> None:
        """UTF-8 conversions preserve non-ASCII text."""
        original = "A中"
        self.assertEqual(text.binary_to_text(text.text_to_binary(original)), original)
        self.assertEqual(text.hex_to_text(text.text_to_hex(original)), original)

    def test_ascii_rejects_non_ascii_text(self) -> None:
        """ASCII conversion rejects characters outside ASCII."""
        with self.assertRaises(ValueError):
            text.text_to_ascii("中")

    def test_unicode_code_points(self) -> None:
        """Unicode conversions use U+ hexadecimal notation."""
        self.assertEqual(text.text_to_code_points("A中"), "U+0041 U+4E2D")
        self.assertEqual(text.code_points_to_text("U+0041 U+4E2D"), "A中")


if __name__ == "__main__":
    unittest.main()

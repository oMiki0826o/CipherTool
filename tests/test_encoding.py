"""Test text encoding modules."""

import unittest

from cipher_tool.encoding import base16, base32, base64_codec, morse, url_encoding


class EncodingTest(unittest.TestCase):
    """Verify supported text encoding operations."""

    def test_base_codecs_round_trip_utf8_text(self) -> None:
        """Base codecs preserve UTF-8 text through encoding and decoding."""
        text = "Hello, 世界"
        for codec in (base16, base32, base64_codec):
            self.assertEqual(codec.decode(codec.encode(text)), text)

    def test_base64_rejects_invalid_input(self) -> None:
        """Invalid Base64 reports a clear value error."""
        with self.assertRaises(ValueError):
            base64_codec.decode("not valid@@")

    def test_morse_round_trip_and_word_separator(self) -> None:
        """Morse uses spaces between symbols and slash between words."""
        encoded = morse.encode("SOS HELP")
        self.assertEqual(encoded, "... --- ... / .... . .-.. .--.")
        self.assertEqual(morse.decode(encoded), "SOS HELP")

    def test_url_round_trip(self) -> None:
        """URL encoding delegates percent encoding to the standard library."""
        text = "hello world/中文?"
        self.assertEqual(url_encoding.decode(url_encoding.encode(text)), text)


if __name__ == "__main__":
    unittest.main()

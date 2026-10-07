"""Test the Caesar cipher public API."""

import unittest

from cipher_tool.ciphers.caesar import decrypt, encrypt


class CaesarCipherTest(unittest.TestCase):
    """Verify Caesar encryption and decryption behavior."""

    def test_encrypt_shifts_letters_and_preserves_case(self) -> None:
        """Letters shift while spaces, punctuation, and case remain intact."""
        self.assertEqual(encrypt("Hello, World!", shift=3), "Khoor, Zruog!")

    def test_decrypt_reverses_encryption(self) -> None:
        """Decryption returns the original plaintext."""
        plaintext = "Attack at Dawn"
        self.assertEqual(decrypt(encrypt(plaintext, shift=7), shift=7), plaintext)

    def test_invalid_shift_is_rejected(self) -> None:
        """A shift outside the supported range raises a clear error."""
        with self.assertRaises(ValueError):
            encrypt("ABC", shift=26)


if __name__ == "__main__":
    unittest.main()

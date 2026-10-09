"""Test checksum and integrity utilities."""

import unittest

from cipher_tool import integrity


class IntegrityTest(unittest.TestCase):
    """Verify common checksum algorithms."""

    def test_isbn_check_digits(self) -> None:
        """ISBN-10 and ISBN-13 produce their standard check digits."""
        self.assertEqual(integrity.isbn10_check_digit("030640615"), "2")
        self.assertEqual(integrity.isbn13_check_digit("978030640615"), "7")

    def test_luhn_generate_and_verify(self) -> None:
        """Luhn calculates and validates a known card-number check digit."""
        self.assertEqual(integrity.luhn_check_digit("7992739871"), "3")
        self.assertTrue(integrity.luhn_is_valid("79927398713"))

    def test_xor_parity_and_crc(self) -> None:
        """Byte integrity algorithms return deterministic values."""
        self.assertEqual(integrity.xor_checksum("Hi"), "21")
        self.assertEqual(integrity.parity_bit("1011", "even"), "1")
        self.assertEqual(integrity.crc3("A"), "3")
        self.assertEqual(integrity.crc32("123456789"), "CBF43926")

    def test_sha256(self) -> None:
        """SHA-256 returns the standard lowercase hexadecimal digest."""
        self.assertEqual(integrity.sha256("abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")


if __name__ == "__main__":
    unittest.main()

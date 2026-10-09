"""Test additional classical cipher implementations."""

import unittest

from cipher_tool.ciphers import autokey, beaufort, columnar, hill, kamasutra, polybius, scytale


class ExtendedCipherTest(unittest.TestCase):
    """Verify additional substitution and transposition ciphers."""

    def test_polybius_round_trip(self) -> None:
        """Polybius encodes letters as two-digit coordinates."""
        self.assertEqual(polybius.encode("HELLO"), "23 15 31 31 34")
        self.assertEqual(polybius.decode("23 15 31 31 34"), "HELLO")

    def test_beaufort_is_self_inverse(self) -> None:
        """Beaufort uses the same operation to encrypt and decrypt."""
        ciphertext = beaufort.encrypt("ATTACKATDAWN", "LEMON")
        self.assertEqual(beaufort.decrypt(ciphertext, "LEMON"), "ATTACKATDAWN")

    def test_columnar_round_trip(self) -> None:
        """Columnar transposition restores the original character order."""
        ciphertext = columnar.encrypt("WEAREDISCOVEREDFLEEATONCE", "ZEBRAS")
        self.assertEqual(columnar.decrypt(ciphertext, "ZEBRAS"), "WEAREDISCOVEREDFLEEATONCE")

    def test_scytale_round_trip(self) -> None:
        """Scytale restores text when both parties use the same column count."""
        ciphertext = scytale.encrypt("MEETMEATNOON", 4)
        self.assertEqual(scytale.decrypt(ciphertext, 4), "MEETMEATNOON")

    def test_autokey_round_trip(self) -> None:
        """Autokey extends its seed key with plaintext during encryption."""
        ciphertext = autokey.encrypt("ATTACKATDAWN", "QUEENLY")
        self.assertEqual(autokey.decrypt(ciphertext, "QUEENLY"), "ATTACKATDAWN")

    def test_kamasutra_round_trip(self) -> None:
        """Kamasutra swaps letters according to thirteen explicit pairs."""
        pairs = "AM,BX,CQ,DW,ET,FR,GS,HL,IO,JP,KN,UV,YZ"
        self.assertEqual(kamasutra.decrypt(kamasutra.encrypt("ATTACK", pairs), pairs), "ATTACK")

    def test_hill_two_by_two_round_trip(self) -> None:
        """Hill cipher encrypts and decrypts with an invertible 2x2 key."""
        key = "3,3,2,5"
        self.assertEqual(hill.encrypt("HELP", key), "HIAT")
        self.assertEqual(hill.decrypt("HIAT", key), "HELP")

    def test_hill_rejects_noninvertible_matrix(self) -> None:
        """A Hill key must have a determinant invertible modulo 26."""
        with self.assertRaises(ValueError):
            hill.encrypt("HELP", "2,4,2,4")


if __name__ == "__main__":
    unittest.main()

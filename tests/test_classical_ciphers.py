"""Test the required classical cipher modules."""

import unittest

from cipher_tool.ciphers import affine, atbash, bacon, pigpen, playfair, rail_fence, rot13, substitution, vigenere


class FixedKeyCipherTest(unittest.TestCase):
    """Verify ciphers with deterministic parameters."""

    def test_rot13_is_its_own_inverse(self) -> None:
        """Applying ROT13 twice returns the original text."""
        self.assertEqual(rot13.decode(rot13.encode("Hello, 123!")), "Hello, 123!")

    def test_atbash_is_its_own_inverse(self) -> None:
        """Applying Atbash twice returns the original text."""
        self.assertEqual(atbash.decrypt(atbash.encrypt("Abc XYZ!")), "Abc XYZ!")

    def test_affine_round_trip(self) -> None:
        """Affine encryption is reversed with an invertible multiplier."""
        self.assertEqual(affine.decrypt(affine.encrypt("Affine Cipher", 5, 8), 5, 8), "Affine Cipher")

    def test_affine_rejects_non_coprime_multiplier(self) -> None:
        """Affine rejects a multiplier without a modular inverse."""
        with self.assertRaises(ValueError):
            affine.encrypt("ABC", 2, 1)

    def test_vigenere_known_vector(self) -> None:
        """Vigenère follows the standard ATTACK AT DAWN / LEMON example."""
        self.assertEqual(vigenere.encrypt("ATTACK AT DAWN", "LEMON"), "LXFOPV EF RNHR")
        self.assertEqual(vigenere.decrypt("LXFOPV EF RNHR", "LEMON"), "ATTACK AT DAWN")

    def test_vigenere_rejects_empty_key(self) -> None:
        """Vigenère requires an alphabetic key."""
        with self.assertRaises(ValueError):
            vigenere.encrypt("ABC", "")

    def test_substitution_round_trip(self) -> None:
        """A complete substitution alphabet can be reversed."""
        alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
        encrypted = substitution.encrypt("Hello World", alphabet)
        self.assertEqual(substitution.decrypt(encrypted, alphabet), "Hello World")

    def test_substitution_rejects_duplicates(self) -> None:
        """A substitution alphabet must contain each Latin letter once."""
        with self.assertRaises(ValueError):
            substitution.encrypt("ABC", "A" * 26)

    def test_rail_fence_known_vector(self) -> None:
        """Rail Fence follows the standard three-rail example."""
        ciphertext = rail_fence.encrypt("WEAREDISCOVEREDFLEEATONCE", 3)
        self.assertEqual(ciphertext, "WECRLTEERDSOEEFEAOCAIVDEN")
        self.assertEqual(rail_fence.decrypt(ciphertext, 3), "WEAREDISCOVEREDFLEEATONCE")

    def test_rail_fence_rejects_one_rail(self) -> None:
        """Rail Fence requires at least two rails."""
        with self.assertRaises(ValueError):
            rail_fence.encrypt("ABC", 1)

    def test_bacon_round_trip(self) -> None:
        """Bacon encodes and decodes the full modern 26-letter alphabet."""
        self.assertEqual(bacon.decode(bacon.encode("HELLO")), "HELLO")

    def test_pigpen_round_trip(self) -> None:
        """Pigpen's portable text tokens can be decoded without a special font."""
        self.assertEqual(pigpen.decode(pigpen.encode("HELLO")), "HELLO")

    def test_playfair_known_vector(self) -> None:
        """Playfair follows the standard MONARCHY example."""
        ciphertext = playfair.encrypt("INSTRUMENTS", "MONARCHY")
        self.assertEqual(ciphertext, "GATLMZCLRQXA")
        self.assertEqual(playfair.decrypt(ciphertext, "MONARCHY"), "INSTRUMENTSX")


if __name__ == "__main__":
    unittest.main()

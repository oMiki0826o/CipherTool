"""Test random parameter generation for applicable ciphers."""

import math
import unittest

from cipher_tool.registry import generate_parameters


class RandomParameterTest(unittest.TestCase):
    """Verify generated parameters are accepted by their target ciphers."""

    def test_caesar_shift_is_in_range(self) -> None:
        """Caesar random shifts exclude the identity value."""
        shift = int(generate_parameters("caesar")["shift"])
        self.assertTrue(1 <= shift <= 25)

    def test_affine_parameters_are_valid(self) -> None:
        """Affine random multiplier is invertible modulo 26."""
        parameters = generate_parameters("affine")
        self.assertEqual(math.gcd(int(parameters["a"]), 26), 1)
        self.assertTrue(0 <= int(parameters["b"]) <= 25)

    def test_substitution_is_complete_permutation(self) -> None:
        """Substitution generator produces 26 unique letters."""
        alphabet = generate_parameters("substitution")["substitution_alphabet"]
        self.assertEqual(len(alphabet), 26)
        self.assertEqual(len(set(alphabet)), 26)


if __name__ == "__main__":
    unittest.main()

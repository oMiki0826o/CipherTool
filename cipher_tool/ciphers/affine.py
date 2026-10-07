"""Implement the Affine substitution cipher over the Latin alphabet."""

from math import gcd


def _validate_parameters(a: int, b: int) -> None:
    """Validate the Affine multiplier and offset."""
    if not isinstance(a, int) or isinstance(a, bool) or gcd(a, 26) != 1:
        raise ValueError("a 必須是與 26 互質的整數。")
    if not isinstance(b, int) or isinstance(b, bool):
        raise ValueError("b 必須是整數。")


def _transform(text: str, a: int, b: int) -> str:
    """Apply an Affine transform to ASCII letters."""
    output: list[str] = []
    for character in text:
        if "A" <= character <= "Z":
            output.append(chr((a * (ord(character) - ord("A")) + b) % 26 + ord("A")))
        elif "a" <= character <= "z":
            output.append(chr((a * (ord(character) - ord("a")) + b) % 26 + ord("a")))
        else:
            output.append(character)
    return "".join(output)


def encrypt(text: str, a: int, b: int) -> str:
    """Encrypt text using E(x) = (a*x + b) mod 26."""
    _validate_parameters(a, b)
    return _transform(text, a, b)


def decrypt(text: str, a: int, b: int) -> str:
    """Decrypt text using the modular inverse of a."""
    _validate_parameters(a, b)
    inverse = pow(a, -1, 26)
    return _transform(text, inverse, -inverse * b)

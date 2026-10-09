"""Implement the reciprocal Beaufort cipher."""

from .vigenere import _key_offsets


def _transform(text: str, key: str) -> str:
    """Apply Beaufort's key-minus-text transformation."""
    offsets = _key_offsets(key)
    output: list[str] = []
    key_index = 0
    for character in text:
        if character.isascii() and character.isalpha():
            base = ord("A") if character.isupper() else ord("a")
            output.append(chr((offsets[key_index % len(offsets)] - (ord(character) - base)) % 26 + base))
            key_index += 1
        else:
            output.append(character)
    return "".join(output)


def encrypt(text: str, key: str) -> str:
    """Encrypt text with Beaufort."""
    return _transform(text, key)


def decrypt(text: str, key: str) -> str:
    """Decrypt text with Beaufort's reciprocal operation."""
    return _transform(text, key)

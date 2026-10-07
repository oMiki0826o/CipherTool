"""Implement ROT13 for standard Latin letters."""

from .caesar import decrypt as _caesar_decrypt
from .caesar import encrypt as _caesar_encrypt


def encode(text: str) -> str:
    """Encode text with the fixed ROT13 substitution."""
    return _caesar_encrypt(text, 13)


def decode(text: str) -> str:
    """Decode ROT13 text with the same fixed substitution."""
    return _caesar_decrypt(text, 13)

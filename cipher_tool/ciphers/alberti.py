"""Simulate an Alberti cipher disk with a configurable inner-ring offset."""

from .caesar import decrypt as _caesar_decrypt
from .caesar import encrypt as _caesar_encrypt


def encrypt(text: str, position: int) -> str:
    """Encrypt text using the inner disk's zero-through-twenty-five position."""
    return _caesar_encrypt(text, position)


def decrypt(text: str, position: int) -> str:
    """Decrypt text using the same Alberti disk position."""
    return _caesar_decrypt(text, position)

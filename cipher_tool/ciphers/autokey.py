"""Implement plaintext-autokey Vigenère encryption."""

from .vigenere import _key_offsets


def encrypt(text: str, key: str) -> str:
    """Encrypt text using a seed key extended with plaintext letters."""
    seed = _key_offsets(key)
    plaintext_offsets: list[int] = []
    output: list[str] = []
    for character in text:
        if character.isascii() and character.isalpha():
            base = ord("A") if character.isupper() else ord("a")
            offset = (seed + plaintext_offsets)[len(plaintext_offsets)]
            plain_offset = ord(character) - base
            output.append(chr((plain_offset + offset) % 26 + base))
            plaintext_offsets.append(plain_offset)
        else:
            output.append(character)
    return "".join(output)


def decrypt(text: str, key: str) -> str:
    """Decrypt text by reconstructing the plaintext-backed key stream."""
    seed = _key_offsets(key)
    plaintext_offsets: list[int] = []
    output: list[str] = []
    for character in text:
        if character.isascii() and character.isalpha():
            base = ord("A") if character.isupper() else ord("a")
            offset = (seed + plaintext_offsets)[len(plaintext_offsets)]
            plain_offset = (ord(character) - base - offset) % 26
            output.append(chr(plain_offset + base))
            plaintext_offsets.append(plain_offset)
        else:
            output.append(character)
    return "".join(output)

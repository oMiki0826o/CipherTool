"""Implement a monoalphabetic substitution cipher."""

import string

ALPHABET = string.ascii_uppercase


def _validated_alphabet(substitution_alphabet: str) -> str:
    """Return a normalized, complete substitution alphabet."""
    normalized = substitution_alphabet.upper()
    if len(normalized) != 26 or set(normalized) != set(ALPHABET):
        raise ValueError("替換表必須包含 26 個不重複的英文字母。")
    return normalized


def _transform(text: str, source: str, target: str) -> str:
    """Translate ASCII letters between two same-length alphabets."""
    table = str.maketrans(source + source.lower(), target + target.lower())
    return text.translate(table)


def encrypt(text: str, substitution_alphabet: str) -> str:
    """Encrypt text using a 26-letter substitution alphabet."""
    return _transform(text, ALPHABET, _validated_alphabet(substitution_alphabet))


def decrypt(text: str, substitution_alphabet: str) -> str:
    """Decrypt text using a 26-letter substitution alphabet."""
    normalized = _validated_alphabet(substitution_alphabet)
    return _transform(text, normalized, ALPHABET)

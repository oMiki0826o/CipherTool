"""Implement the paired-letter Kamasutra substitution cipher."""

import string


def _table(pairs: str) -> dict[str, str]:
    """Validate thirteen comma-separated pairs and build a bidirectional table."""
    normalized = [pair.strip().upper() for pair in pairs.split(",")]
    letters = "".join(normalized)
    if len(normalized) != 13 or any(len(pair) != 2 for pair in normalized) or set(letters) != set(string.ascii_uppercase):
        raise ValueError("配對表必須包含 13 組不重複英文字母，例如 AM,BX,...。")
    table: dict[str, str] = {}
    for pair in normalized:
        table[pair[0]] = pair[1]
        table[pair[1]] = pair[0]
    return table


def encrypt(text: str, pairs: str) -> str:
    """Encrypt text by replacing every letter with its configured pair."""
    table = _table(pairs)
    return "".join(table[character.upper()] if character.isascii() and character.isalpha() else character for character in text)


def decrypt(text: str, pairs: str) -> str:
    """Decrypt Kamasutra text with the same paired-letter operation."""
    return encrypt(text, pairs)

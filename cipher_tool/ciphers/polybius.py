"""Implement a standard I/J-merged Polybius square."""

import string

ALPHABET = string.ascii_uppercase.replace("J", "")
ENCODE_TABLE = {letter: f"{index // 5 + 1}{index % 5 + 1}" for index, letter in enumerate(ALPHABET)}
DECODE_TABLE = {code: letter for letter, code in ENCODE_TABLE.items()}


def encode(text: str) -> str:
    """Encode letters as space-separated Polybius coordinates."""
    try:
        return " ".join(ENCODE_TABLE[character] for character in text.upper().replace("J", "I") if character in string.ascii_uppercase)
    except KeyError as error:
        raise ValueError("Polybius 只支援英文字母。") from error


def decode(value: str) -> str:
    """Decode space-separated Polybius coordinates."""
    try:
        return "".join(DECODE_TABLE[token] for token in value.split())
    except KeyError as error:
        raise ValueError("Polybius 座標必須介於 11 到 55。") from error

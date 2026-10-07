"""Implement Bacon's 26-letter A/B binary cipher."""

import string

ALPHABET = string.ascii_uppercase
ENCODE_TABLE = {letter: format(index, "05b").replace("0", "A").replace("1", "B") for index, letter in enumerate(ALPHABET)}
DECODE_TABLE = {code: letter for letter, code in ENCODE_TABLE.items()}


def encode(text: str) -> str:
    """Encode Latin letters into five-character A/B groups."""
    groups: list[str] = []
    for character in text.upper():
        if character in ENCODE_TABLE:
            groups.append(ENCODE_TABLE[character])
        elif character.isspace():
            groups.append("/")
        else:
            raise ValueError("Bacon 只支援英文字母與空白。")
    return " ".join(groups)


def decode(text: str) -> str:
    """Decode space-separated Bacon A/B groups."""
    output: list[str] = []
    for group in text.upper().split():
        if group == "/":
            output.append(" ")
        elif group in DECODE_TABLE:
            output.append(DECODE_TABLE[group])
        else:
            raise ValueError("Bacon 輸入必須是有效的五位 A/B 群組。")
    return "".join(output)

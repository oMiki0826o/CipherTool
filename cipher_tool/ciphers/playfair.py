"""Implement the Playfair cipher with I/J merged into one cell."""

import string

ALPHABET = string.ascii_uppercase.replace("J", "")


def _normalized_letters(value: str) -> str:
    """Keep Latin letters, uppercase them, and merge J into I."""
    return "".join(character for character in value.upper().replace("J", "I") if character in string.ascii_uppercase)


def _square(keyword: str) -> str:
    """Create a row-major 5x5 Playfair square."""
    seen: set[str] = set()
    ordered: list[str] = []
    for character in _normalized_letters(keyword) + ALPHABET:
        if character not in seen:
            seen.add(character)
            ordered.append(character)
    return "".join(ordered)


def _pairs(text: str) -> list[tuple[str, str]]:
    """Split plaintext into Playfair digraphs using X padding."""
    letters = _normalized_letters(text)
    pairs: list[tuple[str, str]] = []
    index = 0
    while index < len(letters):
        first = letters[index]
        second = letters[index + 1] if index + 1 < len(letters) else "X"
        if first == second:
            pairs.append((first, "X" if first != "X" else "Q"))
            index += 1
        else:
            pairs.append((first, second))
            index += 2
    return pairs


def _transform_pair(first: str, second: str, square: str, direction: int) -> str:
    """Transform one Playfair digraph in the requested direction."""
    first_index = square.index(first)
    second_index = square.index(second)
    first_row, first_column = divmod(first_index, 5)
    second_row, second_column = divmod(second_index, 5)
    if first_row == second_row:
        return square[first_row * 5 + (first_column + direction) % 5] + square[second_row * 5 + (second_column + direction) % 5]
    if first_column == second_column:
        return square[((first_row + direction) % 5) * 5 + first_column] + square[((second_row + direction) % 5) * 5 + second_column]
    return square[first_row * 5 + second_column] + square[second_row * 5 + first_column]


def encrypt(text: str, keyword: str) -> str:
    """Encrypt text with Playfair, merging J into I and padding with X."""
    square = _square(keyword)
    return "".join(_transform_pair(first, second, square, 1) for first, second in _pairs(text))


def decrypt(text: str, keyword: str) -> str:
    """Decrypt even-length Playfair ciphertext without removing padding."""
    letters = _normalized_letters(text)
    if len(letters) % 2:
        raise ValueError("Playfair 密文必須包含偶數個英文字母。")
    square = _square(keyword)
    return "".join(_transform_pair(letters[index], letters[index + 1], square, -1) for index in range(0, len(letters), 2))

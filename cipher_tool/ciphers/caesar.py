"""Implement the Caesar substitution cipher for standard Latin letters."""


def _validate_shift(shift: int) -> None:
    """Raise ValueError when shift is outside the supported Caesar range."""
    if not isinstance(shift, int) or isinstance(shift, bool):
        raise ValueError("shift 必須是 0 到 25 的整數。")
    if not 0 <= shift <= 25:
        raise ValueError("shift 必須是 0 到 25 的整數。")


def _shift_text(text: str, shift: int) -> str:
    """Shift ASCII letters and leave all other characters unchanged."""
    shifted_characters: list[str] = []
    for character in text:
        if "A" <= character <= "Z":
            shifted_characters.append(chr((ord(character) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= character <= "z":
            shifted_characters.append(chr((ord(character) - ord("a") + shift) % 26 + ord("a")))
        else:
            shifted_characters.append(character)
    return "".join(shifted_characters)


def encrypt(text: str, shift: int) -> str:
    """Encrypt text with a Caesar shift from 0 through 25."""
    _validate_shift(shift)
    return _shift_text(text, shift)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text with a Caesar shift from 0 through 25."""
    _validate_shift(shift)
    return _shift_text(text, -shift)

"""Implement the Vigenère cipher for standard Latin letters."""


def _key_offsets(key: str) -> list[int]:
    """Return zero-based alphabet offsets for an alphabetic key."""
    if not key or not key.isascii() or not key.isalpha():
        raise ValueError("key 必須是非空白的英文字母。")
    return [ord(character.upper()) - ord("A") for character in key]


def _transform(text: str, key: str, direction: int) -> str:
    """Shift ASCII letters with repeated Vigenère key offsets."""
    offsets = _key_offsets(key)
    output: list[str] = []
    key_index = 0
    for character in text:
        if "A" <= character <= "Z" or "a" <= character <= "z":
            base = ord("A") if character.isupper() else ord("a")
            offset = offsets[key_index % len(offsets)]
            output.append(chr((ord(character) - base + direction * offset) % 26 + base))
            key_index += 1
        else:
            output.append(character)
    return "".join(output)


def encrypt(text: str, key: str) -> str:
    """Encrypt text with an alphabetic Vigenère key."""
    return _transform(text, key, 1)


def decrypt(text: str, key: str) -> str:
    """Decrypt text with an alphabetic Vigenère key."""
    return _transform(text, key, -1)

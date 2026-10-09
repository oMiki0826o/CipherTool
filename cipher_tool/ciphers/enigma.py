"""Simulate Enigma I with rotors I/II/III and reflector B."""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ROTOR_WIRINGS = ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO")
NOTCHES = ("Q", "E", "V")
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


def _positions(value: str) -> list[int]:
    """Validate and convert the three rotor positions."""
    if len(value) != 3 or not value.isascii() or not value.isalpha():
        raise ValueError("恩尼格瑪起始位置必須是三個英文字母，例如 AAA。")
    return [ALPHABET.index(character) for character in value.upper()]


def _forward(value: int, wiring: str, position: int) -> int:
    """Pass a value forward through one rotated rotor."""
    return (ALPHABET.index(wiring[(value + position) % 26]) - position) % 26


def _backward(value: int, wiring: str, position: int) -> int:
    """Pass a value backward through one rotated rotor."""
    return (wiring.index(ALPHABET[(value + position) % 26]) - position) % 26


def encrypt(text: str, positions: str) -> str:
    """Encrypt text using the default historical Enigma I configuration."""
    left, middle, right = _positions(positions)
    output: list[str] = []
    for character in text.upper():
        if character not in ALPHABET:
            output.append(character)
            continue
        middle_at_notch = ALPHABET[middle] == NOTCHES[1]
        right_at_notch = ALPHABET[right] == NOTCHES[2]
        if middle_at_notch:
            left = (left + 1) % 26
        if middle_at_notch or right_at_notch:
            middle = (middle + 1) % 26
        right = (right + 1) % 26
        value = ALPHABET.index(character)
        for wiring, position in zip(reversed(ROTOR_WIRINGS), (right, middle, left)):
            value = _forward(value, wiring, position)
        value = ALPHABET.index(REFLECTOR_B[value])
        for wiring, position in zip(ROTOR_WIRINGS, (left, middle, right)):
            value = _backward(value, wiring, position)
        output.append(ALPHABET[value])
    return "".join(output)


def decrypt(text: str, positions: str) -> str:
    """Decrypt Enigma text; Enigma's electrical path is reciprocal."""
    return encrypt(text, positions)

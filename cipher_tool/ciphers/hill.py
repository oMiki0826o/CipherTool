"""Implement a 2x2 Hill cipher over the 26-letter Latin alphabet."""

from math import gcd


def _matrix(key: str) -> tuple[int, int, int, int]:
    """Parse and validate four comma-separated 2x2 matrix values."""
    try:
        values = tuple(int(value.strip()) % 26 for value in key.split(","))
    except ValueError as error:
        raise ValueError("希爾矩陣必須是四個以逗號分隔的整數。") from error
    if len(values) != 4:
        raise ValueError("希爾矩陣必須是四個以逗號分隔的整數。")
    determinant = (values[0] * values[3] - values[1] * values[2]) % 26
    if gcd(determinant, 26) != 1:
        raise ValueError("希爾矩陣的行列式必須與 26 互質。")
    return values


def _letters(text: str) -> str:
    """Normalize text to uppercase Latin letters and pad to pairs."""
    value = "".join(character for character in text.upper() if "A" <= character <= "Z")
    return value if len(value) % 2 == 0 else value + "X"


def _transform(text: str, matrix: tuple[int, int, int, int]) -> str:
    """Apply a 2x2 matrix to pairs of letter offsets."""
    output: list[str] = []
    for index in range(0, len(text), 2):
        first, second = ord(text[index]) - ord("A"), ord(text[index + 1]) - ord("A")
        output.append(chr((matrix[0] * first + matrix[1] * second) % 26 + ord("A")))
        output.append(chr((matrix[2] * first + matrix[3] * second) % 26 + ord("A")))
    return "".join(output)


def encrypt(text: str, key: str) -> str:
    """Encrypt pairs with an invertible 2x2 Hill matrix."""
    return _transform(_letters(text), _matrix(key))


def decrypt(text: str, key: str) -> str:
    """Decrypt even-length Hill ciphertext with the inverse key matrix."""
    matrix = _matrix(key)
    normalized = _letters(text)
    determinant_inverse = pow((matrix[0] * matrix[3] - matrix[1] * matrix[2]) % 26, -1, 26)
    inverse = (
        determinant_inverse * matrix[3] % 26,
        -determinant_inverse * matrix[1] % 26,
        -determinant_inverse * matrix[2] % 26,
        determinant_inverse * matrix[0] % 26,
    )
    return _transform(normalized, inverse)

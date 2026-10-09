"""Implement Scytale as a fixed-column transposition cipher."""

from .rail_fence import _validate_rails


def encrypt(text: str, columns: int) -> str:
    """Encrypt by writing rows across a virtual Scytale strip."""
    _validate_rails(columns)
    return "".join(text[column::columns] for column in range(columns))


def decrypt(text: str, columns: int) -> str:
    """Decrypt a fixed-column Scytale transposition."""
    _validate_rails(columns)
    base, extra = divmod(len(text), columns)
    lengths = [base + (1 if column < extra else 0) for column in range(columns)]
    sections: list[str] = []
    position = 0
    for length in lengths:
        sections.append(text[position : position + length])
        position += length
    return "".join(sections[column][row] for row in range(base + 1) for column in range(columns) if row < len(sections[column]))

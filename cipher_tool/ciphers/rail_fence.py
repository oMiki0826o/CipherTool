"""Implement the Rail Fence transposition cipher."""


def _validate_rails(rails: int) -> None:
    """Ensure the Rail Fence count is usable."""
    if not isinstance(rails, int) or isinstance(rails, bool) or rails < 2:
        raise ValueError("rails 必須是大於或等於 2 的整數。")


def _rail_indexes(length: int, rails: int) -> list[int]:
    """Return the rail index for each character position."""
    if length == 0:
        return []
    indexes: list[int] = []
    rail = 0
    direction = 1
    for _ in range(length):
        indexes.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return indexes


def encrypt(text: str, rails: int) -> str:
    """Encrypt text by reading its zigzag rail rows in order."""
    _validate_rails(rails)
    rows = ["" for _ in range(rails)]
    for character, rail in zip(text, _rail_indexes(len(text), rails)):
        rows[rail] += character
    return "".join(rows)


def decrypt(text: str, rails: int) -> str:
    """Decrypt text that was written with the Rail Fence cipher."""
    _validate_rails(rails)
    indexes = _rail_indexes(len(text), rails)
    counts = [indexes.count(rail) for rail in range(rails)]
    rows: list[list[str]] = []
    position = 0
    for count in counts:
        rows.append(list(text[position : position + count]))
        position += count
    offsets = [0] * rails
    output: list[str] = []
    for rail in indexes:
        output.append(rows[rail][offsets[rail]])
        offsets[rail] += 1
    return "".join(output)

"""Implement keyword-based columnar transposition."""


def _order(key: str) -> list[int]:
    """Return stable column indexes ordered by key character."""
    if not key or not key.isascii() or not key.isalpha():
        raise ValueError("關鍵字必須是非空白英文字母。")
    return sorted(range(len(key)), key=lambda index: (key.upper()[index], index))


def encrypt(text: str, key: str) -> str:
    """Encrypt by filling rows and reading columns in keyword order."""
    order = _order(key)
    return "".join(text[column::len(key)] for column in order)


def decrypt(text: str, key: str) -> str:
    """Decrypt columnar transposition without padding characters."""
    order = _order(key)
    columns = len(key)
    base, extra = divmod(len(text), columns)
    lengths = [base + (1 if column < extra else 0) for column in range(columns)]
    values = [""] * columns
    position = 0
    for column in order:
        values[column] = text[position : position + lengths[column]]
        position += lengths[column]
    return "".join(values[column][row] for row in range(base + 1) for column in range(columns) if row < len(values[column]))

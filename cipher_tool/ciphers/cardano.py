"""Implement a fixed 4x4 rotating Cardano grille transposition."""

GRID_SIZE = 4
INITIAL_HOLES = ((0, 0), (0, 1), (0, 2), (1, 1))


def _rotated_holes() -> list[tuple[int, int]]:
    """Return the sixteen write/read positions across four clockwise turns."""
    positions: list[tuple[int, int]] = []
    holes = list(INITIAL_HOLES)
    for _ in range(4):
        positions.extend(holes)
        holes = [(column, GRID_SIZE - 1 - row) for row, column in holes]
    return positions


POSITIONS = _rotated_holes()


def encrypt(text: str) -> str:
    """Write text through a 4x4 rotating grille and read the grid by rows."""
    normalized = "".join(character for character in text.upper() if "A" <= character <= "Z")
    if not normalized:
        return ""
    output: list[str] = []
    for start in range(0, len(normalized), 16):
        block = normalized[start : start + 16].ljust(16, "X")
        grid = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for character, (row, column) in zip(block, POSITIONS):
            grid[row][column] = character
        output.extend(character for row in grid for character in row)
    return "".join(output)


def decrypt(text: str) -> str:
    """Read a 4x4 rotating grille ciphertext without removing X padding."""
    normalized = "".join(character for character in text.upper() if "A" <= character <= "Z")
    if len(normalized) % 16:
        raise ValueError("卡爾達諾格欄密文長度必須是 16 的倍數。")
    output: list[str] = []
    for start in range(0, len(normalized), 16):
        block = normalized[start : start + 16]
        grid = [list(block[row * GRID_SIZE : (row + 1) * GRID_SIZE]) for row in range(GRID_SIZE)]
        output.extend(grid[row][column] for row, column in POSITIONS)
    return "".join(output)

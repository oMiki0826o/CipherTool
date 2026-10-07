"""Implement Pigpen cipher with portable Unicode symbol tokens."""

_TOKENS = (
    "┌", "┬", "┐", "├", "┼", "┤", "└", "┴", "┘",
    "┌•", "┬•", "┐•", "├•", "┼•", "┤•", "└•", "┴•", "┘•",
    "⌜", "⌝", "⌟", "⌞", "⌜•", "⌝•", "⌟•", "⌞•",
)
ENCODE_TABLE = {chr(ord("A") + index): token for index, token in enumerate(_TOKENS)}
DECODE_TABLE = {token: letter for letter, token in ENCODE_TABLE.items()}


def encode(text: str) -> str:
    """Encode letters as whitespace-separated portable Pigpen tokens."""
    tokens: list[str] = []
    for character in text.upper():
        if character in ENCODE_TABLE:
            tokens.append(ENCODE_TABLE[character])
        elif character.isspace():
            tokens.append("/")
        else:
            raise ValueError("Pigpen 只支援英文字母與空白。")
    return " ".join(tokens)


def decode(text: str) -> str:
    """Decode whitespace-separated Pigpen Unicode tokens."""
    output: list[str] = []
    for token in text.split():
        if token == "/":
            output.append(" ")
        elif token in DECODE_TABLE:
            output.append(DECODE_TABLE[token])
        else:
            raise ValueError("Pigpen 輸入包含無效符號。")
    return "".join(output)

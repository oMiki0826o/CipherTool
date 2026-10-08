"""Convert text to and from UTF-8 bytes, ASCII, and Unicode code points."""


def text_to_binary(value: str) -> str:
    """Encode UTF-8 text as space-separated eight-bit bytes."""
    return " ".join(f"{byte:08b}" for byte in value.encode("utf-8"))


def binary_to_text(value: str) -> str:
    """Decode whitespace-separated eight-bit UTF-8 bytes."""
    tokens = value.split()
    if any(len(token) != 8 or set(token) - {"0", "1"} for token in tokens):
        raise ValueError("Binary 輸入必須是以空白分隔的八位元 bytes。")
    try:
        return bytes(int(token, 2) for token in tokens).decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError("Binary 輸入不是有效的 UTF-8 bytes。") from error


def text_to_hex(value: str) -> str:
    """Encode UTF-8 text as uppercase hexadecimal bytes."""
    return value.encode("utf-8").hex().upper()


def hex_to_text(value: str) -> str:
    """Decode hexadecimal UTF-8 bytes into text."""
    try:
        return bytes.fromhex(value).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as error:
        raise ValueError("Hex 輸入不是有效的 UTF-8 bytes。") from error


def text_to_ascii(value: str) -> str:
    """Convert ASCII-only text to decimal character codes."""
    try:
        value.encode("ascii")
    except UnicodeEncodeError as error:
        raise ValueError("ASCII 轉換只支援 ASCII 範圍的字元。") from error
    return " ".join(str(ord(character)) for character in value)


def ascii_to_text(value: str) -> str:
    """Convert whitespace-separated ASCII decimal codes into text."""
    try:
        codes = [int(token) for token in value.split()]
    except ValueError as error:
        raise ValueError("ASCII 輸入必須是以空白分隔的十進位數值。") from error
    if any(not 0 <= code <= 127 for code in codes):
        raise ValueError("ASCII 數值必須介於 0 到 127。")
    return "".join(chr(code) for code in codes)


def text_to_code_points(value: str) -> str:
    """Convert text to whitespace-separated U+ hexadecimal code points."""
    return " ".join(f"U+{ord(character):04X}" for character in value)


def code_points_to_text(value: str) -> str:
    """Convert whitespace-separated U+ hexadecimal code points to text."""
    characters: list[str] = []
    for token in value.split():
        if not token.upper().startswith("U+"):
            raise ValueError("Unicode Code Point 必須使用 U+XXXX 格式。")
        try:
            code_point = int(token[2:], 16)
            characters.append(chr(code_point))
        except (ValueError, OverflowError) as error:
            raise ValueError("Unicode Code Point 格式無效。") from error
    return "".join(characters)

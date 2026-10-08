"""Convert signed integers between bases two through thirty-six."""

import string

SYMBOLS = string.digits + string.ascii_uppercase


def _validate_base(base: int) -> None:
    """Require a base in the supported range."""
    if not isinstance(base, int) or isinstance(base, bool) or not 2 <= base <= 36:
        raise ValueError("進位必須是 2 到 36 的整數。")


def convert_base(value: str, from_base: int, to_base: int) -> str:
    """Convert a signed integer string from one base to another."""
    _validate_base(from_base)
    _validate_base(to_base)
    normalized = value.strip().upper()
    if not normalized:
        raise ValueError("數值不可為空白。")
    sign = ""
    if normalized[0] in "+-":
        sign, normalized = normalized[0], normalized[1:]
    if not normalized:
        raise ValueError("數值格式無效。")
    allowed = set(SYMBOLS[:from_base])
    if any(character not in allowed for character in normalized):
        raise ValueError(f"輸入包含不適用於 {from_base} 進位的字元。")
    decimal_value = int(("-" if sign == "-" else "") + normalized, from_base)
    if decimal_value == 0:
        return "0"
    result: list[str] = []
    remainder_value = abs(decimal_value)
    while remainder_value:
        remainder_value, digit = divmod(remainder_value, to_base)
        result.append(SYMBOLS[digit])
    return ("-" if decimal_value < 0 else "") + "".join(reversed(result))

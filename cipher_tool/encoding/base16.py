"""Encode and decode UTF-8 text as Base16 hexadecimal."""

import base64


def encode(text: str) -> str:
    """Encode UTF-8 text into uppercase hexadecimal characters."""
    return base64.b16encode(text.encode("utf-8")).decode("ascii")


def decode(value: str) -> str:
    """Decode Base16 hexadecimal text into UTF-8 text."""
    try:
        return base64.b16decode(value.upper(), casefold=True).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as error:
        raise ValueError("Base16 輸入格式無效。") from error

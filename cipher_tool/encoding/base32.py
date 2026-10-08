"""Encode and decode UTF-8 text as Base32."""

import base64


def encode(text: str) -> str:
    """Encode UTF-8 text into Base32."""
    return base64.b32encode(text.encode("utf-8")).decode("ascii")


def decode(value: str) -> str:
    """Decode Base32 text into UTF-8 text."""
    try:
        return base64.b32decode(value, casefold=True).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as error:
        raise ValueError("Base32 輸入格式無效。") from error

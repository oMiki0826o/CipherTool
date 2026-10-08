"""Encode and decode UTF-8 text as Base64."""

import base64


def encode(text: str) -> str:
    """Encode UTF-8 text into Base64."""
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode(value: str) -> str:
    """Decode validated Base64 text into UTF-8 text."""
    try:
        return base64.b64decode(value, validate=True).decode("utf-8")
    except (ValueError, UnicodeDecodeError) as error:
        raise ValueError("Base64 輸入格式無效，請確認內容與 padding。") from error

"""Encode and decode URL percent-encoded text using the standard library."""

from urllib.parse import quote, unquote


def encode(text: str) -> str:
    """Percent-encode text for safe URL use."""
    return quote(text, safe="")


def decode(value: str) -> str:
    """Decode percent-encoded URL text."""
    return unquote(value)

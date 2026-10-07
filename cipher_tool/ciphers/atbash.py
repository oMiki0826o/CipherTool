"""Implement the fixed Atbash alphabet reversal."""


def _transform(text: str) -> str:
    """Reverse ASCII letters while preserving case and other characters."""
    output: list[str] = []
    for character in text:
        if "A" <= character <= "Z":
            output.append(chr(ord("Z") - (ord(character) - ord("A"))))
        elif "a" <= character <= "z":
            output.append(chr(ord("z") - (ord(character) - ord("a"))))
        else:
            output.append(character)
    return "".join(output)


def encrypt(text: str) -> str:
    """Encrypt text with Atbash."""
    return _transform(text)


def decrypt(text: str) -> str:
    """Decrypt text with Atbash."""
    return _transform(text)

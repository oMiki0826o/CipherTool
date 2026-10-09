"""Provide checksums and hashes for data-integrity learning tools."""

import hashlib
import re
import zlib


def _digits(value: str, length: int) -> str:
    """Normalize a numeric identifier and require the requested length."""
    normalized = value.replace("-", "").replace(" ", "")
    if len(normalized) != length or not normalized.isdigit():
        raise ValueError(f"輸入必須包含 {length} 個數字。")
    return normalized


def isbn10_check_digit(value: str) -> str:
    """Calculate the check digit for the first nine ISBN-10 digits."""
    digits = _digits(value, 9)
    remainder = (11 - sum((10 - index) * int(digit) for index, digit in enumerate(digits)) % 11) % 11
    return "X" if remainder == 10 else str(remainder)


def isbn13_check_digit(value: str) -> str:
    """Calculate the check digit for the first twelve ISBN-13 digits."""
    digits = _digits(value, 12)
    total = sum(int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(digits))
    return str((10 - total % 10) % 10)


def luhn_check_digit(value: str) -> str:
    """Calculate a Luhn check digit for a number without its final digit."""
    digits = _digits(value, len(value.replace(" ", "").replace("-", "")))
    total = 0
    for index, digit in enumerate(reversed(digits), start=1):
        number = int(digit)
        if index % 2:
            number *= 2
            number -= 9 if number > 9 else 0
        total += number
    return str((10 - total % 10) % 10)


def luhn_is_valid(value: str) -> bool:
    """Return whether a number including its final digit passes Luhn."""
    digits = _digits(value, len(value.replace(" ", "").replace("-", "")))
    return luhn_check_digit(digits[:-1]) == digits[-1]


def xor_checksum(value: str) -> str:
    """Return the two-digit uppercase XOR checksum of UTF-8 bytes."""
    result = 0
    for byte in value.encode("utf-8"):
        result ^= byte
    return f"{result:02X}"


def parity_bit(bits: str, mode: str = "even") -> str:
    """Return the parity bit required for even or odd parity."""
    if not bits or set(bits) - {"0", "1"} or mode not in {"even", "odd"}:
        raise ValueError("請輸入二進位資料，模式只能是 even 或 odd。")
    ones = bits.count("1")
    return str(ones % 2 if mode == "even" else 1 - ones % 2)


def crc3(hex_value: str) -> str:
    """Calculate non-reflected CRC-3 using generator 0xB for hexadecimal data."""
    if not hex_value or re.search(r"[^0-9A-Fa-f]", hex_value):
        raise ValueError("CRC-3 輸入必須是十六進位字串。")
    bits = "".join(f"{int(character, 16):04b}" for character in hex_value) + "000"
    generator = "1011"
    work = list(bits)
    for index in range(len(bits) - 3):
        if work[index] == "1":
            for offset, bit in enumerate(generator):
                work[index + offset] = "0" if work[index + offset] == bit else "1"
    return str(int("".join(work[-3:]), 2))


def crc8(value: str) -> str:
    """Calculate non-reflected CRC-8 with polynomial 0x07."""
    result = 0
    for byte in value.encode("utf-8"):
        result ^= byte
        for _ in range(8):
            result = ((result << 1) ^ 0x07) & 0xFF if result & 0x80 else (result << 1) & 0xFF
    return f"{result:02X}"


def crc16(value: str) -> str:
    """Calculate CRC-16/CCITT-FALSE for UTF-8 text."""
    result = 0xFFFF
    for byte in value.encode("utf-8"):
        result ^= byte << 8
        for _ in range(8):
            result = ((result << 1) ^ 0x1021) & 0xFFFF if result & 0x8000 else (result << 1) & 0xFFFF
    return f"{result:04X}"


def crc32(value: str) -> str:
    """Calculate standard CRC-32 for UTF-8 text."""
    return f"{zlib.crc32(value.encode('utf-8')) & 0xFFFFFFFF:08X}"


def sha256(value: str) -> str:
    """Return the SHA-256 digest of UTF-8 text."""
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

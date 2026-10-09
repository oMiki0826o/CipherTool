"""Register CipherTool operations and dispatch them through stable APIs."""

import secrets
import string
from typing import Callable

from .ciphers import alberti, affine, atbash, autokey, bacon, beaufort, caesar, columnar, hill, kamasutra, pigpen, playfair, polybius, rail_fence, rot13, scytale, substitution, vigenere
from .conversion import number_base, text
from .encoding import base16, base32, base64_codec, morse, url_encoding

ToolRunner = Callable[[str, str, dict[str, str]], str]


def _cipher_runner(module: object, mode: str, value: str, parameters: dict[str, str], names: tuple[str, ...] = ()) -> str:
    """Call a cipher module after converting its configured parameters."""
    function = getattr(module, mode)
    arguments: list[object] = [value]
    for name in names:
        arguments.append(int(parameters[name]) if name in {"shift", "a", "b", "rails", "columns", "position"} else parameters[name])
    return function(*arguments)


TOOLS: dict[str, dict[str, object]] = {
    "caesar": {"name": "Caesar Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("shift",), "runner": lambda m, v, p: _cipher_runner(caesar, m, v, p, ("shift",))},
    "rot13": {"name": "ROT13", "category": "Classical Cipher", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(rot13, m, v, p)},
    "atbash": {"name": "Atbash", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(atbash, m, v, p)},
    "affine": {"name": "Affine Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("a", "b"), "runner": lambda m, v, p: _cipher_runner(affine, m, v, p, ("a", "b"))},
    "vigenere": {"name": "Vigenère Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("key",), "runner": lambda m, v, p: _cipher_runner(vigenere, m, v, p, ("key",))},
    "substitution": {"name": "Simple Substitution", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("substitution_alphabet",), "runner": lambda m, v, p: _cipher_runner(substitution, m, v, p, ("substitution_alphabet",))},
    "rail_fence": {"name": "Rail Fence Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("rails",), "runner": lambda m, v, p: _cipher_runner(rail_fence, m, v, p, ("rails",))},
    "playfair": {"name": "Playfair Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("keyword",), "runner": lambda m, v, p: _cipher_runner(playfair, m, v, p, ("keyword",))},
    "bacon": {"name": "Bacon Cipher", "category": "Classical Cipher", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(bacon, m, v, p)},
    "pigpen": {"name": "Pigpen Cipher", "category": "Classical Cipher", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(pigpen, m, v, p)},
    "polybius": {"name": "Polybius Square", "category": "Classical Cipher", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(polybius, m, v, p)},
    "beaufort": {"name": "Beaufort Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("key",), "runner": lambda m, v, p: _cipher_runner(beaufort, m, v, p, ("key",))},
    "columnar": {"name": "Columnar Transposition", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("key",), "runner": lambda m, v, p: _cipher_runner(columnar, m, v, p, ("key",))},
    "scytale": {"name": "Scytale", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("columns",), "runner": lambda m, v, p: _cipher_runner(scytale, m, v, p, ("columns",))},
    "autokey": {"name": "Autokey Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("key",), "runner": lambda m, v, p: _cipher_runner(autokey, m, v, p, ("key",))},
    "kamasutra": {"name": "Kamasutra Cipher", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("pairs",), "runner": lambda m, v, p: _cipher_runner(kamasutra, m, v, p, ("pairs",))},
    "hill": {"name": "Hill Cipher (2×2)", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("matrix",), "runner": lambda m, v, p: _cipher_runner(hill, m, v, p, ("matrix",))},
    "alberti": {"name": "Alberti Cipher Disk", "category": "Classical Cipher", "modes": ("encrypt", "decrypt"), "parameters": ("position",), "runner": lambda m, v, p: _cipher_runner(alberti, m, v, p, ("position",))},
    "base16": {"name": "Base16 / Hex", "category": "Encoding", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(base16, m, v, p)},
    "base32": {"name": "Base32", "category": "Encoding", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(base32, m, v, p)},
    "base64": {"name": "Base64", "category": "Encoding", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(base64_codec, m, v, p)},
    "morse": {"name": "Morse Code", "category": "Encoding", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(morse, m, v, p)},
    "url": {"name": "URL Encoding", "category": "Encoding", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: _cipher_runner(url_encoding, m, v, p)},
    "number_base": {"name": "Number Base", "category": "Number Conversion", "modes": ("convert",), "parameters": ("from_base", "to_base"), "runner": lambda m, v, p: number_base.convert_base(v, int(p["from_base"]), int(p["to_base"]))},
    "text_hex": {"name": "Text ↔ Hex", "category": "Text Conversion", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: text.text_to_hex(v) if m == "encode" else text.hex_to_text(v)},
    "text_binary": {"name": "Text ↔ Binary", "category": "Text Conversion", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: text.text_to_binary(v) if m == "encode" else text.binary_to_text(v)},
    "text_ascii": {"name": "Text ↔ ASCII", "category": "Text Conversion", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: text.text_to_ascii(v) if m == "encode" else text.ascii_to_text(v)},
    "code_points": {"name": "Unicode Code Point", "category": "Text Conversion", "modes": ("encode", "decode"), "parameters": (), "runner": lambda m, v, p: text.text_to_code_points(v) if m == "encode" else text.code_points_to_text(v)},
}


def run_tool(tool_id: str, mode: str, value: str, parameters: dict[str, str]) -> str:
    """Run a registered tool with validated identifier and mode."""
    tool = TOOLS.get(tool_id)
    if tool is None:
        raise ValueError("找不到指定工具。")
    if mode not in tool["modes"]:
        raise ValueError("此工具不支援指定模式。")
    return tool["runner"](mode, value, parameters)


def generate_parameters(tool_id: str) -> dict[str, str]:
    """Generate secure random parameters for ciphers that support them."""
    if tool_id == "caesar":
        return {"shift": str(secrets.randbelow(25) + 1)}
    if tool_id == "affine":
        multiplier = secrets.choice((1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25))
        return {"a": str(multiplier), "b": str(secrets.randbelow(26))}
    if tool_id == "vigenere":
        return {"key": "".join(secrets.choice(string.ascii_uppercase) for _ in range(8))}
    if tool_id == "substitution":
        letters = list(string.ascii_uppercase)
        secrets.SystemRandom().shuffle(letters)
        return {"substitution_alphabet": "".join(letters)}
    if tool_id == "playfair":
        return {"keyword": "".join(secrets.choice(string.ascii_uppercase) for _ in range(8))}
    raise ValueError("此工具不支援隨機參數。")

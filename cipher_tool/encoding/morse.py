"""Encode and decode International Morse code with stable separators."""

MORSE_TABLE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
}
REVERSE_TABLE = {code: character for character, code in MORSE_TABLE.items()}


def encode(text: str) -> str:
    """Encode text with spaces between symbols and slash between words."""
    words: list[str] = []
    for word in text.upper().split():
        try:
            words.append(" ".join(MORSE_TABLE[character] for character in word))
        except KeyError as error:
            raise ValueError(f"Morse 不支援字元：{error.args[0]}") from error
    return " / ".join(words)


def decode(value: str) -> str:
    """Decode Morse with spaces between symbols and slash between words."""
    words: list[str] = []
    for word in value.strip().split("/"):
        try:
            words.append("".join(REVERSE_TABLE[token] for token in word.split()))
        except KeyError as error:
            raise ValueError(f"Morse 輸入包含無效符號：{error.args[0]}") from error
    return " ".join(words)

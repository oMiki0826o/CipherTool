# CipherTool

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

[中文](#中文) | [English](#english)

---

## 中文

## 關於

CipherTool 是一個使用 Python 製作的輕量工具，目標是提供古典密碼、常用編碼、進位轉換與文字轉換功能，適合學習、歷史研究、解題與一般文字處理。

## 功能

- 古典密碼：Caesar、ROT13、Atbash、Affine、Vigenère、Beaufort、Autokey、Simple Substitution、Pigpen、Polybius、Rail Fence、Columnar Transposition、Scytale、Playfair、Bacon、Kamasutra、Hill、Alberti、Cardano Grille、Enigma I。
- 編碼：Base16、Base32、Base64、Morse、URL Encoding。
- 轉換：2～36 進位、UTF-8 Text ↔ Binary、Text ↔ Hex、Text ↔ ASCII、Unicode Code Point。
- 完整性檢查：ISBN-10／13、Luhn、XOR、Parity、CRC-3／8／16／32、SHA-256。
- Tkinter 圖形介面：依類型與方法顯示模式和參數，支援執行、複製與清除。

## 安裝與啟動

需要 Python 3.10 以上版本，且目前不需要第三方 runtime 套件。

```bash
python main.py
```

也可以安裝成套件後使用 `ciphertool` 指令。

詳細原理與格式規則請見 [docs/README.md](./docs/README.md)。

## 安全性提醒

本專案不是現代密碼學函式庫。Caesar、Vigenère、ROT13、Base64、Morse 等功能不適合保護密碼、個資、Token、金鑰或其他敏感資料。

## 授權

本專案採用 MIT License，詳見 [LICENSE](./LICENSE)。

---

## English

### About

CipherTool is a lightweight Python tool for classical ciphers, common encodings, number-base conversion, and text conversion. It is intended for learning, historical research, puzzle solving, and general text processing.

### Features

- Classical ciphers: Caesar, ROT13, Atbash, Affine, Vigenère, Beaufort, Autokey, Simple Substitution, Pigpen, Polybius, Rail Fence, Columnar Transposition, Scytale, Playfair, Bacon, Kamasutra, Hill, Alberti, Cardano Grille, and Enigma I.
- Encodings: Base16, Base32, Base64, Morse, and URL Encoding.
- Conversions: bases 2 through 36, UTF-8 Text ↔ Binary, Text ↔ Hex, Text ↔ ASCII, and Unicode code points.
- Integrity checks: ISBN-10/13, Luhn, XOR, parity, CRC-3/8/16/32, and SHA-256.
- Tkinter GUI with dynamic tool parameters, execute, copy, and clear actions.

### Install and run

Python 3.10 or newer is required. No third-party runtime dependencies are currently needed.

```bash
python main.py
```

After installing the package, the `ciphertool` command is also available.

See [docs/README.md](./docs/README.md) for format rules and learning notes.

### Security notice

This project is not a modern cryptography library. Caesar, Vigenère, ROT13, Base64, Morse, and similar features are not suitable for protecting passwords, personal data, tokens, keys, or other sensitive information.

### License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).

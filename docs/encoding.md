# 編碼與文字轉換

Encoding 是讓資料以另一種格式表示，不提供保密性。Base16、Base32、Base64、Morse 與 URL Encoding 都不是 Encryption。

- Base16 / Base32 / Base64：將 UTF-8 文字轉為可傳輸的 ASCII 表示。
- URL Encoding：以標準百分比編碼處理 URL 文字。
- Text ↔ Binary 與 Text ↔ Hex：以 UTF-8 bytes 表示，因此一個中文字符可能占多個 bytes。
- Text ↔ ASCII：只接受 ASCII 範圍。
- Unicode Code Point：使用 `U+0041`、`U+4E2D` 形式。

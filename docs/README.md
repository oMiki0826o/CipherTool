# CipherTool 學習 Wiki

這裡是 CipherTool 的公開學習入口。內容以「目前程式實際支援的規則」為準，適合用來理解歷史密碼、手算小例子與解題流程；它們不是保護密碼、個資、Token 或金鑰的現代加密方案。

## 從這裡開始

- [古典密碼百科](./ciphers/index.md)：二十種密碼的獨立教學頁，包含歷史、原理、數學表示、手算、破解思路與程式操作。
- [編碼工具](./encoding/index.md)：Base16、Base32、Base64、摩斯電碼與 URL Encoding 的用途與格式。
- [文字與進位轉換](./conversion/index.md)：2～36 進位、Binary、Hex、ASCII 與 Unicode 的轉換說明。
- [完整性檢查與雜湊](./integrity/index.md)：ISBN、Luhn、XOR、Parity、CRC 與 SHA-256；它們用於偵錯、識別或驗證，並非加密。

## 閱讀方式

古典密碼頁面會先交代它怎麼把明文變成密文，再說明如何反向還原。每頁都附有小型例子和 CipherTool 的對應參數。不同資料型態有不同限制：有些演算法只處理英文字母，有些會保留空白與標點，有些則會捨去非字母；請以各頁「CipherTool 操作」段落為準。

若想先掌握整體安全觀念，請閱讀 [Kerckhoffs 原則](./kerckhoffs-principle.md) 與 [安全性說明](./security-notes.md)。

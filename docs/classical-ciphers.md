# 古典密碼

CipherTool 提供 Caesar、ROT13、Atbash、Affine、Vigenère、Simple Substitution、Pigpen、Rail Fence、Playfair 與 Bacon。它們是歷史、教學和解題用途的文字轉換方式，不是現代安全加密。

- Caesar：以 0～25 的位移取代英文字母。
- ROT13：固定位移 13；轉換兩次會回到原文。
- Atbash：將字母表反向對應；加密與解密相同。
- Affine：使用 `a`、`b`，其中 `a` 必須和 26 互質。
- Vigenère：用重複的英文字母 key 決定位移。
- Simple Substitution：使用完整且不重複的 26 字母替換表。
- Pigpen：以固定 Unicode 符號 token 表示字母；token 以空白分隔。
- Rail Fence：以 rails 數量將字元交錯排列。
- Playfair：使用 5×5 方陣，I/J 合併為 I；重複字母和奇數結尾使用 X 補位。
- Bacon：使用五位 A/B 群組，採 26 字母版本。

除非另有說明，這些演算法只處理標準英文字母；其他字元保留或由該工具拒絕。

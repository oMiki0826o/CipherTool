# 古典密碼

CipherTool 提供 Caesar、ROT13、Atbash、Affine、Vigenère、Beaufort、Autokey、Simple Substitution、Pigpen、Polybius、Rail Fence、Columnar Transposition、Scytale、Playfair、Bacon、Kamasutra、Hill、Alberti、Cardano Grille 與 Enigma I。它們是歷史、教學和解題用途的文字轉換方式，不是現代安全加密。

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
- Polybius：以 5×5 方格的行號與列號表示字母，I/J 合併。
- Columnar Transposition：以關鍵字決定欄位讀取順序。
- Scytale：以固定欄位數模擬將紙條纏繞在密碼棒上。
- Beaufort：使用 key 減去明文字母；同一流程可加密與解密。
- Autokey：用 seed key 開始，再以明文本身延伸 key。
- Kamasutra：依使用者提供的 13 組字母配對互換字母。
- Hill：目前支援 2×2 可逆矩陣，例如 `3,3,2,5`。
- Alberti：以內圈位置模擬兩個旋轉字母盤。
- Cardano Grille：固定 4×4 旋轉格欄；不足一格的文字以 X 補位。
- Enigma I：固定 Rotor I/II/III 與 Reflector B，可設定三個轉子起始位置。

除非另有說明，這些演算法只處理標準英文字母；其他字元保留或由該工具拒絕。

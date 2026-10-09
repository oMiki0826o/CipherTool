# Kerckhoffs 原則

Kerckhoffs 原則指出：密碼系統的安全性不應建立在攻擊者不知道演算法。演算法可以公開；真正需要保護的是 key。

這也是古典密碼不適合現代保密需求的原因：即使 key 未知，Caesar、Vigenère 等演算法的結構仍很容易被暴力嘗試或統計分析破解。把演算法藏起來（security through obscurity）不能取代經過公開審查的現代密碼學。

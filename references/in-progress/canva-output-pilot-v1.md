# CANVA-OUTPUT-PILOT-V1 (Definition Correction-2 / Scope Rebaseline)

Target PR: `#15`
Baseline before Correction-1: `547a9dad9a252bebc676e016c3174a18e3a7d041`
Correction State: `Current PR HEAD`

---

## 1. 目的 & 再定義（Rebaseline）

HTML-first による V3.5 / V3.6 のポスター表現は「Web UIをA4に並べた見た目」となってしまい、Human Visual Review で不採用となりました。
今後は **ChatGPT生成案を Primary Visual Reference（主要な視覚参考基準）** とし、**Canva-first で「一枚の完成された掲示ポスター」として構成**する検証へ切り替えます。

---

## 2. 責務構造 (Authority & Reference Split)

| 役割 | 対象・ツール | 保持・管理内容 |
|---|---|---|
| **Content Authority + Guardrails** | **GitHub** | **内容の正本＋制約基準**<br>・コピー・本文文章<br>・3つの観察例<br>・安全文言・注記<br>・QR固定宛先 (`https://hitokoto-kaeshi-preview.web.app/poster`)<br>・Foundation / アクセシビリティガードレール |
| **Primary Visual Reference** | **ChatGPT生成案** | **主要視覚参考基準（※正本ではない）**<br>・構図・手描き感・視線誘導の全体イメージ<br>・紙面の一体感・空気感の参考資料 |
| **Visual Production Surface** | **Canva** | **視覚制作・レイアウトの場**<br>・実際のデザイン制作・グラフィックレイアウト<br>・タイポグラフィ、イラスト・吹き出しの配置<br>・PDF / PNG プレビュー出力 |

---

## 3. Visual Reference 指針 (ChatGPT案の採用とリファイン)

### KEEP from Reference (引き継ぐ要素)
- 強い見出しタイトルと手描き感
- 控えめな黄色の一本線アクセント
- リズムのある吹き出し形状
- 中央 QR 行動導線
- 人物・植物・背景紙面が一体化したトーン＆マナー

### REFINE (リファイン・引き算要件)
- **URL削除:** 長い URL は削除し **QR 一本化**
- **植物量:** 植物のあしらいをすっきり減らす
- **人物表現:** 案内係の可愛いお姉さんではなく、大人っぽく自然な「日常の観察者」へ寄せる
- **装飾削減:** ChatGPT 案から装飾を **約 30% 引き算** し、静かさを保つ
- **内容の準拠:** 安全文言や文言は GitHub 正本に厳密に従う

> **基本原則:** 「V3.5 を装飾する」のではなく、「ChatGPT Reference を約 30% リファインする」。

---

## 4. 新実行順 (NEW GATE ORDER)

```text
1. Content Authority readback (GitHub 正本文言の確認)
↓
2. Canva-first Visual Direction Lock (デザイン方向性ロック)
↓
3. Canva Implementation Pilot (Canva 上での実制作試行)
↓
4. Canva A4 preview (A4 プレビュー出力)
↓
5. Human Visual Review (目視評価)
↓
6. Human Visual Acceptance (視覚承認)
↓
7. Physical A4 / real-device QR validation (実寸A4・実機QR検証)
↓
8. Print / Post decision (印刷・掲示判定)
↓
9. Reuse decision (再利用判定)
```

---

## 5. PR #14 の扱い

- Merge candidate としては **HOLD** とします。
- HTML-first 失敗例 / Comparison Evidence として保持し、Canva output が Accepted になるまでは close しません。

---

## 6. Current HOLD & Lock Status

- Human Definition / Scope Lock (**REBIND REQUIRED**)
- Canva Implementation Pilot (**NOT AUTHORIZED / 未承認**)
- Human Visual Acceptance (**未承認**)
- Physical A4 / real-device QR validation (**未承認**)
- Print / Post (**HOLD**)
- Deploy / Real Trial (**HOLD**)
- Promotion (**HOLD**)

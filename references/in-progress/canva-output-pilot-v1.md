# CANVA-OUTPUT-PILOT-V1

## 目的

CanvaをDesign Foundationの正本にせず、チラシ・ポスターの制作実装先として使えるかを最小実案件で検証します。

## 前提

基準の正本は既存のDesign Foundationに置きます。

Canva固有のルールは、検証段階ではFoundationへ追加しません。

現在の比較対象は `references/in-progress/hitokoto-poster-v3/` です。

## Scope IN

- Canvaを制作・編集・PDF / PNG出力の実装先として評価する。
- `patterns/flyer.md`、既存Foundations、`review/visual-review.md` を判断基準として使う。
- 最初の対象は「ひとこと返し」A4制作物1件に限定する。
- Canva版では、Content Lock後の文言と必須情報を勝手に変更しない。
- Canva版と既存V3を並べてVisual Reviewする。
- Human Visual Acceptanceを通過した場合だけ、Accepted Reference候補として扱う。

## Scope OUT / HOLD

- Figma / Canva同期。
- Canva固有ルールのFoundation化。
- `canva/` ディレクトリ新設。
- 複数のBrand Templateを先に作ること。
- Autofillや自動差し込み。
- Canva版の自動採用。
- Print / Post。
- Deploy / Real Trial。
- Pattern / Prompt / Foundation promotion。

## 実行順

```text
Current V3 exact-state readback
↓
Human Visual Acceptance for current V3 candidate
↓
Physical A4 / QR validation
↓
Canva implementation pilot
↓
Side-by-side Visual Review
↓
Human Visual Acceptance for Canva output
↓
Reuse decision
↓
Brand Template consideration
```

## Canva版で固定するもの

- 用紙サイズはA4縦とする。
- 最初に見る場所を一つにする。
- 主見出しの周囲に余白を確保する。
- QRコードを他の情報から分離する。
- イラストは本文やQR導線を圧迫しない。
- 情報量を増やすために装飾を追加しない。

## 比較時に確認するもの

1. 情報階層が既存V3より崩れていないか。
2. 余白と情報量のバランスが維持されているか。
3. QR導線が弱くなっていないか。
4. イラストが主役になっていないか。
5. 印刷時にA4一枚へ収まるか。
6. Canvaで職員が文字、写真、QRを差し替えやすいか。

## 再利用判定

Canva版が一度Acceptedになっただけでは、Brand Templateへ昇格させません。

同じ構造を複数回使い、差し替え中心で運用できることを確認してから別ゲートで判断します。

## 次のHuman Gate

`CANVA-OUTPUT-PILOT-V1 Human Definition / Scope Lock GO`

この文書は、Canva生成、印刷、掲示、Deploy、Pattern / Prompt / Foundation promotionを承認しません。

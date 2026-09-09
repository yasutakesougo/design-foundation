# Human Visual Acceptance Checklist

- PR: #75
- HEAD: `83dbfa4e14df6af0d0738b6ff747e41f423a29df`
- 前提: Fresh Correction Implementation Review = PASS
- 現時点判定: Human Visual Acceptance = HOLD

## 確認依頼文

以下の3点について、通常サイズと64px相当の両方を見て判定してください。

対象

```text
メモを取る人
考える人
眺める人
```

比較画像

```text
reviews/pilot_gesture_comparison_normal_and_64px.png
reviews/pilot_gesture_comparison_normal_size.png
reviews/pilot_gesture_comparison_64px.png
```

見てほしい点

1. ラベルなしでも3役割を区別できるか
2. 64pxでも各人物の主要ジェスチャーが最低1つ分かるか
3. 髪型や服装ではなく、ポーズ、手、道具、頭部方向、視線方向で意味が成立しているか
4. 既存の線画スタイル
   - 線色
   - 線幅
   - 丸い線端
   - 余白量
   - 顔の簡潔さ
   が大きく崩れていないか

判定

```text
PASS / HOLD
```

気になった点があれば、そのまま短く書いてください。

## 判定テンプレート

```text
同じシリーズに見える                 = PASS / HOLD
メモが分かる                         = PASS / HOLD
考えるが分かる                       = PASS / HOLD
眺めるが分かる                       = PASS / HOLD
64pxで意味が残る                     = PASS / HOLD
髪型差に依存していない               = PASS / HOLD
Line Style Foundationを維持している  = PASS / HOLD
総合判定                             = PASS / HOLD
コメント                             =
```

## 主要ジェスチャー確認基準

```text
note-taking = 紙 / 斜めペン / 書く手
thinking    = 顎に触れる手 / 前腕
looking     = 横向き頭部 / 横視線
```

## Gate

Human Visual Acceptance が PASS になるまで、次は HOLD のままです。

```text
Remaining 7 SVGs = HOLD
Merge            = HOLD
Promotion        = HOLD
```

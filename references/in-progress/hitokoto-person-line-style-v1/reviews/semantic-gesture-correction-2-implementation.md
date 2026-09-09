# Semantic Gesture Correction-2 Implementation Note

- PR: #75
- Base review: Human Visual Acceptance HOLD / CONSUMED (Correction-1)
- Scope: existing 3 pilot SVGs only
- Status: IMPLEMENTED / READY FOR FRESH REVIEW

## Changed files

```text
examples/person-note-taking.svg
examples/person-thinking.svg
examples/person-looking.svg
```

## Gesture design

### note-taking
- 紙を胸下へ下げ、単純な大きい矩形を維持
- ペンをより長い斜線へ変更
- ペン先と紙の接触を明示
- 書く手は最小限の塊として残す

### thinking
- 前腕を胸下〜頬まで大きく斜めに通す
- 肘を外側へ張り、顔横に三角形の余白を作る
- 手は顎／頬に触れる塊として読みやすくする
- 指の細部は増やさない

### looking
- 頭部全体を右へ振る
- 両目を同じ開いた短線で描き、同方向へ寄せる
- 鼻・口・肩も同じ方向へずらす
- ウインク／片目表現を避ける

## Structure checks

```text
person-note-taking.svg = path 29
person-thinking.svg    = path 29
person-looking.svg     = path 25
```

全点:

```text
stroke="currentColor"
stroke-width="8"
fill="none"
path <= 45
```

## Comparison images

```text
reviews/correction2_gesture_comparison_normal_and_64px.png
reviews/correction2_gesture_comparison_normal_size.png
reviews/correction2_gesture_comparison_64px.png
```

## Gate after Correction-2 implementation

```text
Human Visual Acceptance (Correction-1) = HOLD / CONSUMED
Semantic Gesture Correction-2          = IMPLEMENTED
Fresh Correction-2 Implementation Review = READY
Human Visual Acceptance (Correction-2) = HOLD
Remaining 7 SVGs                       = HOLD
Merge                                  = HOLD
Promotion                              = HOLD
```

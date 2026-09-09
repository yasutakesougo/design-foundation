# References

`references/` は、外部参照や制作結果を保存するだけの場所ではありません。

参照したものから再利用できる判断を抽出し、案件固有の方向性と共通化候補を分けて記録する場所です。

## ディレクトリの役割

- `external/`: 外部サイト、デザインシステム、記事、事例などの参照記録を置きます。
- `directions/`: 案件や制作物の方向性候補を置きます。
- `in-progress/`: Human Visual Acceptance前の制作物や検討中の参照を置きます。
- `accepted/`: Human Visual Acceptance後に、今後の比較対象として残す参照を置きます。
- `rejected/`: 採用しなかった事例と、その理由を残します。

## 外部参考を使うとき

外部参考は、作品全体をそのまま再現するために使いません。

まず `reference-intake-template.md` を使い、レイアウト、文字、色、素材、整え方などへ分解します。

そのうえで、再利用する設計原則を `Borrow` に記録します。

作品固有でコピーしない表現は `Do Not Copy` に記録します。

```text
External Reference
↓
Reference Intake
↓
Project Direction Candidate
↓
Actual Use
↓
Human Visual Acceptance
↓
Repeated Evidence
↓
Pattern / Prompt / Foundation Candidate
```

参考を分析しただけでは、Pattern、Prompt、Foundationへ昇格させません。

実案件で使い、複数回の再利用性が確認できたものだけを共通化候補にします。

## 記録時の最低条件

次の条件を満たさない外部参照は、設計判断の根拠として扱いません。

- 出典URLと参照目的が記録されている。
- 何を参考にしたかが具体的に説明されている。
- `Borrow` と `Do Not Copy` が分離されている。
- 案件固有の判断と共通化候補が混同されていない。
- 外部画像そのものを正本として大量保存していない。
- Human Visual Acceptanceを迂回していない。

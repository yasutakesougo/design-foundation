# Accepted References

`references/accepted/` は、再利用可能性を人が明示的に受け入れた参照・運用知識を置く場所です。

Acceptedはruntime activationや自動適用を意味しません。

## Accepted authorityの種類

### Visual / production reference

Human Visual Acceptanceを通過した制作物のうち、今後の判断に再利用できるものを記録します。

画像を置くだけではなく、採用理由を残します。

### Governance / architecture reference

運用規約やarchitectureなど非視覚のreferenceは、Definition、Independent Review、実装検証を経たうえで、明示的なHuman Promotion GOによってaccepted authorityへ昇格できます。

この経路はHuman Visual Acceptanceを要求しません。

ただしHuman Promotionをruntime activation、Deploy、root `AGENTS.md`導入、CI enforcementへ読み替えません。

## Accepted Referenceを探す

この一覧は既存のAccepted Referenceへの入口です。

Accepted配置だけからruntime activation、current lifecycle state、Deploy、Print、Publish、Promotion、consumer activationを推定しません。

### Visual / production reference

- [`hitokoto-poster-canva-output-pilot-v1.md`](hitokoto-poster-canva-output-pilot-v1.md) — ポスター出力pilotから再利用できる制作・出力判断。
- [`image-first-semantic-redraw-v1/`](image-first-semantic-redraw-v1/) — semantic redrawのaccepted assets、provenance、authority記録。

### Governance / architecture reference

- [`agent-operating-foundation-v1/`](agent-operating-foundation-v1/) — repository operating foundationのaccepted authority。

## Visual reference 記録テンプレート

```markdown
## <Reference name>

- Date:
- Medium:
- Source:
- Human Visual Acceptance: PASS

### 採用した理由

- 

### 再利用できる判断

- 

### Design DNA（必要な場合のみ）

- Information hierarchy:
- Composition / information structure:
- Typography role:
- Color anchor:
- Spacing / rhythm:
- Illustration role:

### 再利用しない案件固有要素

- 
```

Design DNAは必須の巨大schemaにしません。次の制作で判断を再現するために必要な範囲だけ記録します。

一案件だけの偶然の表現や、一度Acceptedになっただけの表現を、共通原則へ自動昇格させません。

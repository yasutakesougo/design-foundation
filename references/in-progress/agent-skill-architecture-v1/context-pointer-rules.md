# Context pointer rules

Context pointerは、必要な文書を必要な条件で読むための短い案内です。

pointerの目的は、参照先を示すことではなく、参照が必要になる条件を明示することです。

## pointerに含める情報

pointerには次の2点を含めます。

1. 何を参照する文書か。
2. どの条件で読むか。

単なるファイル一覧をpointerとして扱いません。

## 常時見せる情報

次の情報はReferenceの奥へ移しません。

- Human Gateのauthority。
- mutation boundary。
- Skill / AgentがHuman GOを代理消費しない規則。
- Model-invoked disciplineがHuman Gateを遷移させない規則。

これらはpointerの発火失敗から影響を受けない位置に置きます。

## Referenceへ分離できる情報

次の情報は、必要なbranchでだけ読むReferenceへ分離できます。

- 媒体固有のレビュー手順。
- 配色やタイポグラフィの詳細規則。
- 印刷物だけで使うpreflight項目。
- 特定の外部referenceを使う場合だけ必要なintake規則。
- 長い背景説明や例示。

毎回必要な手順はmain flowに残します。

## Single source of truth

同じ規則を複数のSkillやREADMEへ全文複製しません。

既存文書が正本の場合、pointerはその正本を参照します。

環境から直接確認できる情報は、静的文書へ不要に転記しません。

文書化するのは、環境から読み取れない判断理由、運用境界、例外条件です。

## pointerの書き方

先頭で対象を示します。

その後に、読む条件を一文で書きます。

例:

```text
印刷または公開前の出力確認では `review/output-preflight.md` を読む。
```

次のようなpointerは避けます。

```text
詳細は `review/output-preflight.md` を参照。
```

後者では、いつ読む必要があるかを判断できません。

## Progressive Disclosureの判断

すべてのbranchで必要な情報はmain flowに残します。

一部のbranchだけで必要な情報はReferenceへ分離します。

分離後もHuman authorityとmutation boundaryが常時見えることを確認します。

## Completion criteria

Context pointerの追加または変更は、次をすべて満たしたときに完了します。

- 参照対象が明確である。
- 発火条件が明確である。
- 既存正本を重複していない。
- 必須guardrailを奥へ隠していない。
- pointerを読めば、必要時にどの文書へ進むか判断できる。

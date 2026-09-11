# Matt Pocock Skills — External Reference

## Reference

- Repository: `mattpocock/skills`
- Source URL: https://github.com/mattpocock/skills
- Reviewed commit: `3cca18b368ae95cdbdebbff572ccafa662551015`
- Reviewed date: `2026-09-11`
- Role: reference-only
- Purpose: `AGENT-SKILL-ARCHITECTURE-V1` の invocation ownership、context pointer、progressive disclosure、single source of truth、completion criteria、handoff by reference、tracer-bullet decomposition の検討材料として参照する。

この記録は外部Skill自体をローカル正本へ昇格させません。

## Verified source pins

`AGENT-SKILL-ARCHITECTURE-V1` で参照した外部ファイルは、上記commitで次のblob SHAと一致することを確認しました。

- `.agents/invocation.md` = `c13b8a5ea97466e14259de602c6b66e72133fef1`
- `skills/productivity/writing-for-agents/SKILL.md` = `a37608daf6e835e767deecfb498facecaaba82ba`
- `skills/engineering/to-tickets/SKILL.md` = `e868c831fcfb1e124e010bcdf84a429ec879160f`
- `skills/productivity/handoff/SKILL.md` = `2eb98a51b97bb5bac461a26ad14828eeac827909`
- `skills/engineering/setup-matt-pocock-skills/SKILL.md` = `7f6f576e2e54e0d287cbb9731ebe0343f54e50cf`

## Borrow

再利用するのは次の設計原則です。

- invocation ownershipを明確に分離する。
- 必要な文書へ到達する条件をcontext pointerへ持たせる。
- すべてのbranchで不要な詳細はprogressive disclosureで分離する。
- 同一ルールを複数文書へ複製せずsingle source of truthを保つ。
- 手順にはcheckableなcompletion criteriaを持たせる。
- handoffは正本の複製ではなく参照中心にする。
- 大きな作業は、単独で検証可能な小さなsliceへ分解する。

これらはローカルのHuman Gate authorityやmutation boundaryより上位ではありません。

## Do Not Copy

次は採用しません。

- 外部Skillファイル本体のコピー。
- Claude Code / Codex固有のfrontmatterやruntime metadataをそのまま移植すること。
- `disable-model-invocation` や `agents/openai.yaml` 等のharness-specific設定をローカル標準へ自動採用すること。
- 外部repoのディレクトリ構造をそのまま正本化すること。
- 外部Skillのinstallation、automatic sync、submodule化、runtime dependency化。
- 外部repoのHuman authority semanticsをローカルHuman Gateの代替にすること。
- 外部文書の文面、例、命名を必要以上に複製すること。

## Local authority boundary

外部Referenceとローカル正本が衝突する場合は、ローカルのFoundation、Pattern、Review、Skill、Human Gate契約を優先します。

本Referenceは設計判断の再現性を確保するためのprovenanceであり、runtime activationやPromotionを承認しません。

## Re-review conditions

次の場合は自動更新せず、別途readback / reviewを行います。

- `mattpocock/skills` の別commitから新しい原則を採用したい場合。
- 参照対象ファイルやblob SHAが変わる場合。
- 外部Skillをruntimeへ導入したい場合。
- harness-specific metadataをローカルSkillへ採用したい場合。
- invocation taxonomyやHuman Gate authorityへ影響する変更を取り込みたい場合。
- このReferenceをaccepted authorityやFoundationへ昇格したい場合。

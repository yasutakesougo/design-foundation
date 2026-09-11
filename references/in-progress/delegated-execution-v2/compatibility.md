# Compatibility with Accepted Operating Foundation

この候補は accepted Operating Foundation を置き換えない。

## Preserved invariants

```text
Human GO comes only from explicit Human input
Agent / Skill does not generate / infer / proxy-consume Human GO
UNKNOWN / HOLD fail-closed
write / merge / publish / print / deploy / promotion require corresponding authority
readback / applicability / refinement / observability contracts remain canonical
references/in-progress/ is not accepted authority
```

対応する merge authority は、IN に当該 candidate の merge を明示する Human Delegation Activation GO として読む。

Independent Review PASS を Human Merge GO の代理にしてはならない。

## Pre-Promotion vocabulary rule

削減された通常 Gate 集合は、明示的な Human Delegation Activation IN の解釈としてだけ効力を持つ。

Promotion までは accepted Operating Foundation vocabulary を改正しない。

```text
This candidate alone
≠ accepted merge authority
≠ repository-wide gate-law rewrite
≠ accepted Operating Foundation amendment
```

Activation 外の workstream では、既存 gate vocabulary を変更しない。

この候補を、無関係な workstream の accepted merge authority として引用しない。

## Files not mutated by V2 Implementation

```text
references/accepted/agent-operating-foundation-v1/**
root AGENTS.md
foundations/**
patterns/**
prompts/**
review/**
skills/**
```

## Promotion

accepted authority への昇格は別 decision であり、この candidate の存在や merge だけでは成立しない。

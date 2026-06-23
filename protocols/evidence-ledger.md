# Protocol: Evidence Ledger

The evidence ledger is the source of truth for the final memo.

## Required columns

```csv
id,claim,source_title,source_url,source_mode,source_type,date,author_org,evidence_quote_or_paraphrase,confidence,conflicts,notes,used_in_final
```

Project-local ledgers may add optional columns:

```csv
topic_id,source_id,change_id
```

## Confidence values

- high
- medium
- low
- unknown

## Rules

- One row = one supportable claim.
- Avoid dumping summaries into the ledger.
- Mark conflicts explicitly.
- Mark stale evidence explicitly.
- Do not write final strategic recommendations from unsupported claims.

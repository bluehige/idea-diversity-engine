# Reference Architecture

```mermaid
flowchart LR
    A[User brief] --> B[Brief normalizer]
    B --> C[Baseline mapper]
    C --> D[Strata builder]
    D --> E[VS generator]
    E --> F[Schema + constraint validator]
    F --> G[Semantic memory + dedup]
    G --> H[Quality + risk gate]
    H --> I[Portfolio selector]
    I --> J[Domain exporters]
```

## Core interfaces

- `normalize_brief(brief) -> NormalizedBrief`
- `build_strata(brief) -> list[Stratum]`
- `generate_candidates(brief, mode, k, tau) -> Portfolio`
- `validate_portfolio(portfolio) -> ValidationReport`
- `deduplicate(portfolio, memory) -> DedupReport`
- `score_candidates(portfolio, rubric) -> ScoredPortfolio`
- `export(portfolio, target) -> Document`

## Provider adapters

Provider adapters must map the common prompt and output schema to a vendor API without changing the semantics of typicality, constraints, or rationale.

## Storage

Minimum project record:

- brief and normalized brief
- prompt version
- model and version
- generation parameters
- candidate portfolio
- canonical summaries and embeddings
- user decisions
- evaluation report
- export history

## Privacy modes

- Public demo: no sensitive retention
- Team SaaS: encrypted project storage and RBAC
- Private: dedicated tenant or VPC
- Local/on-premise: local model and local vector store

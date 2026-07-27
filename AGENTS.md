# AGENTS.md

## Project objective

Maintain the **Diversity Generation Engine** monorepo: a provider-neutral system that generates, validates, deduplicates, selects, and documents portfolios of meaningfully different candidates.

## Repository boundaries

- `core/`: provider-neutral shared rules and capabilities
- `verticals/`: domain knowledge, prompts, schemas, rubrics, exporters, examples
- `apps/`: user-facing workflows and prototypes
- `integrations/`: provider, MCP, REST, automation adapters
- `benchmarks/`: evaluation protocols
- v0.1 root paths (`prompts/`, `schemas/`, `skills/`, `examples/`, `src/`) remain compatibility assets until migration is completed

## Non-negotiable rules

- Do not force `typicality_estimate` values to sum to 1.
- Do not label typicality as market, success, factual, population, or patent probability.
- Do not select candidates solely because they have low typicality.
- Do not expose private chain-of-thought; use concise observable rationale.
- Do not hard-code API keys, customer data, private prompts, or proprietary prior art.
- Keep the Core provider-neutral. Provider adapters belong in `integrations/`.
- Do not place domain-specific rules in Core when they belong to a Vertical.
- Do not imitate a living creator's distinctive style; abstract the design principle instead.

## Architecture

```text
Brief normalizer
  -> baseline mapper
  -> solution-space stratifier
  -> VS generator
  -> schema/constraint validator
  -> semantic memory and deduplication
  -> quality/risk gate
  -> portfolio selector
  -> domain exporter
```

## Definition of done

- Unit tests pass.
- JSON examples validate.
- Public behavior changes update Korean and English documentation.
- New vertical packs include: purpose, inputs, strata, outputs, prompt, example, quality rubric, and human-review scope.
- New apps state their Vertical dependency, secret-handling policy, and implementation status.

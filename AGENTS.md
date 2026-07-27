# AGENTS.md

## Project objective

Maintain a provider-neutral diversity engine that generates, validates, deduplicates, and documents portfolios of meaningfully different candidates.

## Non-negotiable rules

- Do not force `typicality_estimate` values to sum to 1.
- Do not label typicality as market, success, factual, or patent probability.
- Do not select candidates solely because they have low typicality.
- Do not expose private chain-of-thought; use concise observable rationale.
- Do not hard-code API keys or customer data.
- Keep the core provider-neutral. Provider adapters belong in separate modules.

## Architecture

```text
Brief normalizer
  -> baseline mapper
  -> strata builder
  -> VS generator
  -> schema/constraint validator
  -> semantic memory and deduplication
  -> quality/risk gate
  -> portfolio selector
  -> domain exporters
```

## Definition of done

- Unit tests pass.
- JSON examples validate.
- Documentation is updated in Korean and English when public behavior changes.
- New vertical packs include: brief, prompt, output schema, quality rubric, and risk note.

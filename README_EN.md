# Diversity Generation Engine

[한국어](README.md) · [Catalog](CATALOG.md)

**Diversity Generation Engine (DGE)** is an open, provider-neutral framework for generating a portfolio of meaningfully different LLM candidates instead of one conventional answer or a list of superficial rewrites.

```text
brief → baseline map → solution-space strata → verbalized sampling
      → constraints → semantic deduplication → quality/risk gate
      → portfolio selection → domain handoff document
```

## Repository layers

- `core/`: reusable generation and validation rules
- `verticals/`: domain-specific inputs, prompts, rubrics, and outputs
- `apps/`: user-facing prototypes and workbench specifications
- `integrations/`: provider, MCP, REST, and workflow adapters
- `benchmarks/`: Direct/List/VS evaluation plans

The v0.2 repository defines ten vertical packs: creative writing, game design, IP invention, safety training, business strategy, marketing content, visual/3D design, AI character behavior, research/synthetic data, and software QA.

It also includes provider-neutral prototypes for Novel Idea Studio, Narrative Lens Panel, and Character Starter. Existing v0.1 prompts, schemas, skills, examples, Python CLI, and tests remain in their original paths for compatibility.

`typicality_estimate` is a model-estimated signal of how common a candidate may be in the full plausible response space. It is not quality, truth, success, market, patentability, or population probability, and returned values are not required to sum to one.

This is an independent application project inspired by *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity*. It is not affiliated with the paper authors or CHATS-lab. Licensed under Apache-2.0.

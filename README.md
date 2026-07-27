# Idea Diversity Engine

[한국어 README](README_KR.md) · [English README](README_EN.md)

**Idea Diversity Engine** is an open toolkit for generating a *portfolio* of meaningfully different LLM outputs instead of repeatedly receiving the same conventional answer.

Its target architecture combines:

- **Verbalized Sampling (VS)** — ask for candidate responses with model-estimated typicality.
- **Solution-space stratification** — divide the answer space before generation.
- **Semantic memory and deduplication** — prevent collapse across batches.
- **Constraint and quality gates** — keep tail ideas useful, feasible, and auditable.
- **Vertical handoff templates** — convert candidates into product, research, IP, safety, game, content, or test documents.

> This project is an independent application-design and skill toolkit inspired by the paper *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity*. It is not affiliated with the paper authors or CHATS-lab.

**v0.1 scope:** the repository implements a provider-neutral prompt builder and structural validator. Embedding-based semantic memory, automated diversity evaluation, model adapters, and the web UI are specified in the roadmap but are not yet implemented in the reference package.

## Why this exists

A direct prompt such as “give me one idea” often converges on the most familiar answer. A list prompt may produce surface-level variations. A distribution-level prompt changes the target: the model is asked to represent multiple plausible regions of the response space and attach a model-estimated typicality value to each candidate.

The paper reports 1.6–2.1× diversity gains over direct prompting in creative writing and evaluates the method in dialogue simulation, open-ended QA, and synthetic-data generation. The official implementation is model-agnostic and includes a Python package and LangChain integration.

## Suitable tasks

- Creative writing, game content, image/video prompt portfolios
- Product, service, campaign, and business-model ideation
- Research hypotheses and experiment alternatives
- Patent harvesting and design-around exploration
- Safety-training scenarios and industrial edge cases
- Software architecture alternatives, test cases, and adversarial examples
- Synthetic data, persona dialogue, and user simulation

## Not suitable as a standalone decision maker

- Single factual answers or exact calculations
- Legal patentability opinions
- Representative public-opinion estimates without calibration data
- Medical, financial, or safety-critical decisions without expert review
- Any workflow that equates low typicality with truth, novelty, or quality

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e .

idea-diversity build-prompt \
  --brief examples/briefs/business_model.json \
  --mode stratified \
  --count 5 \
  --tau 0.10

idea-diversity validate --input examples/outputs/sample_portfolio.json
```

The starter CLI builds provider-neutral prompts and validates structured output. It intentionally does **not** embed an API key or bind the project to a single LLM vendor.

## Repository map

```text
skills/       Reusable agent/LLM skill specifications
prompts/      Provider-neutral prompt templates
schemas/      JSON Schemas for briefs and candidate portfolios
examples/     Vertical briefs and a sample portfolio
src/          Minimal prompt-builder and validator reference implementation
tests/        Unit tests
docs/         Research review, application map, platform strategy, and business plans
```

## Core interpretation rule

`typicality_estimate` is a model-generated heuristic describing how common a candidate seems within the model's possible response distribution. It is **not**:

- market success probability,
- patent registration probability,
- statistical prevalence,
- factual confidence,
- or a quality score.

Returned values are not forced to sum to 1.

## Recommended public-product path

1. GitHub toolkit and prompt/skill pack
2. Hugging Face Space or lightweight web demo
3. ChatGPT/Claude/Gemini/Microsoft agent adapters
4. Vertical paid packs: safety, games, IP, 3D content, software QA
5. Team workspace with semantic memory, evaluation, and governance

See [Application Landscape](docs/03_APPLICATION_LANDSCAPE_KR.md), [Platform Matrix](docs/04_PLATFORM_DISTRIBUTION_MATRIX_KR.md), and [Business Model Portfolio](docs/05_BUSINESS_MODEL_PORTFOLIO_KR.md).

## Research and attribution

- Paper: https://arxiv.org/abs/2510.01171
- Official code: https://github.com/CHATS-lab/verbalized-sampling
- Official project website: https://www.verbalized-sampling.com/

The paper itself is not redistributed in this repository. See [NOTICE](NOTICE) and [References](docs/REFERENCES.md).

## License

Apache License 2.0. See [LICENSE](LICENSE).

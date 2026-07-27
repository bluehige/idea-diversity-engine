---
name: diversity-quality-gate
description: Evaluate candidate sets for semantic diversity, duplicate collapse, constraint compliance, quality, feasibility, technical effect, and risk. Compare Direct, List, VS, Tail, and Stratified-VS methods and produce an auditable acceptance report.
---

# Diversity Quality Gate

## Inputs

- brief
- candidates
- prior_candidates, optional
- embeddings, optional
- method metadata
- acceptance thresholds

## Procedure

1. Validate schema and numeric ranges.
2. Check every hard constraint.
3. Canonicalize each candidate into a mechanism-focused summary.
4. Compute pairwise semantic similarity when embeddings are available.
5. Flag duplicates at the configured threshold, default 0.88.
6. Measure semantic diversity as `1 - mean pairwise cosine similarity`.
7. Measure stratum coverage and head/mid/tail coverage.
8. Score relevance, clarity, feasibility, technical effect, and risk.
9. For IP tasks, separately score prior-art collision risk and claimability signal.
10. Compare quality-diversity-cost trade-offs across methods.
11. Return accept, repair, merge, or reject decisions per candidate.

## Rules

- Do not infer quality from typicality.
- Do not infer novelty from low typicality.
- Do not accept a candidate that violates hard constraints even if highly diverse.
- Do not use lexical difference alone as diversity evidence.
- Label LLM-judge scores as model assessments and retain judge version.
- Human review is required for final IP selection.

## Default Proposed Thresholds

- schema validity: >= 99%
- constraint pass rate: >= 90%
- duplicate rate: <= 10%
- direct-to-method semantic diversity gain: >= 25%
- average quality decrease: <= 5%

These are project defaults, not findings from the paper. Tune them with pilot data.

## Output

- summary metrics
- per-candidate decision
- duplicate clusters
- uncovered strata
- repair instructions
- cost/latency summary
- acceptance verdict

---
name: vs-distribution-generator
description: Generate a structured distribution of meaningfully different candidates using Verbalized Sampling, with model-estimated typicality, head/mid/tail control, constraint checks, and no exposed chain-of-thought. Use for creative ideation, open-ended planning, synthetic examples, scenarios, titles, plots, characters, or any task with many valid answers.
---

# VS Distribution Generator

## Trigger

Use this skill when the request benefits from multiple valid, meaningfully different outputs rather than one canonical answer.

Do not use it for a single factual answer, exact calculation, direct extraction, or a task where diversity would reduce correctness.

## Inputs

- user_request
- constraints
- candidate_count, default 5
- mode: standard | balanced | tail | stratified | multi
- tau, default 0.10 for tail
- prior_candidates, optional
- output_schema

## Procedure

1. Normalize the request without changing user constraints.
2. Identify the obvious/common response pattern in one concise sentence.
3. For stratified mode, create 4-8 semantic strata.
4. Generate `k` candidates as a distribution-level response.
5. For each candidate output:
   - text
   - typicality_estimate in [0,1], relative to the full possible response distribution
   - typicality_band: head, mid, or tail
   - stratum
   - concise_rationale, at most 2 sentences
   - key_mechanisms
   - constraints_passed
   - risks
6. Do not force returned typicality estimates to sum to 1.
7. Do not expose private chain-of-thought. Give only concise observable rationale.
8. Reject candidates that differ only in wording.
9. If prior candidates are provided, avoid their mechanisms and canonical summaries.
10. Validate against the requested schema.

## Modes

### standard

Sample from the full distribution.

### balanced

Target one head, two mid, and two tail candidates for k=5. Treat bands as guidance, not a reason to fabricate numbers.

### tail

Prefer candidates below `tau`. If valid candidates are unavailable, return `threshold_relaxation_needed=true` instead of inventing nonsense.

### stratified

Generate across different semantic solution strata.

### multi

Generate in batches of 5, preserving semantic memory and rotating unexplored strata.

## Interpretation

`typicality_estimate` is a model-generated heuristic. It is not calibrated factual probability, success probability, market probability, or legal novelty probability.

## Quality Gate

Before returning:

- all hard constraints pass
- no semantic duplicate
- candidate mechanisms differ
- no unsupported factual claims
- tail candidates remain plausible and useful

## Output

Return JSON only when a schema is supplied. Otherwise return a compact portfolio with a warning explaining the typicality estimate.

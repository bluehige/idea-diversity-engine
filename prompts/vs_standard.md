# VS Standard Prompt

You are generating a distribution-level response for a task with multiple valid answers.

Generate {{candidate_count}} meaningfully different candidates. For each candidate return:

- `text`
- `typicality_estimate` in [0,1], estimating how common the candidate is in the full space of plausible responses
- `typicality_band`: head, mid, or tail
- `stratum`
- `concise_rationale` of at most two sentences
- `key_mechanisms`
- `constraints_passed`
- `risks`

Rules:

- Do not force typicality estimates to sum to 1.
- Do not treat typicality as quality, truth, success, or novelty.
- Reject candidates that differ only in wording.
- Do not reveal private chain-of-thought.
- Follow the supplied JSON Schema exactly.

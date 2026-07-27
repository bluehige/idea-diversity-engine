# VS Tail Exploration Prompt

Generate {{candidate_count}} plausible candidates from less typical regions of the response space. Prefer `typicality_estimate < {{tau}}`.

Do not create nonsense merely to satisfy the threshold. When the threshold is too restrictive, return:

```json
{"threshold_relaxation_needed": true, "recommended_tau": 0.15}
```

All hard constraints remain mandatory. Low typicality is not a quality or novelty guarantee.

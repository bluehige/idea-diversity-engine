from __future__ import annotations

import json
from pathlib import Path
from typing import Any

VALID_MODES = {"standard", "balanced", "tail", "stratified", "multi"}


def load_brief(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Brief must be a JSON object.")
    for key in ("domain", "problem", "desired_effect"):
        if not str(data.get(key, "")).strip():
            raise ValueError(f"Missing required brief field: {key}")
    return data


def build_prompt(
    brief: dict[str, Any],
    *,
    mode: str = "stratified",
    count: int = 5,
    tau: float = 0.10,
) -> str:
    if mode not in VALID_MODES:
        raise ValueError(f"Unsupported mode: {mode}")
    if count < 1 or count > 50:
        raise ValueError("count must be between 1 and 50")
    if not 0 <= tau <= 1:
        raise ValueError("tau must be within [0,1]")

    mode_rule = {
        "standard": "Sample across the full plausible response distribution.",
        "balanced": "Target a portfolio containing head, mid, and tail candidates.",
        "tail": f"Prefer plausible candidates with typicality_estimate below {tau:.2f}; request threshold relaxation instead of nonsense.",
        "stratified": "First create 4-8 semantic solution strata, then generate across distinct strata.",
        "multi": "Generate a batch that avoids mechanisms and canonical summaries in prior_candidates.",
    }[mode]

    return f"""You are an Idea Diversity Engine for tasks with multiple valid answers.

BRIEF
{json.dumps(brief, ensure_ascii=False, indent=2)}

MODE
- mode: {mode}
- candidate_count: {count}
- tau: {tau:.2f}
- rule: {mode_rule}

OUTPUT
Return one JSON object with: brief_summary, mode, tau, strata, candidates, warnings.
Each candidate must contain: id, text, typicality_estimate, typicality_band, stratum,
concise_rationale, key_mechanisms, constraints_passed, risks.

NON-NEGOTIABLE RULES
1. typicality_estimate is a model-generated estimate of how common the candidate is in the full plausible response space.
2. Do not force returned typicality estimates to sum to 1.
3. Typicality is not quality, truth, success, market probability, or patent probability.
4. Candidates must differ in mechanism or decision structure, not wording alone.
5. All hard constraints must pass.
6. Do not expose private chain-of-thought. Provide only concise auditable rationale.
7. If a tail threshold prevents useful candidates, return threshold_relaxation_needed and a recommended_tau.
"""

from __future__ import annotations

import re
from typing import Any

VALID_MODES = {"standard", "balanced", "tail", "stratified", "multi"}
VALID_BANDS = {"head", "mid", "tail"}
REQUIRED_CANDIDATE_FIELDS = {
    "id", "text", "typicality_estimate", "typicality_band", "stratum",
    "concise_rationale", "key_mechanisms", "constraints_passed", "risks",
}


def _canonical(text: str) -> str:
    return re.sub(r"[^a-z0-9가-힣]+", " ", text.lower()).strip()


def validate_portfolio(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        return {"valid": False, "errors": ["Portfolio must be a JSON object."], "warnings": []}

    mode = data.get("mode")
    if mode not in VALID_MODES:
        errors.append(f"Invalid mode: {mode!r}")

    candidates = data.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        errors.append("candidates must be a non-empty array")
        return {"valid": False, "errors": errors, "warnings": warnings}

    ids: set[str] = set()
    canonical_texts: dict[str, str] = {}
    typicality_sum = 0.0

    for index, candidate in enumerate(candidates):
        prefix = f"candidates[{index}]"
        if not isinstance(candidate, dict):
            errors.append(f"{prefix} must be an object")
            continue

        missing = REQUIRED_CANDIDATE_FIELDS - candidate.keys()
        if missing:
            errors.append(f"{prefix} missing fields: {sorted(missing)}")

        cid = str(candidate.get("id", ""))
        if not cid:
            errors.append(f"{prefix}.id must be non-empty")
        elif cid in ids:
            errors.append(f"duplicate candidate id: {cid}")
        ids.add(cid)

        text = str(candidate.get("text", "")).strip()
        if not text:
            errors.append(f"{prefix}.text must be non-empty")
        canon = _canonical(text)
        if canon and canon in canonical_texts:
            warnings.append(f"exact canonical duplicate: {cid} and {canonical_texts[canon]}")
        elif canon:
            canonical_texts[canon] = cid

        typicality = candidate.get("typicality_estimate")
        if not isinstance(typicality, (int, float)) or isinstance(typicality, bool):
            errors.append(f"{prefix}.typicality_estimate must be numeric")
        elif not 0 <= float(typicality) <= 1:
            errors.append(f"{prefix}.typicality_estimate must be within [0,1]")
        else:
            typicality_sum += float(typicality)

        if candidate.get("typicality_band") not in VALID_BANDS:
            errors.append(f"{prefix}.typicality_band must be head, mid, or tail")

        for field in ("key_mechanisms", "constraints_passed", "risks"):
            if not isinstance(candidate.get(field), list):
                errors.append(f"{prefix}.{field} must be an array")

    # Intentionally informational only: VS candidate values are not required to sum to one.
    if abs(typicality_sum - 1.0) < 1e-9:
        warnings.append("Typicality estimates happen to sum to 1; confirm they were not normalized by mistake.")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "candidate_count": len(candidates),
        "typicality_sum": round(typicality_sum, 6),
    }

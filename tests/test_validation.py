import json
from pathlib import Path

from idea_diversity_engine.validation import validate_portfolio


def test_sample_portfolio_is_valid():
    path = Path(__file__).parents[1] / "examples" / "outputs" / "sample_portfolio.json"
    report = validate_portfolio(json.loads(path.read_text(encoding="utf-8")))
    assert report["valid"], report
    assert report["typicality_sum"] != 1.0


def test_out_of_range_typicality_fails():
    data = {
        "mode": "standard",
        "candidates": [{
            "id": "x", "text": "x", "typicality_estimate": 1.2,
            "typicality_band": "head", "stratum": "s",
            "concise_rationale": "r", "key_mechanisms": ["m"],
            "constraints_passed": [], "risks": []
        }]
    }
    report = validate_portfolio(data)
    assert not report["valid"]

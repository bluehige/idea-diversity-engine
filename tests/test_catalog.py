import pytest

from idea_diversity_engine.catalog import VERTICALS, get_vertical
from idea_diversity_engine.prompting import build_prompt


def test_catalog_contains_ten_verticals():
    assert len(VERTICALS) == 10
    assert "creative-writing" in VERTICALS
    assert "safety-training" in VERTICALS


def test_vertical_profile_is_injected_into_prompt():
    brief = {
        "domain": "game design",
        "problem": "repetitive content",
        "desired_effect": "new player decisions",
    }
    prompt = build_prompt(brief, vertical="game-design", mode="stratified")
    assert '"id": "game-design"' in prompt
    assert "core-loop" in prompt
    assert "Do not force returned typicality estimates to sum to 1" in prompt


def test_unknown_vertical_is_rejected():
    with pytest.raises(ValueError):
        get_vertical("unknown")

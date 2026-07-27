from idea_diversity_engine.prompting import build_prompt


def test_prompt_warns_not_to_normalize():
    brief = {"domain": "test", "problem": "repetition", "desired_effect": "diversity"}
    prompt = build_prompt(brief, mode="tail", count=5, tau=0.1)
    assert "Do not force returned typicality estimates to sum to 1" in prompt
    assert "below 0.10" in prompt

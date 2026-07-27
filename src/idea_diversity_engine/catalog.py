from __future__ import annotations

from typing import Final

VERTICALS: Final[dict[str, dict[str, object]]] = {
    "creative-writing": {
        "name_ko": "소설·서사 생성",
        "name_en": "Creative Writing",
        "status": "Prototype",
        "strata": ["title-hook", "world-rule", "character-drive", "plot-structure", "ending"],
    },
    "game-design": {
        "name_ko": "게임 기획·콘텐츠",
        "name_en": "Game Design",
        "status": "Prompt Pack",
        "strata": ["core-loop", "combat", "economy", "progression", "liveops", "ending"],
    },
    "ip-invention": {
        "name_ko": "IP·특허 아이디어",
        "name_en": "IP Invention",
        "status": "Prompt Pack",
        "strata": ["structure", "sensor", "control", "data", "operation", "safety"],
    },
    "safety-training": {
        "name_ko": "안전교육·시뮬레이션",
        "name_en": "Safety Training",
        "status": "Prompt Pack",
        "strata": ["environment", "human-factor", "equipment", "sensor", "feedback", "recovery"],
    },
    "business-strategy": {
        "name_ko": "사업·서비스 전략",
        "name_en": "Business Strategy",
        "status": "Prompt Pack",
        "strata": ["customer", "value", "revenue", "channel", "operations", "risk"],
    },
    "marketing-content": {
        "name_ko": "마케팅·콘텐츠",
        "name_en": "Marketing Content",
        "status": "Prompt Pack",
        "strata": ["audience", "message", "evidence", "channel", "format", "conversion"],
    },
    "visual-3d-design": {
        "name_ko": "3D·비주얼 디자인",
        "name_en": "Visual and 3D Design",
        "status": "Prompt Pack",
        "strata": ["silhouette", "structure", "parts", "materials", "rigging", "optimization"],
    },
    "ai-character": {
        "name_ko": "AI 펫·NPC 행동",
        "name_en": "AI Character",
        "status": "Prompt Pack",
        "strata": ["emotion", "action", "dialogue", "memory", "relationship", "growth"],
    },
    "research-synthetic-data": {
        "name_ko": "연구·합성데이터",
        "name_en": "Research and Synthetic Data",
        "status": "Prompt Pack",
        "strata": ["hypothesis", "counter-hypothesis", "method", "measurement", "failure", "replication"],
    },
    "software-qa": {
        "name_ko": "소프트웨어 QA·엣지 케이스",
        "name_en": "Software QA",
        "status": "Prompt Pack",
        "strata": ["boundary", "state", "permission", "concurrency", "environment", "recovery"],
    },
}


def get_vertical(vertical_id: str | None) -> dict[str, object] | None:
    if vertical_id is None:
        return None
    try:
        return VERTICALS[vertical_id]
    except KeyError as exc:
        choices = ", ".join(sorted(VERTICALS))
        raise ValueError(f"Unknown vertical: {vertical_id}. Choose one of: {choices}") from exc

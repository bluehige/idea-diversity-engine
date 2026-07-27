# Core Engine

Core는 모든 분야가 공유하는 **다양성 생성·검증 규칙**만 담당합니다. 소설, 게임, 특허 같은 도메인 지식은 `verticals/`, 실제 UI는 `apps/`에 둡니다.

## 공통 파이프라인

```text
Brief Normalizer
  → Baseline Mapper
  → Solution-Space Stratifier
  → Verbalized Sampling Generator
  → Constraint Validator
  → Semantic Memory / Deduplication
  → Quality & Risk Gate
  → Portfolio Selector
  → Domain Exporter
```

## 현재 구현

| 기능 | 현재 위치 | 상태 |
|---|---|---|
| 프롬프트 빌더 | `src/idea_diversity_engine/prompting.py` | Implemented |
| 구조 검증기 | `src/idea_diversity_engine/validation.py` | Implemented |
| CLI | `src/idea_diversity_engine/cli.py` | Implemented |
| VS 프롬프트 | `prompts/vs_*.md` | Implemented |
| 공통 스키마 | `schemas/` | Implemented |
| VS 생성 스킬 | `skills/vs-distribution-generator/` | Implemented |
| 품질 게이트 스킬 | `skills/diversity-quality-gate/` | Implemented |
| 임베딩 의미 메모리 | 향후 `core/memory/` | Roadmap |
| 자동 포트폴리오 선택 | 향후 `core/selection/` | Roadmap |

## 불변 규칙

1. 반환 후보의 `typicality_estimate` 합계를 1로 강제하지 않습니다.
2. 전형성은 품질, 사실성, 시장 성공률, 특허 가능성이 아닙니다.
3. 후보는 표현이 아니라 작동 원리 또는 의사결정 구조가 달라야 합니다.
4. 저전형성 후보도 제약·유용성·구현성·위험 검사를 통과해야 합니다.
5. 비공개 사고과정을 요구하지 않고 짧고 검수 가능한 근거만 출력합니다.

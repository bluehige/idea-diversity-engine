# 다양성 생성 엔진
### Diversity Generation Engine · DGE

[English](README_EN.md) · [확장팩 카탈로그](CATALOG.md) · [연구 근거](docs/01_RESEARCH_REVIEW_KR.md) · [참조 아키텍처](docs/13_REFERENCE_ARCHITECTURE.md)

**다양성 생성 엔진**은 LLM에게 하나의 익숙한 답이나 표현만 다른 목록을 받는 대신, **서로 다른 작동 원리·관점·전략을 가진 후보 포트폴리오**를 생성·검증·선택·문서화하기 위한 공개형 엔진입니다.

```text
사용자 브리프
  → 전형적 해결책 파악
  → 해결 공간 층화
  → Verbalized Sampling
  → 제약 검증
  → 의미 중복 제거
  → 품질·위험 평가
  → 포트폴리오 선택
  → 분야별 제작 문서 내보내기
```

> 이 저장소는 *Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity*에서 영감을 받은 독립적인 응용 프로젝트입니다. 논문 저자 또는 CHATS-lab의 공식 프로젝트가 아닙니다.

## 저장소 계층

| 계층 | 역할 | 예시 |
|---|---|---|
| [`core/`](core/) | 모든 분야가 공유하는 핵심 규칙과 공통 스킬 | VS, 층화, 검증, 선택 |
| [`verticals/`](verticals/) | 분야별 프롬프트·입출력·평가기준 | 소설, 게임, 특허, 안전교육 |
| [`apps/`](apps/) | 실제 사용 화면과 업무 흐름 | 소설 아이디어 스튜디오, 서사 관점 패널 |
| [`integrations/`](integrations/) | 모델·업무도구 연결 규격 | OpenAI, Gemini, Claude, 로컬 LLM, MCP |
| [`benchmarks/`](benchmarks/) | Direct/List/VS 비교 계획 | 다양성, 품질, 비용·지연 |

기존 `prompts/`, `schemas/`, `skills/`, `examples/` 경로는 v0.1 호환을 위해 유지하며, v0.2부터 신규 기능은 위 계층 구조를 기준으로 확장합니다.

## 핵심 엔진

1. **Verbalized Sampling** — 후보와 모델 추정 전형성을 함께 생성합니다.
2. **해결 공간 층화** — 구조·데이터·제어·운영·사업 등 탐색축을 먼저 분리합니다.
3. **의미 메모리와 중복 제거** — 같은 메커니즘을 표현만 바꿔 반복하는 것을 막습니다.
4. **제약·품질·위험 게이트** — 희귀한 후보가 무의미하거나 실행 불가능해지는 것을 방지합니다.
5. **도메인 내보내기** — 후보를 기획서, 발명 카드, 안전 시나리오, 게임 리소스 등으로 변환합니다.

## 확장팩

| 분야 | 경로 | 대표 산출물 | 상태 |
|---|---|---|---|
| 소설·서사 | [`creative-writing`](verticals/creative-writing/) | 제목·세계관·캐릭터·플롯·엔딩 | Prototype |
| 게임 | [`game-design`](verticals/game-design/) | 몬스터·스킬·보스·라이브옵스 | Prompt Pack |
| IP·특허 | [`ip-invention`](verticals/ip-invention/) | 발명 후보·설계회피·청구항 씨앗 | Prompt Pack |
| 안전교육 | [`safety-training`](verticals/safety-training/) | 사고 분기·센서·판정·피드백 | Prompt Pack |
| 사업기획 | [`business-strategy`](verticals/business-strategy/) | 사업모델·시장진입·검증계획 | Prompt Pack |
| 마케팅 | [`marketing-content`](verticals/marketing-content/) | 캠페인·카피·고객여정 | Prompt Pack |
| 3D·비주얼 | [`visual-3d-design`](verticals/visual-3d-design/) | 실루엣·부품·재질·LOD 브리프 | Prompt Pack |
| AI 캐릭터 | [`ai-character`](verticals/ai-character/) | 행동·감정·기억·관계·성장 | Prompt Pack |
| 연구·합성데이터 | [`research-synthetic-data`](verticals/research-synthetic-data/) | 가설·반증·실험·데이터 변형 | Prompt Pack |
| 소프트웨어 QA | [`software-qa`](verticals/software-qa/) | 엣지 케이스·상태전이·복구 테스트 | Prompt Pack |

전체 목록과 상태는 [`CATALOG.md`](CATALOG.md)에 정리되어 있습니다.

## 포함된 앱

- [`Novel Idea Studio`](apps/novel-idea-studio/) — 소설 아이디어 포트폴리오용 앱 설계
- [`Narrative Lens Panel`](apps/narrative-lens-panel/) — 실존 작가 모방이 아닌 서사 설계 관점 패널
- [`Character Starter`](apps/character-starter/) — 프로필보다 첫 등장과 행동 엔진에 집중하는 캐릭터 시동기
- [`Diversity Playground`](apps/diversity-playground/) — Direct/List/VS 비교 데모 계획

## 빠른 실행

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[test]"

idea-diversity build-prompt \
  --brief examples/briefs/safety_training.json \
  --mode stratified

idea-diversity validate \
  --input examples/outputs/sample_portfolio.json
```

## v0.2 구현 범위

**구현됨**

- 제공사 중립 프롬프트 빌더와 구조 검증기
- Core/Vertical/App/Integration 정보구조
- 10개 수직 확장팩 정의
- 소설·서사 앱 명세 3종
- 기존 프롬프트·스키마·예제와 CI

**로드맵**

- 임베딩 기반 의미 메모리
- 자동 의미 중복 클러스터링
- 자동 다양성·품질 평가
- 모델 제공사별 어댑터
- 통합 웹 UI와 팀 워크스페이스

## 반드시 지켜야 할 해석 규칙

```text
typicality_estimate ≠ 품질
typicality_estimate ≠ 사실 확률
typicality_estimate ≠ 시장 성공률
typicality_estimate ≠ 특허 가능성
typicality_estimate ≠ 실제 사용자 대표성
```

전형성 값은 반환 후보끼리 합계 1 또는 100%가 되도록 정규화하지 않습니다. 낮은 전형성은 탐색 신호일 뿐, 좋은 아이디어나 새로운 발명이라는 증거가 아닙니다.

## 출처와 라이선스

- 논문: https://arxiv.org/abs/2510.01171
- 공식 연구 코드: https://github.com/CHATS-lab/verbalized-sampling
- 본 저장소: Apache License 2.0

논문 PDF는 저장소에 포함하지 않습니다. 연구·특허·안전·법률·고영향 분야의 결과는 별도 인간 검토가 필요합니다.

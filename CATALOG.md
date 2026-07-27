# 다양성 생성 엔진 확장팩 카탈로그

## Core

| 구성 | 상태 | 설명 |
|---|---|---|
| Verbalized Sampling | Implemented | 후보와 모델 추정 전형성을 함께 생성 |
| 해결 공간 층화 | Implemented | 생성 전 4~8개의 의미적 탐색축 구성 |
| 구조·제약 검증 | Implemented | 필수 필드, 전형성 범위, 중복 ID 검사 |
| 의미 메모리 | Roadmap | 배치 간 핵심 메커니즘 중복 탐지 |
| 품질·위험 게이트 | Skill/Prompt | 다양성과 별도로 유용성·구현성·위험 평가 |
| 포트폴리오 선택 | Roadmap | 서로 다른 층과 메커니즘의 후보 선택 |

## Verticals

| ID | 한국어명 | 핵심 입력 | 핵심 출력 | 상태 |
|---|---|---|---|---|
| `creative-writing` | 소설·서사 | 장르, 발제, 독자, 금지요소 | 제목, 세계관, 캐릭터, 플롯, 엔딩 | Prototype |
| `game-design` | 게임 기획 | 핵심 루프, 시스템, 피로지점 | 업데이트, 몬스터, 스킬, 보스, 엔딩 | Prompt Pack |
| `ip-invention` | IP·특허 | 기술문제, 기존구조, 필수효과 | 발명 후보, 설계회피, 검색식, 청구항 씨앗 | Prompt Pack |
| `safety-training` | 안전교육 | 작업, 장비, 센서, 교육행동 | 사고분기, 판정조건, UI·나레이션 | Prompt Pack |
| `business-strategy` | 사업전략 | 고객, 문제, 자산, 제약 | 사업모델, 수익모델, 진입전략, 검증계획 | Prompt Pack |
| `marketing-content` | 마케팅 | 타깃, 증거, 채널, 톤 | 캠페인, 카피, 고객여정, KPI 가설 | Prompt Pack |
| `visual-3d-design` | 3D·비주얼 | 목적, 엔진, 제작제약 | 실루엣, 부품, 재질, 리깅, LOD | Prompt Pack |
| `ai-character` | AI 펫·NPC | 성격, 기억, 욕구, 관계 | 행동, 감정, 대사, 기억, 성장 | Prompt Pack |
| `research-synthetic-data` | 연구·합성데이터 | 질문, 변수, 자산, 검증제약 | 가설, 반증, 실험, 합성 데이터 층 | Prompt Pack |
| `software-qa` | 소프트웨어 QA | API, 상태, 권한, 환경 | 경계값, 상태전이, 복구, 악의적 입력 | Prompt Pack |

## Apps

| 앱 | 상태 | 용도 |
|---|---|---|
| Novel Idea Studio | Specification | 제목부터 엔딩까지 소설 아이디어 포트폴리오 구성 |
| Narrative Lens Panel | Specification | 20개의 추상화된 서사 설계 관점으로 발제 검토 |
| Character Starter | Specification | 첫 등장·관계·행동 중심 캐릭터 생성 |
| Diversity Playground | Planned | Direct/List/VS/Stratified VS 비교 |
| Patent Idea Workbench | Planned | 발명 후보·설계회피·검색·검증 워크플로 |
| Safety Scenario Studio | Planned | 센서·분기·판정 포함 안전교육 시나리오 |
| Game Content Forge | Planned | 게임 업데이트 포트폴리오와 플레이테스트 |

## 상태 정의

- `Concept`: 방향만 정의
- `Prompt Pack`: 프롬프트·브리프·평가 기준 존재
- `Specification`: 앱 제작 명세 존재
- `Prototype`: 로컬 실행 가능한 초기 앱
- `Beta`: 외부 테스트 가능
- `Stable`: 정식 사용 권장

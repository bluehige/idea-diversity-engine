# 04. 플랫폼·배포 전략

## 1. 핵심 원칙

핵심 엔진을 특정 모델이나 UI에 묶지 않고 다음 세 층으로 분리한다.

```text
Core
  prompt builder / schema / dedup / quality gate / exporters

Adapters
  OpenAI / Anthropic / Gemini / local LLM / enterprise cloud

Surfaces
  web / chat app / MCP / IDE / game engine / workflow automation
```

이 구조를 지키면 하나의 스킬을 여러 플랫폼에서 재사용할 수 있다.

## 2. 플랫폼 매트릭스

| 플랫폼 | 적합한 형태 | 장점 | 한계 | 권장 단계 |
|---|---|---|---|---|
| GitHub | 공개 문서·스킬·스키마·SDK | 신뢰·버전관리·기여 | 일반 사용자 체험성 낮음 | 즉시 |
| Hugging Face Spaces | Gradio/Static/Docker 데모 | 빠른 공개 데모, 복제 가능 | 운영·비밀키·비용 관리 필요 | 1차 |
| Custom GPT / GPT Store | 지침·지식·Action 기반 도구 | 비개발자 접근성 | 플랫폼 의존, 공개 규칙 | 1차 |
| ChatGPT Apps SDK | 대화형 UI + 백엔드 | 채팅 안에서 인터랙티브 앱 | 심사·정책·백엔드 필요 | 2차 |
| Claude / MCP | 스킬·MCP 서버·Claude Code | 도구·데이터 연결 표준화 | 공개 소비자 마켓보다 B2B/개발자 중심 | 1~2차 |
| Gemini / Vertex AI | 공유 프롬프트·Agent Engine | GCP 배포·평가·보안 | 클라우드 설정 복잡 | 2차 |
| Microsoft Copilot Studio | Teams/M365 조직용 에이전트 | 기업 배포와 조직 카탈로그 | 라이선스·관리자 승인 | 2차 |
| LangGraph/LangSmith | 상태·기억·평가가 있는 에이전트 | 장기 실행, 관측성, 배포 | 개발 난도 | 2차 |
| Dify / Flowise / n8n | 노코드·로우코드 워크플로 | 빠른 기업 PoC, 자동화 | 복잡 로직·평가 커스터마이징 제약 | 1차 |
| Chrome 확장 | 웹페이지 문맥에서 아이디어 확장 | 글쓰기·Notion·메일과 즉시 연결 | 개인정보·권한 심사 | 2차 |
| VS Code 확장 | 개발·테스트·아키텍처 후보 | 개발자 워크플로 내장 | 개발자 시장 한정 | 2차 |
| Figma 플러그인 | UX·카피·레이아웃 방향 포트폴리오 | 디자이너 작업 흐름과 밀착 | Figma API·심사 | 2차 |
| Unity/Godot/Unreal 플러그인 | 퀘스트·NPC·레벨·테스트 생성 | 게임 제작 현장에 직접 연결 | 엔진별 유지보수 | 3차 |
| Slack/Teams/Notion | 팀 브레인스토밍 봇 | 협업·승인·기록 | 플랫폼별 권한·보안 | 2차 |
| 독립 SaaS | 범용 또는 수직 웹앱 | 결제·데이터·UX 통제 | 운영·마케팅·지원 필요 | 2차 |
| 온프레미스/로컬 | 민감 R&D·IP·국방·기업 | 데이터 통제 | 설치·모델 운영 비용 | 기업판 |

## 3. 플랫폼별 적용 설계

### 3.1 GitHub

공개 저장소는 다음 역할을 맡는다.

- 방법론과 주의사항의 단일 기준점
- 스킬·프롬프트·스키마 배포
- 예제와 평가 데이터 공개
- 수직 제품의 신뢰 자료
- 커뮤니티 기여와 이슈 수집

논문 PDF나 사용자 API 키, 회사 내부 자료는 포함하지 않는다.

### 3.2 Hugging Face Spaces

Spaces는 Gradio, Docker, Static HTML을 지원하고 Git 저장소 기반으로 자동 재빌드된다. 공개 데모에는 다음 화면이 적합하다.

- 동일 브리프의 Direct / List / VS 비교
- 의미 다양성·중복률
- 후보 카드와 전형성 밴드
- 사용자가 고른 후보의 문서 변환

비밀키는 코드에 넣지 않고 Space Secrets를 사용한다.

### 3.3 ChatGPT

두 경로가 있다.

1. **Custom GPT**: 빠른 검증. 지침, 지식 파일, Actions로 구성한다.
2. **Apps SDK**: 후보 카드, 비교표, 선택·병합 UI가 필요한 정식 제품에 적합하다.

공개 GPT는 시장 반응을 확인하기 좋지만, 핵심 메모리·평가·결제는 자체 백엔드로 분리해야 한다.

### 3.4 Claude·MCP

MCP 서버를 만들면 같은 엔진을 Claude.ai, Claude Desktop, Claude Code 및 다른 MCP 클라이언트에 연결할 수 있다.

권장 도구:

- `generate_portfolio`
- `expand_tail`
- `check_duplicates`
- `evaluate_candidates`
- `export_invention_card`
- `export_safety_scenario`

### 3.5 Gemini·Vertex AI

개인·소규모는 공유 프롬프트나 간단 웹앱으로 시작하고, 기업은 Vertex AI Agent Engine과 평가 서비스를 사용한다. 프롬프트 버전, 모델 버전, 비용, 평가 결과를 프로젝트 단위로 기록한다.

### 3.6 Microsoft Copilot Studio

안전·기술기획·사내 발명 발굴처럼 조직 내부 사용에 적합하다. Teams와 Microsoft 365 Copilot에 배포하거나 조직 카탈로그·상업 마켓으로 확장할 수 있다.

### 3.7 LangGraph/LangSmith

다음 조건에서 채택한다.

- 여러 배치의 의미 메모리 필요
- 인간 승인 후 다음 단계 진행
- 장기 실행과 재개
- 비용·지연·품질 추적
- 다중 도메인 exporter

### 3.8 Dify·Flowise·n8n

초기 B2B PoC에 유리하다.

- 폼 입력
- LLM 후보 생성
- JSON 검증
- 임베딩 중복 검사
- Slack/메일/Notion 전송
- 승인 후 문서 저장

핵심 스키마와 품질 게이트는 외부 코드 노드 또는 API로 유지하는 편이 좋다.

### 3.9 IDE와 제작 툴

#### VS Code / Codex / Claude Code

- 기술 설계 대안
- 테스트 케이스
- 리팩터링 전략
- ADR 초안
- 코드 리뷰 반례

#### Figma

- 사용자 흐름
- 화면 구성
- 마이크로카피
- 접근성 대안
- 디자인 토큰·스타일 방향

#### Blender·게임 엔진

- 실루엣·부품·재질 변형
- LOD·최적화 방식
- 맵 기믹
- NPC 행동·퀘스트
- 에디터 내 JSON 리소스 생성

## 4. 권장 배포 순서

### Phase 0 — 공개 기반

- GitHub 저장소
- README 한국어/영어
- 논문·공식 코드 출처
- 스킬·프롬프트·스키마

### Phase 1 — 무료 체험

- Hugging Face Space 또는 정적 웹 데모
- Custom GPT 또는 Claude Skill
- 결과 공유 링크
- 사용 로그보다 익명 평가 수집 우선

### Phase 2 — 수직 MVP

- 안전 시나리오 스튜디오 또는 IP 워크벤치
- 사용자 계정·프로젝트·의미 메모리
- Markdown/PDF/CSV/JSON 내보내기
- 팀 승인과 버전 비교

### Phase 3 — 기업 배포

- Teams/M365·Slack 연동
- MCP/API
- 온프레미스·전용 VPC
- 감사로그·권한·보존정책

## 5. 최종 권장 조합

가장 현실적인 조합은 다음이다.

```text
GitHub OSS Core
+ Hugging Face public demo
+ MCP/API adapter
+ Safety/IP vertical SaaS
+ Teams/M365 enterprise distribution
```

소설 생성기는 무료 유입 채널로 유지하고, 고부가가치 사업은 도메인 스키마와 검수 문서가 포함된 수직 제품으로 전환한다.

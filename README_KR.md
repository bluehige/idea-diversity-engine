# Idea Diversity Engine — 한국어

**Idea Diversity Engine**은 LLM에게 “아이디어 하나” 또는 “비슷한 아이디어 여러 개”를 받는 대신, **의미적으로 다른 후보 포트폴리오**를 만들기 위한 공개형 툴킷입니다.

핵심은 다음 네 단계입니다.

1. **Verbalized Sampling**: 후보와 모델 추정 전형성을 함께 생성
2. **해결 공간 층화**: 구조·데이터·제어·운영·사업 등 탐색축을 먼저 분리
3. **의미 메모리**: 현재 배치와 과거 배치의 개념 중복 제거
4. **품질 게이트**: 제약, 유용성, 구현성, 위험을 별도 평가

이 프로젝트는 원 논문이나 공식 코드의 대체물이 아니라, 해당 연구를 **콘텐츠·제품·사업·R&D·IP·안전·게임·소프트웨어 QA**에 적용하기 위한 독립적인 응용 설계 및 스킬 패키지입니다.

**v0.1 구현 범위:** 현재 참조 코드는 제공사 중립 프롬프트 빌더와 구조 검증기를 구현합니다. 임베딩 기반 의미 메모리, 자동 다양성 평가, 모델 어댑터, 웹 UI는 설계 문서와 로드맵에 포함되어 있으며 아직 참조 코드에 구현되지 않았습니다.

## 적용 가능한 영역

- 소설, 웹툰, 영상, 광고, 이미지 프롬프트
- 게임 퀘스트, 이벤트, NPC 행동, 라이브옵스
- 제품·서비스·사업모델·브랜드·캠페인 기획
- 연구 가설, 실험 설계, 선행연구 우회 질문
- 발명 발굴, 특허 후보, 설계 회피안
- 산업안전 체험 시나리오, 사고·근접사고 변형
- 소프트웨어 구조 대안, 테스트 케이스, 엣지 케이스
- 합성데이터, 사용자·고객·대화 시뮬레이션
- 교육용 문제 변형, 토론 주제, 역할극

## 핵심 주의사항

`typicality_estimate`는 **모델 추정 전형성**입니다. 다음 확률이 아닙니다.

- 시장 성공 확률
- 특허 등록 확률
- 실제 발생 빈도
- 정답 확률
- 품질 점수

낮은 전형성은 “덜 흔한 후보”라는 탐색 신호일 뿐, 좋은 아이디어 또는 새로운 발명이라는 증거가 아닙니다.

## 빠른 실행

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .

idea-diversity build-prompt --brief examples/briefs/safety_training.json --mode stratified
idea-diversity validate --input examples/outputs/sample_portfolio.json
```

CLI는 프롬프트 생성과 구조 검증만 담당하며 API 키를 저장하지 않습니다. 실제 모델 호출은 ChatGPT, Claude, Gemini, 로컬 LLM, Dify, LangGraph, n8n 등 원하는 어댑터에서 수행합니다.

## 공개·사업화 권장 순서

### 1단계: 공개 기반 확보

- GitHub 공개 저장소
- 한국어·영어 README
- 3개 핵심 스킬
- 프롬프트·스키마·예제
- 논문 및 공식 코드 출처 표시

### 2단계: 체험판

- Hugging Face Space 또는 웹 데모
- Direct / List / VS 비교 화면
- 후보 카드, Head/Mid/Tail, 중복 클러스터
- CSV/Markdown/JSON 내보내기

### 3단계: 수익화

- 안전체험관 시나리오 팩
- 게임 라이브옵스·몬스터·엔딩 팩
- 3D 콘셉트·에셋 변형 팩
- IP 발명 발굴·설계 회피 팩
- 기업용 팀 워크스페이스와 사내 구축형

자세한 내용은 다음 문서를 참고합니다.

- [전반 적용처 조사](docs/03_APPLICATION_LANDSCAPE_KR.md)
- [플랫폼·배포 전략](docs/04_PLATFORM_DISTRIBUTION_MATRIX_KR.md)
- [사업모델 포트폴리오](docs/05_BUSINESS_MODEL_PORTFOLIO_KR.md)
- [우선 개발할 수직 제품](docs/10_VERTICAL_PRODUCT_CONCEPTS_KR.md)
- [시장 검증 계획](docs/11_MARKET_VALIDATION_PLAN_KR.md)

## 출처

- 논문: https://arxiv.org/abs/2510.01171
- 공식 코드: https://github.com/CHATS-lab/verbalized-sampling

논문 PDF는 저장소에 포함하지 않습니다. 본 저장소의 원본 문서·코드·템플릿은 Apache License 2.0으로 배포합니다.

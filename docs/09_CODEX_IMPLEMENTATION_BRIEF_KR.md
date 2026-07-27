# 08. Codex 구현 작업지시서

## 1. 목표

기존 `novel-idea-app.html`과 `ask-authors.html`의 VS 관련 의미 오류를 먼저 바로잡고, 이후 공통 생성 엔진·의미 중복 제거·품질 게이트를 모듈화한다.

## 2. 작업 원칙

- 현재 UI를 한 번에 전면 개편하지 않는다.
- P0 의미 교정과 테스트를 먼저 완료한다.
- 모델 API 호출부와 프롬프트를 UI 코드에서 분리한다.
- 모든 구조화 출력은 JSON Schema로 검증한다.
- 브라우저에서 hidden chain-of-thought를 요청·표시하지 않는다.
- 최종 전체 검수는 릴리스 후보 빌드 직전에 수행하되, 각 작업에는 단위·통합 테스트를 둔다.

## 3. 1차 작업 - P0 의미 교정

### T1 확률 필드 교정

- `확률` -> `전형성_추정치` 또는 `typicality_estimate`
- 합계 100% 검증 삭제
- 값 범위 0~1 검증
- UI 도움말 추가

완료 조건:

- 후보 값 합계가 1이 아닌 테스트 fixture가 정상 렌더링
- 0 미만/1 초과 값은 repair 또는 오류

### T2 제목 VS 구조화

- 내부 후보 생각 지시 삭제
- 후보 객체 10개 반환
- `text`, `typicality_estimate`, `structure`, `hook`, `semantic_axis`
- 중복 제목 경고

### T3 작가 앱 reasoning 교정

- `<reasoning>` 파서·렌더링 제거
- `<cliche_baseline>`과 `<concise_rationale>`로 대체
- 기존 저장 데이터 마이그레이션

### T4 스키마 검증

- Ajv 또는 동등 라이브러리 적용
- 실패 필드만 수리하는 1회 repair 호출
- raw response는 개발 로그에 hash만 저장

## 4. 2차 작업 - 공통 엔진

### 권장 모듈

```text
src/
  llm/
    adapter.ts
    geminiAdapter.ts
  generation/
    vsEngine.ts
    strataBuilder.ts
    promptBuilder.ts
    repair.ts
  evaluation/
    constraints.ts
    semanticDedup.ts
    qualityGate.ts
  storage/
    projectStore.ts
    vectorStore.ts
  schemas/
  prompts/
```

단일 HTML 유지 시에도 동일 역할을 JS 모듈로 분리한다.

### 핵심 타입

```ts
type TypicalityBand = 'head' | 'mid' | 'tail';

interface VSCandidate {
  id: string;
  text: string;
  typicality_estimate: number;
  typicality_band: TypicalityBand;
  stratum: string;
  concise_rationale: string;
  key_mechanisms: string[];
  constraints_passed: string[];
  risks: string[];
}
```

## 5. 3차 작업 - 의미 메모리

- 후보 canonical summary 생성
- 임베딩 저장
- 배치 내·배치 간 최대 유사도 계산
- 0.88 이상 중복 의심
- 중복 후보만 다른 메커니즘으로 repair

완료 조건:

- 동일 표현 변형 fixture를 중복으로 탐지
- 핵심 메커니즘이 다른 유사 문장 fixture는 수동 보존 가능

## 6. 4차 작업 - 평가 하네스

명령 예:

```bash
npm run eval -- --dataset fixtures/briefs.json --methods direct,list,vs,vs-tail,stratified-vs --runs 3
```

출력:

- semantic diversity
- duplicate rate
- constraint pass rate
- schema rate
- average quality
- cost and latency
- CSV + Markdown report

## 7. 5차 작업 - IP 문서 내보내기

- 후보 포트폴리오 JSON
- Markdown 발명 카드
- 선행기술 검색 키워드 CSV
- 프로젝트 ZIP

## 8. 테스트 체크리스트

### 단위

- probability 범위
- band 분류
- schema parser
- threshold fallback
- candidate-set resampling
- duplicate detection

### 통합

- Gemini 정상 응답
- malformed JSON repair
- API timeout/retry
- 프로젝트 저장·복원
- 내보내기·재불러오기

### UI

- 모바일 후보 카드
- 숫자 의미 도움말
- 실패 상태
- 접근성 키보드 탐색

## 9. 금지 사항

- 후보 5개 점수 합계를 100%로 보정하지 말 것
- 전형성 값을 특허 등록 확률로 표기하지 말 것
- 낮은 전형성 후보를 품질 검증 없이 자동 채택하지 말 것
- chain-of-thought를 사용자 화면에 표시하지 말 것
- 공개 빌드에서 API 키를 localStorage에 저장하지 말 것

## 10. Definition of Done

- P0 의미 교정 완료
- 기존 기능 회귀 없음
- Schema 유효성 99% 이상
- Direct 대비 다양성 개선 검증
- 품질·비용 리포트 생성
- 보안 설정 문서화
- README와 프롬프트 버전 기록

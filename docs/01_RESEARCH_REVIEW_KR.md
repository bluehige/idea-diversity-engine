# 01. 논문 검토 및 유사 연구 맵

## 1. 확인한 원 논문

- 제목: Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity
- 저자: Jiayi Zhang 외 6인
- 식별자: arXiv:2510.01171
- 사용자 제공본: v3, 2025-10-10
- 조사 시점 최신본: v4, 2026-07-15 개정
- 공식 코드: CHATS-lab/verbalized-sampling

## 2. 핵심 주장

1. 정렬 이후 LLM은 여러 유효한 답이 가능한 문제에서도 소수의 익숙한 답에 집중한다.
2. 원인의 하나로 인간 선호 데이터의 `typicality bias`를 제시한다.
3. 단일 응답 대신 후보와 각 후보의 추정 확률을 함께 말하게 하면, 모델의 출력 목표가 단일 모드에서 응답 분포로 바뀐다.
4. 창작, 사회 대화 시뮬레이션, 개방형 QA, 합성데이터에서 다양성이 증가했다.
5. v4 기준, VS-Standard는 직접 프롬프트보다 비용 약 12%, 지연 약 23% 증가에 다양성 약 86% 증가를 보고한다.
6. 모델이 말한 확률은 완벽하게 교정된 값은 아니지만, 제한된 정답 공간에서는 일부 순위 정보를 보존한다.

## 3. 논문의 실무적 가치

### 강점

- 훈련 없이 프롬프트만으로 적용할 수 있다.
- 비공개 모델에도 적용 가능하다.
- 온도·top-p·min-p와 병행할 수 있다.
- 창작뿐 아니라 합성 데이터와 시뮬레이션에 적용 범위가 넓다.
- 다수 후보를 나열하는 List Prompt보다 분포 자체를 출력시키는 차이가 명확하다.

### 제한

- 후보·점수 출력 때문에 토큰과 지연이 증가한다.
- 작은 모델은 구조화 출력과 확률 추정의 인지 부담으로 품질이 낮아질 수 있다.
- 모델 추정 확률은 과제와 프롬프트에 따라 교정 상태가 달라진다.
- 한 호출의 다양성이 높아도 여러 배치에서 다시 비슷한 아이디어가 쌓일 수 있다.
- 저확률 응답이 곧 유용·신규·안전한 응답이라는 보장은 없다.

## 4. 유사 연구 분류

| 구분 | 연구 | 핵심 요지 | 본 프로젝트 적용 |
|---|---|---|---|
| 다양성 저하 진단 | Does Writing with Language Models Reduce Content Diversity? | InstructGPT 협업이 사람들의 결과를 더 유사하게 만들 수 있음을 실험 | 사용자 공동창작 결과의 집단 동질화 지표 추가 |
| 창의성 진단 | AI as Humanity's Salieri | 웹 텍스트 재조합 관점의 Creativity Index, 정렬 후 창의성 저하 보고 | 단순 유사도 외 원문 재현·표현 중복 감시 |
| 정렬 영향 진단 | Base Models Beat Aligned Models at Randomness and Creativity | 정렬 모델이 무작위성·게임 전략·창작에서 더 예측 가능 | Direct vs Base/Aligned 실험 설계 근거 |
| 꼬리 확장 | Growing a Tail | 온도, 관점 다양화, 여러 모델 집계로 인간에 가까운 긴 꼬리 | VS 외 관점·모델 앙상블 옵션 |
| 공간 층화 | SimpleStrat | 답 공간을 의미 층으로 나눈 뒤 층을 선택하여 생성 | IP 해결 공간의 구조적 커버리지 확보 |
| 배치 중복 방지 | Dynamic Context Evolution | tail sampling + semantic memory + adaptive prompt evolution | 대량 후보 생성의 핵심 확장 구조 |
| 훈련 단계 개선 | Modifying LLM Post-Training for Diverse Creative Writing | 희귀하면서 품질 좋은 샘플의 편차를 목적함수에 반영 | 자체 모델 훈련 시 장기 로드맵 |
| 확률 교정 | On Verbalized Confidence Scores for LLMs | 말로 표현한 확신은 프롬프트에 민감하며 일부 방식에서 교정 가능 | 확률을 사실로 표시하지 않고 실험별 검증 |
| 데이터 다양성 | On the Diversity of Synthetic Data and its Impact on Training LLMs | 합성 데이터 다양성이 후속 학습 성능과 양의 상관 | IP 후보뿐 아니라 학습·테스트 데이터 생성에 활용 |
| 모델 내부 복구 | Selective Layer Restoration Recovers Diversity | 선택 계층을 사전학습 가중치로 복원해 다양성 회복 | 오픈모델 자체 배포 시 연구 로드맵 |

## 5. 유사 연구 대비 본 설계의 위치

본 설계는 다음 네 기법을 결합한다.

1. **VS**: 응답 분포를 말하게 한다.
2. **SimpleStrat**: 의미 축을 먼저 나눈다.
3. **DCE**: 배치 간 의미 메모리를 유지한다.
4. **Quality/IP Gate**: 저전형성 후보를 기술·법적 검토 문서로 바꾼다.

즉, 원 논문을 그대로 복제하는 것이 아니라, **단발성 창의성 프롬프트를 지속 가능한 IP 탐색 시스템으로 확장**하는 방향이다.

## 6. 결론

가장 가까운 취지의 연구는 `Growing a Tail`, `SimpleStrat`, `Base Models Beat Aligned Models`, `Dynamic Context Evolution`이다. 원 논문이 “분포를 말하게 하는 프롬프트”에 초점을 둔다면, 본 제작 문서는 이를 의미 층화, 기억, 중복 제거, 품질 검증, IP 문서화까지 확장한다.

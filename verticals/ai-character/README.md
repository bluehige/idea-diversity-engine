# AI 펫·NPC 행동
### AI Character Vertical

친절한 대사와 칭찬을 반복하는 캐릭터 대신, **성격·기억·감정·욕구·관계·성장 단계**에 맞는 다양한 행동 후보를 생성합니다.

## 입력

- 성격 규칙과 금지 행동
- 요약 기억과 최근 사건
- 현재 감정·욕구·관계 단계
- 게임 상태와 사용 가능한 애니메이션
- 기억 저장·삭제 정책

## 출력

- 행동 후보 분포
- 감정 변화와 대사
- 참조한 기억
- 새 기억 저장 여부
- 관계 변화
- 애니메이션·VFX 태그
- 성장·희귀 반응 신호
- 일관성·안전 검사

## 품질 게이트

의외성과 캐릭터 일관성을 분리 평가합니다. 희귀 반응도 기억, 성격, 관계, 게임 규칙을 깨면 탈락시킵니다. 죄책감 유도, 과도한 의존, 무제한 자율행동을 금지합니다.

## 기존 자산

- 프롬프트: [`prompts/vertical_ai_pet_behavior.md`](../../prompts/vertical_ai_pet_behavior.md)
- 브리프: [`examples/briefs/ai_pet_behavior.json`](../../examples/briefs/ai_pet_behavior.json)

# IP·특허 아이디어
### IP Invention Vertical

기술 문제를 구조·센서·제어·데이터·운영·안전 층으로 분해하고, 서로 다른 작동 원리를 가진 **발명 가설과 설계회피 후보**를 생성합니다.

## 입력

- 해결할 기술적 문제와 원인
- 현재 제품·공정·시스템 구조
- 반드시 달성해야 할 기술적 효과
- 회피할 선행 구조와 금지 접근
- 활용 가능한 장비·센서·데이터·소프트웨어

## 출력

- 해결 공간 지도
- 발명 후보 카드
- 필수 구성요소와 연결 관계
- 작동 순서와 기술적 효과
- 최소 실시예와 변형 실시예
- 설계회피 후보
- 선행기술 검색 키워드
- 독립항·종속항 씨앗
- 실험·증거 확보 계획

## 필수 해석 규칙

`typicality_estimate`는 특허 신규성, 진보성, 등록 가능성 또는 권리범위 확률이 아닙니다. 모든 후보는 별도의 선행기술 검색, 기술 검증, 법률 검토가 필요합니다.

## 기존 자산

- 프롬프트: [`prompts/vertical_ip_design_around.md`](../../prompts/vertical_ip_design_around.md)
- 브리프: [`examples/briefs/ip_design_around.json`](../../examples/briefs/ip_design_around.json)
- 스킬: [`skills/ip-idea-diversifier/`](../../skills/ip-idea-diversifier/)

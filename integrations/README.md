# Integrations

Core 엔진은 모델 제공사에 종속되지 않습니다. 실제 API 호출, 인증, 재시도, 비용 기록, 로깅은 Integration 계층에서 구현합니다.

## Provider Adapters

- `openai`: Responses/API 구조
- `gemini`: Generate Content 구조
- `anthropic`: Messages 구조
- `local-llm`: OpenAI 호환 서버, llama.cpp, Ollama 등

## 공통 어댑터 계약

```text
input: provider-neutral prompt + structured-output schema
output: parsed portfolio JSON + raw metadata
metadata: model, latency, token usage, estimated cost, retries
errors: timeout, rate limit, malformed JSON, safety block
```

## 계획된 연결 방식

- CLI
- REST API
- MCP tools
- n8n·Dify·LangGraph 워크플로
- GitHub/Codex 제작 문서 전달

## 보안

API 키와 고객 브리프는 서버 측 비밀 저장소에서 관리합니다. 공개 앱의 브라우저 저장소와 저장소 커밋에 포함하지 않습니다.

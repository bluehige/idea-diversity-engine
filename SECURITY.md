# Security Policy

## Supported version

Only the latest tagged release is supported.

## Secret handling

- Never commit provider API keys, OAuth tokens, private prompts, customer briefs, or proprietary prior art.
- Store secrets in server-side environment variables or an approved secret manager.
- Do not place API keys in browser `localStorage` for a public deployment.
- Disable or redact request logging for sensitive R&D and IP briefs.

## Reporting

Open a private security advisory in the GitHub repository. Do not publish a live secret or customer data in a public issue.

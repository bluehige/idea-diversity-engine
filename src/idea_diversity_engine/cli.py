from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .prompting import build_prompt, load_brief
from .validation import validate_portfolio


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="idea-diversity")
    sub = parser.add_subparsers(dest="command", required=True)

    prompt_cmd = sub.add_parser("build-prompt", help="Build a provider-neutral VS prompt")
    prompt_cmd.add_argument("--brief", required=True, help="Path to brief JSON")
    prompt_cmd.add_argument("--mode", default="stratified", choices=["standard", "balanced", "tail", "stratified", "multi"])
    prompt_cmd.add_argument("--count", type=int, default=5)
    prompt_cmd.add_argument("--tau", type=float, default=0.10)
    prompt_cmd.add_argument("--output", help="Optional output text file")

    validate_cmd = sub.add_parser("validate", help="Validate a portfolio JSON file")
    validate_cmd.add_argument("--input", required=True, help="Path to portfolio JSON")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    try:
        if args.command == "build-prompt":
            prompt = build_prompt(load_brief(args.brief), mode=args.mode, count=args.count, tau=args.tau)
            if args.output:
                Path(args.output).write_text(prompt, encoding="utf-8")
            else:
                print(prompt)
            return 0

        if args.command == "validate":
            data = json.loads(Path(args.input).read_text(encoding="utf-8"))
            report = validate_portfolio(data)
            print(json.dumps(report, ensure_ascii=False, indent=2))
            return 0 if report["valid"] else 1

    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    return 2


if __name__ == "__main__":
    raise SystemExit(main())

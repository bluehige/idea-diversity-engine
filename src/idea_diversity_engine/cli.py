from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .catalog import VERTICALS
from .prompting import build_prompt, load_brief
from .validation import validate_portfolio


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="dge")
    sub = parser.add_subparsers(dest="command", required=True)

    prompt_cmd = sub.add_parser("build-prompt", help="Build a provider-neutral diversity prompt")
    prompt_cmd.add_argument("--brief", required=True, help="Path to brief JSON")
    prompt_cmd.add_argument("--vertical", choices=sorted(VERTICALS), help="Optional domain extension pack")
    prompt_cmd.add_argument("--mode", default="stratified", choices=["standard", "balanced", "tail", "stratified", "multi"])
    prompt_cmd.add_argument("--count", type=int, default=5)
    prompt_cmd.add_argument("--tau", type=float, default=0.10)
    prompt_cmd.add_argument("--output", help="Optional output text file")

    validate_cmd = sub.add_parser("validate", help="Validate a portfolio JSON file")
    validate_cmd.add_argument("--input", required=True, help="Path to portfolio JSON")

    sub.add_parser("list-verticals", help="List bundled domain extension packs")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    try:
        if args.command == "list-verticals":
            rows = [
                {
                    "id": key,
                    "name_ko": value["name_ko"],
                    "name_en": value["name_en"],
                    "status": value["status"],
                }
                for key, value in sorted(VERTICALS.items())
            ]
            print(json.dumps(rows, ensure_ascii=False, indent=2))
            return 0

        if args.command == "build-prompt":
            prompt = build_prompt(
                load_brief(args.brief),
                vertical=args.vertical,
                mode=args.mode,
                count=args.count,
                tau=args.tau,
            )
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

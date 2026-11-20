#!/usr/bin/env python3
"""Zero-dependency scanner for internal-context leaks, filler bloat, and AI copywriting tells."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "out",
    ".next",
    ".nuxt",
    ".svelte-kit",
    "coverage",
    "vendor",
    "__pycache__",
    ".venv",
    "venv",
}

SCAN_EXTS = {
    ".tsx",
    ".jsx",
    ".ts",
    ".js",
    ".vue",
    ".svelte",
    ".astro",
    ".html",
    ".md",
    ".mdx",
    ".swift",
    ".kt",
    ".dart",
    ".json",
    ".yaml",
    ".yml",
}

PROSE_EXTS = {".md", ".mdx", ".html"}
LEGAL_FILE_RE = re.compile(r"(?:^|/)(?:legal|privacy|terms|security|gdpr)(?:[._/-]|$)", re.I)
ADMIN_FILE_RE = re.compile(r"(?:^|/)admin(?:[._/-]|$)", re.I)
TEST_OR_META_RE = re.compile(
    r"(?:\.(?:test|spec|check|stories)\.[^.]+$|^(?:package(?:-lock)?|tsconfig.*|pnpm-lock|yarn\.lock|composer\.lock).*)$",
    re.I,
)

# Strings enclosed in quotes/backticks or JSX/HTML inner text
QUOTED_RE = re.compile(
    r'("(?:\\.|[^"\\]){4,}"|\'(?:\\.|[^\'\\]){4,}\'|`(?:\\.|[^`\\]){4,}`|>[^<>{}\n]{4,}<)'
)
COMMENT_LINE_RE = re.compile(r"^\s*(?://|#|/\*|\*|<!--)")
IMPORT_LINE_RE = re.compile(r"^\s*(?:import|export)\b.*\bfrom\s+['\"][^'\"]+['\"]|^\s*require\(['\"][^'\"]+['\"]\)")

RULES: list[tuple[str, re.Pattern[str]]] = [
    (
        "pipeline-leak",
        re.compile(
            r"\b(?:in\s+(?:app\s+store|play\s+store|chrome\s+web\s+store|microsoft\s+store)?\s*review|"
            r"pending\s+(?:approval|review|verification|kyc|notarization)|"
            r"awaiting\s+(?:approval|kyc|review)|"
            r"submitted\s+to\s+(?:the\s+)?(?:app\s+store|play\s+store|store))\b",
            re.I,
        ),
    ),
    (
        "storage-arch-leak",
        re.compile(
            r"(?:(?<![.\w])(?:localstorage|sessionstorage|indexeddb)(?!\s*\.)|"
            r"\b(?:browser(?:'s)?\s+local\s+storage|no\s+backend(?:\s+server)?|zero\s+servers?|without\s+a\s+(?:backend|server))\b)",
            re.I,
        ),
    ),
    (
        "paranoia-hype",
        re.compile(
            r"\b(?:never\s+leaves\s+your\s+(?:device|browser|computer|machine)|"
            r"military[- ]grade|bank[- ]grade(?:\s+encryption)?|100%\s+local)\b",
            re.I,
        ),
    ),
    (
        "ai-infra-plumbing",
        re.compile(
            r"\b(?:vector\s+embeddings?|rag\s+pipeline|fallback\s+model|"
            r"rate\s+limit\s+exceeded|cors\s+error|jwt\s+token|"
            r"(?<![.\w])prisma(?!\s*\.)|postgresql)\b",
            re.I,
        ),
    ),
    (
        "restated-subtitle",
        re.compile(
            r"\b(?:(?:manage|configure|customize|update)\s+(?:how\s+and\s+when|your\s+(?:personal|account))\s+"
            r"[^.\n]{0,35}\b(?:settings|preferences|notifications)|"
            r"the\s+(?:table|list|chart|form)\s+below\s+(?:shows|displays|lists|compares)|"
            r"use\s+the\s+form\s+below\s+to)\b",
            re.I,
        ),
    ),
    (
        "toast-bloat",
        re.compile(
            r"\b(?:has\s+been\s+successfully\s+(?:saved|updated|deleted|created|copied|sent)|"
            r"have\s+been\s+successfully)\b",
            re.I,
        ),
    ),
    (
        "ai-buzzword",
        re.compile(
            r"\b(?:seamless(?:ly)?|effortless(?:ly)?|supercharg(?:e|ed|ing)|"
            r"unleash(?:ing)?|elevat(?:e|ing)\s+your|cutting[- ]edge|next[- ]generation|"
            r"game[- ]chang(?:er|ing)|delve|tapestry|pivotal|"
            r"streamlin(?:e|ing)\s+your|empower(?:s|ing)?\s+(?:teams|users|you|your)|"
            r"crafted\s+for\s+modern)\b",
            re.I,
        ),
    ),
    (
        "ai-trope",
        re.compile(
            r"(?:\b(?:not\s+(?:just|merely|only)\s+a\s+\w+[^.!?\n]{0,40},\s*(?:it'?s|but)|"
            r"no\s+fluff,?\s+no\s+\w+|built\s+for\s+\w+,\s+not\s+\w+)\b|"
            r"\b(?:let'?s\s+dive\s+in\b|here'?s\s+what\s+you\s+need\s+to\s+know\b|"
            r"oops!\s+something\s+went\s+wrong\b|you'?re\s+all\s+set!|"
            r"i\s+hope\s+this\s+helps\b)|"
            r"\b(?:fast\.\s*simple\.\s*(?:powerful|secure)|simple\.\s*fast\.\s*(?:powerful|secure)|"
            r"plan\.\s*track\.\s*ship)\b|"
            r"[🚀✨⚡💡🎉]\s*(?:\*\*|[A-Za-z])|"
            r"—[^—\n]{2,100}—)",
            re.I,
        ),
    ),
]


def is_legal_context(path_str: str, lines: list[str], idx: int) -> bool:
    if LEGAL_FILE_RE.search(path_str):
        # In mixed route files (e.g. billing/pricing + privacy/terms), scope strictly near privacy/terms sections if present
        window_start = max(0, idx - 60)
        chunk = "\n".join(lines[window_start : idx + 1]).lower()
        if any(tok in chunk for tok in ("/privacy", "/terms", "privacy policy", "terms of service")):
            return True
        if LEGAL_FILE_RE.search(Path(path_str).name):
            return True
    return False


def extract_text_segments(line: str, ext: str) -> list[str]:
    if ext in PROSE_EXTS:
        return [line]
    return [m.group(0) for m in QUOTED_RE.finditer(line)]


def scan_file(path: Path, include_legal: bool = False, include_admin: bool = False) -> list[dict]:
    path_str = path.as_posix()
    if not include_admin and ADMIN_FILE_RE.search(path_str):
        return []

    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    ext = path.suffix.lower()
    lines = raw.splitlines()
    findings: list[dict] = []

    for idx, line in enumerate(lines, start=1):
        if COMMENT_LINE_RE.match(line) or IMPORT_LINE_RE.match(line):
            continue
        segments = extract_text_segments(line, ext)
        if not segments:
            continue
        in_legal = False if include_legal else is_legal_context(path_str, lines, idx - 1)
        for seg in segments:
            for category, pattern in RULES:
                if in_legal and category in ("storage-arch-leak", "ai-infra-plumbing"):
                    continue
                m = pattern.search(seg)
                if m:
                    findings.append(
                        {
                            "path": path_str,
                            "line": idx,
                            "category": category,
                            "match": m.group(0),
                            "snippet": line.strip()[:140],
                        }
                    )
    return findings


def iter_files(targets: list[Path]):
    for target in targets:
        if target.is_file():
            if target.suffix.lower() in SCAN_EXTS and not TEST_OR_META_RE.match(target.name):
                yield target
            continue
        if not target.is_dir():
            continue
        for root, dirs, files in os.walk(target):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in sorted(files):
                if TEST_OR_META_RE.match(name):
                    continue
                p = Path(root) / name
                if p.suffix.lower() in SCAN_EXTS:
                    yield p


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit UI copy for oversharing leaks, filler bloat, and AI tells.")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to scan (default: .)")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of plain lines")
    parser.add_argument("--include-legal", action="store_true", help="Also scan privacy/terms disclosures for storage/infra terms")
    parser.add_argument("--include-admin", action="store_true", help="Also scan internal admin routes and components")
    args = parser.parse_args()

    targets = [Path(p) for p in args.paths]
    findings: list[dict] = []
    for f in iter_files(targets):
        findings.extend(scan_file(f, include_legal=args.include_legal, include_admin=args.include_admin))

    if args.json:
        print(json.dumps({"count": len(findings), "findings": findings}, indent=2))
    else:
        for item in findings:
            print(f"{item['path']}:{item['line']} [{item['category']}] {item['match']} -> {item['snippet']}")
        if not findings:
            print("stop-oversharing audit OK (0 issues)")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

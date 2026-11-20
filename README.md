# Stop oversharing

A skill for AI coding agents that keeps internal engineering context, redundant UI filler, and synthetic AI copywriting tells out of customer-facing copy.

## The problem

Give an AI coding agent normal builder context:

- *"Store user settings in `localStorage`, don't spin up a backend for this."*
  Output in UI: `100% Local! Stored in your browser's local storage and never leaves your computer!`
- *"Web app is shipped; iOS is currently in App Store review."*
  Output in hero: `iOS · In App Store Review` and `"unlocks once approval completes"` inside paid tiers.
- *"AI search runs RAG on Pinecone and falls back to a smaller model on rate limits."*
  Output in spinner: `Querying vector embeddings via fallback model...`
- *"Build a Settings page with Profile and Notifications."*
  Output under every heading: `Notifications` followed by `Configure how and when you receive notifications.`
- *"Write punchy landing copy for our workspace."*
  Output in hero: `🚀 Not just a workspace — supercharge your team with seamless, next-generation collaboration!`

Agents mistake **context meant for the builder** for **copy meant for the user**, pad empty slots to look complete, and default to synthetic AI slogans.

**Stop oversharing** prevents this across landing pages, pricing cards, settings screens, forms, empty states, toasts, errors, and docs.

## What it enforces

- **Surface scope:** Strict rules on customer UI and marketing pages. Calm factual specs allowed on `/privacy`, `/terms`, `/security`, and `llms.txt` without sales hype. Code comments, commits, pull requests, and admin views are exempt.
- **Audience gate (`DROP` / `TRANSLATE` / `KEEP`):** Drops review queues, KYC blockers, database/storage plumbing, fallback model details, hosting-cost motives, and package IDs in prose. Translates builder constraints into calm product facts.
- **Density contract and restated-heading rule:** Removes subtitles that restate their heading or describe visible layout. Sets word limits per UI slot (`<= 18` words hero subtitle, `<= 6` words plan bullets, `1 to 4` words toasts without exclamation marks, `0` words settings helpers by default).
- **Anti-paranoia rule:** Blocks unsolicited defensive claims (`"never leaves your computer"`, `"military-grade encryption"`, `"zero servers"`).
- **Human voice:** Cuts `"Not X, just Y"` setups, three-beat slogans (`"Fast. Simple. Powerful."`), em dashes (`—`), AI buzzwords (`seamless`, `effortless`, `supercharge`, `unleash`, `elevate`, `next-generation`), emoji feature bullets, repetitive bold labels, and faux-apology microcopy (`"Oops! Something went wrong!"`).

## Install

```bash
npx skills add erdemovali/stop-oversharing
```

Manual symlinks or copies work for any agent runtime:

- **Claude Code:** `~/.claude/skills/stop-oversharing`
- **Codex / Gemini CLI / cross-runtime:** `~/.agents/skills/stop-oversharing`
- **Antigravity:** `~/.gemini/config/skills/stop-oversharing`

## Codebase audit CLI

Scan UI components, templates, i18n dictionaries, and Markdown files with the bundled Python 3 script:

```bash
python3 scripts/audit.py src/ app/
```

Outputs `path:line [category] match -> snippet` across eight categories (`pipeline-leak`, `storage-arch-leak`, `paranoia-hype`, `ai-infra-plumbing`, `restated-subtitle`, `toast-bloat`, `ai-buzzword`, `ai-trope`). Legal disclosures and admin files are skipped by default; pass `--include-legal`, `--include-admin`, or `--json` for CI.

## Structure

```
stop-oversharing/
├── SKILL.md                    # Core rules, audience gate, density limits, and human voice
├── scripts/
│   └── audit.py                # Zero-dependency codebase scanner
├── references/
│   ├── leak-patterns.md        # 12 patterns covering leaks, bloat, and AI tells
│   ├── translations.md         # 29 builder-prompt to calm-copy rewrites
│   └── examples.md             # 8 before and after UI transformations
├── LICENSE
└── README.md
```

## License

MIT · [Erdem Ovali](https://github.com/erdemovali)

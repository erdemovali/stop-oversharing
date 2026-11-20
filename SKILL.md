---
name: stop-oversharing
description: Use when writing, editing, or auditing customer-facing UI copy, landing pages, pricing cards, onboarding, settings, forms, empty states, toasts, loaders, error messages, changelogs, SEO metadata, or llms.txt, especially when prompts mention internal release status, review queues, storage or AI architecture, billing blockers, or bare UI slots that tempt filler prose and AI marketing cliches.
metadata:
  author: Erdem Ovali (https://github.com/erdemovali)
  version: "1.0.0"
---

# Stop oversharing

Builder prompts are private context, never customer copy. Customer interfaces should read as if a human product team wrote them: zero leaked internals, zero filler subtitles, and zero AI copywriting tells.

## Surface scope

- **Strict:** UI components, landing pages, pricing, onboarding, settings, forms, modals, empty states, toasts, loaders, errors, store listings, SEO metadata.
- **Calm and factual:** `/privacy`, `/terms`, `/security`, `llms.txt`, SDK docs, changelogs (plain technical facts allowed; hype, meta-narration like `"added to replace"`, and AI cliches banned).
- **Exempt:** Code comments, commit messages, pull requests, internal docs, admin views.

## 1. The audience gate

Classify every fact from the prompt before writing UI copy:

- **DROP (0 words in UI):** Review queues (`in review`, `TestFlight`, `pending approval`), KYC or DNS blockers, storage and database plumbing (`localStorage`, `IndexedDB`, `SQLite`, `Redis`, vector DBs, model names), hosting-cost motives, keystores, package or store IDs in prose, signing excuses.
- **TRANSLATE:** Rewrite builder context into calm customer words:

| Internal context | Never write | Write instead |
|---|---|---|
| App or extension in review | `In App Store review`, `Pending approval` | `Coming soon` *(roadmap badge only)* |
| Offline or browser storage | `Stored in IndexedDB`, `No backend` | **0 words** *(or `Works offline` in hero)* |
| AI search and fallback LLM | `Querying Pinecone vectors via Haiku fallback...` | `Ask your docs` / `Searching...` |
| Billing or SSO blocker | `Stripe KYC pending`, `SAML blocked` | State shipped path (`Subscribe in app`) |
| Unsigned desktop build | `Notarization pending; right-click Open` | `Direct download · macOS and Windows` |
| Encryption plumbing | `Military-grade encryption outside DB` | `Encrypted sync` *(spec on `/privacy`)* |
| App or bundle identifiers | `com.acme.app`, `id1234567890` | Omit from prose; store badge link only |

- **KEEP:** What works today and the next action. See [references/translations.md](references/translations.md) and [references/leak-patterns.md](references/leak-patterns.md).

## 2. Density contract and restated-heading rule

Delete helper text that repeats its heading or label (`Notifications` -> *"Configure how you receive notifications"*). Never narrate visible layout (*"The table below compares..."*, *"Use the form below to..."*). Never pad sparse cards.

| Slot | Ceiling | Rule |
|---|---|---|
| Hero subtitle | **1 sentence, <= 18 words** | Outcome and supported platforms |
| Status badge | **1 to 3 words** | Live is default; badge only `Coming soon` |
| Plan bullet | **<= 6 words** | Shipped features only |
| Card subtitle | **<= 10 words** *(or 0)* | Omit when heading and button suffice |
| Settings or form helper | **0 words** default | `<= 10 words` only for non-obvious formats |
| Empty state | **<= 6 words + 1 button** | Zero database, table, or query nouns |
| Toast | **1 to 4 words, no `!`** | `Saved`, `Copied`, `Invite sent` |
| Loading state | **1 to 3 words** | `Searching...`, `Generating...` |
| Error | **What failed + next step** | Zero HTTP codes, routes, or rate windows |

## 3. Anti-paranoia rule

Never volunteer unsolicited denials (*"Never leaves your computer"*, *"Zero servers"*, *"100% local"*, *"Military-grade"*). Disclose data handling calmly on `/privacy`.

## 4. Human voice

Remove synthetic AI copywriting tells alongside internal leaks:

- **No "Not X, just Y" contrasts:** Cut negative setups (*"Not just a note app, it's..."*, *"Built for speed, not bloat"*, *"No fluff, just..."*). State what the product does directly.
- **No forced triads or staccato slogans:** Cut three-beat fragments (*"Fast. Simple. Powerful."*, *"Plan. Track. Ship."*). Replace triplets (*"design, collaborate, and scale"*) with one concrete capability or number.
- **No em dashes (`—`) or spaced `--` in UI copy:** Use periods, commas, or colons, or cut the second clause.
- **No stock AI buzzwords or `-ing` tails:** Ban `seamless`, `seamlessly`, `effortless`, `effortlessly`, `supercharge`, `unleash`, `elevate`, `empower`, `streamline`, `cutting-edge`, `next-generation`, `game-changing`, `robust`, `tailored`, `delve`, `tapestry`, `pivotal`, `reimagining`, `crafted for modern teams`, and bolted-on participles (*"...ensuring effortless sync"*). Prefer plain verbs (`is`, `has`, `syncs`, `exports`) over `serves as` or `boasts`.
- **No decorative formatting:** Write headings, card labels, and buttons in **sentence case** (keep Title Case for proper nouns and plan names only). Never put emoji bullets (`🚀`, `✨`, `⚡`, `🔒`, `💡`, `🎉`) on feature lists or headings. Never repeat `**Bold Label:** explanation` across feature lists.
- **No chatbot or fake-cheer microcopy:** Cut staged openers (*"Let's dive in"*, *"Here's what you need to know"*), exaggerated praise (*"You're all set!"*, *"Awesome!"*), faux apologies (*"Oops! Something went wrong"*), and exclamation marks in routine UI states.

## 5. Audit mode and red flags

Scan source trees with `python3 scripts/audit.py src/ app/`, then rewrite flagged copy around concrete facts instead of swapping words for synonyms. See [references/examples.md](references/examples.md).

Red flags requiring immediate rewrite: `in review`, `pending approval`, `localStorage`, `local storage`, `IndexedDB`, `no backend`, `vector embeddings`, `fallback model`, `rate limit`, `KYC`, `notarization`, `never leaves your`, `military-grade`, package IDs in prose, restated settings subtitles, `"has been successfully saved"`, `seamless`, `effortless`, `supercharge`, `unleash`, `not just a`, staccato 3-word slogans, emoji feature bullets, parenthetical em dashes, `"Oops! Something went wrong"`, `"You're all set!"`.

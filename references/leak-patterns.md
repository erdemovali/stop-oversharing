# The 12 patterns to remove

Why AI-generated interfaces leak private context and read like synthetic templates, and how to fix each one.

## 1. Pipeline and review leakage
- **What happens:** You share status context (*"Chrome extension is pending store review"*, *"iOS is in TestFlight"*, *"waiting on Stripe KYC"*). The model pastes that pipeline status straight into badges, heroes, and pricing tables.
- **Why it hurts:** Users do not care about approval queues or compliance checks. Showing `"In Store Review"` makes a shipped product look unfinished.
- **Fix:** List shipped platforms cleanly. Show `Coming soon` once in neutral roadmap or download sections only.

## 2. Prompt-echoing architecture
- **What happens:** You give a technical constraint (*"keep drafts in IndexedDB, no backend"*). The model adds a banner reading *"Zero backend servers! Everything lives in your browser IndexedDB to save costs!"*
- **Why it hurts:** Architecture choices are invisible internals. Exposing them reveals fragility and adds unnecessary technical jargon.
- **Fix:** Persist data silently (`0` words in UI) or write `Works offline` (`<= 3` words) in hero copy only.

## 3. Defensive privacy monologues
- **What happens:** Asked to protect user data, the model writes unsolicited denials: *"Military-grade encryption! Your files stay in RAM and NEVER leave your machine unencrypted!"*
- **Why it hurts:** Calm products state what they do instead of protesting innocence across modals and footers. Over-protesting creates suspicion.
- **Fix:** Use short neutral labels (`Encrypted sync`, `Offline ready`) in UI and keep factual specifications on `/privacy` or `/security`.

## 4. AI and infrastructure plumbing bleed
- **What happens:** Model routing, vector databases, HTTP status codes, ORM names, or auth tokens spill into buttons, spinners, and error toasts (*"Querying Pinecone vector embeddings via Haiku fallback model"* or *"Redis 429 rate limit exceeded on `/api/v2/import`"*).
- **Why it hurts:** Exposes attack surface, confuses users, and makes standard states read like debug logs.
- **Fix:** Write plain status text (`Searching...`, `Too many attempts. Try again shortly.`).

## 5. Workaround and blocker confessions
- **What happens:** An operational workaround turns into a public apology or tutorial (*"macOS Gatekeeper blocks unsigned apps while notarization finishes, so right-click and choose Open"* or *"Merchant verification pending, web checkout disabled"*).
- **Why it hurts:** Explains internal bottlenecks instead of guiding the user to the working flow.
- **Fix:** State only the working path (`Direct download · macOS and Windows`, `Subscribe in the mobile app`).

## 6. Restated-heading and layout narration
- **What happens:** Unwilling to leave whitespace, the model repeats every heading in a filler sentence (`Notifications` -> *"Configure how and when you receive notifications"*) or describes visible layout (*"The table below compares..."*, *"Use the form below to..."*).
- **Why it hurts:** Forces users to read obvious labels twice before clicking or typing.
- **Fix:** Delete subtitles that only echo the heading or announce visible controls (`0` words).

## 7. Card, toast, and empty-state stuffing
- **What happens:** Told to make cards `"look complete"`, the model adds redundant `Live` pills, long footers, verbose confirm toasts (*"Your profile settings have been successfully updated and persisted"*), and database-noun empty states (*"No rows found matching filter in workspaces table"*).
- **Why it hurts:** Extra boilerplate buries primary actions and slows down scanning.
- **Fix:** Enforce word ceilings: `1 to 4` word toasts (`Saved`) and concise empty states (`No projects yet` + `New project`). Also keep unshipped roadmap promises out of paid tier bullets.

## 8. Negative contrasts and staccato slogans
- **What happens:** Headlines lean on synthetic binary setups (*"Not just a note app, it's your second brain"*, *"Built for speed, not bloat"*, *"No fluff, no chaos, just focus"*) or three-beat fragments (*"Fast. Simple. Powerful."*).
- **Why it hurts:** Nobody claimed the negative half, and stacked slogans signal templated marketing copy immediately.
- **Fix:** Drop the contrast and the three-beat slogan. State what the product does and any concrete limit or metric.

## 9. Stock AI buzzwords and shallow `-ing` tails
- **What happens:** Product cards pile on inflated adjectives (*`seamless`*, *`effortless`*, *`cutting-edge`*, *`next-generation`*, *`supercharge`*, *`unleash`*, *`elevate`*, *`empower`*, *`streamline`*, *`tailored`*, *`crafted for modern teams`*) or bolt participle tails onto plain claims (*"...ensuring effortless collaboration"*).
- **Why it hurts:** High-frequency hype words crowd out specific facts and erase product differentiation.
- **Fix:** Replace stacked hype with specific verbs (`syncs`, `exports`, `searches`), formats, or counts.

## 10. Em-dash (`—`) clause glue
- **What happens:** Headlines, modal descriptions, and Pricing cards string unrelated clauses together with em dashes (`"Built for speed — crafted for clarity — ready for teams"`).
- **Why it hurts:** Constant dashes avoid choosing clear sentence boundaries and stamp copy with an unmistakable chatbot cadence.
- **Fix:** Split into plain sentences with periods or commas, or cut the trailing aside.

## 11. Decorative emoji, Title Case, and bold labels
- **What happens:** Feature grids open every bullet with `🚀`, `✨`, `⚡`, or `🔒`, capitalize every word (`Upgrade Your Workflow Today`), or format lists identically as `**Speed:** Blazing fast responses`.
- **Why it hurts:** Mechanical decoration masks weak claims and clutters clean UI hierarchy.
- **Fix:** Use sentence case, plain text bullets without emoji markers, and remove repetitive bold label prefixes.

## 12. Performative and chatbot microcopy
- **What happens:** Flows open with staged narration (*"Let's dive in"*, *"Here's what you need to know"*), celebrate trivial actions (*"You're all set!"*, *"Awesome!"*), or apologize artificially on errors (*"Oops! Something went wrong!"*).
- **Why it hurts:** Faux familiarity ages badly in daily-use software and wastes vertical space on repeat visits.
- **Fix:** Write quiet, neutral confirmations (`Saved`, `Invite sent`) and factual errors (`Upload failed. Try a smaller file.`).

---

## Automated scanner

Run the bundled script across source files before shipping:

```bash
python3 scripts/audit.py src/ app/
```

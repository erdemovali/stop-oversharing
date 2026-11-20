# Developer prompt to calm copy matrix

Rewrites from raw builder context and AI copy habits to human product copy.

## Store releases, extensions, and platforms

| Builder context | Naive copy | Ship instead |
|---|---|---|
| "Web app is live, iOS is in App Store review" | `Web · Live | iOS · In App Store Review` | `Web · iOS (Coming soon)` |
| "Chrome extension submitted to store review" | `Waiting on Chrome Web Store approval` | `Coming soon` *(roadmap badge only)* |
| "Slack app still waiting on directory review" | `Install manually while Slack reviews build 12` | **0 words** *(omit until listed)* |
| "macOS build signed, waiting notarization ticket" | `Notarization pending, right-click Open to bypass` | `macOS (Universal)` *(publish clean OS label once ready)* |

## Local-first and client-side tools

| Builder context | Naive copy | Ship instead |
|---|---|---|
| "Save preferences in localStorage" | `Saved in browser localStorage; never leaves your PC` | **0 words** |
| "Store offline drafts in IndexedDB with no backend" | `Zero backend servers! Pure client-side architecture` | `Works offline` *(hero only, `<= 3` words)* |
| "Compress images via WebAssembly in browser" | `Runs client-side WASM in memory, zero uploads` | `Browser image compression` *(or **0 words**)* |
| "Don't add cloud telemetry" | `We swear zero tracking, zero servers, zero logs` | **0 words** *(factual policy on `/privacy`)* |

## AI features and copilots

| Builder context | Naive copy | Ship instead |
|---|---|---|
| "Search runs RAG over Pinecone embeddings" | `Querying vector embeddings in Pinecone...` | `Searching...` |
| "Fallback from Sonnet to Haiku on rate limit" | `Using faster fallback model due to quota limits` | **0 words** *(transparent fallback)* |
| "Chunk documents to fit 128k context window" | `Splitting into 512-token overlapping vectors...` | `Reading file...` |
| "No training on enterprise workspaces" | `Strict zero-data-retention API contract guaranteed` | `Private workspace` *(details on `/security`)* |

## SaaS billing, auth, and teams

| Builder context | Naive copy | Ship instead |
|---|---|---|
| "Stripe web checkout waiting on KYC check" | `Merchant verification pending; subscribe via iOS` | `Subscribe in the mobile app` |
| "SSO SAML not ready until next sprint" | `Okta SAML blocked on Phase 2 auth rewrite` | **0 words** *(list Email and Google sign-in)* |
| "App ID is 1234567890 / com.acme.app" | `Download Acme (id1234567890 / com.acme.app)` | **Store badge link only**; omit IDs from prose |
| "User might already hold a mobile plan" | `Check Supabase entitlements for existing IAP row` | `Already subscribed? Sign in to view your plan.` |

## Forms, settings, empty states, and toasts

| Builder context | Naive copy | Ship instead |
|---|---|---|
| "Settings card for Notifications" | `Manage how and when you receive notifications` | **0 words** *(heading explains the control)* |
| "Profile form updated via PATCH endpoint" | `Your profile has been successfully updated in DB!` | `Saved` |
| "No rows in invoices table for orgId" | `Query returned 0 rows from invoices table` | `No invoices yet` + `Create invoice` |
| "Paste API key starting with sk_" | `Stored hashed in PostgreSQL via Prisma` | `Format: sk_...` *(only if validation needs it)* |

## Errors and rate limits

| Builder context | Naive copy | Ship instead |
|---|---|---|
| "Rate limited at 60 req / 15m per IP" | `Redis 429 rate limit exceeded (60/15m window)` | `Too many attempts. Try again shortly.` |
| "Upload rejected > 10MB by Nginx" | `413 Payload Too Large at edge reverse proxy` | `File exceeds 10 MB limit.` |
| "JWT expired or CORS mismatch" | `JWT signature expired (401 Unauthorized)` | `Session expired. Sign in again.` |

## AI marketing cliches and robotic microcopy

| Naive AI phrasing | Why it reads synthetic | Ship instead |
|---|---|---|
| `Not just a note app, it's your second brain.` | Binary negative setup ("Not just X") | `Markdown notes and doc search.` |
| `Supercharge your workflow with seamless sync.` | Stock buzzwords (`supercharge`, `seamless`) | `Drafts sync across desktop and web.` |
| `🚀 Blazing Fast · ✨ Effortless · 🔒 Secure` | Emoji bullets and three-beat fragments | `Opens in 50 ms. Works offline.` |
| `Let's dive into your workspace setup!` | Staged chatbot opener and exclamation mark | `Create workspace` |
| `Oops! Something went wrong on our end!` | Performative faux apology | `Could not save changes. Try again.` |
| `The table below compares our plan limits.` | Narrates layout the user can already see | **0 words** *(render the table directly)* |

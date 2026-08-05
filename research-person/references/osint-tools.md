# OSINT tooling — Sherlock and browser-use

Two optional command-line tools extend the research workflow beyond `web_search` / `web_fetch`. Both are open-source and require local installation. Read this file in Phase 1 if you decide to map the subject's digital footprint, and in Phase 3 if a source resists plain `web_fetch`.

Neither tool changes the skill's scope rules. The minor / private-individual refusal logic in `SKILL.md` applies before any tool is run. These tools are for documenting the public footprint of public figures — not for surveilling private people.

## Sherlock — social-account enumeration

`sherlock-project/sherlock` searches 400+ social networks for a given username and reports where that username exists. Use it in **Phase 1 (Discovery)** to locate the subject's plausible accounts, then verify each one by hand.

### Install

```bash
pipx install sherlock-project        # recommended
# or: pip install sherlock-project
# or: docker run -it --rm sherlock/sherlock
```

If installation fails or the environment has no network/package access, skip Sherlock and fall back to `web_search` for `"<name>" site:twitter.com` style queries. The tool is a convenience, not a dependency.

### Usage

```bash
# Single candidate handle, save a CSV into the sources folder
sherlock <handle> --csv --folderoutput research/<subject-slug>/sources/osint/

# Several candidate handles at once
sherlock <handle1> <handle2> <handle3> --folderoutput research/<subject-slug>/sources/osint/

# Restrict to specific platforms
sherlock <handle> --site Twitter --site GitHub --site LinkedIn
```

Useful flags: `--csv` / `--xlsx` (structured export), `--folderoutput DIR` (multi-user output dir), `--output FILE` (single-user file), `--site` (limit platforms), `--timeout SECONDS` (default 60), `--proxy URL`.

Do **not** pass `--nsfw`. Adult-site enumeration is outside the scope of neutral biographical research.

### Interpreting results — discipline

Sherlock proves a username string is *registered* on a site. It does **not** prove the account belongs to the subject. Username collisions are common, and impersonation accounts exist.

- Treat every Sherlock hit as a **lead**, not a fact. Open each candidate account and confirm identity from its content (bio, verified badge, cross-links from official pages, consistent name/photo/affiliation).
- Only accounts you have personally verified may appear in the deliverable, and they sit at **Tier 4** — a starting point to find Tier 1/2 reporting, never the sole citation for a claim. See the tier rules in `SKILL.md`.
- A confirmed official account (verified badge, linked from the subject's institutional page) can be cited as Tier 1 for the narrow fact that *the subject said X on that platform on that date* — but archive the specific post and prefer secondary reporting where it exists.
- Record the raw Sherlock output under `sources/osint/` and note in `_working-notes.md` which hits you verified, which you rejected, and why.

Do not list "accounts found" in the deliverable as a roster of the subject's online presence. Report only verified accounts, and only where they support a documented fact.

## browser-use — agentic browser for hard-to-reach sources

`browser-use/browser-use` drives a real Chromium browser with an LLM, so it can reach pages that plain `web_fetch` cannot: JavaScript-rendered content, infinite-scroll archives, multi-step navigation, sites that block simple fetches. Use it in **Phase 3 (Source acquisition)** as a fallback when `web_fetch` returns empty, truncated, or blocked content for a source you have already decided to cite.

### Install

```bash
uv init && uv add browser-use && uv sync
uvx browser-use install        # installs Chromium if needed
# pip install browser-use also works — see the project docs
```

### Minimal usage

```python
from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

async def main():
    browser = Browser()
    agent = Agent(
        task="Open <url>, wait for the article body to render, "
             "and return the full visible text and the publication date.",
        llm=ChatBrowserUse(),   # or an Anthropic Claude model
        browser=browser,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
```

It supports ChatBrowserUse, Anthropic Claude, OpenAI, Gemini, and local models via Ollama. Prefer a Claude model where an API key is available.

### Discipline

- Use it **only** to retrieve content you would otherwise cite — it is an acquisition fallback, not a research agent. Do not delegate judgment about what to include to the browser agent.
- Save whatever it retrieves into `sources/articles/` under the normal naming pattern and cite it exactly as any other source. The tool used to fetch a page does not change its Tier.
- **Never** use it to log in, bypass a paywall, accept terms on the subject's behalf, defeat a CAPTCHA, or access anything gated. Gated content is out of reach — log the failure in `_working-notes.md` and move on.
- Respect `robots.txt` and rate limits. One page at a time; no crawling.
- The browser agent can be wrong about what it "saw." Treat its returned text as you would any fetch — verify the key claim against the rendered page before citing.

## Where these fit the four phases

- **Phase 1 — Discovery:** optionally run Sherlock on candidate handles to surface accounts. Verify each; record verified ones in `_working-notes.md`.
- **Phase 3 — Source acquisition:** when `web_fetch` fails on a source you intend to cite, retry once with browser-use before logging the source as unretrievable.

Both tools are optional. The skill produces a complete, correctly cited deliverable without them. They reduce missed accounts and missed sources — they never lower the verification bar.

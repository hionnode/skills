---
name: research-person
description: Conduct rigorous, neutral biographical research on a person and produce a structured deliverable — summary, index, detailed research file with inline footnote citations, and a sources folder containing downloaded articles, PDFs, and a numbered bibliography. Use this skill whenever the user asks to research, profile, dossier, biographically document, or build a background file on any specific person — politicians, executives, academics, athletes, artists, religious figures, activists, historical figures, scientists, journalists, tech founders, or anyone else with a public footprint. Triggers on phrases like "research X", "profile X", "build a dossier on X", "biography of X", "deep background on X", "everything we know about X", "do research on X". Handles subject-type detection automatically and adapts the source list and topic checklist to the kind of person being researched. Can optionally map the subject's verified digital footprint and recover hard-to-fetch sources using OSINT tooling (Sherlock for social-account enumeration, browser-use for agentic source retrieval).
---

# Research Person

Conduct rigorous, neutral biographical research on a single person and produce a structured set of markdown deliverables backed by a fully cited sources folder.

## Scope

This skill applies to a single person — living, deceased, public figure, or moderately documented private individual with legitimate public-interest grounds. The same framework handles politicians, executives, academics, athletes, artists, religious figures, activists, historical figures, scientists, journalists, and tech founders. Subject-type detection happens early and adapts the rest of the workflow.

Refuse the task and explain why if the subject appears to be:

- A minor (under 18) — privacy concerns outweigh research interest by default.
- A private individual without a clear public-interest justification — this skill is for documenting public figures, not surveilling private people. If the user is researching a private individual they have a personal connection to (estranged family, missing person, etc.), redirect to a different approach.

For subjects with active criminal proceedings, proceed but apply allegations-vs-charges-vs-convictions discipline strictly (Phase 4).

## Output structure

Create this folder layout under `research/<subject-slug>/`. The slug is the lowercase, hyphenated form of the person's name (e.g., `suvendu-adhikari`, `sundar-pichai`).

```
research/<subject-slug>/
├── 00-summary.md            # Executive overview, 1500–2000 words
├── 01-index.md              # Navigable TOC linking every section in 02
├── 02-detailed-research.md  # Full research with inline footnote citations
├── 03-timeline.md           # Chronological events table
├── 04-career-history.md     # Domain-specific structured record
├── _working-notes.md        # Live scratchpad — open questions, contradictions
└── sources/
    ├── citations.md         # Bibliography, numbered footnote style
    ├── pdfs/                # Court orders, official filings, downloaded PDFs
    ├── articles/            # Saved markdown of cited web articles
    ├── osint/               # Raw Sherlock output (only if OSINT tooling used)
    └── archive-links.md     # archive.org snapshots for every web source
```

Templates for the five output files are in `assets/templates/`. Read them at the start of Phase 4 — don't reinvent the structure.

## Workflow — four phases

The phases are sequential. Don't start writing prose in Phase 4 before the citations file is robust enough to support it; don't start gathering specific sources in Phase 3 before you know which topics need them.

### Phase 1 — Discovery

Goal: map the territory and classify the subject. No prose drafting yet.

1. Run 5–10 broad web searches: full name + role, full name + biography, full name + recent news, full name + controversies. Cast wide.
2. Identify the subject type — politician, executive, academic, athlete, artist, religious figure, activist, historical figure, scientist, journalist, tech founder, or "other / mixed". Then read the corresponding section in `references/subject-types.md`. That file lists Tier-1 sources and the topic checklist for the type.
3. Locate primary sources: official records, governing-body filings, court documents, institutional pages, peer-reviewed publications.
4. Populate `sources/citations.md` with every source you find — even ones you may not end up citing. Use the format in `references/citation-format.md`.
5. Sketch a topic outline in `_working-notes.md` based on the subject-type checklist, plus any subject-specific themes that emerge from initial searches.
6. *Optional — digital footprint:* if the subject's online presence matters and OSINT tooling is available, run Sherlock on candidate handles to surface social accounts. Every hit is a lead, not a fact — verify each account by hand before recording it, and treat verified accounts as Tier 4. See `references/osint-tools.md` for installation, usage, and verification discipline. Skip this step entirely for subjects whose footprint is well documented by Tier 1/2 sources already.

Proceed to Phase 2 once `citations.md` has at least 25 entries spanning Tier 1 and Tier 2. If you cannot reach 25 quality sources, the subject likely has insufficient public footprint — check with the user before continuing.

### Phase 2 — Deep dive

Work through the subject-type's topic checklist (in `references/subject-types.md`). For each topic:

1. Targeted web searches and `web_fetch` on the most relevant results.
2. Note findings in `_working-notes.md` with source numbers attached.
3. Add new sources to `citations.md` as you find them.

Throughout: distinguish allegations from charges, charges from convictions, and convictions from upheld convictions. Use those exact words. Where reputed outlets disagree on a fact, log both versions in working notes — don't adjudicate yet.

### Phase 3 — Source acquisition

For every source you intend to cite, save it locally:

- Articles: `web_fetch` and save to `sources/articles/YYYY-MM-DD_outlet-slug_short-headline.md`.
- PDFs: download to `sources/pdfs/` with the same naming pattern.
- Archive every web URL: record an `https://web.archive.org/web/*/<url>` lookup in `sources/archive-links.md`. Note explicitly when no snapshot exists.
- If `web_fetch` returns empty, truncated, or blocked content for a source you intend to cite (JavaScript-rendered pages, infinite-scroll archives, multi-step navigation), retry once with browser-use before giving up. See `references/osint-tools.md`. Never use it to bypass paywalls, logins, or CAPTCHAs — gated content stays out of reach.
- If retrieval fails, log the failure and reason in `_working-notes.md`. Don't silently drop the source.

See `references/citation-format.md` for full naming conventions, archive workflow, and bibliography format.

### Phase 4 — Synthesis

Read the templates in `assets/templates/` first. Then write in this order:

1. `02-detailed-research.md` — source of truth. Every claim cited with a footnote.
2. `03-timeline.md` and `04-career-history.md` — derivative tables. Must be consistent with 02.
3. `00-summary.md` — distilled from 02. Make no claim that 02 doesn't support.
4. `01-index.md` — anchor links resolve to sections in 02.

Before writing prose for any section of 02, list its claims as bullets with citations attached, then expand into prose. This catches single-source claims and unsupported assertions before they get buried in flowing text.

## Source tier system

Tiers define source weight. The Tier-1 list is subject-type-dependent — see `references/subject-types.md`. Cross-type defaults below.

- **Tier 1** — Primary sources: official records, court documents, governing-body filings, institutional records, peer-reviewed publications.
- **Tier 2** — Established outlets of record. International: BBC, Reuters, AP, AFP, FT, NYT, WSJ, Economist, Guardian. Indian context: The Hindu, Indian Express, Telegraph India, Frontline, Scroll, The Wire, The Print, Hindustan Times, Times of India. Equivalents per region.
- **Tier 3** — Reputed long-form opinion / analysis / academic blogs. Used to add context, not as sole support for factual claims.
- **Tier 4** — Wikipedia, party / company / personal websites, social media. Starting points only. Never the sole citation for a claim.

Rules:

- Every factual claim in `02-detailed-research.md` must have at least one Tier 1 or Tier 2 citation.
- Single-source claims carry a `[single-source]` tag inline.
- Tier 4 sources never appear as sole citation. They may be used to find Tier 1 / 2 sources.
- Where outlets disagree, present both versions with citations — do not adjudicate.

## Writing style

- Neutral, factual, encyclopedic. Not advocacy, not hagiography, not hit piece. The reader should not be able to guess your view of the subject from the prose.
- Active voice, concrete details over abstract characterisation.
- Drop editorialising adjectives ("controversial," "fiery," "veteran," "firebrand," "embattled," "polarising") — let cited facts carry the weight.
- Names: full name + role on first mention, surname thereafter.
- Dates: `19 December 2020` (DD Month YYYY).
- Regional conventions for the subject's primary context: Indian English for Indian subjects, etc. Currency in local denomination first (Rs. / crore / lakh for Indian context), with USD equivalent where useful.
- No AI-tells: avoid "delve," "tapestry," "in the realm of," "navigate the complexities," gratuitous three-item rhetorical lists, dramatic em-dashes for effect.

## Multilingual sources

When the subject's primary context uses non-English sources, treat them as first-class:

- Record the original outlet name and date in the original Romanisation.
- Provide a brief English translation note in the footnote — explain what the source says, don't just quote the headline.
- Don't skip a Tier-1 or Tier-2 source because it's non-English.
- Common non-English outlets to check by region: Bengali (Anandabazar Patrika, Bartaman, Ei Samay), Hindi (Dainik Jagran, Amar Ujala, Dainik Bhaskar), Tamil (Dinamani, Dinamalar), Marathi (Loksatta, Sakal), and equivalents in French, Spanish, Arabic, Mandarin, Japanese, etc.

## Process discipline

- Update `_working-notes.md` continuously: open questions, contradictions found, sources to chase.
- Refresh `citations.md` after every 5–10 sources gathered, not at the end.
- For any claim that cannot be verified to Tier 1/2 standard, either drop it or include with explicit `[unverified]` tag and one-line explanation in the footnote. Never let an unverified claim sit unflagged.

## Stop conditions

Pause and ask the user before:

- Exceeding 60 web_search/web_fetch calls — research can rabbit-hole; check the user wants more depth before going past this.
- Making characterological claims about motive, intent, or personality. Stick to documented actions and stated positions.
- Including unreported detail about ongoing legal proceedings.
- Researching a subject who appears to be a minor, or a private individual without clear public-interest grounds.

## Definition of done

Before declaring complete, verify:

- All five top-level `.md` files exist and are internally coherent.
- Every footnote in `02-detailed-research.md` resolves to an entry in `sources/citations.md`.
- `sources/pdfs/` and `sources/articles/` contain local copies of every retrievable cited source.
- `sources/archive-links.md` has an entry for every web URL.
- Index links in `01-index.md` resolve to anchors in `02`.
- Timeline and career-history tables are consistent with `02`.
- Summary in `00` makes no claim that `02` doesn't support.

## Reference files

Read on demand:

- `references/subject-types.md` — Per-type Tier-1 sources and topic checklists for ten subject categories. Read in Phase 1 after classifying the subject.
- `references/citation-format.md` — Detailed citation rules, file naming, archive workflow, and bibliography format. Read at the start of Phase 3.
- `references/osint-tools.md` — Sherlock (social-account enumeration) and browser-use (agentic source retrieval): installation, usage, and verification discipline. Read in Phase 1 before mapping the digital footprint, and in Phase 3 if a source resists `web_fetch`.
- `assets/templates/*.md` — Boilerplate for the five output files. Read at the start of Phase 4.

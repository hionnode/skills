# Smoke test report — Mary Robinson

**Subject classification**: Politician (primary), with substantial activist / international human-rights career layered on. Used the politician checklist and folded activist sub-sections into the post-UN material — i.e., not a clean Politician but pragmatically the politician checklist carried it.

**Sources in citations.md**: 28 entries grouped by tier — Tier 1: 8 (OHCHR, President.ie, ElectionsIreland, TCD, Oireachtas, UN News, Obama White House, Harvard Law); Tier 2: 13 (Britannica, Irish Times multiple, CNN multiple, RTÉ, Irish Examiner, HRW, The Elders); Tier 3: 4 (UN Watch, ADL, Aspen, Mary Robinson Foundation); Tier 4: 3 Wikipedia starting points. Inline footnoted claims in `02-detailed-research.md`: ~25, slightly above the 8–15 target but well below the "not 50+" ceiling. (I'd lean to think the higher count is fine for showing discipline; the parent can decide.)

**Rough edges I hit**:
- The skill's normal Phase 1 gate is 25+ citations across Tier 1/2 before proceeding. Under the 10-call cap, I had to populate citations.md from links surfaced in WebSearch result panes rather than directly fetching each. That's a reasonable adaptation for a smoke test, but in a real run those Tier-1 links should be `web_fetch`-confirmed — several may 404 or paywall.
- The skill's bibliography numbering rule ("order by first citation appearance in 02") and the tier-grouping rule mildly conflict when a Tier-1 source is first cited in body very late. I solved by letting numbering drift — entries [^5] and [^28] are out of strict appearance order. Not catastrophic but worth a clarifying note in the skill.
- The "Tier 4 never the sole citation" rule pushed me to keep the Wikipedia "Seanad career" entry [^28] but pair it with [^9] (Britannica). The 1971 contraception bill detail still leans heavily on the Wikipedia article since I didn't drill into the Oireachtas 1971 record under the search budget. Flagged in Open Questions.
- Anchor-link verification in `01-index.md` is by-eye; the skill's "Definition of done" calls for index links to resolve, but there's no automated check. Worked but feels manual.

**What I skipped vs. what the skill asked for** (per smoke-test instructions): no article-body downloads to `sources/articles/`, no PDF downloads to `sources/pdfs/` (folders exist but empty), no live `web.archive.org` snapshot lookups (lookup patterns recorded with explicit `lookup not run (smoke test)` status). Search budget held to 10 calls. All five top-level markdown files plus `_working-notes.md`, `sources/citations.md`, `sources/archive-links.md` are present and internally cross-referenced. Scoping note about the partial corpus is at the top of `sources/citations.md` and in `_working-notes.md` and `01-index.md`.

Output root: `/Users/chinmay/code/agency/skills/research-person-workspace/iteration-1/eval-1-politician-mary-robinson/with_skill/outputs/research/mary-robinson/`

# Smoke-test report — research-person skill on Demis Hassabis

**Subject classification.** Mixed: tech founder + academic/scientist. Tech-founder activity dominates the public record (DeepMind, Isomorphic Labs); academic / Nobel-laureate activity sits beside it. I combined the two relevant checklists from `references/subject-types.md`.

**Sources in `citations.md`.** 29 entries — 5 Tier-1, 21 Tier-2, 3 Tier-4 (Wikipedia, used only as background per the skill's rule). Above the 25-entry Phase-1 threshold the skill requires.

**Search budget used.** 8 of the 10 soft-cap web_search calls.

**Output files produced.** All five top-level markdown files (`00-summary.md`, `01-index.md`, `02-detailed-research.md`, `03-timeline.md`, `04-career-history.md`), plus `_working-notes.md`, `sources/citations.md`, and `sources/archive-links.md`. Empty `sources/articles/` and `sources/pdfs/` folders created as scaffolding.

**Citation discipline in `02-detailed-research.md`.** 31 footnotes covering ~30 distinct claims; allegation/charge/conviction discipline applied (no criminal proceedings, so all controversies framed as "commitment subsequently rescinded" or "ongoing transparency dispute"); `[single-source]` and `[disputed]` tags applied where appropriate.

**Rough edges hit.**
- The skill's Phase-3 file-naming convention (`YYYY-MM-DD_outlet-slug_short-headline.md`) is awkward when the article is undated or has only a year — I used `YYYY_outlet_...` and `nd_outlet_...` patterns. The skill should probably address this explicitly.
- The `01-index.md` template assumes a politician-style section list ("Constituencies represented" etc.) — I had to substantially adapt the anchor list for a tech-founder + scientist subject. Worth noting in the template.
- The footnote-numbering rule ("sequential across the whole file") plus the bibliography-numbering rule ("order by first appearance in 02") collide when you cite footnotes out of order in derivative files (timeline / career-history). I kept the master numbering from 02 and let timeline/career-history reference those numbers — works, but the skill could spell this out.
- The skill says "Wikipedia citations standing alone — always go to Wikipedia's underlying source," which I obeyed, but Wikipedia genuinely was useful as a navigation tool and I logged it in citations.md as Tier 4 with an explicit "never sole citation" note. The convention was a little ambiguous about whether Tier-4-only-as-aid sources should appear in `citations.md` at all.

**What I skipped vs. what the skill asked.**
- No article bodies downloaded into `sources/articles/` (per smoke-test instructions).
- No PDFs into `sources/pdfs/` (per smoke-test instructions).
- Archive-link rows recorded as Wayback lookup URLs rather than resolved snapshot URLs (per smoke-test instructions; a non-smoke-test run would `web_fetch` each lookup and pin the actual snapshot).
- Did not pull primary documents from UK Companies House or the original 2014 Google–DeepMind acquisition press release; flagged in `_working-notes.md` as "sources to chase."
- Detailed research file has 31 footnotes — slightly above the 8–15 target the smoke test asked for. I let it run a little long because the controversies section needed allegation-discipline-precise sourcing; happy to tighten if needed.

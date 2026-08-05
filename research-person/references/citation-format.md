# Citation format and source workflow

This file defines the exact citation conventions, file naming, archive procedure, and bibliography format used across the research deliverable. Read at the start of Phase 3.

## Footnote citations in the research file

Every factual claim in `02-detailed-research.md` carries an inline footnote. Format:

```
Suvendu Adhikari joined BJP on 19 December 2020 at a rally in Medinipur addressed by Amit Shah.[^1]
```

The footnote definition appears at the bottom of the same file:

```
[^1]: The Hindu (2020-12-19). "Suvendu Adhikari joins BJP at Amit Shah's rally in Medinipur."
      URL: https://thehindu.com/...
      Archive: https://web.archive.org/web/20201220.../...
      Local: sources/articles/2020-12-19_thehindu_suvendu-joins-bjp.md
      Tier: 2
      Accessed: 2026-05-09
```

Use sequential numbering across the whole file — don't restart per section.

## Inline tags

Append tags after the citation marker when applicable:

- `[single-source]` — claim rests on only one Tier 1/2 source.
- `[unverified]` — included but not verifiable to Tier 1/2 standard. Add a one-line explanation in the footnote.
- `[allegation]`, `[charged]`, `[convicted]`, `[acquitted]` — for legal matters; use the precise word that matches the actual legal status.
- `[disputed]` — reputed outlets disagree; both versions are presented in the footnote.

Example:

```
The minister allegedly received Rs. 5 crore in 2014.[^12] [allegation] [single-source]
```

## File naming

All retrieved sources go into `sources/` with this pattern:

```
YYYY-MM-DD_outlet-slug_short-headline-slug.<ext>
```

Examples:

- `2020-12-19_thehindu_suvendu-joins-bjp.md`
- `2024-03-15_eci_affidavit-loksabha.pdf`
- `2023-06-02_supreme-court_judgment-narada.pdf`

Outlet slugs (consistent across files):

- International: bbc, reuters, ap, afp, ft, nyt, wsj, economist, guardian
- Indian English: thehindu, indianexpress, timesofindia, hindustantimes, telegraphindia, scroll, thewire, theprint, frontline
- Non-English Indian: anandabazar, bartaman, eisamay, dainikjagran, dainikbhaskar, amarujala, dinamani, loksatta
- Government / institutional: eci, mca, sebi, sec, mha, cag, supreme-court, hc-<state-slug>, lok-sabha, rajya-sabha

Use lowercase ASCII for slugs. Strip diacritics from headlines.

## Bibliography in citations.md

`sources/citations.md` is the master bibliography. Every footnote in 02 has a matching entry. Format:

```
[1] The Hindu (2020-12-19). "Suvendu Adhikari joins BJP at Amit Shah's rally in Medinipur."
    URL: https://thehindu.com/...
    Archive: https://web.archive.org/web/20201220.../https://thehindu.com/...
    Local: sources/articles/2020-12-19_thehindu_suvendu-joins-bjp.md
    Tier: 2
    Accessed: 2026-05-09
    Notes: (optional — translation note for non-English sources, contextual flags)

[2] ...
```

Group entries by Tier in the file:

```
## Tier 1 sources

[1] ...
[2] ...

## Tier 2 sources

[3] ...
[4] ...
```

Within a tier, order by first citation appearance in `02-detailed-research.md`. This makes the numbering match the order claims first appear, which helps a reader cross-reference quickly.

## Archive workflow

For every web URL cited:

1. Construct the lookup URL: `https://web.archive.org/web/*/<original-url>`
2. `web_fetch` the lookup to find existing snapshots.
3. If snapshots exist, use the most recent one as the archive URL.
4. If no snapshot exists, attempt to trigger one via `https://web.archive.org/save/<original-url>`. If that succeeds, use the resulting snapshot URL.
5. If still no snapshot, record `(no archive snapshot available, attempted YYYY-MM-DD)` in `sources/archive-links.md` and in the footnote.

Track all archive operations in `sources/archive-links.md`:

```
| Source ID | Original URL | Archive URL | Status | Date |
|-----------|--------------|-------------|--------|------|
| 1 | https://thehindu.com/... | https://web.archive.org/web/.../... | ok | 2026-05-09 |
| 2 | https://example.com/... | — | no snapshot | 2026-05-09 |
```

PDFs from official sources don't need archiving — the local copy is the archive.

## Non-English sources

For sources not in English:

1. Record outlet name in original Romanisation (e.g., "Anandabazar Patrika," not "ABP" alone).
2. Provide a brief English translation note in the footnote. Format:

   ```
   [^15]: Anandabazar Patrika (2021-04-02). "ননদীগ্রামে রায় বদলালো..."
          [Bengali; English: "Nandigram verdict overturned..."]
          URL: ...
          Translation note: Article reports recount in Nandigram constituency;
            key claim cited is the recount margin.
          Tier: 2
   ```

3. Don't paraphrase from non-English sources into English without flagging — translation is interpretation, and the reader should know.

## What not to cite

- Personal social media posts unless the post itself is the subject of cited reporting.
- AI-generated summaries of unknown sources.
- Aggregator sites without verifying the underlying source — go to the original.
- Wikipedia citations standing alone — always go to Wikipedia's underlying source and cite that. Wikipedia can flag a source you might otherwise miss; it can't be the source itself.

## Quality check before finishing

For `citations.md`:

- Every entry has URL, Archive (or "no snapshot" note), Local, Tier, Accessed.
- Numbering matches first-citation order in 02.
- Tier groupings are accurate.
- Local file references resolve to actual files in `sources/articles/` or `sources/pdfs/`.

For `02-detailed-research.md`:

- Every footnote number resolves to a `citations.md` entry.
- No claim lacks a footnote.
- No single-source claims are missing the `[single-source]` tag.
- No legal-matter claim is missing the precise allegation / charge / conviction language.
- Every footnote that uses a non-English source has a translation note.

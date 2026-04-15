---
name: vedic-chart-reading
description: When the user provides a Vedic birth chart (as structured text, a screenshot, or an export from software like Jagannatha Hora / AstroSage / Parashara's Light) and wants a reading, predictions, life guidance, or "what does my chart say," produce a long, ceremonial, beautifully typeset PDF reading grounded in P.V.R. Narasimha Rao's three books (bundled in this skill). The reading covers a high-level life-area synthesis followed by a house-by-house breakdown, a Vimshottari dasha forecast, identified yogas, and a full remedies section. Every substantive claim is traceable to a specific page of the source books. Trigger this skill whenever the user mentions Vedic astrology, jyotish, a janma kundali, a rasi chart, a birth chart with planetary placements in Indian style, a D-9/navamsa, a dasha period, or asks for predictions/readings/life guidance from astrology — even if they don't explicitly say "Vedic" or "PDF." If in doubt, assume they want this skill.
---

# Vedic Chart Reading

A skill for producing **long, traceable, book-grounded Vedic astrology readings** as beautiful PDFs, from a user-supplied birth chart.

## What this skill is, and what it is not

**Is**: a reading engine. The user brings a chart (computed elsewhere — Jagannatha Hora, AstroSage, Parashara's Light, screenshot of a paper chart). You synthesize and deliver a polished PDF reading, every claim of which you can point to a book and page for.

**Is not**: an ephemeris or chart calculator. Do not attempt to compute planetary positions from a birth time — that's not what this skill does and the books are unambiguous about needing accurate software for calculation (Textbook preface, p.ix).

**Why this separation matters**: calculation errors compound silently and ruin readings. By refusing to compute, we keep the skill honest.

## The source corpus

Three books, all by **P.V.R. Narasimha Rao**, all in the Parashari tradition, all internally consistent:

| Filename | Short cite | Full title | What it is |
|---|---|---|---|
| `vedic_astro_textbook.pdf` | **Textbook** | *Vedic Astrology: An Integrated Approach* (2000) | 515-page reference textbook. Primary source for houses, yogas, dashas, interpretation methodology, and remedies. |
| `book1-for-CD.pdf` | **Lessons-I** | *Lessons on Vedic Astrology, Volume I* (Lessons 1–45) | 122-page pedagogical companion. Sequential lessons with example charts. Useful for grounding teaching-style explanations and for example-chart analogies. |
| `book2-for-CD.pdf` | **Lessons-II** | *Lessons on Vedic Astrology, Volume II* (Lessons 46–77) | 149-page continuation. Advanced techniques. |

These files live at the root of this skill and are opened with the Read tool (they are PDFs — use the `pages:` parameter to scope). **The Textbook is the spine of most readings.** The Lessons volumes are for supplementing with examples and teaching-style language.

The author's style is precise, unornamented, slightly engineer-flavored. The books' predictive content is organized by numbered yogas, bhava meanings, and dasha effects — structure that makes citation easy. Lean into that structure.

## Citation policy — the non-negotiable part

The user asked for traceability, so every substantive claim in the final PDF gets an inline citation. "Substantive" means: any statement about what a placement *means*, *predicts*, *implies*, or *requires as a remedy*. Generic framing sentences don't need citations. When in doubt, cite.

**Format**: bracket-inline, right after the claim. Use these exact shortcuts:

- `[Textbook Ch 7, p.67]` — chapter + internal book page
- `[Textbook §34.2, p.451]` — when you want to point at a subsection (preferred for remedies)
- `[Lessons-I L16, p.65]` — Lessons Volume I, Lesson 16, page 65
- `[Lessons-II L54, p.22]` — Lessons Volume II, Lesson 54, page 22

Internal book page numbers (the ones printed on the page) — not PDF page numbers. The Textbook's printed pages happen to start counting from the real Chapter 1 (internal p.3 = PDF p.16). When you open the book at runtime, note both numbers; cite only the printed one. A reader (or a skeptical friend of the native) should be able to open the PDF, jump to the printed page, and find the source line within a few paragraphs.

**Do not fabricate citations.** If a claim you're about to make isn't grounded in a page you can point to, either (a) drop the claim, or (b) go find the grounding. If a claim you want to make is *common to all Vedic astrology* and found in many places, cite the most canonical location in the Textbook — usually the chapter introducing that concept (see `references/source_map.md`).

**Do not paraphrase too thinly.** Paraphrase enough that the reading is in natural prose, but the claim behind the paraphrase must exist in the source. If you're stretching to extrapolate, call it out with hedged language ("Rao hints at this — see Textbook p.X — though he does not state it outright.").

## The workflow

Follow these steps in order. Each step says *why* it's there.

### Step 1 — Receive and validate the chart

The user gives you a chart. It may be:

1. **Structured text** — e.g., "Lagna: Virgo 12°, Sun in Leo (11th), Moon in Cancer (10th) …"
2. **An image** — a North Indian (diamond) or South Indian (fixed-sign) square chart, often with planet abbreviations (Ra, Ke, Ma, Ju, etc.).
3. **A software export** — PDF from Jagannatha Hora, Parashara's Light, AstroSage, etc. These contain the rasi chart plus often D-9, D-10 and dasha tables.

**Parse it into a structured digest** before doing any analysis. The digest must include:

- Lagna (ascendant) sign + degree
- Sign + house of each of the 9 grahas (Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, Rahu, Ketu)
- Retrogression flags if given
- Current Vimshottari Mahadasha lord and, if given, Antardasha lord, plus the date the current period ends
- D-9 (Navamsa) planet placements if given — the Navamsa is *critical* for marriage, Dharma, and overall strength; Rao emphasizes it as the "chart within the chart" (Textbook Ch 6).
- D-10 (Dasamsa) placements if given — primary divisional chart for career
- Any nakshatras, aspects, or yogas the user has already flagged

If the input is an image, extract what you can and **then restate the digest back to the user, asking them to confirm or correct** before you start writing the reading. This is critical: image OCR of Indian-style charts is lossy and mis-reading a planet's house cascades into every later claim. A 10-second confirmation from the user is much cheaper than regenerating a 30-page PDF.

If an image is low-resolution or ambiguous, say so and ask for a text chart.

If the input is a software PDF, use the pdf skill or the Read tool to extract planet positions.

**Minimum viable input**: lagna, nine planet positions by sign+house, and current Mahadasha lord. Without these the reading cannot be responsibly produced — refuse and ask the user for them.

### Step 2 — Orient yourself in the source material

Open `references/source_map.md` — this is the index that maps every type of claim (house meaning, yoga, dasha effect, remedy) to the specific chapter(s) and page(s) in the books where it's discussed. Keep it mentally loaded as you write.

Read `references/houses.md` for the 12-bhava briefing (karakas, significations, and which pages in the Textbook discuss each).

Read `references/life_areas.md` for the synthesis mapping — it tells you which houses/lords/karakas/divisional charts together form each life-area judgment.

Read `references/remedies.md` for the remedy routing — it's a digest of Textbook Chapter 34 with page pointers.

Read `references/dasha_analysis.md` for how Rao approaches dasha interpretation (house-based, sub-period chaining).

**These reference files are navigation indexes, not substitutes for the books.** For any specific claim, actually open the relevant book page and ground the claim in what Rao wrote there. The references get you to the right page quickly; they don't replace reading it.

### Step 3 — Plan the reading

Before writing prose, build a structured plan (as an internal note — you don't need to show the user). The plan should cover:

- **Chart digest** (what's rendered at the top of the PDF — the dry facts)
- **Overall tenor** — strong chart? mixed? afflicted? lagna lord strength, kendra/trikona occupation, major yogas present. One paragraph of orienting judgment, with citations.
- **Life-area synthesis** — for each high-level area, which houses/lords/planets you'll synthesize and what the dominant read is. Areas to cover:
  1. Self & Personality (1st house, lagna lord, Moon sign, Ascendant sign)
  2. Wealth & Finances (2nd, 11th, Jupiter, dhana yogas)
  3. Family & Emotional Foundation (4th, Moon, mother; 2nd for extended family)
  4. Education & Intellect (4th, 5th, Mercury, Jupiter)
  5. Career & Professional Life (10th, 10th lord, Sun, Saturn, D-10)
  6. Marriage & Relationships (7th, Venus for men / Jupiter for women, D-9, upapada)
  7. Children (5th, Jupiter, D-7 if available, D-3)
  8. Health & Vitality (1st, 6th, 8th, Sun-Moon axis)
  9. Spiritual Life & Inner Growth (9th, 12th, Ketu, Jupiter, D-20 if available)
  10. Longevity & Later Life (8th, Saturn, Ayur calculations — Textbook Ch 14)
- **House-by-house section** — 1 through 12. For each: lord placement, occupants, key aspects, notable yogas involving this house, dasha relevance, concrete predictions.
- **Active yogas identified** — name and predict each; cite the Textbook Ch 11 yoga definition.
- **Dasha forecast** — current Mahadasha, current Antardasha, and the next 2-3 Antardashas. What the lord of each period signifies in *this chart* (not generic).
- **Remedies** — curated, not exhaustive. Pick remedies that target this chart's weaknesses. Full coverage across: gemstone(s), mantras, deity worship, good deeds / charity, dietary & fasting guidance. Cite Textbook Ch 34 sections.
- **Closing** — a measured, non-fatalistic note. Rao himself is firm that karma sets the pattern but free will shapes the details (Textbook §34.1, p.450). Echo that tone.

**Why this structure**: the books do not themselves produce synthesized life-area readings — they explain technique. The skill's value-add is *synthesizing* that technique into a coherent reading for one specific chart. The house-by-house section grounds the synthesis in primary technical material; the life-area synthesis is the derived product. Both are necessary. Skipping the house-by-house section makes the reading ungroundable; skipping the synthesis makes it dry and useless to the native.

### Step 4 — Write the reading

Prose conventions:

- **Address the native in the second person**: "You have Venus in the 7th house…" Not "The native has…" Exception: the opening page may use third-person honorific framing if the user supplied a name.
- **Sanskrit terms**: use them, but translate on first use. "Lagna (ascendant)", "Navamsa (the ninth divisional chart, D-9)", "Dhana yoga (a combination for wealth)." Italicize Sanskrit on first appearance.
- **Don't moralize or frighten**. Rao's own voice is rational and clinical. Match it. When discussing difficult placements (8th-house transits, Saturn dashas), be factual about challenges and constructive about remedies. Never predict death, divorce, or disease with finality — the books don't, and neither should you.
- **Hedge calibrated predictions appropriately**. Dasha-period timings are approximate; transit effects are zones not points; yoga activations depend on dasha context. Use language like "during this period you are likely to experience…", "this yoga becomes active when…"
- **Remedies are suggestions, not prescriptions**. Introduce the remedies section with language like "the books suggest the following remedial measures; consider them in consultation with a priest or experienced jyotishi."
- **No length limit.** If a chart is rich with yogas and the current dasha period is significant, the reading may run 40+ pages. That's fine. But don't pad.

### Step 5 — Render the PDF

Use the bundled script:

```bash
python scripts/render_pdf.py <reading.json> <output.pdf>
```

The script takes a structured JSON of the reading (schema documented in `scripts/render_pdf.py` header) and renders it with WeasyPrint into a PDF using `assets/template.html` and `assets/styles.css`.

**Do not write your own HTML or try to invoke WeasyPrint directly.** Use the script — it enforces consistent typography, handles Sanskrit script, and formats the Sources appendix correctly.

If WeasyPrint is not installed on the user's machine, the script will print an installation hint (`pip install weasyprint`). Tell the user. Alternatively, if the user would prefer, the skill can fall back to a Markdown output with the same structure — offer this if PDF rendering fails for environment reasons.

### Step 6 — Deliver and explain

Show the user the resulting PDF path. Offer to:

- Expand any section they want longer (e.g., "I want a deeper read on the 7th house" → regenerate with an expanded marriage section)
- Generate a second PDF focused on a specific life area
- Produce a companion "remedies-only" PDF (useful for sharing with a priest)

## Divisional charts — when and how to use them

Rao treats divisional charts as essential, not optional. Guidelines:

- **D-9 Navamsa**: always consult if provided. It refines marriage (7th-house analysis is incomplete without it), shows overall Dharma and strength of promises in the rasi, and is the primary chart for spirituality. Textbook Ch 6, pp.51–66.
- **D-10 Dasamsa**: always consult if provided for career/10th-house analysis. Without D-10, career predictions are coarser. Textbook Ch 6.
- **D-7 Saptamsa**: use if provided for children (5th-house analysis).
- **D-3 Drekkana**: siblings and courage (3rd-house).
- **Other vargas** (D-12 parents, D-16 vehicles/comforts, D-20 spirituality, D-24 education, D-30 misfortunes, D-60 overall): only consult if the user provides them and the life area is directly addressed.

If the user provided only the rasi chart, state this as a limitation at the top of the reading: "This reading is based on your rasi chart alone. Divisional charts (D-9, D-10, etc.) would refine specific areas — if you can provide them, I can produce a more granular reading of marriage and career."

## Handling sensitive prediction topics

Some life areas are emotionally loaded. Handle them with care:

- **Marriage timing and partner quality**: the books do discuss these (7th house, D-9, upapada). Report what the chart shows, but hedge — "Rao notes such combinations often correlate with X; this does not foreclose other outcomes." Never predict divorce with finality.
- **Health and disease**: the 6th house relates to disease, the 8th to chronic conditions and surgery (Textbook Ch 7). Discuss tendencies and recommended vigilance periods via dasha, not definite illness. Always encourage medical consultation — the books themselves are clear that astrology complements, not replaces, medicine (Textbook §34.1.1, p.450).
- **Death / longevity**: Textbook Ch 14 discusses longevity analysis (Balarishta, Shoola, Ayur). *Do not predict death timing or duration of life in the reading.* You may note general longevity-range indicators (short/medium/full life span) with appropriate hedging, and only if the user explicitly asks. Otherwise omit.
- **Children — especially absence of children**: the 5th house, Jupiter, and D-7 can indicate delays or denial. If the chart shows such indications, report them with maximum compassion, cite remedies (Jupiter propitiation, deity worship, specific fasts), and encourage the native not to treat the reading as destiny.

**Why this caution matters**: a bad prediction delivered with confidence can do real harm. Rao himself warns that even correct knowledge "fed to unworthy students" is a mistake (Textbook Preface, p.xi). Better to hedge and be useful than to be dramatic and wrong.

## A note on the books' limits

The Textbook is explicitly an introductory reference. Rao himself writes at the end of Chapter 34 (§34.6, p.459): *"no topic has been covered exhaustively… Readers should refer to other textbooks for more details."* If a user asks a question that requires depth the source material does not cover (e.g., advanced KP techniques, intricate prashna, detailed muhurta for a specific event), say so — don't manufacture citations from thin material. Recommend they consult a human jyotishi for that depth.

---

## Quick orientation for repeat readings

If you find yourself reading the same chart twice (e.g., the user asks a follow-up), don't re-parse from scratch — ask for the previous reading's digest or regenerate the structured JSON and start from there.

## Files in this skill

```
SKILL.md                                 (this file)
vedic_astro_textbook.pdf                 (Rao, 2000 — Textbook)
book1-for-CD.pdf                         (Rao — Lessons Vol I)
book2-for-CD.pdf                         (Rao — Lessons Vol II)
references/
  source_map.md                          (topic → book/chapter/page index)
  houses.md                              (12 bhavas with page refs)
  life_areas.md                          (life area → houses/planets/divs mapping)
  remedies.md                            (Textbook Ch 34 distilled)
  dasha_analysis.md                      (Vimshottari interpretation method)
scripts/
  render_pdf.py                          (JSON → PDF via WeasyPrint)
assets/
  template.html                          (Jinja2 template for the reading)
  styles.css                             (typography & layout)
evals/
  evals.json                             (test prompts for iteration)
```

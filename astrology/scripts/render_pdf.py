#!/usr/bin/env python3
"""
Render a Vedic astrology reading from a structured JSON file to a PDF.

Usage:
    python scripts/render_pdf.py <reading.json> <output.pdf>

The reading JSON schema is documented below.

Dependencies:
    pip install weasyprint jinja2 markdown

If weasyprint is not installed, the script prints an installation hint and
exits with a non-zero status.

================================================================================
READING JSON SCHEMA
================================================================================

{
  "native": {
    "name":         "Arjun Menon",
    "birth_date":   "1989-07-14",          # ISO or human
    "birth_time":   "06:42 IST",           # optional
    "birth_place":  "Kochi, Kerala, India",# optional
    "coordinates":  "9°56'N, 76°16'E"      # optional
  },

  "generated_on": "2026-04-15",

  "chart_digest": {
    "ascendant": "Virgo 12°",
    "planets": [
      { "name": "Sun",      "sign": "Cancer",    "degree": "28°",
        "house": 11, "nakshatra": "Ashlesha",
        "retrograde": false, "extra": "AK"     },
      ...
    ],
    "current_dasha": "Jupiter Mahadasha (2015–2031), Saturn Antardasha (Jun 2024 – Jan 2027)",
    "divisional_charts_provided": ["D-9", "D-10"],
    "notes": "This reading uses the rasi chart and the two divisional charts above. D-7 (children) and D-20 (spirituality) were not supplied and so those areas are discussed only at the rasi level."
  },

  "sections": [
    # any number of section objects, in the order they should appear
    # each has a "kind" — see SECTION KINDS below.
  ],

  "sources": [
    { "short": "Textbook",   "full": "P.V.R. Narasimha Rao, Vedic Astrology: An Integrated Approach (2000)." },
    { "short": "Lessons-I",  "full": "P.V.R. Narasimha Rao, Lessons on Vedic Astrology, Volume I (Lessons 1–45), comp. Sri Jagannath Center-Boston." },
    { "short": "Lessons-II", "full": "P.V.R. Narasimha Rao, Lessons on Vedic Astrology, Volume II (Lessons 46–77), comp. Sri Jagannath Center-Boston, 2007." }
  ]
}

================================================================================
SECTION KINDS
================================================================================

{ "kind": "prose",
  "title": "Overall Tenor",
  "subtitle": "A mixed chart with powerful Raja yogas activating in midlife",
  "body": "... markdown text with inline [Textbook Ch 7, p.67] citations ..." }

{ "kind": "life_areas_intro",
  "body": "... optional prose framing this part ..." }

{ "kind": "life_area",
  "title": "Career & Professional Life",
  "verdict": "Strong — late-career peak likely",
  "body": "... markdown ...",
  "current_period_note": "... markdown ...",    # optional
  "remedies": ["Wear emerald ...", "Recite Mercury mantra ..."]   # optional
}

{ "kind": "houses_intro",
  "body": "..." }

{ "kind": "house",
  "house_number": 1,
  "title": "Tanu Bhava — Self",
  "metadata": { "Lord": "Mercury in 3rd (Scorpio)",
                "Occupants": "Sun, Mars",
                "Aspects": "Jupiter's 9th aspect" },
  "body": "... markdown ..." }

{ "kind": "yogas_intro",
  "body": "..." }

{ "kind": "yoga",
  "name": "Gajakesari Yoga",
  "description": "Jupiter in a kendra from the Moon",
  "body": "... markdown ..." }

{ "kind": "dasha_forecast",
  "mahadasha_title": "Jupiter (2015–2031)",
  "mahadasha_html": "... markdown ...",       # the renderer accepts either
  "antardasha_title": "Saturn (Jun 2024 – Jan 2027)",
  "antardasha_html": "... markdown ...",
  "upcoming": [
    { "title": "Mercury Antardasha (Jan 2027 – Apr 2029)", "body": "... markdown ..." },
    ...
  ]
}

{ "kind": "remedies",
  "opening":        "... markdown ...",
  "gemstones":      ["Wear ...", "..."],
  "mantras":        ["*Om Aim Klim Brihaspataye Namah* ...", "..."],
  "deities":        ["Propitiate Vishnu ...", "..."],
  "good_deeds":     ["Donate chick peas on Thursday mornings ...", "..."],
  "common_sense":   ["Drive carefully during ...", "..."],
  "closing":        "... markdown ..."
}

{ "kind": "closing",
  "title": "A Closing Note",
  "body": "... markdown ..." }
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError:
    print("error: jinja2 is not installed. Install with: pip install jinja2", file=sys.stderr)
    sys.exit(2)

try:
    import markdown as md
except ImportError:
    print("error: markdown is not installed. Install with: pip install markdown", file=sys.stderr)
    sys.exit(2)


CITATION_RE = re.compile(
    r"\[(?:Textbook|Lessons-I|Lessons-II)[^\]]*\]"
)


def wrap_citations(text: str) -> str:
    """Wrap inline [Textbook ...] style citations in <span class="cite">..</span>."""
    return CITATION_RE.sub(lambda m: f'<span class="cite">{m.group(0)}</span>', text)


def render_markdown(text: str | None) -> str:
    """Render markdown to HTML and style the citations."""
    if not text:
        return ""
    # Render markdown first, then wrap citations (they're plain brackets that survive markdown).
    html = md.markdown(text, extensions=["extra", "sane_lists"])
    return wrap_citations(html)


def render_inline_markdown(text: str | None) -> str:
    """Render inline markdown (for list items, source strings). Strips the wrapping <p>."""
    if not text:
        return ""
    html = md.markdown(text, extensions=["extra"]).strip()
    # Strip a single wrapping <p>...</p> if that's all we got — inline items shouldn't be block-wrapped.
    if html.startswith("<p>") and html.endswith("</p>") and html.count("<p>") == 1:
        html = html[3:-4]
    return wrap_citations(html)


def precompute_bodies(sections: list[dict]) -> list[dict]:
    """
    For each section, materialize a `*_html` field for every markdown field.
    Keeps the template simple and keeps all rendering in one place.
    """
    out = []
    for s in sections:
        s = dict(s)  # shallow copy
        kind = s.get("kind")

        # Most sections have a "body" markdown field.
        if "body" in s:
            s["body_html"] = render_markdown(s["body"])

        if kind == "life_area":
            if "current_period_note" in s:
                s["current_period_note_html"] = render_markdown(s["current_period_note"])

        if kind == "dasha_forecast":
            if "mahadasha" in s and "mahadasha_html" not in s:
                s["mahadasha_html"] = render_markdown(s["mahadasha"])
            if "antardasha" in s and "antardasha_html" not in s:
                s["antardasha_html"] = render_markdown(s["antardasha"])
            if "mahadasha_html" in s and not isinstance(s["mahadasha_html"], str):
                s["mahadasha_html"] = ""
            # already-rendered HTML passthrough is fine; if it's markdown, convert:
            if isinstance(s.get("mahadasha_html"), str) and "<" not in s["mahadasha_html"][:40]:
                s["mahadasha_html"] = render_markdown(s["mahadasha_html"])
            if isinstance(s.get("antardasha_html"), str) and "<" not in s["antardasha_html"][:40]:
                s["antardasha_html"] = render_markdown(s["antardasha_html"])

            new_upcoming = []
            for u in s.get("upcoming", []) or []:
                u = dict(u)
                if "body" in u:
                    u["body_html"] = render_markdown(u["body"])
                new_upcoming.append(u)
            s["upcoming"] = new_upcoming

        if kind == "remedies":
            if "opening" in s:
                s["opening_html"] = render_markdown(s["opening"])
            if "closing" in s:
                s["closing_html"] = render_markdown(s["closing"])
            # Remedy bullet items can contain inline markdown (bold, italic) and citations.
            for field in ("gemstones", "mantras", "deities", "good_deeds", "common_sense"):
                if field in s and isinstance(s[field], list):
                    s[field] = [render_inline_markdown(item) for item in s[field]]

        if kind == "life_area":
            # Per-area remedies bullets also support inline markdown.
            if "remedies" in s and isinstance(s["remedies"], list):
                s["remedies"] = [render_inline_markdown(item) for item in s["remedies"]]

        out.append(s)
    return out


def render(reading_path: Path, output_path: Path, skill_root: Path) -> None:
    with reading_path.open("r", encoding="utf-8") as f:
        reading = json.load(f)

    reading["sections"] = precompute_bodies(reading.get("sections", []))

    # Sources: render inline markdown in each source's "full" field, and expose as `full_html`.
    rendered_sources = []
    for src in reading.get("sources", []):
        src = dict(src)
        if "full" in src:
            src["full_html"] = render_inline_markdown(src["full"])
        rendered_sources.append(src)
    reading["sources"] = rendered_sources

    env = Environment(
        loader=FileSystemLoader(str(skill_root / "assets")),
        autoescape=select_autoescape(enabled_extensions=("html",)),
    )
    template = env.get_template("template.html")
    html = template.render(**reading)

    # Import weasyprint late — the script should be able to at least validate/render
    # HTML even if weasyprint isn't available.
    try:
        from weasyprint import HTML  # noqa: WPS433
    except ImportError:
        print(
            "error: weasyprint is not installed.\n"
            "install with: pip install weasyprint\n"
            "on macOS you may also need: brew install pango cairo gdk-pixbuf libffi",
            file=sys.stderr,
        )
        # Save the intermediate HTML next to the output path so the user can inspect.
        html_fallback = output_path.with_suffix(".html")
        html_fallback.write_text(html, encoding="utf-8")
        print(f"wrote html-only fallback to: {html_fallback}", file=sys.stderr)
        sys.exit(3)

    HTML(string=html, base_url=str(skill_root / "assets")).write_pdf(str(output_path))
    print(f"wrote: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Vedic reading JSON to PDF.")
    parser.add_argument("reading_json", type=Path, help="path to the reading JSON")
    parser.add_argument("output_pdf", type=Path, help="path to write the PDF")
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    render(args.reading_json, args.output_pdf, skill_root)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render reading.md into a beautiful PDF via weasyprint."""
import os
import re
import markdown
from weasyprint import HTML, CSS

HERE = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(HERE, "reading.md")
HTML_PATH = os.path.join(HERE, "reading.html")
PDF_PATH = os.path.join(HERE, "reading.pdf")

with open(MD_PATH, "r", encoding="utf-8") as f:
    md_text = f.read()

body_html = markdown.markdown(
    md_text,
    extensions=["extra", "sane_lists", "toc", "smarty"],
)

# Wrap into a nicely styled standalone HTML doc
doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>A Vedic Astrological Reading for Priya Iyengar</title>
<style>
  @page {{
    size: A4;
    margin: 22mm 20mm 22mm 20mm;
    @bottom-center {{
      content: counter(page) " of " counter(pages);
      font-family: 'EB Garamond', 'Georgia', serif;
      font-size: 9pt;
      color: #6b5a3a;
    }}
    @top-right {{
      content: "Priya Iyengar · Jyotisha";
      font-family: 'EB Garamond', 'Georgia', serif;
      font-size: 9pt;
      font-style: italic;
      color: #6b5a3a;
    }}
  }}
  @page :first {{
    @top-right {{ content: ""; }}
    @bottom-center {{ content: ""; }}
  }}

  html, body {{
    font-family: 'EB Garamond', 'Palatino Linotype', 'Palatino', 'Georgia', serif;
    color: #221a10;
    background: #fbf7ef;
    font-size: 11.5pt;
    line-height: 1.55;
  }}

  h1 {{
    font-family: 'Cinzel', 'Trajan Pro', 'Palatino Linotype', serif;
    font-size: 26pt;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-align: center;
    color: #5a3a1a;
    border-bottom: 2px double #a07a3a;
    padding-bottom: 10px;
    margin-top: 0.2em;
    margin-bottom: 0.8em;
  }}
  h2 {{
    font-family: 'Cinzel', 'Palatino Linotype', serif;
    font-size: 16pt;
    color: #6b3a0a;
    border-bottom: 1px solid #c9a768;
    padding-bottom: 4px;
    margin-top: 1.8em;
    margin-bottom: 0.6em;
    page-break-after: avoid;
  }}
  h3 {{
    font-family: 'Cinzel', 'Palatino Linotype', serif;
    font-size: 13pt;
    color: #7a4a15;
    margin-top: 1.2em;
    margin-bottom: 0.3em;
    page-break-after: avoid;
  }}
  h4 {{
    font-size: 12pt;
    color: #6b3a0a;
    font-style: italic;
    margin-top: 1em;
    margin-bottom: 0.25em;
  }}
  p {{
    margin: 0 0 0.7em 0;
    text-align: justify;
    hyphens: auto;
  }}
  ul, ol {{
    margin: 0.4em 0 0.9em 1.4em;
  }}
  li {{
    margin-bottom: 0.3em;
  }}
  strong {{ color: #3b1f02; }}
  em {{ color: #4a2a08; }}
  hr {{
    border: none;
    border-top: 1px solid #c9a768;
    margin: 1.5em 0;
  }}
  blockquote {{
    border-left: 3px solid #c9a768;
    background: #f5ecd6;
    margin: 0.8em 0;
    padding: 0.4em 1em;
    font-style: italic;
  }}
  code {{
    font-family: 'Menlo', 'Consolas', monospace;
    background: #f1e7cb;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 10.5pt;
  }}

  /* Cover-style first section */
  .cover {{
    text-align: center;
    margin-top: 20mm;
    margin-bottom: 30mm;
    page-break-after: always;
  }}
  .cover .title {{
    font-family: 'Cinzel', 'Trajan Pro', serif;
    font-size: 32pt;
    color: #5a3a1a;
    letter-spacing: 2px;
    margin-bottom: 0.4em;
  }}
  .cover .subtitle {{
    font-family: 'EB Garamond', serif;
    font-size: 14pt;
    font-style: italic;
    color: #6b3a0a;
    margin-bottom: 3em;
  }}
  .cover .glyph {{
    font-size: 40pt;
    color: #a07a3a;
    margin-bottom: 1.6em;
  }}
  .cover .meta {{
    font-size: 12pt;
    color: #3b2a10;
    line-height: 1.8;
  }}
  .cover .meta strong {{ color: #5a3a1a; }}

  .ornament {{
    text-align: center;
    font-size: 16pt;
    color: #a07a3a;
    margin: 1em 0;
    letter-spacing: 8px;
  }}
</style>
</head>
<body>

<section class="cover">
  <div class="glyph">&#x0950;</div>
  <div class="title">Vedic Astrological Reading</div>
  <div class="subtitle">A jyotisha portrait &amp; dasha forecast</div>
  <div class="ornament">&#x2767; &#x2042; &#x2767;</div>
  <div class="meta">
    <p><strong>For:</strong> Priya Iyengar</p>
    <p><strong>Born:</strong> 12 March 1992, 04:18 AM IST<br/>Bangalore, India (12°58' N, 77°35' E)</p>
    <p><strong>Lagna:</strong> Capricorn (Makara), 7°23' &mdash; Shravana</p>
    <p><strong>Current period:</strong> Rahu Mahadasha &middot; Saturn Antardasha</p>
    <p style="margin-top:2em;"><em>Prepared 15 April 2026</em></p>
  </div>
</section>

{body_html}

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(doc)

HTML(string=doc, base_url=HERE).write_pdf(PDF_PATH)
print(f"Wrote {PDF_PATH}")

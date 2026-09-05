---
name: yt-corpus
description: Fetch, clean, catalogue and publish YouTube transcripts into Obsidian vault notes and a chunked JSONL retrieval corpus. Use when asked to get a transcript from a YouTube video, playlist or channel, to ingest a talk or lecture series into the vault, to make video content searchable or RAG-ready, or when a YouTube URL is shared with intent to read, study, quote-locate or index what was said in it. Also use when auto-caption output looks duplicated, unpunctuated, or has mangled technical terms.
---

# yt-corpus

Tooling lives at `~/code/agency/yt-corpus`. Stdlib Python driving `yt-dlp`.
Read that repo's `README.md` for the reasoning; this file is the operating procedure.

## The pipeline

```bash
cd ~/code/agency/yt-corpus
python3 tools/fetch.py     --source <id> --probe   # enumerate, write nothing
python3 tools/fetch.py     --source <id>           # captions -> cache/
python3 tools/clean.py     --source <id> --stats   # -> corpus/
python3 tools/suspects.py  --source <id>           # find ASR manglings
python3 tools/notes.py     --source <id>           # -> vault notes
python3 tools/chunk.py     --source <id>           # -> chunks.jsonl
python3 tools/catalogue.py                         # -> CATALOGUE.md
```

Always `--probe` first and show the user the enumeration before downloading.

For a one-off with no catalogue entry:
`python3 tools/fetch.py --url <url> --id <slug>`, then the same stages with
`--source <slug>` — the downstream stages resolve ad-hoc sources from the ledger.

## Adding a new source

Append an entry to `sources.json` (`id`, `title`, `url`, `channel`, `kind`,
`topic`, `vault_out`, `corrections`). `vault_out` is relative to
`~/code/social-vault` — point it at an existing topic folder when the material
belongs to one, otherwise `video-notes/<id>`.

## The one workflow step people skip

After the **first** `clean.py` on a new source, run `suspects.py`. Auto-captions
mangle every product name the recogniser has not heard: in the LangChain RAG
playlist, ColBERT arrived as "cold bear" and "co bear", LangChain as "l chain",
LLM as "lm". `suspects.py` prints the n-gram shapes that betray these — a short
token that is not ordinary English. Triage them into `corrections/<name>.json`,
then re-run `clean.py` → `notes.py` → `chunk.py`. Skipping this ships a
transcript where the subject's own name is wrong.

## Hard rules

- **`json3`, never `vtt`/`srt`.** VTT repeats each caption line as the rolling
  window advances — 2.98× the word count on a measured sample. If you are
  writing dedupe logic for repeated lines, you fetched the wrong format.
- **A transcript here is not a source.** ASR output plus heuristic casing.
  Never footnote it in a research note; find where something was said, watch
  the video, cite that. Same rule the vault applies to `claude-chats/`.
- **Never publish it.** Local personal archive of someone else's video — not
  into a site, an artifact, or anything shared.
- **Never hand-edit generated notes.** Re-running regenerates the block between
  the `ytc:transcript` markers. Write in the `## Notes` section between the
  `ytc:notes` markers — that is read back and preserved verbatim.
- **Record failures, never drop them.** An unavailable video appears in the
  ledger, the catalogue and the index note's Gaps table with a reason.

## Ingested so far

`rag-from-scratch` — LangChain's *RAG From Scratch*, 14 of 15 entries
(index 11 is hidden), ~14.8k words, 135 chunks →
`social-vault/video-notes/rag-from-scratch/`.

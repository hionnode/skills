# Spaced Repetition — Practical Reference

A deeper look at how spacing works, what intervals to use, and how "encompassings" compress the review queue. Use this when a user asks specifically about review scheduling, SRS tools, or why they're forgetting things.

## The core finding

Hermann Ebbinghaus (1885) showed that memory decays rapidly after learning — the "forgetting curve." But if you review just before decay becomes severe, memory is not only restored but *consolidated further*, pushing the next forgetting curve out further. Stack enough spaced reviews and the interval between reviews eventually grows to years (Bahrick et al., 1993).

This is one of the largest and most robust findings in learning research (Rohrer, 2009). It has 255+ replications across a century. It is still rarely used in classrooms.

## The core trade-off

If you review *too early*, memory is still strong — the review doesn't do much work and you're wasting effort.

If you review *too late*, memory is gone — the review feels like re-learning from scratch and you don't move forward in the schedule.

The sweet spot is reviewing *just before you would have forgotten*. This maximizes the desirable difficulty.

## Expanding intervals — a sensible default

A workable starting schedule for a new topic:

| Repetition | Lag since previous | Cumulative time since first learn |
|---|---|---|
| 1 (initial learn) | — | day 0 |
| 2 | ~1 day | day 1 |
| 3 | ~3 days | day 4 |
| 4 | ~1 week | day 11 |
| 5 | ~2 weeks | ~day 25 |
| 6 | ~1 month | ~day 55 |
| 7 | ~2 months | ~day 115 |
| 8 | ~4 months | ~day 235 |
| 9 | ~8 months | ~day 475 |
| 10 | ~16 months | ~day 955 |

**Adjust dynamically:**
- If a review is easy and fluent → extend the next interval more (multiply by ~2.5 instead of ~2).
- If a review is slow or mistake-ridden → shorten the next interval (back up one step).
- If a review fails outright → re-queue as if the topic were newly learned.

This is roughly the behavior of Anki's SM-2 algorithm and similar tools. You don't have to implement it yourself — use an SRS.

## Tool recommendations for self-learners

- **Anki** — the canonical flashcard SRS. Powerful, free, open-source. Ugly UI, steep learning curve, but the algorithm is solid. Best for bite-size facts, vocabulary, formulas, definitions, language grammar.
- **Mochi** — prettier, simpler Anki alternative. Same core model.
- **RemNote** — integrates notes + SRS in the same app. Good if you want your flashcards to emerge from notes.
- **Orbit** (Andy Matuschak) — embeds spaced reviews directly into articles/essays. Niche but interesting for writers.
- **Math Academy** itself, for math.

**What NOT to use SRS for.** Big, complex skills that require holistic practice (e.g., writing an essay, soldering, playing a piece of music end-to-end). Those need scheduled practice, not flashcards. Use SRS for atomic factual and procedural components; use calendar-scheduled practice for the holistic skill.

## Encompassings — the compression trick

Math Academy's deepest scheduling optimization: many advanced tasks *implicitly* exercise simpler ones. If the learner is due for reviews on 10 topics but one advanced problem encompasses all 10, the learner only has to do that one problem. The simpler topics are credited review by transitive practice.

**Examples of encompassings:**
- Long multiplication encompasses single-digit multiplication and addition with carrying.
- Solving a quadratic by factoring encompasses factoring integers, recognizing binomials, and basic arithmetic.
- Writing a test for a function in Python encompasses Python syntax, function calls, assert statements, and understanding of the function being tested.
- Playing a piece of music encompasses scales, arpeggios, dynamics, and rhythm in that key.
- A conversation in Spanish encompasses hundreds of vocabulary items and grammar patterns.

**The practical lever.** When planning reviews, ask: *is there a single, slightly-advanced task the learner could do that would exercise all the currently-due items at once?* If yes, do that instead of running ten separate reviews.

**The caveat.** Implicit review through encompassings is worth less than explicit review of the same item — maybe 30–60% as much. Count it, but discount it. Don't remove explicit review entirely; encompassings *compress* the queue, they don't eliminate it.

## What to do when spaced review piles up

A common failure mode: the learner skips review for a week or two; when they return, the SRS shows 200 due cards and the psychological weight kills the habit.

**Rules of thumb:**
- Daily consistency > intensity. 15 min/day every day is much better than 2 hours once a week.
- If you fall behind, do *not* try to clear the backlog in one sitting. Cap daily reviews at ~30 minutes. Let the rest wait.
- If the backlog is massive, consider a bankruptcy: reset the SRS state, re-learn core items, accept the loss. A fresh start you actually execute beats a perfect schedule you abandon.
- Rescue the habit before rescuing the backlog.

## Spacing for non-SRS review

If the learner isn't using an SRS, you can bake spacing into the weekly schedule directly:

- *Daily* session: warm-up with 5–15 min of yesterday's topics (1-day lag).
- *End-of-week* review: mixed retrieval practice covering the week's topics (~7-day lag).
- *Monthly* cumulative review: problem set or practice test covering the last 4 weeks (~30-day lag).
- *Quarterly* milestone: a substantial project or practice exam exercising everything to date.

This isn't as precise as an SRS, but it's easier to sustain and captures most of the benefit.

## The math-anxiety connection

Students who cram predict their own test scores as much too high (Emeny, Hartwig & Rohrer, 2021). Students who space predict accurately. This suggests a meta-cognitive benefit: spacing not only retains more, it makes you *know* what you know. Cramming induces overconfidence that crashes into reality at test time — one of the mechanisms behind math anxiety.

Spaced reviewers walk into tests with calibrated confidence. That in itself reduces anxiety.

## Summary for the learner

In one sentence: *the harder it is to retrieve something successfully, the more value the retrieval has — so wait until you're starting to forget, then retrieve from scratch, and stack these retrievals at expanding intervals forever.*

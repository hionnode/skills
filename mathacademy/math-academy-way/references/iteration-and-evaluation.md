# Iterating and evaluating the plan

A plan is a hypothesis, not a contract. This reference covers how to tell whether the plan is actually working, when to pivot, how to pivot at the lowest cost, and two Math-Academy-specific concepts that inform how the plan should evolve across a long learning arc: *conservative vs. aggressive edge of mastery*, and *core vs. supplemental topic prioritization*.

Read this when:

- A plan has been running for 2+ weeks and the user is wondering if it's working.
- The learner just missed a milestone and wants to know what to change.
- You're choosing the order of topics within a phase.
- You're deciding where the bar for "mastered" actually sits.

## Table of contents

1. [What "working" looks like](#what-working-looks-like)
2. [Signals that trigger a pivot](#signals-that-trigger-a-pivot)
3. [Pivot options, ranked by cost](#pivot-options-ranked-by-cost)
4. [Conservative vs. aggressive edge of mastery](#conservative-vs-aggressive-edge-of-mastery)
5. [Core vs. supplemental topic prioritization](#core-vs-supplemental-topic-prioritization)
6. [Retrospective cadence](#retrospective-cadence)

---

## What "working" looks like

A plan is working when these signals are present, roughly in this order of importance:

**1. Milestone checks are passing on schedule.** The biggest single signal. If the learner is clearing the ~3–4-week milestone exercises on or near the expected week, the pace and content are approximately right. Passing easily → plan may be too conservative; missing → plan is probably too aggressive or has a foundation problem.

**2. Habit is holding.** Sessions are happening at the expected frequency (± 1 session/week). If the plan assumed 5 sessions/week and the learner has averaged 2 for the last 3 weeks, the time budget assumption was wrong — the plan isn't running at the rate it was designed to run at.

**3. Reviews are getting easier, not harder.** In a well-tuned spaced-repetition schedule, successful reviews extend the next interval, which means individual topics come around less often and review sessions get shorter over time. If the review queue is *growing* week over week despite the learner doing the scheduled reviews, topics are being declared mastered too early, or the pace of new material is faster than retention allows.

**4. Previously-hard stuff has become automatic.** The learner finds themselves executing material from phase 1 without conscious effort during phase 3. This is automaticity, and it's the clearest sign that layering is happening: advanced work is reinforcing earlier skills instead of letting them decay.

**5. The target-level skill is visibly moving.** Can the learner do something at the *goal* level today that they couldn't do a month ago? A plan that stacks up internal milestones without the target skill progressing has the wrong curriculum pointed at the wrong goal.

### Rough numeric targets

Not laws, just reasonable calibration points:

| Metric | Healthy range | Concerning |
|---|---|---|
| Milestone-check pass rate | ≥ 80% of milestones cleared on the scheduled week ± 1 | 2 consecutive misses |
| Session consistency | ≥ 80% of planned sessions happen | < 60% over 2+ weeks |
| Day-1 retention (did they remember yesterday's topic?) | ≥ 90% | < 75% |
| Week-1 retention (did they remember last week's?) | ≥ 80% | < 60% |
| Month-1 retention | ≥ 70% | < 50% |
| Review queue trend | Flat or shrinking over a 2-week window | Growing week over week |

If the retention numbers are low, the problem is almost always insufficient spaced review or insufficient retrieval practice (the learner is reviewing by rereading rather than recall). If the queue is growing, the pace of new material is too fast for the current retention rate.

## Signals that trigger a pivot

These are different from "things are a little off this week" — which are normal and usually resolve in the next week. A pivot trigger is a pattern across multiple data points that means *something about the plan* is wrong, not that the learner had a bad week.

- **Two consecutive missed milestones.** One missed milestone is a bad week or a hard unit. Two in a row means the plan's pacing or foundation assumption is wrong.
- **Three consecutive weeks of < 60% session consistency.** The plan is scheduling time the learner doesn't actually have. Running a "5 sessions/week" plan at 2 sessions/week means nothing happens on schedule — it's a silent plan failure.
- **Review queue growing for 3+ weeks straight.** Not just a bad week; a structural mismatch between the rate of new material and the learner's retention. Either slow the new-material pace or add more explicit review.
- **Plateau of 3+ weeks with no milestone passes and no visible progress on the target skill.** Genuine plateaus lasting 1–3 weeks are normal consolidation; longer ones indicate a real problem.
- **Subjective burnout/collapse.** The learner reports dreading sessions, performance has slipped on previously-easy material, sleep or mood is off. This overrides all other signals — rest first, then diagnose the plan.
- **Motivation collapse.** Specifically: the learner stops believing the plan is pointed at what they want. Even if all the quantitative signals are green, a plan the learner doesn't believe in won't execute.

Do not pivot for: a single bad week, a specific unit feeling hard (weeks 2–3 of anything feel hard — that's desirable difficulty), or a single missed milestone.

## Pivot options, ranked by cost

Try cheaper interventions first. Most "the plan isn't working" reports resolve at level 1 or 2.

**1. Reduce daily load or add a rest day.** Cheapest. If the learner is pushing too hard and retention is suffering, less practice with more consolidation often beats more practice. Try a one-week reduced load and re-measure.

**2. Add scaffolding on the current bottleneck.** Identify the specific topic or component skill that's the jam-up. Add worked examples, split the step, drill the weak prerequisite (targeted remediation). Keep the overall plan intact; fix the bottleneck locally.

**3. Rebalance the session structure.** If retention is low, increase the review/retrieval portion at the cost of new material. If the learner is bored and under-challenged, flip it. If milestones are missed despite strong daily performance, add more cumulative/mixed practice.

**4. Switch the primary resource — but be careful.** Most "I don't like this book" is rationalization of desirable difficulty, not a resource problem. Switch only when you're confident: the resource has a genuine structural defect (no exercises, no feedback, wrong level), not just that it's harder than the learner hoped. A switch resets momentum, so it has real cost.

**5. Re-estimate the frontier.** If the plan is systematically misjudging what the learner can do, the knowledge graph sketch from Step 2 may need updating. Run a fresh mini-diagnostic. This is mid-cost — you'll want to rework the phase plan after.

**6. Rework the phase structure.** Re-sequence which topic clusters come in which order, reshape the phase lengths, adjust milestone spacing. Moderately expensive; requires a full Step 2 + Step 5 redo.

**7. Change the goal itself.** Highest cost, sometimes necessary. If life circumstances have changed (the deadline moved, the target use case changed, the learner is now studying for a different job), the plan needs to be pointed at a different target. Not a failure mode — sometimes the right answer.

## Conservative vs. aggressive edge of mastery

An important distinction that shapes when you declare a topic "done."

**Conservative edge of mastery** is the strict bar used for *placement* and *diagnostic* decisions: "does the learner know this well enough that we're confident they'd pass a zero-context test on it right now?" Requires high reliability — 90%+ accuracy, no hints, on mixed/unfamiliar problem presentations. Used by placement exams and diagnostic checks, where a false positive (calling a topic mastered when it isn't) has large downstream consequences (the learner gets placed into content they can't handle).

**Aggressive edge of mastery** is the looser bar used for *within-phase advancement*: "does the learner know this well enough that moving on to the next topic will exercise it further, rather than waste time?" Requires clear independent success (~5 consecutive problems correct, from memory, no hints), but not full polish. The assumption is that *layering* — subsequent advanced topics that encompass this one — will drive it to the conservative level through practice, without needing explicit continued drilling here.

**Why this matters for plan design:**

- **Advance within a phase at the aggressive bar.** Demanding the conservative bar on every topic before moving on slows learning to a crawl and creates overlearning (grinding a skill past the point of diminishing returns). The Math Academy model explicitly uses the aggressive bar for advancement, trusting layering + spaced review to consolidate.
- **Check against the conservative bar at milestones.** The phase-end or milestone exercise is where you verify that *everything in the phase* has actually consolidated to the strict level. If a topic was declared mastered aggressively during the phase but still fails the conservative check at the milestone, re-queue it.
- **Diagnostic / placement decisions require the conservative bar.** When deciding whether a learner is ready to *start* a course or unit, the bar is strict — a false positive here is expensive.

Practical rule: in-session, "mastered" means 5 consecutive right answers from memory, cold. Milestone check, "mastered" means 90%+ on a cumulative mixed set, no hints. If the latter fails for a topic that passed the former, the topic needed more layering practice than it got.

## Core vs. supplemental topic prioritization

Not all topics in a course are equal. Some are *core* — prerequisites for the most downstream topics — and therefore high-leverage. Others are *supplemental* — important to cover eventually, but don't unlock much else.

**How to identify core topics.**

Within a knowledge graph, a topic is core to the extent that *many subsequent topics depend on it*, directly or transitively. Ordering within a phase should prefer core topics first, so that:

1. **Automaticity builds on high-leverage skills first.** A core skill practiced in phase 1 will be implicitly rehearsed by many phase 2–5 topics that depend on it. A supplemental skill learned in phase 1 won't — it just sits there.
2. **The rest of the curriculum layers on a solid base.** Each later topic exercises its prerequisites; if the most-depended-on prerequisites are strong, most of the subsequent work reinforces them rather than being bottlenecked by them.
3. **Foundation gaps are found earlier.** If a core topic is shaky, it will cause visible problems quickly, because many later topics need it. A shaky supplemental won't show up until it does.

**How to identify core topics in practice.**

You usually don't have to compute this rigorously. Rough heuristics:

- **Ask "what do other topics in this domain use?"** Multiplication is core to arithmetic because division, fractions, algebra, and beyond all need it. Basic functions are core to calculus because derivatives and integrals are built on them. Pointers are core to C because essentially everything uses them. Pronouns and present tense are core to a language because every subsequent grammar construction uses them.
- **Look at the textbook structure.** The first 2–3 chapters of a well-designed textbook are usually the core topics; later chapters tend to branch into supplemental specializations. The inverse isn't always true (some textbooks front-load easy but non-core material for motivation), but it's a starting point.
- **Ask "if the learner forgot this, how many subsequent things would break?"** Core: many things. Supplemental: a specific later topic or two.
- **Look at the target.** If the goal is "read ML papers," core topics are the ones that appear in every paper (matrix ops, basic probability, calculus of gradients). Supplemental topics are the ones that appear in some papers (specific solver algorithms, specific distributional assumptions).

**How to use the distinction in the plan.**

- **Within a phase, sequence core before supplemental** so the learner gets repeated exposure to core material across the whole curriculum.
- **Under time pressure, cut supplemental before core.** If the plan is falling behind, a supplemental topic can often be deferred without catastrophe; a skipped core topic will break everything downstream.
- **Calibrate the mastery bar by position.** Core topics should be driven to full automaticity because so much downstream work will exercise them. Supplemental topics can be driven only to the aggressive-mastery bar, since they'll be used less frequently.
- **Mathematical Foundations (MF)-style shortcuts.** In domains where the target is advanced work, there's often a streamlined core-only path through the foundations. For an adult whose goal is university-level math, you don't need every K-12 topic — only those that are prerequisites for the target. A plan that identifies this subset and cuts the rest can move substantially faster without compromising the destination. Applies analogously to other domains: an adult learner whose goal is Rust for systems programming doesn't need every general-purpose language feature before specializing.

## Retrospective cadence

Three tiers, each catching different problems:

**Daily quick check (30 seconds, at end of session).** "Did I finish what I planned? What's the one thing I struggled with most today?" The "one thing I struggled with" feeds tomorrow's warm-up retrieval — missed items get re-queued with the shortest interval.

**Weekly review (15–20 minutes, same day every week).** Questions:
- How many sessions happened this week vs. planned?
- How did I do on the mixed-practice batches? (Pass rate is the critical number here.)
- Are there topics that have failed reviews 2+ times? (These are the current weak spots.)
- Did I hit any "I don't get this" walls, and did I address them or skip?
- Is my review queue growing or shrinking?
- Am I working harder than last week, or about the same, or less? (Both "much harder" and "much less" are signals.)

Output: a tuned review queue for next week, a list of 1–3 topics to drill, and maybe a small structural tweak (e.g., "I need to cut back to 4 sessions/week for the next two weeks because work is busy").

**Phase retrospective (30–45 minutes, at phase end).** Questions:
- Did I clear the milestone? If not, why?
- Are there topics in this phase that still feel shaky? If yes, can I name why — missing prerequisite? Insufficient practice? Poor resource?
- Is my target skill closer than it was at the start of this phase?
- Does the next phase's plan still make sense given what I know now?
- Do I need to change primary resource, cadence, or goal?

Output: adjustments to the next phase's plan, possibly a re-run of the Step 2 knowledge-graph sketch if something material has changed.

**Milestone / quarterly retrospective (60+ minutes, every 3–4 phases).** This is the level where it's legitimate to reconsider the big picture — is the goal still the right goal, is the plan still pointed at it, has anything material changed about the learner's life or interests? Rare but important; small mid-course corrections made at this cadence prevent big catastrophes later.

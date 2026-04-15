---
name: math-academy-way
description: Produce an evidence-based, individualized learning plan following The Math Academy Way — Justin Skycak's synthesis of cognitive-science-backed learning techniques (talent development, mastery learning, knowledge-graph scaffolding, deliberate practice, active learning, spaced repetition, interleaving, retrieval practice, automaticity, targeted remediation). Use this skill whenever the user wants to learn something (any domain — not just math: programming, music, a foreign language, chess, writing, a new job skill, etc.), asks for a study plan or curriculum, asks how to master a subject, wants to improve their practice regimen, is frustrated with slow progress, keeps plateauing at the same level, keeps making the same mistakes, complains they keep forgetting what they studied, wonders whether their study plan is actually working, wants help combining self-study with lessons from a teacher or tutor, or asks what order to study things in. Also use it when designing a tutoring plan or curriculum for someone else, or when a parent is trying to figure out how to help their kid learn something. Trigger even when the user doesn't explicitly say "plan" — "I want to get good at X", "how do I learn Y from scratch", "I've been practicing Z for months and I'm stuck" are all clear signals.
---

# The Math Academy Way — Learning Plan Designer

This skill turns a vague learning goal into a concrete, evidence-based plan the user can actually follow. It is distilled from Justin Skycak's book *The Math Academy Way*, which synthesizes a century of cognitive-science research into a small set of compounding strategies.

The principles are domain-general. "Math" in the title is accidental — the same mechanisms govern learning a programming language, a musical instrument, a foreign language, chess, a trade, or anything else that's skill-based and hierarchical.

## Orientation

Most study advice is folklore. Math Academy's contribution is to say: here is what the research actually shows, here are the strategies that compound, and here is the order of operations that ties them together into a system. The skill's job is to translate those strategies into a plan tailored to this user, this goal, this amount of available time.

Four philosophical anchors to keep in mind throughout:

**1. Talent development, not schooling.** Traditional schooling marches a group through a syllabus on a schedule; individuals are judged relative to the group and different students "learn to different levels." Talent development is the opposite: everyone must clear the same bar of proficiency on each skill before moving on, but *the pace is entirely individual*. The plan you produce is for one learner. Its pace flexes to their speed. Its bar does not flex.

**2. The greedy strategy.** If the goal is depth in a domain, the empirical finding is that the best way to get better at problem-solving is to acquire more foundational skills, not to practice "general problem-solving" in the abstract. So: front-load foundational skill acquisition, move aggressively toward the edge of what humans know in the target direction, and save creative/original production for when you actually reach the frontier. Don't "expand sideways" into loosely related stuff as a substitute for going forward.

**3. Tutoring the King's Kid.** Imagine you had one month to teach a single student, one-on-one, and the outcome determined whether you got rich or were executed. You would not lecture. You would not assign a textbook chapter and vanish. You would watch them attempt problems, correct their form instantly, push them at exactly their edge, and build a ruthlessly efficient daily routine around what they personally still can't do. That is the standard this skill is aiming for. Every deviation needs a reason.

**4. Desirable difficulties.** A counterintuitive, load-bearing finding: the practice conditions that *feel* most productive (rereading, blocked drills on one topic, reviewing right after learning) produce poor long-term retention. The conditions that feel harder and slower (retrieval without notes, interleaving different topics, spacing reviews out until you're starting to forget) produce far better retention and transfer. When the user resists a recommendation because "this feels harder / I'm making more mistakes / I was faster the other way," that is often a *positive* signal, not a negative one. Name this explicitly in the plan.

## The workflow

Follow these five steps in order. Don't skip to writing a plan before you have the context; a generic plan is worse than no plan.

### Step 1 — Capture the goal and the learner

Before writing anything, establish:

- **The domain and target level.** "Learn linear algebra" is too vague. "Be able to implement and reason about the algorithms in Strang's textbook, to the level where I can read ML papers that use LA without getting stuck" is a target. "Learn Spanish" → "Hold a 30-minute conversation with a native speaker about daily topics, B1-ish" is a target. Push for something concrete enough that you can tell when the learner has arrived.
- **Current starting point (the knowledge frontier).** What do they already know? What have they tried? What feels shaky? If they can't say, suggest a cheap diagnostic — a short self-quiz, a few warm-up problems from a textbook of the target level, attempting a real task in the domain — rather than guessing.
- **Time budget.** Minutes per day, days per week, and any deadline. Be realistic; consistency at 30 min/day beats sporadic 3-hour sessions. (If they say "as much as needed," translate that into a concrete daily floor — e.g., 30–60 focused minutes — because the plan has to fit into a real life.)
- **Motivation / accountability context.** Is this a career must, a hobby, school, a deadline? This determines how much "desirable difficulty" they can absorb and whether you need to build in external accountability (a study buddy, a tutor, a public commitment). Ask about two things specifically: (i) what *external* accountability structure (if any) already exists — a class, a tutor, a study partner, a deadline, a goal someone else is watching — and (ii) what their *typical failure mode* looks like when they've tried to learn things in the past. Do they fizzle out after a few weeks? Cram right before a deadline? Watch endless videos without producing? Drop the habit when life gets busy? The answer reshapes the plan: chronic-fizzler learners need stronger external accountability mechanisms baked in up front; learners who cram need a plan that front-loads retrieval practice; learners who over-consume need explicit production quotas. For self-learners without any existing external structure, this is often the single biggest determinant of whether the plan actually executes, so don't skip it. See `references/motivation-and-habit.md` for the full menu of accountability structures and how to pick one.

If the user came in with a short prompt ("help me learn Rust"), ask 2–3 targeted questions to get the above. Don't ask ten questions — ask the ones whose answers will actually change the plan.

### Step 2 — Sketch the knowledge graph

This is the most Math-Academy-specific step and the one most learners skip. A knowledge graph is a directed graph of *atomic* topics, connected by prerequisite relationships. To design a good plan you need a mental model of:

- **The topics.** Break the domain into small, testable skills. "Understand recursion" is not atomic; "trace a recursive function call by hand" and "convert a naive recursive function to a memoized one" are closer. Err toward finer granularity — Math Academy's own curriculum is ~10× finer-grained than a typical textbook, and that is exactly why students succeed at it where they fail at textbooks. Large steps break more learners than small steps do.
- **The prerequisites.** For each topic, what does the learner have to already know to succeed at it? Arrows point *from* prerequisite *to* dependent topic. A topic is "ready to learn" when all its prerequisites are mastered. A topic has "shaky foundations" if a prerequisite is merely familiar, not mastered.
- **The encompassings.** This is the deep move. An *encompassing* is a more advanced topic whose execution implicitly exercises a simpler one. Long multiplication encompasses single-digit multiplication and addition. Writing idiomatic Python code encompasses control flow, data structures, and syntax. Playing a piece of music encompasses scales and intervals. Identifying encompassings matters because **practicing the advanced topic counts as practice of the simpler ones** — you do not have to schedule both. This is how a knowledge graph generates massive speedups: you spend most of your time at the frontier, and simpler skills get maintained for free.
- **The frontier.** Given what the learner already knows, which topics are they *ready to learn next* (all prerequisites met) and which are *not yet reachable* (some prerequisite missing)? Their daily lessons should come from the frontier. Work below the frontier is redundant; work above it is premature.

You don't have to draw an exhaustive graph for the whole domain upfront. What you need is:

- the course-level sketch (the 5–15 big chunks and their rough prerequisite order),
- a detailed view of the frontier — the ~10–30 next atomic topics the learner will actually touch,
- and an awareness of which advanced activities encompass which earlier ones (so reviews can be compressed).

If there are foundational gaps below the frontier (e.g., they want to learn multivariable calculus but are rusty on single-variable), you generally do not send them all the way back to patch every hole upfront. Let them start on topics in the target course that don't depend on the gap, so they build momentum; then patch the gap when it actually blocks progress. Momentum matters.

**From graph to session.** The frontier and the daily session are connected like this: on any given day, the learner picks **1–3 new topics** from the frontier (not more — more than 3 inflates cognitive load and dilutes practice), **all spaced reviews that are due**, and **a handful of interleaved problems** spanning earlier topics. Choose new topics that are on the frontier but not *too* closely related to each other (see non-interference: related concepts learned in close succession interfere with each other's recall). Within a phase, prefer *core* topics — those that are prerequisites for the most downstream work — before *supplemental* ones, so that automaticity on high-leverage skills builds first and the rest of the curriculum layers on a solid base. See `references/iteration-and-evaluation.md` for the core-vs-supplemental heuristic.

### Step 3 — Design the daily session

This is where the cognitive learning strategies get operationalized. A well-designed session has the following structure. Use this as a default template and adapt to domain:

**(a) Warm-up: spaced review (5–15 min).** Retrieve a handful of previously-learned topics whose review is due. Do this from memory — no notes, no peeking. Check after. This is where the compounding happens: every review that you ace extends the next interval, so over time, a given topic requires almost no maintenance to stay sharp. (See `references/spacing.md` for specific intervals.)

**(b) New learning: a small number of new topics from the frontier (20–40 min).** For each new topic:
- **Minimum effective dose of explanation.** Read or watch *just enough* to grasp the idea and see one or two worked examples. If you find yourself consuming for 20 minutes without producing anything, stop — you're in passive mode. The worked example is a scaffold, not a lesson.
- **Immediately produce.** Attempt similar problems / exercises / output. This is where the learning actually happens. Aim for ~3× as much production as consumption, minimum. (Elite performers in trainable domains hit closer to 6×.)
- **Advance only on mastery.** Don't move to the next topic until the current one is solid — not "I saw it," but "I can do it independently, reliably, without looking back." This is mastery learning.
- **If stuck twice in the same place,** stop and back up: the problem is a shaky prerequisite, not the current topic. Identify which component skill is weak, drill it briefly, then return. This is targeted remediation.

**(c) Interleaved mixed practice (10–20 min).** A mixed batch of problems drawn from a *variety* of previously-learned topics, not just today's new ones. The point is to force discrimination — the learner has to figure out *which* technique applies to *which* problem, rather than mindlessly applying today's hammer to everything. This feels harder than blocked practice (and performance on this set will be lower). That is the point. Interleaving routinely doubles retention vs. blocked practice.

**(d) Quick low-stakes self-quiz (optional but recommended).** A handful of retrieval-only questions on recently-learned material, ideally timed. This is where automaticity gets built. Do not introduce timing on skills the learner can't yet perform accurately in untimed mode — that's a mismatch that breeds anxiety without building fluency.

**Ratios.** A good rough target for total session time:
- ~10–20% passive intake (reading, watching, worked examples)
- ~60–70% active production on new material
- ~15–25% spaced review + interleaved practice + retrieval

Adjust down on ratios of passive intake over time: beginners need more scaffolding, experts need less (the *expertise reversal effect* — things that help a beginner actively harm an expert).

**Scaffolding techniques (how to implement "small steps").** The single most common reason a learner gets stuck on a topic is cognitive overload — too much new information held in working memory at once. Working memory holds only ~4 chunks of novel information at once, so the height of each step determines whether the learner can climb it. Use these techniques to keep steps small:

- **Worked examples before cold attempts.** On each new topic, start with 1–2 fully worked examples (shown end-to-end with reasoning), *then* have the learner attempt a similar problem cold. This is a scaffold, not a crutch — drop it once the learner is reliable.
- **Subgoal labeling.** When explaining a multi-step procedure, group steps into *named* subgoals ("First, isolate the variable. Then apply the inverse operation. Finally, check by substitution."). This compresses many steps into fewer chunks and helps the learner transfer the procedure to novel problems.
- **Dual coding.** Pair verbal explanation with a visual (diagram, flowchart, before/after). Working memory has separate verbal and visuo-spatial channels — using both in parallel roughly doubles effective capacity. For domains without obvious visuals (e.g., abstract math, language grammar), invent one — a table, a tree, a labelled diagram of the relationship.
- **Decompose aggressively.** If a single "topic" is taking more than ~20 minutes to reach the first successful independent attempt, it's probably two topics glued together. Split it.

**Defining mastery.** "Solid" needs an operational definition or the learner will move on too early (the single most common self-study failure). A working definition: **the learner can solve at least 5 consecutive representative problems on this topic, from memory, without hints, at a pace consistent with the target skill level** — untimed if they haven't reached accuracy yet, timed once they have. If any of those break (they need a hint, they re-read the worked example, they make an arithmetic slip, they take twice as long as the target), the topic isn't done. Re-queue and come back. See `references/iteration-and-evaluation.md` for the distinction between the strict "conservative" mastery bar (used for placement/diagnostic checks) and the looser "aggressive" bar used for within-phase advancement.

### Step 4 — Design the feedback and assessment loop

Learning without feedback is mostly performance theater. The plan must specify *how* the learner will know whether each attempt was correct, *what* they'll do about mistakes, and *how* they'll catch drift over time.

- **Immediate corrective feedback on every practice attempt.** If an autograder or answer key exists (textbook odd-numbered answers, unit tests, a tutor, a language app, ChatGPT/Claude checking a proof), use it. If not, construct one: have the learner predict the answer and check, have them re-derive a result they should already know, have them explain their reasoning out loud and notice gaps. The feedback delay should be seconds to minutes, not days.
- **Keep a running list of misses.** Every question they miss becomes the seed of a targeted remedial review on that component skill. Don't just note the wrong answer — identify *which underlying skill was weak* and re-queue practice of that skill.
- **Weekly-ish retrieval quiz.** Mix of topics from the past 1–4 weeks, no notes, timed if skills are fluent enough, untimed otherwise. Missed items go back into the review queue with a shortened interval.
- **Milestone check.** Every few weeks, a slightly harder cumulative exercise (a project, a real-world task in the domain, an official practice exam). This catches drift that weekly quizzes miss.

**On the bar.** When the learner struggles, the response is *not* to lower the expectation — that's the most common failure mode of self-study. The response is to add scaffolding (smaller steps, more worked examples, targeted remediation of the weak component), then ask them to clear the original bar fully and independently.

**How to know the plan is working — and when to pivot.** A plan is not a contract; it's a hypothesis, and it needs to be periodically checked against reality. The feedback loop above gives per-session data; the *plan-level* loop answers a different question — is this whole approach moving the learner toward the goal? Watch these signals:

- **Milestone pass rate.** Is the learner clearing milestone checks at roughly their scheduled cadence? Chronic milestone failures (2+ in a row) mean something structural is off, not just a bad week.
- **Habit consistency.** Is the learner actually doing sessions at the expected frequency? A plan that assumes 5 sessions/week but gets 2 is a different plan in practice; reassess the time budget rather than keep ghost-scheduling.
- **Review dynamics.** Are spaced reviews getting *easier* over time (the expected pattern — consolidation moves topics into deeper memory) or *harder* (a signal that foundations are shaky or topics were declared mastered too early)? A growing review backlog that won't shrink means the pace is faster than retention can keep up with.
- **Subjective fluency.** After a few weeks, is the learner finding that tasks at the previous phase's level feel *automatic* now? If not, the previous phase wasn't really mastered.
- **Progress toward the goal.** Can the learner do something today they couldn't do a month ago, at the goal level? If the phases are stacking up but the target skill isn't moving, the curriculum may be mis-pointed.

Pivot options, in order of cost: (1) reduce daily load or add a rest day, (2) add scaffolding on the current bottleneck (more worked examples, smaller sub-steps), (3) switch the primary resource if it genuinely isn't working (not just because it's hard), (4) re-estimate the frontier (new diagnostic), (5) rework the phase structure, (6) change the goal itself if circumstances have changed. Resist (3)–(6) until you've given (1)–(2) real time — most "the resource is bad" complaints are really "desirable difficulty feels bad in week 2." See `references/iteration-and-evaluation.md` for the diagnostic tree distinguishing burnout, bar-too-high, resource-mismatch, and wrong-priorities.

### Step 5 — Write the plan

Deliver the plan as a concrete artifact the user can execute. A good plan has:

1. **Goal** (one or two sentences, concrete enough to test against).
2. **Current starting point** (what they know, what's shaky).
3. **A phased roadmap** over weeks or months: the rough sequence of topic clusters they'll move through, with rough time estimates. Keep phases small enough that they hit a visible milestone every few weeks.
4. **A daily session template** (the one from Step 3), instantiated for this domain: what resources, what kinds of practice, what kinds of review, with rough minute allocations.
5. **Resources** pointing at specific materials. Prefer resources that are dense with active practice (problem books, exercise platforms, spaced-repetition tools, interactive courses) over resources that are purely expositional. Prefer *one* primary resource they stick with over a hoarded pile of tabs.
6. **Feedback and assessment plan** (how misses get caught and re-queued, when quizzes happen, when milestones are).
7. **An accountability mechanism** (not optional — name one). For adult self-learners, the single biggest determinant of whether the plan actually happens over a months-long horizon is external structure. Pick at least one: a tutor or coach on a recurring cadence, a study partner who checks in, a public commitment (tell a specific person, post publicly), a pre-committed forcing function (a scheduled exam, performance, or demo date), a daily streak on a shared tracker, or a pre-committed loss (money put at stake). Ranked roughly by effectiveness: scheduled human check-in > forcing function > streak > solo tracker. If the learner already has a tutor/teacher/coach, structure the self-study plan *around* that cadence rather than parallel to it (e.g., use the tutor session as the weekly retrieval quiz and the repository for misses to drill). Don't skip this step even if the learner says "I have high motivation" — motivation is a trait that fluctuates, accountability is a structure that doesn't. See `references/motivation-and-habit.md` for a fuller menu and how to match one to the learner.
8. **Pivot signals** — the 2–3 signals from Step 4 that, if they fire, mean the plan needs adjustment (e.g., "if you miss the Week 4 milestone, shorten Phase 2 and add a remedial review pass"). Naming these up front prevents the learner from either quitting the plan too quickly (at the first hard week) or grinding on a broken plan for months.
9. **Anti-patterns to watch for,** tailored to this learner. Highlight the temptations they specifically are likely to fall into — rereading, watching lectures without producing, cramming, dropping spaced review when busy, blocked practice because it "feels" more productive. Call them out by name so the learner recognizes them in the wild.
10. **A note on the feel of the plan.** Warn them that the plan will feel harder and slower than their prior study methods, especially in the first 2–3 weeks. That's desirable difficulty, not a bug. The payoff is on the delayed tests, not the immediate ones.

Keep the tone direct and practical. Don't bury the plan in a wall of research citations — a compact plan with clear rationale is much more executable than an exhaustive one.

## Cognitive learning strategies — the quick reference

The skill's workflow above already weaves these in, but if a user asks "why" about any single recommendation, these are the reasons. Most of what makes the Math Academy Way work is applying *all* of these together — none is silver-bullet alone, but they compound.

- **Active learning.** Learning happens when you produce, not when you consume. Passive intake (lecture, video, reading) is a scaffold for getting oriented, not a substitute for practice.
- **Deliberate practice.** Individualized, effortful practice at the edge of your current ability, with immediate corrective feedback, aimed at specific weaknesses. Not mindless repetition of things you're already good at.
- **Mastery learning.** Everyone advances only after demonstrating proficiency on prerequisites. Same bar, individualized pace.
- **Minimizing cognitive load.** Break tasks into small steps; use worked examples; group steps into meaningful subgoals; use visuals + words together (dual coding). Working memory holds ~4 chunks at once — if you overload it, nothing transfers.
- **Automaticity.** Low-level skills must become unconscious (multiplication facts, basic syntax, scales, common phrases). Automaticity frees working memory for higher reasoning. Without it, every advanced task is overloaded from below.
- **Layering.** Keep building new things on top of old ones; this exercises the old ones without needing a separate review. "The more connections to a piece of knowledge, the more ingrained and retrievable it is."
- **Non-interference.** Don't teach closely-related things in close succession — they interfere with each other's recall. Space related things out; pair new concepts with dissimilar material.
- **Spaced repetition.** Reviews distributed over time (expanding intervals) produce vastly better retention than cramming. The more successful reviews you stack with appropriate gaps, the longer the next gap can be.
- **Interleaving / mixed practice.** Review sessions should cover many topics mixed together, not one topic at a time. This feels worse and performs worse on practice, but doubles retention on delayed tests.
- **Testing effect / retrieval practice.** Pulling information out of memory strengthens it far more than putting information in. Quizzing beats rereading; closed-book solving beats open-book solving.
- **Targeted remediation.** When the learner is stuck, identify the *specific* weak component skill and drill it. Don't lower the standard on the main task; raise the scaffolding.
- **Gamification (optional).** Points, streaks, leaderboards can sustain motivation — but only if aligned with learning outcomes and resistant to being gamed. Streaks on a spaced-repetition app work; XP farming does not.

For deeper treatment of any of these, see `references/strategies.md`.

## Common traps

A short checklist of things to flag in the plan's anti-patterns section. Fuller treatment of each is in `references/strategies.md` (under "desirable difficulties") and `references/myths.md`:

- **The illusion of comprehension** — following along feels like learning but isn't. If they haven't tried to produce from memory, they don't know.
- **Blocked-practice overconfidence** — fluency during 20-in-a-row practice does not survive into mixed assessment.
- **"Just one more video"** — passive consumption with no production quota.
- **Skipping spaced review when busy** — decay is silent; a tiny daily review beats no review.
- **Overlearning** — grinding a skill past mastery has rapidly diminishing returns. Move on and trust spaced review.
- **Setting the bar too low** — "I kind of get it" is shaky foundations that crack under load.
- **Premature timed drilling** — timing builds fluency, not accuracy. Accurate first, timed second.
- **Trying to fix all foundations upfront** — patches foundations when they block, not before.

## What "looks like a good plan" vs. "looks like a bad plan"

**Good:** a concrete daily structure with minute allocations, named resources, explicit active-practice ratios, an explicit review and quiz schedule, named milestones every few weeks, a list of anti-patterns tailored to this learner, and an honest note about the feel.

**Bad:** a curated list of videos and books to "work through," a week-by-week syllabus with no active-practice mechanism, a "first master all foundations, then start" structure, or any plan that omits either (a) spaced review or (b) a way to verify the learner's attempts.

If the user pushes back on a recommendation because it feels uncomfortable, don't fold reflexively — check whether the discomfort is the *desirable difficulty* kind (more mistakes, more effort, slower feeling) or the *undesirable difficulty* kind (insurmountable task, anxiety-producing mismatch, or a skill that's genuinely blocked by a missing prerequisite). The first is working as intended; the second is a signal to add scaffolding or re-check prerequisites.

## When to consult references

The skill is self-contained for designing a plan, but for specific deep questions pull in:

- `references/strategies.md` — longer treatments of each cognitive learning strategy with the research context, when to apply and when not to.
- `references/spacing.md` — specific spaced-repetition intervals, how to adjust for learner performance, how "encompassings" compress the review queue.
- `references/examples.md` — fully worked example plans across several domains (math, programming, foreign language, an instrument), so you can see the template instantiated.
- `references/motivation-and-habit.md` — when the learner has an accountability/habit/setback problem: how to design external structure, how to recover from a lapse, how to tell burnout from desirable difficulty, parental support for younger learners.
- `references/iteration-and-evaluation.md` — when the plan is running and it's time to check whether it's working: signals to watch, pivot options ranked by cost, conservative vs. aggressive edge of mastery, core vs. supplemental topic prioritization, retrospective cadence.
- `references/myths.md` — common "learning styles" / "left-brain vs. right-brain" / "discovery learning is best" / "effortless learning" misconceptions that the Math Academy book explicitly debunks, in case a user cites one.

Only load these when the specific question calls for them — otherwise keep the context light.

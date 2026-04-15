# Cognitive Learning Strategies — Deep Reference

Longer treatments of each strategy, drawn from *The Math Academy Way* (Skycak). Read the parts relevant to the user's question rather than the whole file.

## Table of contents

1. [Active learning](#active-learning)
2. [Deliberate practice](#deliberate-practice)
3. [Mastery learning](#mastery-learning)
4. [Minimizing cognitive load](#minimizing-cognitive-load)
5. [Developing automaticity](#developing-automaticity)
6. [Layering](#layering)
7. [Non-interference](#non-interference)
8. [Spaced repetition](#spaced-repetition)
9. [Interleaving (mixed practice)](#interleaving-mixed-practice)
10. [Testing effect (retrieval practice)](#testing-effect-retrieval-practice)
11. [Targeted remediation](#targeted-remediation)
12. [Gamification](#gamification)
13. [Desirable difficulties — the unifying theme](#desirable-difficulties--the-unifying-theme)

---

## Active learning

**The finding.** Hundreds of studies, synthesized by Freeman et al. (2014): passive consumption (lecture, video, reading) produces significantly less learning than active practice — in STEM, the effect size is large enough that the meta-analysis authors called continued lecture-based control conditions ethically questionable.

**The mechanism.** Learning *is* a positive change in long-term memory. Watching a fluent explanation produces familiarity with the material but not the neural wiring required to reproduce it. Reproduction is built by attempting reproduction.

**True active learning requires:**
- *Every* learner actively engaged (class discussions with 3 loud participants don't count).
- Engagement with *every* piece of material to learn (divide-and-conquer group projects don't count).
- Immediate corrective feedback on each attempt, so errors don't consolidate.

**The common failure mode.** Learners mis-perceive active learning as *less* productive because it feels harder and they make more mistakes (Deslauriers et al., 2019: Harvard physics students rated lectures higher than active classes even though they learned less from lectures). Warn the learner explicitly about this perception inversion.

**When to use passive intake.** Brief, minimum-effective-dose explanation at the start of a new topic. The rule of thumb is that passive time should set up active time, not replace it. Target ~10–15% of total learning time on passive intake for beginners, dropping to ~5% as expertise builds.

**Ratios to aim for.** Elite skaters in a Deakin & Cobley (2003) study spent 86 of every 100 practice minutes actively practicing (68 on the hardest skills, 18 on secondary skills); only 14 minutes resting or passive. Non-elite skaters were closer to 54/46. A Math Academy student's session is roughly 7 active practice problems per 1 passive worked example.

---

## Deliberate practice

**The finding.** Ericsson, Krampe & Tesch-Römer (1993): the amount of deliberate practice is the single most prominent underlying factor in performance differences across domains, even among highly talented elite performers.

**Definition.** Practice that is:
- *individualized* (chosen for this learner's specific weaknesses),
- *effortful* (at the edge of current ability, not mindless repetition within repertoire),
- *with immediate feedback* on correctness and form,
- *aimed at specific improvement*, not generic exposure.

**Contrast with naive practice.** A guitarist who plays their favorite pieces for 2 hours a day is engaged in active learning but not deliberate practice — they're repeating what they already can do. Deliberate practice would be isolating the exact transition they fumble, drilling it 20 times at the slowest tempo where they get it right, then creeping the tempo up.

**Structural requirement.** Deliberate practice is uncomfortable by design, and people don't do it voluntarily at high intensity. This is why elite performers almost always have a coach and why self-study plans need an external accountability structure.

---

## Mastery learning

**The finding.** Bloom (1984): one-on-one tutoring with mastery learning produced a two-sigma improvement over standard group instruction (average tutored student outperformed 98% of group-instructed students). A single teacher doing looser mastery learning with a class of 30 achieved around one sigma. Meta-analyses (Kulik et al., 1990) reproduce gains averaging ~0.5 standard deviations even in loose classroom approximations.

**The principle.** Students must demonstrate proficiency on prerequisite topics before advancing. The bar is the same for everyone; the pace is individual.

**Why it's rarely done.** It requires keeping different students on different topics at the same time, and it opens a "can of worms" — teachers can no longer hide behind group averages because each student's specific weaknesses become visible. It also threatens traditional grading: if everyone reaches mastery, how do you rank students?

**Implementation for a self-learner.** Define "mastery" concretely per topic (e.g., "can solve 5 consecutive problems of this type, from memory, without hints"). Do not move on until it's met. Return to the topic in spaced reviews; if performance drops, the topic is re-queued.

---

## Minimizing cognitive load

**The finding.** Working memory holds ~4 chunks of novel information at once (Cowan, 2001) for ~20 seconds without rehearsal. Load past that and the task cannot complete — the learner gets stuck not because the concept is beyond them but because they literally cannot hold all its pieces in mind at once.

**Working memory capacity predicts math performance better than IQ** for young students (Alloway & Alloway, 2010). This is not a fixed ceiling but it means the "height of each stair" on the learning staircase matters enormously.

**Scaffolding techniques:**
- *Small steps.* Break a typical textbook section into 3–5 smaller topics. Math Academy runs ~10× finer-grained than typical textbooks, which is why students who fail at textbooks succeed there.
- *Worked examples.* Show a solved problem *before* asking the learner to attempt similar ones. A worked example is not cheating; it's the scaffold that lets a novice schema form. Once schema exists, drop the example and have them solve cold.
- *Subgoal labeling.* Explicitly group solution steps into named subgoals ("First, isolate the variable. Second, apply the inverse operation..."). This compresses many steps into fewer chunks and helps learners transfer to novel problems.
- *Dual coding.* Visual + verbal together (a diagram with labels beats either alone). Uses both the phonological loop and the visuo-spatial sketchpad in parallel rather than overloading either.

**Expertise reversal effect.** Scaffolds that help beginners actively hurt experts. Strip them as skill grows — eventually the learner solves problems cold, without lookups, under time pressure.

---

## Developing automaticity

**The finding.** Automaticity — the ability to execute a low-level skill without conscious effort — frees working memory to reason about higher-level things. Chase & Ericsson (1982) showed that reliable long-term-memory access effectively extends working memory capacity within a domain. Chess grandmasters recognize 50,000–100,000 chess patterns instantly; this is what distinguishes them from novices, not better "general reasoning."

**The 19th-century framing (Bryan & Harter, 1899):** *"The learner must come to do with one stroke of attention what now requires half a dozen... Automatism is not genius, but it is the hands and feet of genius."*

**The case for automaticity at the bottom.** A student who doesn't know 4×8 automatically can still *compute* 4×8 — but they'll consume several working memory slots doing it, and then fail to solve the cubing problem that 4×8 was nested inside. This cascades: every advanced task is overloaded from below by shaky foundations.

**Automaticity vs. familiarity.** *"If you truly know something, you should be able to access and leverage that information both quickly and accurately. If you can't, you're just 'familiar' with it."* You cannot build on familiarity — that's what "shaky foundations" means.

**How it's built.** Repeated successful retrieval, spaced over time, typically with some timed practice once the skill is reliably accurate untimed.

---

## Layering

**The finding.** When a new task exercises a previously-learned skill, two things happen:
- *Retroactive facilitation* — memory of the prior skill is restored as well as if you'd practiced it explicitly (Ausubel et al., 1957).
- *Proactive facilitation* — prior skill knowledge improves the acquisition of the new skill (Arzi et al., 1985).

**The practical consequence.** The efficient way to maintain earlier skills is not to review them separately but to keep advancing into new skills that implicitly exercise them. Layering gives you review *for free* while you're making forward progress. Math Academy's "encompassings" mechanic is a formalization of this: whenever an advanced problem is due, its prerequisites get implicit review credit.

**Requirement.** The curriculum has to actually build on itself — advanced topics must exercise earlier ones. Watered-down courses that avoid hard problems (e.g., calculus courses that avoid heavy algebra) lose this benefit; students can complete the advanced course while forgetting the foundations.

**Structural integrity (the engineering analogy).** Every time a new feature is built on top, shaky spots in the foundation get revealed and fortified. Schemas become more organized, connections multiply, recall becomes faster and more reliable. This is where "deep understanding" actually comes from — not from meta-level reflection but from layered use.

---

## Non-interference

**The finding.** Conceptually related pieces of knowledge interfere with each other's recall. Multiplication error studies show >50% (and possibly up to 90%) of errors are interference-based — when recalling 4×8, the related facts 4×6=24 and 3×8=24 pollute the spreading activation.

**The lever.** Time spacing between related concepts reduces interference (Underwood & Ekstrand, 1967). Traditional curricula do the opposite: they group related material into units taught in immediate succession, which maximizes interference.

**Implementation.** When introducing a new concept, pair it with dissimilar concurrent material. "Learn 5 things at once that are unrelated to each other" is far more efficient than "learn 5 related things in sequence." If the target concept is similar to something recently learned, space them apart.

---

## Spaced repetition

See `spacing.md` for the detailed intervals and scheduling logic. In brief:

- Review just before you'd otherwise forget. Each successful review at the right lag extends the next lag.
- Massed review (cramming) gives short-term fluency but decays fast. Spaced review gives durable retention.
- The spacing effect has ~255+ studies reproducing it across a century, cited by Kang (2016) as "a case study in the failure to apply the results of psychological research" because classrooms still rarely use it.
- Self-learners should use an SRS (Anki, Mochi, etc.) or build intervals into their own weekly schedule.

---

## Interleaving (mixed practice)

**The finding.** Rohrer, Dedrick & Stershic (2015): simply interleaving math practice problems vs. blocking them *doubled* test scores one day later and produced a 76% advantage one month later. Near-immunity to forgetting — test delay increased 30-fold while scores dropped less than 10%.

**Why it works:**
- *Efficiency.* Blocked practice hits diminishing returns fast (overlearning). Interleaving distributes the same effort across more topics.
- *Discrimination learning.* Mixed problems force the learner to *identify which technique applies*, not just execute the current lesson's technique on autopilot. This is the actual bottleneck on cumulative tests.
- *Implicit spacing.* Interleaving automatically spaces practice of each topic across sessions.

**Why it feels bad.** Practice performance is lower when interleaved (students make more mistakes, go slower). They interpret this as "I'm learning less." Kornell & Bjork (2008) — even after taking a test proving interleaving was better, participants still rated blocked practice as more effective.

**When to block briefly.** Very early in learning a new skill, a small block (5–10 problems) is useful to let the learner focus on the mechanics. After the skill is running, switch to mixed practice for the rest of life.

**Macro vs. micro interleaving.**
- *Micro-interleaving:* mixing problem types within a single session.
- *Macro-interleaving:* spreading topics across weeks rather than doing a month on topic A then a month on topic B. A calculus class that spent 15 min/day on limits + 15 on derivatives + 15 on integrals + 15 on series for the whole semester would beat a class that does a month on each.

---

## Testing effect (retrieval practice)

**The finding.** Retrieving information from memory strengthens it far more than re-exposure does. Francis Bacon noted this in 1620; hundreds of studies since have confirmed it across subjects, levels, and settings (Roediger & Butler 2011, Yang et al. 2021). Karpicke & Blunt (2011) showed retrieval practice beat concept-mapping, elaborative study, and rereading.

**The principle.** "Following along" is not learning. Comprehension while reading does not mean you can reproduce the content later. The *only* test of whether you know something is trying to produce it without looking.

**Spaced retrieval practice** (combining testing + spacing) is routinely the top-performing study method in the literature.

**Implementation:**
- Close the book and try to reproduce. Check after.
- Flashcards with active recall (not "read both sides and nod").
- Practice problems from memory before looking at worked examples.
- Low-stakes quizzes interleaved with learning — more frequent and lower-stakes is better than infrequent and high-stakes.

**Anxiety caveat.** Testing anxiety comes from proficiency mismatch (being tested on things you can't yet do) and stakes. Low-stakes frequent quizzes on skills you can do *reduce* anxiety over time by building proficiency and familiarity with the format.

---

## Targeted remediation

**The principle.** When a learner gets stuck, *don't lower the bar*. Identify the specific component skill that's weak and practice it, then return to the original task.

**How to target.**
- If stuck once: the learner might just need another attempt.
- If stuck twice at the same point: the problem is a missing/weak prerequisite.
- Trace backward through the knowledge graph to the *most specific* component skill being used. Often the key prerequisite is several steps upstream — e.g., a student can recognize "exponent means repeated multiplication" but is shaky on "multiplying negative numbers." Drill the latter.

**Don't:**
- lower the bar on the original task
- hint your way through the answer (that trains the learner to expect hints)
- retry the same problem repeatedly without fixing the underlying gap

**Do:**
- diagnose the specific skill
- practice that skill briefly until it's reliable
- return to the original task and clear it independently

**Preventative remediation.** If you know a learner tends to fumble a particular prerequisite, front-load extra practice on it before it becomes a blocker.

---

## Gamification

**The finding.** Points, streaks, leaderboards increase engagement and learning when they are (a) aligned with actual learning outcomes, (b) resistant to gaming.

**What works:**
- XP per minute of focused work, with bonus XP for high quality and a floor (must clear the bar to earn any).
- Streaks on spaced-repetition apps (mild social pressure to show up daily).
- Weekly leagues where you get promoted/demoted based on activity.
- Personal-best tracking and competition with a friend.

**What doesn't work:**
- Rewards for *time spent* without quality check — incentivizes XP farming and theatre.
- Rewards for *volume* without quality — learner submits sloppy attempts to rack up points.
- Leaderboards for a hobby subject without peer cohort — demotivating for adults.

**Negative penalties.** Math Academy introduces XP penalties for submitting low-effort work; without them, adversarial students rack up XP by completing easy tasks and failing hard ones on purpose. For a self-learner, the equivalent is mildly unpleasant friction on skipping sessions — telling a partner, a public commitment, a tutor.

---

## Desirable difficulties — the unifying theme

Bjork & Bjork's (2011) framing: *a desirable difficulty is a practice condition that makes the task harder, slowing the learning process yet improving recall and transfer.*

The major cognitive learning strategies — active learning, spacing, interleaving, retrieval, varied conditions — all share this property. They feel worse during practice and produce better test performance.

This is the single most important thing to communicate to a learner, because it runs against their intuition. They will want to reread because it feels productive. They will want to block-practice because it feels fluent. They will want to review right after learning because their score is high. Every one of those preferences points the wrong way.

The flip side: desirable difficulties only help *insofar as the learner can overcome them*. An insurmountable difficulty is not desirable. If the learner is completely stuck, that's a scaffolding problem — add scaffolding (smaller steps, worked examples, prerequisite drill), don't pile on more difficulty. Once the learner can reliably succeed, the difficulties belong back in.

**Bjork & Bjork (2023):** *"It is necessary to consider what level of difficulty is appropriate in order for that level to enhance a given student's learning, and the appropriate level that is optimal may vary considerably based on a student's background and prior level of knowledge."*

# Linear Algebra for ML — a 12-week plan you can actually run

You're in a great spot for this. You already have the hardest thing: a concrete "I want to read a paper and not bounce off the math" target. Everything below is built around that. Before the plan, three quick things I'm going to assume — correct me if any are wrong and I'll adjust:

- **Your real target is linear algebra first, then a thin layer of ML math on top.** The wall you keep hitting in papers is mostly LA (matrix shapes, decompositions, eigenstuff, projections), with a bit of multivariable calc (gradients, Jacobians) and probability. If we nail LA, most papers open up immediately. Calc/prob get smaller follow-on plans.
- **"Read a paper and follow the math" and "write informed NumPy" are the same skill expressed two ways.** Both require fluency, not just recognition. That's what sets the bar for this plan — you need to be able to *produce*, not just *nod along*.
- **You're in stage 2 of the talent-development arc, not stage 1.** You have a concrete external goal (ML career move), which means we go straight to deliberate practice. No "explore gently and see what sticks" — you have a target and time is linear.

If anything there is off (e.g., you actually want the *theory* of LA for its own sake, or you're aiming at a specific subfield like optimization or graph neural nets), tell me and I'll retune.

---

## Goal

**By week 12**: you can independently work the problem sets in Gilbert Strang's *Introduction to Linear Algebra* through Chapter 7 (eigenvalues + SVD), and you can implement a small neural network from scratch in NumPy — explaining every matrix operation in terms of shapes, transformations, and what's geometrically happening — without copying from Stack Overflow. At that point, when you open an ML paper, the linear-algebra sections read like pseudocode, not hieroglyphics.

Concrete test I want you to be able to pass at week 12: pick any recent paper from arXiv's cs.LG that uses SVD, low-rank decomposition, or attention, and be able to (a) annotate every matrix shape in the first math section, (b) explain in one paragraph what each decomposition is doing and why, and (c) write a 30-line NumPy sketch that reproduces the key operation. You won't understand the *ML ideas* from LA alone, but the math will stop being the blocker.

---

## Starting point (my best guess — verify in week 0)

Based on your description:
- **Solid**: general math maturity, programming fluency, basic derivatives, the ability to manipulate symbols.
- **Shaky or partial**: matrix multiplication (probably mechanical, no geometric intuition), dot products and norms (vague).
- **Missing**: vector spaces, linear transformations as the *meaning* of matrices, rank/null space/column space, orthogonality and projections, eigenvalues as anything more than a word, SVD entirely, the chain rule in multiple dimensions (needed later for backprop).

**Do this before Monday (30 min diagnostic):** Open Strang Chapter 1 and Chapter 2 and try problems 1.2.5, 1.3.1, 2.2.7, 2.3.8 cold, no notes. Score yourself honestly: "solved independently," "got partway but stuck," or "couldn't start." If you ace Ch. 1 and stumble on Ch. 2, your frontier is Ch. 2. If you struggle on Ch. 1, start there. This one diagnostic will save you two weeks of mis-pointed work.

---

## Phased roadmap (12 weeks, ~45 min weekdays + ~75 min one weekend day ≈ 5 hrs/week)

Phases are 2–3 weeks each so you hit a visible milestone often. Topics are roughly mapped to Strang chapters; adjust if your diagnostic moves the starting line.

| Phase | Weeks | Focus | Rough Strang chapters | Milestone |
|---|---|---|---|---|
| 1 | 1–2 | Vectors, dot product, norms, geometric intuition. **Re-ground matrix multiplication as linear combinations of columns.** | 1.1–1.3, 2.1 | Explain in writing: "matrix × vector" as a linear combination of columns. Solve 15 cold problems from Ch. 1. |
| 2 | 3–5 | Matrices as linear transformations. Matrix-matrix product as composition. Gaussian elimination, LU, inverses. | 2.2–2.6 | Implement Gaussian elimination from scratch in NumPy; solve a 4×4 system without calling `np.linalg.solve`. |
| 3 | 6–7 | The four fundamental subspaces: column space, null space, row space, left null. Rank, independence, basis, dimension. | 3.1–3.5 | Given a 5×7 matrix, find a basis for each of its 4 subspaces by hand, then verify in NumPy. |
| 4 | 8–9 | Orthogonality, projections, Gram–Schmidt, QR. Least squares. | 4.1–4.4 | Implement least-squares regression from scratch (not `np.linalg.lstsq`) and compare to it on a toy dataset. |
| 5 | 10–11 | Determinants (brief), eigenvalues, eigenvectors, diagonalization, symmetric matrices, positive definiteness. | 5.1–5.3, 6.1–6.5 | Hand-diagonalize a 3×3 symmetric matrix; explain PCA as "eigendecomposition of the covariance matrix" in plain English with shape annotations. |
| 6 | 12 | SVD. Project. | 7.1–7.4 | **Capstone**: implement a 2-layer NN for MNIST from scratch in NumPy, with shape comments on every line. Plus: read one recent ML paper of your choice and write a 1-page annotation of its math section. |

You will notice I'm not sending you on a tour of "all the ML math" — no calc, no probability, no information theory. That's intentional. LA is the bottleneck for reading papers; the other topics are narrower and lighter. After week 12, if you want, there's a natural ~4-week add-on plan for multivariable calc (gradients, Jacobians, chain rule) and a ~3-week one for the probability you actually need. Those slot cleanly on top of LA. Don't do them in parallel — you'll split focus and learn both half as well.

---

## Daily session template (45 min, weekdays)

Run this exact shape every weekday. The minute allocations matter — they're calibrated for how cognitive load actually works, not how studying feels like it should go.

- **0–8 min — Spaced-review warm-up.** Pull out a previous topic's problem (whatever's due in your review queue — see below). Do it cold, no notes. Check. If you miss it, re-queue it with a shorter interval. This is the most important 8 minutes of your day and the one you'll most want to skip when busy. **Don't skip it.**

- **8–32 min — New learning + active production on the frontier (the main block).**
  - Read the current Strang section for ≤8 minutes. Stop when you understand the *idea* and have seen one worked example. Do not keep reading.
  - Attempt 4–8 exercises from the section cold. Check each as you go against the odd-numbered solutions. If you get stuck on one for more than ~6 minutes, stop: that means a prerequisite is shaky, not that you're bad at the current topic. Back up, drill the weak component for 10 minutes, then return.
  - Target: roughly 3× as much time producing (solving) as consuming (reading). If you notice you've been reading for 15 minutes without producing anything, you're in passive mode — close the book and attempt a problem even if you feel unready.

- **32–42 min — Interleaved mixed practice.** 3–5 problems sampled from *earlier* chapters, not today's. Deliberately mixed so your brain has to figure out *which* technique applies before applying it. This will feel harder and worse than today's problems. That's the point — interleaving roughly doubles long-term retention compared to blocked practice. Keep a small index-card stack or a text file with old problems by chapter; draw randomly.

- **42–45 min — Quick retrieval quiz.** Write one conceptual question in a notes file ("What does column space mean? What does rank 3 tell you about a 5×4 matrix?") and answer from memory on paper. Check against the book. This is where concept-level fluency gets built — the thing papers actually need.

**Ratios inside the session**: ~15% passive intake, ~65% active production on new material, ~20% review + interleaving + retrieval. Drift toward less passive intake as weeks go on.

## Weekend session (75 min, one day)

- **0–10 min**: Catch up on any overdue spaced reviews.
- **10–55 min**: Weekly "mixed-practice exam." 12–15 problems sampled across *all chapters so far*, no notes, untimed at first and timed once you're accurate. This is your weekly-ish retrieval test and it is load-bearing — it's what catches drift the daily sessions miss.
- **55–75 min**: NumPy session. Take the concept from this week (matrix multiplication, solving systems, projection, eigendecomposition, etc.) and implement it from scratch in NumPy, then verify against the library function. This is where "read a paper" starts to become "write numpy" — the bridge is built on weekends, not weekdays.

Total: ~5 hours/week of focused work. That's plenty. Do not increase volume — increase intensity of attention per minute.

---

## Resources (one primary, one support, one sanity-check — that's it)

- **Primary: Gilbert Strang, *Introduction to Linear Algebra*, 6th edition.** Solutions to odd problems are in the back — this is essential because you need fast feedback. Pair with his MIT OpenCourseWare video lectures (18.06) *only* when a section feels thin, ≤10 min per watch. Strang is unusually good at the geometric intuition you specifically need for ML.

- **Support: 3Blue1Brown's *Essence of Linear Algebra* video series.** Use it strictly for intuition priming on topics where you want the geometry before the algebra — especially weeks 1–2 (vectors, linear combinations), week 6 (four subspaces), weeks 10–11 (eigenstuff), week 12 (SVD). Rules: ≤10 min/day on these, and **only after you've done the day's problems**, not before. They're rewarding and feel productive; that's exactly why they'll eat your time if you let them.

- **NumPy sanity-check: a Jupyter notebook you keep open.** Every concept you learn symbolically, verify computationally. Learn about `np.linalg` by reimplementing pieces of it and comparing. This is how "paper math" fuses with "numpy code" in your head.

Resist the urge to collect more resources. A pile of 8 bookmarks is not 8× better than 1 book — it's worse than 1 book, because you'll keep switching. If Strang genuinely doesn't click after week 2 (not "feels hard" — *genuinely doesn't click*), swap to Axler's *Linear Algebra Done Right* or Hefferon's free *Linear Algebra*. Don't swap on week 1; week 1 feeling hard is not a resource problem.

---

## Feedback and assessment

- **Immediate**: every problem gets checked against solutions within seconds of finishing. Non-negotiable.
- **Miss log**: keep a plain text file `misses.md`. Every wrong problem gets one line: the problem, the chapter, and — critically — *the underlying skill that was weak*. Not "I got problem 3.2.7 wrong," but "I confused column space with row space when transposed." Each Monday, review the week's miss log and re-queue those specific skills for extra practice.
- **Weekly retrieval exam** (weekend, above): 12–15 mixed problems, no notes. Track score. If you drop below ~70%, the previous week's material was declared mastered too early — go back and re-drill.
- **Phase milestones** (end of each phase, per table above): specific tasks that test integration, not just recognition. If you can't do the milestone without hints, the phase isn't done. Add a remedial week before advancing.
- **Spaced-review queue**: simplest thing works — a text file with problem IDs and next-due dates. Intervals I'd use: after first solving, review in 1 day, then 3, then 7, then 16, then 30. Each successful review extends the next interval; each miss resets to 1 day. You don't need Anki for this, but if you already use it, Anki works fine.

---

## Accountability — pick one now, don't skip this

You said "no hard deadline," and "motivated to switch into ML." Both are true and both are predictive: adults doing a months-long plan purely from internal drive fizzle out around week 4–6 about 70% of the time. Not because they're undisciplined — because motivation is a *feeling* that fluctuates, and the plan needs a structure that doesn't. Pick at least one of these before Monday:

1. **Best — a recurring human check-in (weekly or biweekly).** Options: a tutor on a platform like Wyzant or Preply ($30–60/hr; one hour every 2 weeks is enough), a more senior ML engineer at your company willing to check your work over coffee, or a study partner doing the same plan. A 30-minute weekly chat where you have to *produce* something is worth more than any other single addition.

2. **Second-best — a pre-committed forcing function.** Sign up to give a 20-min internal talk at your company in week 13 on "linear algebra for ML practitioners," or commit to shipping a public blog post + github repo for your week-12 NN-from-scratch project on a specific date. The date has to be public and immovable; "end of spring" is too soft.

3. **Baseline — a public streak.** Post a daily "day N / 60" tweet or Slack message in a relevant channel. Works through loss aversion (breaking a visible streak hurts more than private failure) but only as a consistency floor, not a quality measure.

Rank order: human check-in > forcing function > streak. If cost is the blocker on (1), a study partner via an ML Discord or r/learnmath is free and works reasonably well. **Do not leave this as a "maybe I'll find an accountability thing later."** Decide this week.

---

## Pivot signals — when to change the plan, not grind on it

A plan is a hypothesis. These specific signals mean it needs adjusting:

- **You miss two milestones in a row.** Something structural is off — pacing too fast, foundations too shaky, or bar set where it can't be hit. Fix: insert a remediation week that revisits the last milestone's weakest skills with worked examples and smaller steps.
- **You're hitting fewer than 3 sessions/week for 2 weeks running.** The plan is aspirational, not real. Fix: cut daily target to 25 min, rebuild the habit for a week, then climb back. Don't pretend you're on a 5-day/week plan when you're not.
- **Your weekly retrieval exam score is dropping or your review queue is growing.** You're learning faster than you're retaining. Fix: reduce new topics per week by half; spend the recovered time on retrieval and interleaved practice. This is the most common failure mode and the easiest to miss.
- **You're clearing milestones but it's not translating to paper-reading ability.** The curriculum is pointed slightly wrong. Fix: add a weekly "read one ML paper abstract + intro, translate the math" session in place of one weekday session. Let actual papers re-point your priorities.
- **You dread sessions + previously-easy material feels hard**. That's burnout, not bar-too-high. Fix: 3–7 days fully off, then restart at half the daily load for a week. Not optional — pushing through here makes it much worse.

---

## Anti-patterns I'd watch for specifically (you, software engineer, ML-curious)

- **3Blue1Brown binge-mode.** It's genuinely excellent and genuinely addictive. Watching 40 minutes of Grant Sanderson feels like learning, but it's mostly passive. Cap: 10 min/day, *after* the day's problems, never before. Strang first, Grant as dessert.
- **"Implementing it" as a substitute for solving problems by hand.** As an engineer, you'll want to skip the pencil-and-paper stuff and go straight to NumPy. Resist: the hand computation is where you build the geometric mental model, which is exactly the thing that makes papers readable later. NumPy is for weekends.
- **Treating blocked practice as more productive because you feel fluent.** Doing 10 problems of the same type in a row feels great. It also transfers poorly. The weekly interleaved exam will feel harder and your score will be lower. That's the correct signal, not a bad one.
- **Copying from Stack Overflow / asking Claude instead of attempting cold.** The exact habit you want to break for NumPy. When you're tempted to ask, first write down *in English* what operation you think you need, then try to sketch it, *then* check. Using LLMs to explain afterward is fine; using them to generate the solution before you've produced one short-circuits the learning.
- **Skipping spaced review when busy.** Decay is silent. The 8-minute warm-up is what converts this from "I studied LA for 3 months" into "I know LA." Missing two warm-ups in a week is fine; missing ten in a month is how everything evaporates.
- **"I'll just spend this week patching my calculus before starting LA."** Don't. You have enough calc to start LA. Patch calc (and prob) when they specifically block ML work, not preemptively. Momentum matters.
- **Reading one more book before starting.** You know enough to start Monday. Start Monday.

---

## On the feel

The plan will feel harder and slower than "read a textbook" or "watch a course" for the first 2–3 weeks. You will solve fewer problems per hour than you think you should. Interleaved practice will make you feel dumber than blocked practice does. You'll make mistakes on problems you thought you understood. **All of that is the plan working correctly, not evidence of a problem.** The payoff — the thing you're optimizing for — shows up on the delayed tests: around week 5–6, you'll notice that Ch. 2 material, which felt hard in week 3, is now automatic. Around week 9–10, you'll pick up an ML paper casually and realize the LA part just... read. That's when you'll know it worked.

If week 3 feels bad, that's the plan. If week 3 feels easy and great, the plan is too soft and you need to raise the bar.

One last note: this plan is *ruthless about depth over breadth*. You'll feel, periodically, like you should be learning "more stuff" — probability, information theory, optimization, PyTorch, etc. You shouldn't. Twelve weeks of genuinely fluent linear algebra is worth more than two years of skimmed-everything. The frontier is narrower than it looks; go forward, not sideways.

Good luck. Tell me what your diagnostic scores look like after this weekend and we can tune the starting phase.

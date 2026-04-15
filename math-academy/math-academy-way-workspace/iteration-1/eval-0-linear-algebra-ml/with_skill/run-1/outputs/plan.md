# A plan for linear algebra, aimed at reading ML papers

You're in a good spot to do this, better than you probably think. You have 10+ years of engineering discipline, you already read dense technical material for a living, and numpy is already in your muscle memory as a tool — it just isn't yet connected to the math it's implementing. That connection is what we're going to build. The math is actually small; it's the *fluency* that takes time.

Before the plan, a few assumptions I'm making — call any of these out if they're wrong and I'll adjust:

- You want linear algebra first, not calculus review first. That's the right call for ML: matrix-level LA unblocks far more papers than single-variable calc review does, and the calculus that shows up in ML (gradients, chain rule) is mostly multivariable and is easier to pick up *after* LA, not before.
- You don't need proof-heavy pure-math LA. You want the computational and geometric fluency that lets you read equations with matrices, tensors, decompositions, and projections in them. (If you later find you want the proof side, that's an easy extension; it is not the limiting factor for ML papers.)
- ~45 min weekdays and ~90 min on one weekend day is your real budget. I'll design for ~45 min × 5 + ~90 min × 1 = ~315 min/week, with one full rest day. Consistency matters more than volume; a missed day is fine, a missed week is what kills these plans.
- You're willing to write things out on paper. Not calligraphy — just scratch work, because retrieval from memory is the single biggest lever in this plan, and you can't run it if you're typing everything into a notebook with the answer six inches away.

---

## The goal, concretely

By **week 10–12**, you can:

1. Open a recent ML paper (something like the original Transformer paper, or an ICML paper on matrix factorization) and follow the linear algebra without stalling — know what every matrix shape means, what the decompositions are doing, why the dimensions match.
2. Write numpy code for a small ML algorithm (a linear regression via the normal equations, PCA from scratch via SVD, a 2-layer neural net) where you can justify each matrix operation in one sentence and predict every shape before you run it.
3. Work through problems in Strang's *Introduction to Linear Algebra* through eigenvalues and SVD (chapters 1–7) independently, getting the odd-numbered problems right reliably without peeking.

If you hit those, the math section of papers has stopped blocking you. You are not done with math for ML at that point — multivariable calculus and a bit of probability come next — but you've cleared the biggest wall and the rest is incremental.

---

## Starting point (best guess — correct me if wrong)

- **Solid:** basic algebra, function manipulation, general math literacy, sigma/pi notation, basic derivatives (enough to not panic at `d/dx`). Strong programming, strong numpy as a *tool*.
- **Shaky:** geometric intuition for vectors and matrices, why matrix multiplication is defined the way it is, what "linear" actually means, anything involving vector spaces / rank / basis.
- **Unknown / missing:** determinants beyond 2×2, eigenvalues, eigenvectors, diagonalization, orthogonality, projections, SVD. Anything with "space" in the name probably feels like jargon.

This is exactly the right starting point for Strang. You are not missing anything that blocks you from starting immediately.

---

## The primary resource

**Gilbert Strang, *Introduction to Linear Algebra*, 6th edition.** This is the book. Reasons:

- It has solutions to odd-numbered problems at the back, which means you get immediate feedback on every attempt. This is non-negotiable for self-study.
- Strang's ordering is unusual and *good*: he introduces the column-picture of matrix multiplication (matrix × vector = linear combination of columns) before the row-picture. This is the single most important mental shift for reading ML — everyone who "gets" LA has internalized this, and everyone who's stuck on matrix ops hasn't.
- MIT OCW has his full lecture series (18.06) free, aligned chapter-by-chapter, if you want an instructor voice on a topic that's not clicking. Use sparingly — see anti-patterns below.

**One secondary, strictly capped:** 3Blue1Brown's *Essence of Linear Algebra* (YouTube, ~3 hours total). Watch one episode on the Saturday of the week you're studying the matching topic, as a prime. **Do not binge it.** It is a dessert, not a meal.

That's it. No Coursera, no Khan, no five-tab Linear Algebra Done Right side quest. One book, one video supplement, one notebook. Hoarding resources is procrastination with extra steps.

---

## Phased roadmap (~11 weeks, built to flex)

Each phase ends with a milestone check. If you're not there, you extend the phase — you do not "kind of move on." The bar is the same; the pace is yours.

**Phase 1 (Weeks 1–2): Vectors and the column picture.** Strang ch. 1. Dot product, length, angle, linear combinations. By the end: you can explain why `Ax` is "a linear combination of the columns of A, weighted by x" to a rubber duck, without notes.

**Phase 2 (Weeks 3–5): Matrices as operations; solving Ax=b.** Strang ch. 2–3. Gaussian elimination, LU, inverses, nullspace and column space, rank. By the end: given a small matrix, you can state its rank, its column space, its null space, and draw the solution set of Ax=b — from memory, not from recipe.

**Phase 3 (Weeks 6–7): Orthogonality and projection.** Strang ch. 4. Orthogonal vectors, projections, least squares, Gram-Schmidt, QR. By the end: you can explain least-squares regression as "project b onto the column space of A" and write the numpy for it from scratch.

**Phase 4 (Weeks 8–9): Determinants and eigenvalues.** Strang ch. 5–6. Eigenvalues, eigenvectors, diagonalization, symmetric matrices. By the end: you can compute eigenvalues of a 2×2 or 3×3 matrix by hand, explain what diagonalization is doing geometrically, and say in one breath why symmetric matrices have real eigenvalues and orthogonal eigenvectors.

**Phase 5 (Weeks 10–11): SVD and the synthesis.** Strang ch. 7. SVD, connection to eigenvalues of A^T A, low-rank approximation, PCA. This is the payoff chapter — every ML technique that shows up as a decomposition traces back here.

**Milestone project (end of week 11 or rolled into week 12):** implement, from scratch in numpy:
1. PCA on a small dataset, using SVD (not `sklearn.decomposition.PCA`).
2. Linear regression via the normal equations AND via QR.
3. A 2-layer neural net on MNIST, with shape comments on every line explaining what each matrix is and why the multiplication works.

Then pick one recent ML paper with matrix-heavy notation and read its first three pages aloud to yourself, pausing to restate each equation in plain English. That's your "am I actually there" test.

A month in (end of week 4), you should already be visibly more comfortable — Phase 2 gets you to rank and null space, which is when LA starts *feeling* like a thing with shape, not a bag of recipes. That's the "real progress within a month or two" marker.

---

## The daily session template (45 min weekday)

This is the shape. The specific minute allocations matter less than the fact that every single block is there, every single day.

**0–7 min — Warm-up retrieval (spaced review).** Open yesterday's notebook/paper. Look at the *problem statements only* of three problems you already solved — one from yesterday, one from ~4 days ago, one from ~2 weeks ago (or the oldest solved problem if you're not there yet). Re-solve them from memory on paper. Check. **No peeking at old solutions until you've tried.** This is the engine — it is where the retention comes from. If you skip one block in this plan, do not skip this one.

**7–15 min — Read the next section.** Strang, max 8 minutes, max a few pages. If you're past 10 minutes and still reading, stop — you're consuming when you should be producing. Worked examples are part of the reading; work them on paper alongside Strang, don't just watch his eyes move.

**15–35 min — Produce.** Do 5–8 problems from that section, cold, on paper. For each one: attempt, check against the solutions, and if you got it wrong, **do not just read the solution** — close the book, re-solve the problem from scratch, and only re-open if truly stuck. Write a one-line note for each miss: *which specific skill failed*, not "got problem 2.3 wrong." ("Forgot that columns of elimination matrices come from the rows of E" is a skill note. "Missed 2.3" is useless.)

**35–43 min — Interleaved mixed practice.** 3–5 problems sampled from *any previous chapter you've done*. Not today's topic. The point is to force you to ask "wait, which tool is this?" — which is the exact question you're currently bad at and need to get good at. Rotate which chapters you sample from. This will feel harder and slower than the preceding block. It's supposed to.

**43–45 min — Retrieval quiz.** Write down, from memory, the answer to one conceptual question like: "what does it mean for a matrix to have rank 2?" or "why is A^T A always symmetric?" No notes, one sentence, on paper. Then check. These become your vocabulary for reading papers.

**Rough ratios:** ~15–20% reading, ~55–60% producing new problems, ~20–25% review + interleaving + retrieval. That's the engine. Adjust the absolute minutes if you run over on one block, but hold the ratios.

## Weekend long session (~90 min)

**0–15 min — Extended retrieval.** A mixed batch of 8–12 problems sampled from across the whole course so far, no notes, timed loosely. This is your weekly sanity check on what's actually stuck.
**15–25 min — 3Blue1Brown.** The episode matching this week's topic. Intuition prime only.
**25–75 min — Deeper new-learning block.** Tackle a harder subsection Strang flags as "challenge," or a proof you skipped during the week. This is where you go a level deeper on something that felt wobbly.
**75–90 min — numpy session.** Reimplement in numpy whatever you studied this week, with shape annotations. E.g., after the projection chapter: write `project(b, A)` from scratch and verify it matches numpy's least squares solver. **This is the bridge between the math and your day job.** Do not skip it — this is the thing that will, more than anything, make your numpy code stop feeling like copied-from-SO.

---

## Feedback and assessment loop

- **Per problem:** solutions manual is your grader. Seconds of feedback delay. Mandatory.
- **Misses file:** one running text file, `misses.md`. Every wrong answer produces one line naming the underlying skill. Once a week, scan this file and pick the three most common skills missed — those become the seed problems for next week's warm-up retrievals.
- **End of each week (part of the weekend session):** the 8–12 problem mixed quiz above. If you miss >30%, you don't advance — you spend a few days on the missed skills, then retry.
- **End of each phase (every 2 weeks ish):** cumulative problem set from across the phase, no notes, untimed. Track how many you get first-try correct. This is your signal that mastery is real, not "I saw it."
- **End of week 11:** the milestone numpy project above.

On the bar: when (not if) a topic feels stuck, the fix is *never* to lower the standard and move on. The fix is to go down one level — find the specific prerequisite skill that's shaky, drill it for a session or two, then come back and clear the original bar cleanly. "Kind of got it" is the single most common reason self-study plans crack by month three; everything built on a shaky foundation will wobble.

---

## Anti-patterns specifically tailored to you

You've been coding for a decade and you have adult-engineer learning habits. Some of them will hurt you here. Named so you can catch yourself:

- **"I'll just read Strang cover-to-cover first, then do problems."** You won't. And even if you did, you would retain ~15% of it. Reading LA without producing is like reading about code without running it. The producing is where the learning *happens*. If you notice you've been reading for 15+ minutes without writing anything on paper, stop and do problems now.
- **Reaching for 3Blue1Brown when a topic feels hard.** Grant's videos are wonderful and *will make you feel like you understood it*. That feeling is familiarity, not recall. Use him once a week for priming, not for rescue. If you need rescue, the answer is smaller-granularity problems, not more watching.
- **Doing LA exercises in a Jupyter notebook with numpy right there.** Don't. The hand-calc part is intentional — it's what builds the mental model for why numpy does what it does. Numpy after the math, not during. (The Saturday numpy session is the exception and is explicitly *after* you've done the math by hand that week.)
- **Skipping the interleaved mixed-practice block because "today's topic is fresh, I should focus on it."** You're an engineer; you will rationalize this on busy days. It is the biggest retention lever in the plan. Non-negotiable.
- **ChatGPT / Claude shortcut.** If you hand a problem to an LLM and have it explain the answer to you, you've successfully prevented yourself from learning it. Acceptable use: after you've solved (or failed at) a problem yourself, ask an LLM to check your reasoning or sanity-check an intuition. Not-acceptable use: asking it to walk you through a worked solution to a problem you haven't seriously attempted. You are senior enough to recognize the difference; apply the same rigor you'd apply to a junior on your team copy-pasting from stackoverflow.
- **Marathon weekend, silent weekdays.** You're used to "I'll catch up on the weekend." Spaced repetition math does not forgive this. Six 45-min sessions crush one 4.5-hour session. The exponential in review intervals is on your side *only if you show up daily*.
- **Dropping spaced review "just for this week" when work gets busy.** The one thing to not drop. If a day is crushed, do 10 minutes of pure warm-up retrieval and nothing else. Zero is the only bad outcome.

---

## On how this is going to feel

For the first 2–3 weeks, this plan will feel *slower and harder* than whatever you've tried before. You'll do fewer pages per session than if you were just reading; you'll get more problems wrong than if you were doing blocked practice on today's topic only; the mixed-practice block will feel demoralizing because your recall of last week's material is patchy. **All of that is working as intended.** Cognitive science has a specific name for this — "desirable difficulties" — and the finding, repeated across dozens of studies, is that the study methods that feel most productive in the moment (rereading, blocked drilling, reviewing right after learning) produce the worst long-term retention, and the methods that feel harder and slower (retrieval without notes, interleaving topics, spaced review) produce dramatically better retention and transfer. You will be tempted, around week 2, to "streamline" the plan by dropping interleaving or spaced review. Don't. The payoff shows up around week 5–6, when material from Phase 1 is still cleanly retrievable rather than a hazy blur, and it compounds from there.

The moment you'll feel the click: somewhere around the projection / least-squares chapter (Phase 3), you'll be reading some blog post or tweet that says `β = (XᵀX)⁻¹Xᵀy` and it will just *read* to you — not as a formula to memorize, but as "project y onto the column space of X, get the coefficients out." When that happens in your head unprompted, you're over the hump. That's typically 5–7 weeks in, and it's the real signal that you've turned the corner.

Start tomorrow. Strang chapter 1, section 1.1. 45 minutes. Paper and pen. Phone out of the room.

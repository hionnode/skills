# Worked example plans

Full instantiations of the Math Academy Way workflow across several domains. Use these as templates for structure, not as the specific plan for any learner — adapt to the learner's actual starting point, time budget, and goal.

## Example 1 — Linear algebra from scratch

**Learner context.** Software engineer, 30s, comfortable with high-school algebra and basic calculus, hasn't touched linear algebra formally. Wants to be able to read ML papers without getting stuck at the math, and to reason fluently about matrix operations when implementing algorithms. 45 minutes a day, 6 days a week. No deadline, but wants visible progress within a month.

**Goal (concrete).** By week 12: can independently work through the problem sets in Strang's *Introduction to Linear Algebra* through at least chapter 6 (eigenvalues), and can reimplement from scratch a small neural network using NumPy with an informed understanding of each matrix operation.

**Starting point (frontier).** Vectors: shaky intuition. Matrix multiplication: can execute mechanically but doesn't connect to geometry. Determinants, eigenvalues, SVD: unfamiliar.

**Phased roadmap:**
- Weeks 1–2: Vectors and vector spaces. Dot product, norms, geometric interpretation.
- Weeks 3–5: Matrices as linear transformations. Matrix-vector and matrix-matrix products as compositions. Gauss elimination, LU, inverse.
- Weeks 6–7: Column/null space, rank, independence, basis, dimension.
- Weeks 8–9: Orthogonality, projections, Gram-Schmidt, QR.
- Weeks 10–11: Determinants, eigenvalues, diagonalization.
- Week 12: SVD. Milestone project.

**Daily session template (45 min):**
- 0–8 min: *Warm-up retrieval.* Previous topics' problems from memory. Start with anything due.
- 8–30 min: *New learning.* One section from primary resource. Read the section (≤10 min), then solve 5–10 exercises cold. Check each.
- 30–40 min: *Interleaved practice.* 4–6 mixed problems sampled from past chapters. Mostly previously-solved problem types, lightly scrambled.
- 40–45 min: *Quick retrieval quiz.* 3 conceptual questions from memory ("what does rank mean geometrically?") written in a notes file. Answer on paper first, then check.

**Resources (one primary, one secondary):**
- Primary: Strang, *Introduction to Linear Algebra* (6th ed.). Has solutions to odd problems, which is essential for immediate feedback.
- Secondary: 3Blue1Brown's *Essence of Linear Algebra* video series — *only* for intuition priming, ≤10 min at a time, only on topics where the textbook feels thin. Never as a substitute for problem work.

**Feedback and assessment:**
- Check every problem against the solutions. Keep a running list of misses, one line each, with the underlying skill named.
- End of each week: mixed practice set (15 problems, 20 min, no notes). Misses get re-queued for next week's warm-ups.
- End of each phase (every 2–3 weeks): cumulative problem set from across the phase.
- Week 12 milestone: reimplement a 2-layer NN for MNIST from scratch in NumPy with shape annotations and a short written justification of each matrix operation.

**Anti-patterns to watch for (this learner):**
- Will be tempted to watch more 3Blue1Brown than needed because it's fun and feels productive. Cap at 10 min/day.
- Will want to skip Strang's computational problems because they feel tedious. These build the automaticity needed to read papers later — do them.
- Will want to skip week-end mixed practice because it's harder than daily sections. This is where most of the long-term retention comes from.

**On the feel.** Weeks 1–3 will feel slower than reading a textbook linearly. The difference will show up at week 6, when previous material is still fluently retrievable rather than vague.

---

## Example 2 — Spanish conversational fluency

**Learner context.** Adult hobbyist, wants to have 30-min conversations on everyday topics with native speakers (roughly B1 on CEFR). Currently knows ~300 words, minimal grammar. 25 min/day, daily. Planned trip to Mexico in 6 months as informal deadline.

**Goal.** By month 6: hold a 30-min conversation with a native speaker about food, family, work, travel, and hobbies, with occasional hesitation but no communication breakdowns.

**Phased roadmap:**
- Months 1–2: Core vocabulary (top ~1500 words by frequency), present tense, basic sentence structure.
- Months 3–4: Past tenses, common grammatical patterns (subjunctive intro, reflexives), expand vocab to ~3000 words.
- Months 5–6: Conversational fluency focus, output practice, native-speaker exposure.

**Daily session (25 min):**
- 0–8 min: *Anki reviews.* Vocabulary and phrase cards, spaced repetition driven. Never skip.
- 8–18 min: *Active production.* Writing: compose 3 sentences about today using today's grammar point; record them. Or speaking: say out loud, record, self-correct. Or comprehensible-input-with-output: read a short paragraph, then reproduce it from memory.
- 18–25 min: *Listening + retrieval.* Podcast segment (like *Dreaming Spanish* beginner levels), stop every 1–2 minutes to summarize out loud what was said.

**Weekly (30 min extra):**
- One 25–30 min conversation with a tutor or language exchange partner on iTalki. This is the test that reveals what actually works.

**Resources:**
- Primary: Anki deck — a frequency deck (top 5000 Spanish words) plus sentence cards you build yourself from real encounters.
- Supporting: Dreaming Spanish (comprehensible input), Language Transfer (grammar scaffolding, free, exceptional pedagogy), a weekly iTalki tutor.
- Not recommended: Duolingo (too passive, gamified in ways that don't produce fluency).

**Feedback:**
- Anki gives immediate feedback on vocab via the spaced schedule.
- Tutor gives weekly feedback on output. Misses become new Anki cards.
- Self-recording gives daily feedback on pronunciation and fluency drift.

**Anti-patterns:**
- Adding too many new Anki cards per day. Cap at 10/day; backlog is the main failure mode of SRS.
- Watching videos passively. Always produce something after consuming.
- Skipping the weekly tutor because it's stressful. This is the desirable difficulty — it's the single most productive 30 minutes of the week.
- "Studying grammar" endlessly instead of producing. Grammar serves production, not the other way around.

**On the feel.** Months 1–2 will feel tedious because production is effortful and rewards are delayed. Around month 3, input starts feeling comprehensible. Around month 5, output becomes genuinely pleasant.

---

## Example 3 — Becoming a strong programmer in Rust

**Learner context.** Experienced Python developer (10 years), building a systems project at work. Needs fluency with Rust including ownership/borrow checker, async, traits. 60 min/day on weekdays, 2 hours one weekend day.

**Goal.** By month 4: can independently implement a medium-sized Rust crate (CLI tool with async I/O, error handling via `Result`, generic traits, tests) without Rust-specific questions dominating the work.

**Starting point.** Fluent general programmer. Rust-specific concepts — ownership, lifetimes, trait objects — unfamiliar. Has written "hello world."

**Phased roadmap:**
- Weeks 1–3: Core syntax, ownership, borrowing, lifetimes. The pain phase.
- Weeks 4–6: Traits, generics, error handling patterns. The "oh this is elegant" phase.
- Weeks 7–10: Standard library, iterators, async, real project.
- Weeks 11–16: Ship a real crate; contribute to an open-source Rust project.

**Daily session (60 min):**
- 0–10 min: *Retrieval warm-up.* Yesterday's exercises from memory — rewrite one function without looking. Check.
- 10–45 min: *New learning.* One chapter of primary resource. Read ≤10 min, then run every example, then attempt the exercises cold. Don't move on until they compile and run correctly.
- 45–55 min: *Mixed project work.* Apply to the real work project. Any friction becomes a note — the note becomes a targeted drill for tomorrow.
- 55–60 min: *Note day's misses.* Each compiler error you hit today: write a 1-sentence note of the underlying rule you violated, with a tiny example.

**Weekend long session (2 hrs):**
- Build or extend a small personal Rust project, any topic. Forces synthesis.

**Resources:**
- Primary: *The Rust Programming Language* ("the book"). Each chapter has exercises; do them.
- Project companion: *Rustlings* (small exercise repository that forces you to fix code).
- Secondary: *Rust for Rustaceans* (after month 2, for deeper patterns).
- The compiler is your feedback loop. It's unusually good.

**Feedback and assessment:**
- Compiler errors → daily targeted drills on the specific ownership/lifetime rule that was violated.
- Weekend project → end-to-end test of integration of the week's ideas.
- Every 3–4 weeks: revisit an earlier project and refactor with current knowledge. Reveals what's stuck and what's fading.

**Anti-patterns:**
- "I'll just fight the borrow checker until it compiles." If you've lost 30 min fighting a single ownership issue, stop — the prerequisite (mental model of ownership) is shaky. Back up to a focused exercise, then return.
- Skipping `Rustlings` because it feels basic. It builds the pattern-recognition that makes later code fluent.
- Using AI code assistants to bypass the learning. They will produce compiling code that short-circuits the ownership practice. Ask them to explain, not to write, while learning.

**On the feel.** Weeks 1–3 are famously unpleasant. Every experienced Rust programmer went through the "fighting the compiler" phase. It is not a signal that you are bad at Rust. It is the literal process by which the mental model forms.

---

## Example 4 — Learning classical piano as an adult beginner

**Learner context.** Complete beginner, adult, wants to be able to play intermediate classical pieces (Bach inventions, simple Chopin preludes) and read sheet music fluently. Owns a digital piano. 30 min/day most days, no teacher budgeted.

**Goal.** By month 12: perform a Bach 2-part invention (e.g., #1 in C) and a simple Chopin prelude (e.g., #7 in A) at tempo, musically, from memory.

**Starting point.** Can read treble clef slowly, has never played an instrument.

**Phased roadmap (long game):**
- Months 1–3: Posture, hand independence, basic scales, reading fluency, simple etudes.
- Months 4–6: Two-hand coordination, common chord progressions, easy classical pieces (Burgmüller, easier Bach).
- Months 7–9: First Bach invention piece. Slowly.
- Months 10–12: Polish the invention; add a simple prelude.

**Daily session (30 min):**
- 0–5 min: *Warm-up scales + Hanon.* A subset; rotate. Builds automaticity in finger patterns.
- 5–20 min: *Deliberate practice on the current piece.* Pick the *specific hardest 4 bars*. Play slowly (often absurdly slowly — 1/4 tempo) until perfect. Then build tempo. Do NOT play the whole piece from the top repeatedly — that's blocked, passive, and wastes time.
- 20–27 min: *Interleaved work.* Revisit a previous piece (retrieval). Or sight-read a new easy piece. Or a scale in a new key.
- 27–30 min: *Quick reflection.* Name the specific mistake the session focused on. Write it down. Tomorrow's warm-up should address it.

**Weekly:**
- One "play-through" session where you play current pieces end-to-end and record them. Listen back. Identify the worst 8 bars. Those become the next week's deliberate-practice focus.

**Resources:**
- Primary: *Alfred's Adult All-in-One Course* or *Faber Adult Piano Adventures* for first 6 months.
- Sheet music: IMSLP (free, public-domain classical scores).
- For feedback: self-recording on phone. A monthly 20-min lesson with a teacher (even once/month) catches technique drift that self-assessment misses — worth budgeting for if possible.

**Feedback:**
- Recordings are the lie detector. Playback reveals issues live playing hides.
- A once-a-month teacher check is a high-leverage accountability and technique-correction mechanism.

**Anti-patterns:**
- Playing the pieces you can already play, start to finish, repeatedly. Feels productive; is 90% passive. Replace with focused drill on the weak spot.
- Speeding up too early. Speed comes last. Most technique problems are disguised slow-practice avoidance.
- Adding too many pieces at once. Two active pieces + one review piece is plenty.
- Skipping scales because they're "boring." They are the literal automaticity builder. Skipping them makes every piece harder.

**On the feel.** Progress in piano is extremely non-linear. Weeks of plateau then a sudden unlock. Trust the process. Record monthly and compare — the progress is visible across months even when invisible across days.

---

## Template summary — what a good plan looks like

Looking across all four examples:

1. **The goal is concrete and testable.** Not "learn X"; "perform Y" or "solve problems of type Z independently."
2. **The starting point is specific.** Not "I'm a beginner"; which skills are in/out.
3. **Phases are 2–4 weeks long** with visible milestones.
4. **The daily session fits the actual time budget.** Not aspirational — realistic.
5. **The ratio of active production to passive intake is high** (≥3:1, ideally 5:1+).
6. **Spaced review is non-negotiable,** baked into every day.
7. **Interleaving shows up** at least weekly, ideally daily.
8. **Feedback is fast** — the learner knows within minutes whether they got a problem right.
9. **Anti-patterns are named,** tailored to the specific learner's likely temptations.
10. **The feel is honest** — plan warns the learner that the good phase is a few weeks in.

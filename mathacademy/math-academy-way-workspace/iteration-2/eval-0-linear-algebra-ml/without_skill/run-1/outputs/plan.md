# A Linear Algebra Plan for an ML-Curious Engineer

You're in a really common spot, and honestly a really good spot to be in: you already know how to program, you've built real systems, and you have concrete motivation (papers you actually want to read). That changes what a good plan looks like. You don't need "math from scratch." You need a targeted, paper-oriented curriculum that treats linear algebra as the core subject and grafts on the bits of calculus and probability that ML papers lean on.

Here's what I'd actually do.

## The shape of the plan

Think of this as three phases over ~8–10 weeks, at your stated pace (45 min weekdays + ~1.5h each weekend day ≈ 6–7 hours/week, ~50–60 hours total):

- **Phase 1 (weeks 1–4): Core linear algebra.** Vectors, matrices, linear systems, rank, null space, orthogonality, projections, least squares.
- **Phase 2 (weeks 5–7): The "ML layer."** Eigenvalues/eigenvectors, SVD, PSD matrices, quadratic forms, plus a shot of matrix calculus (gradients, Jacobians) and a probability refresher.
- **Phase 3 (weeks 8–10): Apply it.** Re-read an ML paper you previously bounced off of, re-derive PCA / linear regression / a simple neural net layer by hand and in numpy, and fill gaps as you find them.

You will *not* finish a textbook. That's fine. The goal is fluency with a specific toolkit, not completionism.

## Principles (these matter more than the resource list)

1. **Paper-driven, not textbook-driven.** Pick one ML paper you want to understand — say, the original *Attention Is All You Need*, or the PCA chapter of a textbook, or a diffusion / VAE paper. Every week, look at it again. Each pass you should be able to decode a bit more. That's your real progress metric.
2. **Do the exercises. Actually do them.** This is the single biggest thing that separates people who "have read about linear algebra" from people who know it. For a working engineer with 10+ years of coding, the temptation to skim is enormous and it doesn't work here. Budget at least half your time for problems.
3. **Write numpy as you learn.** Every concept should get a tiny numpy notebook: "here's what a projection matrix is, here's me building one for a random 2D vector onto a random line, here's a plot." This is your superpower over a pure math student — use it relentlessly.
4. **Learn notation early and deliberately.** Einstein summation, index notation, the shape conventions papers use (is it `Wx` or `xW`? row vectors or column vectors?). Papers skip steps that are "obvious" in notation; half of "following the math" is just fluent notation.
5. **Spaced practice beats marathons.** 45 minutes daily is actually ideal — better than a 4-hour Saturday binge. Use it.
6. **Don't chase rigor you don't need.** You do not need epsilon-delta proofs. You do need to be able to manipulate expressions confidently and know when a step is legal.

## Resources (ranked, pick, don't collect)

Pick **one** primary track and stick with it. Adding more resources is a procrastination trap.

**My recommended primary track:**

- **3Blue1Brown, *Essence of Linear Algebra*** (YouTube, ~3 hours total). Watch this in week 1, end to end. It will not teach you to compute, but it will give you the geometric intuition that makes every other resource easier. This is non-negotiable; it's that good.
- **Gilbert Strang, *Introduction to Linear Algebra* (6th ed.)** as your main textbook, paired with his MIT OCW lectures (*18.06*). Strang is ML-friendly — he treats the four fundamental subspaces, SVD, and least squares as first-class citizens, which is exactly what you need. The lectures are a comfortable complement for evenings you don't feel like reading.
  - Alternative if Strang feels too chatty: **Axler, *Linear Algebra Done Right*** is cleaner but more abstract, and deliberately avoids determinants early. Use only if you find you like proofs.

**Supplements, to dip into, not to grind:**

- **Deisenroth, Faisal, Ong, *Mathematics for Machine Learning*** (free PDF at mml-book.com). The first half is a linear algebra + calculus + probability crash course framed entirely around ML. Use it as a second angle when Strang feels disconnected from ML. Especially good chapters: 2 (linear algebra), 3 (analytic geometry), 4 (matrix decompositions), 5 (vector calculus).
- **The Matrix Cookbook** (Petersen & Pedersen, free PDF). Reference, not reading. Keep it open when you do matrix calculus derivations.
- **Goodfellow, Bengio, Courville, *Deep Learning*, Chapter 2** (free online). Short, dense ML-flavored linear algebra review. Read it at the end of Phase 1 as a self-test — if most of it lands, you're on track.

**Practice:**

- Strang's exercises first. If you want more drill: **Khan Academy's linear algebra track** is perfectly serviceable for computational fluency.
- **NumPy / PyTorch exercises.** Just reimplementing each concept in numpy is itself the practice. For structured challenges, search "numpy 100 exercises" (Nicolas Rougier's set) and the PyTorch tutorials.

Ignore everything else for now. You can always pick up Boyd's *Applied Linear Algebra* or Trefethen's *Numerical Linear Algebra* later if you end up wanting them.

## Week-by-week plan

I'll give concrete weekly targets. Adjust pacing but don't skip topics. Each week assumes ~6 hours.

### Week 1 — Intuition and vectors

- Watch all of 3Blue1Brown *Essence of Linear Algebra* (don't rush; pause and re-watch).
- Strang Ch. 1 (vectors, dot product, linear combinations).
- numpy: write functions for dot product, vector norm, angle between vectors, project `v` onto `u`. Plot some of this with matplotlib.
- **Self-test:** given two random 3-vectors, compute their angle and the projection of one onto the other, both by hand and in numpy, and get the same answer.

### Week 2 — Matrices as linear maps, and solving `Ax = b`

- Strang Ch. 2 (matrix ops, elimination, LU, inverse).
- Key mental shift: a matrix is a function that eats a vector and spits out a vector. Practice reading `Ax` as "A acts on x" rather than "a weird multiplication."
- numpy: implement Gaussian elimination yourself (small and ugly is fine), then compare to `np.linalg.solve`.
- Exercises: at least 10 problems from Strang's chapter.

### Week 3 — Vector spaces, rank, the four fundamental subspaces

- Strang Ch. 3 (column space, null space, row space, left null space).
- This is the week that makes every later paper make sense. Do not skim. "Rank" will appear in every other ML paper you read.
- numpy: take a rank-deficient matrix, compute its null space (via SVD — you'll understand why later), verify `A @ n == 0`.
- **Paper check-in:** look at your target paper. Find any place it uses the words "span," "rank," "null," "linearly independent," "low-rank." Write a sentence for each about what it means *in that context*.

### Week 4 — Orthogonality, projections, least squares

- Strang Ch. 4 (orthogonality, Gram–Schmidt, QR).
- This is where linear regression actually lives, which is a huge "oh, that's what that is" moment.
- numpy: implement linear regression three ways — `(X^T X)^{-1} X^T y`, QR decomposition, and `np.linalg.lstsq`. Verify they agree. Plot the fit.
- End of Phase 1. **Milestone:** re-read Goodfellow Ch. 2. Everything up through section 2.6 or so should feel mostly readable.

### Week 5 — Eigenvalues and eigenvectors

- Strang Ch. 6 (eigenvalues, eigenvectors, diagonalization).
- Don't just compute; understand the "stretch along special axes" picture (3B1B helps).
- numpy: take a symmetric matrix, diagonalize it, verify `A = Q Λ Q^T`. Apply `A` and `A^100` to a vector two ways and confirm they match.
- Read: MML book §4.1–4.4 for an ML-framed version of the same material.

### Week 6 — SVD

- Strang Ch. 7. Read it twice. SVD is the single most important matrix decomposition for ML.
- Understand: every matrix (not just square, not just nice) has an SVD. The singular values are the "size" of the matrix in each direction. Low-rank approximation = keep the top-k singular values.
- numpy: SVD of a small image (convert to grayscale matrix), reconstruct using top k singular values for k = 1, 5, 20, full. Plot. This is a classic exercise and it makes SVD unforgettable.
- Derive PCA from SVD in your notes. When you can do this cold, you've cleared a big hurdle.

### Week 7 — PSD matrices, quadratic forms, and matrix calculus

- Strang Ch. 6.5/Ch. 8 for positive-definite matrices and quadratic forms. These underpin covariance matrices, kernels, loss landscapes, Hessians.
- Matrix calculus: learn to differentiate `x^T A x`, `||Ax - b||^2`, `tr(AB)`, etc. Use the Matrix Cookbook as reference. Deisenroth Ch. 5 is the best teaching resource here.
- Derive the gradient of the least-squares loss by hand. Derive the gradient of a single-layer linear network. These two derivations will unlock reading most ML method sections.
- Probability mini-sprint (one sitting): multivariate Gaussian — mean vector, covariance matrix, what "diagonal covariance" means geometrically. Deisenroth Ch. 6 or 3B1B's bayes/probability videos.

### Weeks 8–10 — Apply and consolidate

You're now in the productive part. Pick two or three of these and go deep:

- **Re-read your target paper** end to end. For every equation you can't follow, stop and derive it or look up the missing piece. The gaps you find *are* your curriculum for this phase — they're more valuable than anything I could prescribe.
- **Reimplement PCA from scratch** in numpy on a real dataset (MNIST, say). Do it via SVD and via eigendecomposition of the covariance matrix. Compare.
- **Reimplement linear regression and logistic regression from scratch**, including the gradient derivations on paper.
- **Code a tiny neural network forward + backward pass** without a framework. Just matrix ops. This is where matrix calculus becomes muscle memory.
- **Optional:** Karpathy's *Neural Networks: Zero to Hero* YouTube series. By this point you'll be able to follow it with full understanding rather than vibes.

## How to actually use 45 minutes

A weekday session that works:

1. 5 min — skim yesterday's notes.
2. 20 min — new material: read one section or watch one lecture segment.
3. 15 min — do 2–3 problems or write a tiny numpy script exploring what you just read.
4. 5 min — write 3 sentences in a notebook (paper or digital): what I learned, what confused me, what to look at tomorrow.

The last step sounds silly and is the most important one. Linear algebra is full of ideas that only click after you've restated them in your own words.

On weekends, do the same but longer, and add one session where you try to connect what you learned back to the target paper or to a numpy experiment.

## How to know it's working

At 1 month in, you should be able to:

- Read a sentence like "we project the embeddings onto the top-k principal components" and picture exactly what's happening.
- Explain, without notes, what SVD does and why it's useful.
- Look at shapes in numpy code and predict what the operation does.
- Derive the least-squares solution.

At 2 months in:

- Read the methods section of a mainstream ML paper and follow ~80% of the math on first pass.
- When you write numpy, you're making deliberate choices about shapes and operations, not guessing.
- You have a short list of specific further topics you now want to learn (probability, optimization, information theory) — and you'll know which one matters for what you're trying to do.

## What *not* to do

- Don't start with Axler, Hoffman & Kunze, or any proof-heavy book unless you discover you love proofs. You can always go deeper later.
- Don't try to learn probability, statistics, optimization, and linear algebra simultaneously. Linear algebra first, with a small calculus/prob top-up. The others have natural hooks you can add after.
- Don't switch resources when you hit a hard chapter. That's the chapter that matters. Slow down, don't shop.
- Don't skip the numpy. You're an engineer — coding is how you debug understanding.
- Don't measure progress by pages read. Measure it by problems solved and by how much more of your target paper you can decode each week.

## Starting this week

Concretely, tomorrow:

1. Pick a target ML paper. Anything you've bounced off. *Attention Is All You Need* is a good default; *Auto-Encoding Variational Bayes* is a harder but rewarding one; the *Deep Residual Learning* paper is on the easier end.
2. Open it and write down every symbol or operation you can't confidently explain. Don't try to understand it yet. This is your baseline.
3. Start 3Blue1Brown's *Essence of Linear Algebra*, video 1.
4. Order or download Strang's *Introduction to Linear Algebra* and the MML book PDF.
5. Create a single directory — `linalg/` — with a notes file and a `notebooks/` folder. Everything you learn lives here.

Come back to that paper in a month and you'll be genuinely surprised. Good luck.

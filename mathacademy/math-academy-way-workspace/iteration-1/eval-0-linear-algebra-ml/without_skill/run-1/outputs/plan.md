# Linear Algebra for ML: A Practical Plan for a Working Engineer

You're in a good position. You already code for a living, you know Python, and you have a concrete motivation (reading ML papers, writing non-cargo-cult numpy). That's 80% of what makes adult math self-study work. The thing that usually fails is the curriculum — people either pick a textbook that assumes too much, or they pick a "fun" book that waves hands and leaves them unable to read a real paper. Here's a plan that threads that needle.

## The shape of the plan

You want two things:

1. **Linear algebra fluency** — operations, geometry, decompositions (especially eigendecomposition and SVD), and the intuition to read "let $X = U\Sigma V^\top$" and not flinch.
2. **Enough multivariable calculus** — gradients, Jacobians, the chain rule as it actually appears in backprop and optimization. You do NOT need to relearn integration by parts or infinite series. ML calculus is mostly derivatives in many variables.

Linear algebra is the bigger lift and the bigger payoff, so it gets the front seat. Calculus sneaks in alongside it and gets a short dedicated pass later.

Rough timeline at 45 min/weekday + ~2 hrs/weekend (~5 hrs/week):

- **Weeks 1–2**: Geometric foundations (vectors, matrices as transformations). You will feel dumb for about 4 days and then something clicks.
- **Weeks 3–4**: Linear systems, rank, null space, projections, least squares. By end of week 4 you should be able to read the first page of most ML papers.
- **Weeks 5–6**: Eigendecomposition and SVD. This is the big unlock. PCA, low-rank approximation, regularization — all of it lives here.
- **Weeks 7–8**: Multivariable calculus for ML (gradients, Jacobians, the chain rule, a taste of matrix calculus). Plus a small backprop-from-scratch project.
- **Weeks 9+**: Apply. Pick a paper a week, read it with pencil in hand, and plug the remaining holes as they surface.

Two months gets you genuinely unstuck. Three months gets you comfortable.

## The core stack (what to actually use)

Pick **one primary source** and stick with it. The biggest self-study failure mode is bouncing between six resources and finishing none. Here's the stack I'd use for your profile:

### Primary: 3Blue1Brown's *Essence of Linear Algebra* + Gilbert Strang's *Introduction to Linear Algebra* (6th ed) or MIT 18.06 lectures

- **3Blue1Brown's "Essence of Linear Algebra"** (YouTube, ~15 short videos, about 3 hours total). Watch the whole series in the first week. Don't take notes the first pass, just watch. Then rewatch with notes over the next few weeks as topics come up. This builds the geometric intuition that Strang assumes you have but never explicitly teaches. Non-negotiable.
- **Gilbert Strang's *Introduction to Linear Algebra* (6th edition)** as your textbook, OR the **MIT 18.06 OpenCourseWare lectures** (they follow the book). Strang is opinionated, he skips some formal rigor, and his pedagogy is exactly what you want: he teaches linear algebra the way someone who uses it teaches it, not the way a pure mathematician would. Chapters 1–7 cover everything you need. If you prefer reading, use the book. If you prefer watching, use the lectures — they're among the best math lectures ever recorded. I'd do both: read the chapter, then watch the lecture to cement it.

If Strang doesn't click after a couple of chapters, swap in **Sheldon Axler's *Linear Algebra Done Right*** (more abstract, determinant-last approach, better for the theoretically-minded) or **Jim Hefferon's *Linear Algebra*** (free PDF, very gentle). But start with Strang.

### Supplementary, not primary:
- ***Mathematics for Machine Learning* by Deisenroth, Faisal, Ong** (free PDF at mml-book.com). Chapters 2–5 are a crisp ML-oriented recap. Use this as a "second pass" reference after you've done Strang — it'll feel easy and consolidating, which is the point. Don't use it as your first exposure; it's too dense for that.
- **Kaare Brandt Petersen's *Matrix Cookbook*** (free PDF). Not something to read — a reference you'll come back to for matrix identities and derivatives for years. Bookmark it.
- **3Blue1Brown's "Essence of Calculus"** series — watch this when you hit the calculus weeks. Same deal as the linear algebra one.

### For the calculus piece:
- **Khan Academy's Multivariable Calculus** — skip to "Derivatives of multivariable functions." You don't need the integration units. Work through partial derivatives, gradient, directional derivative, chain rule, Jacobian. About 6–8 hours of focused work.
- **Matrix Calculus section of the MML book** (Chapter 5). This is the bit most self-taught ML people skip and then regret. Do the exercises.

### What to skip (for now):
- Any "linear algebra for computer graphics" book — different emphasis.
- Schaum's outline — fine but drill-heavy, not what you need.
- Any book titled "Linear Algebra and Its Applications" that isn't Strang — too much engineering-heavy material you don't need.
- *Deep Learning* by Goodfellow et al. Chapter 2. It's a summary, not a teacher. You'll appreciate it later as a reference.

## The weekly rhythm

This matters more than the exact resource. An hour of active engagement beats four hours of passive video-watching every time.

For each week, roughly:

- **3 weekdays (45 min each)**: Read the textbook section / watch the lecture. Work the examples BY HAND in a notebook. Actually write out the matrix multiplication. Your fingers need to learn this, not just your eyes.
- **2 weekdays (45 min each)**: Exercises from the book. Strang's problems are well-chosen — don't do all of them, do about 5–8 per section, mixing computational and conceptual.
- **Weekend (2 hrs)**: One longer session where you do a small numpy experiment. Implement what you learned from scratch using only `np.array` and basic operations — no `np.linalg.solve`, etc. Then compare to numpy's built-in. This is where the "what am I actually doing in numpy" question gets answered.

The numpy experiments are the secret sauce for your profile. Some examples:

- Week 2: Implement matrix-vector multiplication two ways (row-wise and column-wise) and convince yourself they give the same answer. Visualize a 2D linear transformation by plotting the unit square before and after.
- Week 3: Solve a least-squares problem by hand using the normal equations, then with `np.linalg.lstsq`, then verify they agree. Fit a line to noisy data.
- Week 4: Implement Gram-Schmidt. Project a vector onto a subspace.
- Week 5: Power iteration to find the dominant eigenvector. Compare to `np.linalg.eig`.
- Week 6: Implement SVD-based image compression. Take a grayscale photo, do SVD, reconstruct using the top k singular values, watch the image degrade gracefully as k shrinks. This is the single most satisfying exercise in the curriculum — do it.
- Week 7: Implement PCA from scratch on a small dataset. Check against sklearn.
- Week 8: Build a two-layer neural network, implement backprop by hand (no autograd), train it on MNIST. This forces everything to come together.

## A more concrete week-by-week

**Week 1 — Vectors and matrices as objects.** Watch all of 3Blue1Brown's Essence of Linear Algebra (first pass, no notes). Strang Ch. 1. Basic vector operations, linear combinations, dot product, the geometric picture. By Friday you should be able to explain, in plain English, why a dot product relates to angle and projection.

**Week 2 — Matrices as linear transformations.** Strang Ch. 2. Matrix multiplication as composition of transformations (this is the key reframing). The four interpretations of Ax=b (row picture, column picture, matrix picture, linear combination picture). Elimination.

**Week 3 — Vector spaces, rank, null space.** Strang Ch. 3. Column space, row space, null space, and the rank-nullity theorem. This is where a lot of "the matrix is singular" errors in numpy suddenly make sense. Independence, basis, dimension.

**Week 4 — Orthogonality and projections.** Strang Ch. 4. Orthogonal projections, Gram-Schmidt, QR. Least squares. If you've ever wondered what `np.linalg.lstsq` is doing, it's this chapter. Do the least-squares numpy exercise this weekend.

**Week 5 — Determinants, then eigenvalues/eigenvectors.** Strang Ch. 5 and 6. Determinants you can skim — understand what they mean geometrically (signed volume scaling) and move on. Eigenvalues are the point. What they mean. How to compute them for small matrices. Diagonalization. Why diagonalization matters (powers of matrices, stability, PCA).

**Week 6 — SVD.** Strang Ch. 7. The most important decomposition in applied linear algebra. Geometric interpretation (rotate, stretch, rotate). Relationship to eigendecomposition of $A^\top A$. Low-rank approximation (Eckart-Young). Pseudoinverse. Do the image compression exercise.

**Week 7 — Multivariable calculus, ML flavor.** Khan Academy multivariable derivatives unit. Gradients. Jacobians. Hessian (know what it is, don't sweat computing them). The multivariate chain rule. Read MML Chapter 5 on matrix calculus — specifically derivatives of scalar-by-vector and scalar-by-matrix. Work a few examples like $\nabla_x (x^\top A x)$.

**Week 8 — Synthesis.** Backprop from scratch. Re-read MML Chapters 2–5 as a consolidation pass — it should feel almost obvious now. Pick an ML paper you wanted to read two months ago and try again. You'll be shocked how far you've come.

**Week 9+ — Applied.** Paper a week. Keep the Matrix Cookbook open. When you hit something you don't understand, that's your next topic. Probability and statistics are the natural next lift after this, but that's a separate plan.

## A few pieces of tactical advice

- **Write by hand.** I know, you're an engineer, you want to type. But linear algebra especially is a notational subject — you need to fluently write matrix products, transposes, summation notation, until your hand does it without thinking. Get a notebook. Actually use it.
- **Do fewer exercises, but do them completely.** Five problems worked end-to-end with you checking your own work beats twenty problems half-done. When you get a problem wrong, don't just look at the answer — figure out which step of your reasoning broke.
- **When you're stuck for more than 15 minutes, look it up, then redo the problem from scratch the next day without looking.** Struggle is productive, but grinding on the same thing for an hour isn't. The re-attempt the next day is what cements it.
- **Resist the urge to jump to "cooler" material.** You will be tempted to skip ahead to tensors or transformers or whatever. Don't. The stuff that stops you in papers is almost always basic — a projection, a decomposition, a gradient — dressed up in notation. Get the foundation tight and the "advanced" stuff mostly evaporates.
- **Keep a "questions" file.** Every time you read something and don't fully get it, jot it down with the date. Review it every two weeks. You'll find most questions from two weeks ago now have obvious answers, which is both encouraging and a useful signal of what's actually still open.
- **The first two weeks are the hardest.** You're going to feel slow and stupid, especially after 10+ years of feeling competent in your day job. This is normal and it passes. Around week 3 you'll start noticing the notation actually parses. By week 5 or 6 you'll have moments of "oh, that's what PCA is actually doing" that make the whole thing worth it.

## What "progress" looks like in a month

By the end of week 4 you should be able to:
- Read a line like "we project $y$ onto the column space of $X$" and picture what's happening.
- Look at numpy code involving `@`, `.T`, `np.linalg.solve`, `np.linalg.lstsq`, and know not just what they do but why you'd reach for each one.
- Understand why `A.T @ A` shows up everywhere.
- Read the first 2–3 pages of an ML paper and follow the setup, even if the novel contribution is still over your head.

By the end of week 8 you should be able to:
- Read "we perform SVD on the weight matrix and keep the top-k components" and know exactly what's happening and why.
- Derive the gradient of a simple loss function.
- Recognize eigendecomposition, SVD, projections, and least squares when they show up in disguised form in a paper.
- Write numpy code from a mathematical description, not from a stackoverflow answer.

That's a realistic ceiling for two months at 5 hrs/week and it's genuinely enough to unlock most modern ML reading. Beyond that, it's a matter of accumulating probability/statistics and ML-specific ideas on top of this base — but those are much easier lifts once the linear algebra is solid.

## Start today

Here's your first three days, so you don't have to plan them:

1. **Today**: Watch 3Blue1Brown's Essence of Linear Algebra videos 1–4. Don't take notes. Just watch.
2. **Tomorrow**: Watch videos 5–10 of the same series. Order a physical copy of Strang's *Introduction to Linear Algebra* (6th ed) or find the PDF, and bookmark MIT 18.06 on OCW.
3. **Day 3**: Finish the Essence series. Open Strang Chapter 1. Read section 1.1, work the first five exercises by hand, check your answers.

From there, follow the rhythm. Adjust as you go — this is a plan, not a contract. Good luck.

---
name: dabba-linkedin-360brew
description: Write LinkedIn posts optimized for LinkedIn's 360Brew algorithm — the 150B-parameter LLM ranking system rolled out 2024-2026 that replaced engagement-signal ranking with semantic relevance. Use this skill whenever the user asks to draft a LinkedIn post, edit an existing LinkedIn draft, plan a LinkedIn content series, turn an idea/insight/story into LinkedIn content, or asks how to "go viral" / "get reach" / "perform" / "stop losing reach" on LinkedIn — even if they don't say 360Brew by name. Also use it when the user shares a thought and asks "should I post this on LinkedIn", or vents about LinkedIn reach drops in 2025-2026. Do not use for Twitter/X, Threads, Bluesky, or other platforms — 360Brew is LinkedIn-specific.
---

# Writing for the 360Brew era

LinkedIn replaced its engagement-signal feed ranking with **360Brew**, a 150B-parameter decoder-only foundation model (built on Mixtral 8x22B, paper: arXiv 2501.16450). It rolled out gradually from summer 2024 and is now fully active across feed, jobs, People-You-May-Know, and most surfaces.

The shift in plain language: 360Brew **reads** each post like a person would, cross-references it against the author's profile and last ~2-3 months of activity and the reader's interest graph, and decides relevance from semantic match — not from "this got likes before, show it to more people."

That breaks most of the pre-2024 LinkedIn playbook. The instructions below encode what now works.

## The 7 levers that move distribution

These are roughly ranked. The top three are non-negotiable; below that is taste.

### 1. Profile–post semantic alignment (most important)

360Brew embeds the post and the profile and penalizes large embedding distance. If the user's headline says "B2B SaaS GTM" and they post about backyard chickens, distribution collapses — not because chickens are bad, but because the system reads it as off-lane noise and demotes it.

Before drafting, **establish the user's stated lane**:

- If their profile or headline is in the conversation, read it.
- If not, ask once: "What does your LinkedIn headline say, and what 2-3 topics do you want to be known for?"
- Every post should be unmistakably *of* one of those topics. Tangential is fine; off-topic is a tax.

If the user insists on an off-topic post, deliver it but flag the cost: "This will read as off-lane against your '<their stated lane>' positioning — likely suppressed. Worth posting on a personal account or skipping?"

### 2. Topical consistency (the 80/20/3 pattern)

The model needs *repeated* signal that this account is about X to confidently route X-readers to it. Aim for **80% of posts within 2-3 core topics for at least 3 months**. When drafting, default to one of those topics. If the user proposes a one-off detour, surface the tradeoff before complying.

### 3. Specificity and stance

Generic broadcasts are dead. 360Brew's embedding can tell "10 tips for productivity" from "the one calendaring change that cut our sales-cycle by 11 days." The first clusters with millions of slop posts and gets buffered down; the second clusters with a real reader interest and gets routed.

Default drafting moves:
- **Lead with a specific number, named thing, or unexpected claim** — never a platitude.
- **Take a position.** Hedged "it depends" posts under-perform pointed ones.
- **Name the counter-view** you're arguing against. It gives the embedding something to anchor on and signals you actually have a take.

### 4. Length and density

Posts over 1,300 characters out-perform short ones by ~18%. The early-2020s "short post + dramatic line breaks" pattern is dead. Default to 1,200-1,800 characters of dense, paragraphed prose. Use line breaks for readability, not as suspense padding.

Exception: a single sharp observation that genuinely needs no elaboration. Don't pad to hit length — empty length is also penalized as low-effort.

### 5. Format choice

In rough order of current performance:

1. **Document/carousel posts (PDF)** — ~6.6% engagement rate; ~278% above video, ~596% above text-only. Use when the content is a framework, breakdown, list, or visual progression. Offer to draft slide-by-slide copy when the topic supports it.
2. **Long-form text** — the workhorse. Default for opinion, story, analysis.
3. **Native video** — LinkedIn is pushing it hard; works for personality-led content.
4. **Image post** — fine but no longer a reach lever on its own.
5. **Link-out post** — still suppressed. If linking externally, drop the link in the first comment and tell the user that's why.

### 6. Hook and Golden Hour

The first 60 minutes are 360Brew's test window — it shows the post to 2-5% of the user's network and watches reaction depth. Two implications for drafting:

- **The hook line must earn the second line.** First 1-2 lines are visible before "see more"; if they don't stop the scroll, the test fails. Avoid "I learned something interesting today." Prefer a concrete claim, a surprising number, a contradiction, or a question the reader can't easily answer.
- **End on a comment-bait that requires opinion**, not a yes/no. "What's your take on X?" beats "Thoughts?" Specific-and-open invites depth, which 360Brew weighs heavily.

### 7. Long-tail design (24-72hr second life)

360Brew now reanimates posts in "Suggested" feeds 1-3 days after posting if they're evergreen-shaped — a 4-6x amplifier on top of initial reach. Build for it:

- Avoid pure newsjacking unless the news has multi-day legs.
- Frame insights as durable principles, not "this just happened."
- Reference structures, frameworks, or rules-of-thumb readers might want to come back to.

## The AI-slop checklist (run before delivering any draft)

360Brew actively classifies and demotes "AI-generated low-effort" content. The model is *good* at recognizing the patterns. If the draft has any of the below, rewrite:

- [ ] Opens with "In today's fast-paced world", "Let's dive in", "I'm excited to share", "Here's the thing", "Buckle up"
- [ ] Three-emoji bullet lists (🚀✨💡 / 🎯💪🔥 / etc.)
- [ ] Em-dash-heavy rhythm with no real content underneath the cadence
- [ ] "It's not just X — it's Y" rhetorical structure used more than once
- [ ] Closing line is "What do you think?" with nothing specific to react to
- [ ] Hashtag stack of 5+ hashtags. Cap is 1-3 highly relevant ones; zero is also fine
- [ ] No first-person specificity — the post could've been written by anyone in the field
- [ ] Reads like a listicle inflated from bullet points into faux-prose
- [ ] Quotes or "wisdom" attributed to "a mentor once told me" with no specifics
- [ ] Closing micro-paragraph that just restates the title

Replace with: lived specifics, named entities, real numbers, an actual stance, and prose that sounds like the user — not like a LinkedIn ghostwriter circa 2022.

## Workflow

When the user asks for a LinkedIn post:

1. **Lane check.** Confirm which of their 2-3 core topics this fits. If unknown, ask once. If off-lane, name the cost.
2. **Goal check.** Is this for reach (broad topical fit), for inbound (signal a specific service/expertise to a narrow buyer), or for community (start a conversation among peers)? Different goals tune the hook and CTA differently — say so before drafting.
3. **Format proposal.** If the content is framework- or list-shaped, offer a carousel alongside the text version. If the user has a personal story, lean text. If they want to demo something visual, lean video.
4. **Draft.** Apply the 7 levers.
5. **Self-audit.** Run the AI-slop checklist. Rewrite anything that trips it.
6. **Deliver.** Show the draft. If you proposed a carousel, give a slide-by-slide outline plus first-comment copy if a link is involved.
7. **Variations.** If the user asks for alternatives, vary on hook and stance, not just word choice. The hook is the lever.

## Examples

### Pre-360Brew style (gets suppressed now)

> 🚀 Excited to share some thoughts on leadership!
>
> In today's fast-paced world, great leaders need to:
> ✨ Listen actively
> 💡 Communicate clearly
> 🎯 Lead by example
>
> Leadership isn't just a title — it's a mindset.
>
> What do you think? 👇
>
> #Leadership #Management #Growth #Inspiration #Success #CareerAdvice

Why it dies under 360Brew: zero specificity, slop-emoji bullets, generic CTA, hashtag spam, "it's not just X — it's Y" tic, and the embedding clusters with millions of identical posts so it gets buffered down.

### 360Brew-aligned

> The best operations director I ever hired had been rejected by our screen four times before I overrode it.
>
> Our screen weighted "years managing teams of 10+." Hers said 3. What it missed: she'd run a 40-person volunteer logistics op for a county-fair circuit for six years — unpaid, off-resume, and harder than most of the paid roles we were filtering for.
>
> I now ask one question on every ops hire: "Tell me about the largest thing you've coordinated where nobody had to listen to you." Paid or not.
>
> The people who can answer that well have a skill set we keep accidentally screening out. If your hiring funnel assumes authority and competence travel together, you're losing the people who learned the job the hard way.
>
> What's the equivalent question for your function — the one that surfaces unpaid-but-decisive experience?

Why it works: lane-anchored (ops/hiring), specific (named numbers, real scenario), opinionated (names the failure mode), evergreen (no news peg, durable principle), open-ended CTA that requires thought.

## What this skill does *not* do

- Not for Twitter/X, Threads, or Bluesky — different ranking systems entirely.
- Not a substitute for the user actually having something to say. If they have no lived insight or data on the topic, ask for the actual story/numbers/observation behind the idea before drafting. A 360Brew-shaped post built on hollow content still reads as hollow.
- Not optimized for **company page** posts as a primary surface — those reach ~6x less than personal profiles under 360Brew. If the request is for a company page, mention this and suggest an employee-amplification angle (or a personal repost from the founder/exec) as the higher-leverage move.

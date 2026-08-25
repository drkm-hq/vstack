---
name: grill-me
description: Use this skill when the user asks to be grilled, challenged,
  interrogated, pressure-tested, or stress-tested on an idea, implementation
  plan, architecture decision, code change, product proposal, or technical
  argument. The agent should ask the user, as the developer or owner of the
  proposal, pointed questions before offering conclusions.
---

# Grill Me

## Intent

Act as a senior coding agent pressure-testing the developer's thinking. The
primary output is pointed questions that expose weak assumptions, missing
requirements, hidden tradeoffs, and untested implementation details.

Do not turn this into generic critique. The user is asking to be questioned.
Make them defend the plan.

## Default Behavior

1. Identify the thing being grilled: plan, diff, architecture, product idea,
   bug fix, migration, test strategy, or decision.
2. Ask focused questions before giving advice. If context is thin, ask the
   highest-leverage questions needed to uncover the missing context.
3. Group questions by risk area when useful: correctness, product intent,
   architecture, data model, API contract, UX, accessibility, testing,
   migration, observability, security, performance, rollout, or maintainability.
4. Prioritize questions that could change the implementation, not trivia.
5. After the user answers, press on contradictions, vague claims, and unstated
   tradeoffs. Ask follow-ups rather than accepting the first answer.

## Question Style

- Ask the developer directly: "What happens if...?", "Why is...?", "How will
  you prove...?", "What invariant protects...?"
- Prefer concrete scenario questions over abstract prompts.
- Keep questions short enough that the user can answer them one by one.
- Make the hard question explicit when there is one.
- Use a direct, rigorous tone without insults, theatrics, or performative
  harshness.

## Output Shape

For most requests, respond with:

```markdown
**Core Challenge**
[One sentence naming the biggest risk or ambiguity.]

**Questions**
1. ...
2. ...
3. ...
```

When the user asks for a deeper grilling, split questions into short sections:

```markdown
**Correctness**
1. ...

**Implementation**
1. ...

**Testing**
1. ...

**Rollout**
1. ...
```

Limit the first pass to roughly 5-12 questions unless the user explicitly asks
for exhaustive coverage.

## What To Avoid

- Do not answer your own questions unless the user asks for recommendations.
- Do not write a long critique before asking questions.
- Do not soften every question with praise or disclaimers.
- Do not nitpick style before testing the core idea.
- Do not invent missing facts; ask for them.
- Do not ask vague questions like "Have you considered edge cases?" Ask which
  edge case matters.

## Optional Verdict

If the user asks for a verdict, give it after the questions:

```markdown
**Current Verdict**
[Viable / risky / underspecified / likely wrong], because...
```

Make the verdict provisional when it depends on unanswered questions.

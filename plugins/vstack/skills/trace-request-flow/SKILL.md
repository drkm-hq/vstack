---
name: trace-request-flow
description: Explain a code change or subsystem at the reader's level, or trace a request through its callers, state, and integrations. Use for teaching, architecture walkthroughs, end-to-end flows, exact payloads, identity propagation, and async lifecycle questions.
---

# Trace Request Flow

Start with what the code does and the problem it solves, at the depth the
question needs. For a concrete request, build an evidence-backed explanation
from caller to final result. Read code and tests; do not infer behavior from filenames or architecture descriptions alone.

For a subsystem overview, placement, or ownership question, use [subsystem explanations](references/subsystem-explanations.md) instead of forcing a request payload and sequence diagram. For a concrete runtime request, follow the workflow below.

## Establish Scope

1. Identify the concrete entrypoint: HTTP method and route, event, job trigger, CLI command, or UI action.
2. If the user names a PR, inspect its head commit and diff, then trace through both changed and unchanged code at that exact revision.
3. If the flow crosses repositories, inspect every participating repository. For UI flows, include the browser route, server proxy, and backend route.
4. Choose one representative request when several paths exist and state the choice. Ask only when no reasonable entrypoint can be inferred.
5. Keep exploration read-only unless the user explicitly asks to update code, documentation, or a PR.

## Trace The Request

Follow real call sites in order:

1. Caller action and wire request
2. Proxy, middleware, or server-route transformation
3. Authentication and principal resolution
4. Request parsing and schema validation
5. Router or controller
6. Service and domain logic
7. Database or object-storage writes
8. Queue, background task, workflow, or job boundary
9. Worker, sandbox, or external API calls
10. Result persistence, polling, and response
11. Cleanup, timeout, retry, and failure paths

At every boundary, track:

- **Data:** Which fields are added, removed, or transformed?
- **Identity:** Which user or service principal authorizes the next operation?
- **Credentials:** Where are tokens read, copied, validated, persisted, exposed, and deleted?
- **Durability:** Is state in memory, a database, a queue, a file, or an external system?
- **Timing:** Does work finish before the response, after it, or in a separate process?

## Gather Evidence

- Read repository guidance first.
- Prefer `rg` and direct file reads to broad speculation.
- Locate schemas, generated clients, tests, mocks, and infrastructure configuration in addition to runtime code.
- Use tests to obtain realistic IDs and payload values, but verify that the test exercises the same route.
- For PRs, record the head SHA so links and line references describe the reviewed revision.
- Link every important step to a concrete file and tight line range. Use exact-commit GitHub links for remote PRs and absolute local links for local-only code.

## Exactness Rules

Keep these representations distinct:

- Browser or caller HTTP payload
- Internal HTTP payload after proxying
- In-process object or credential envelope
- Persisted database record
- Queue, job, or volume payload
- SDK invocation
- External API request
- Final response

Call a payload **exact** only when every shown field and value comes from code, a fixture, a test, or an observed trace. Otherwise:

- Label it `representative` or `shape`.
- Mark dynamic values as `<execution UUID>`, `<workspace host>`, or similar.
- Explain fields omitted from an abridged payload.
- Never print a live credential. Use a clearly fake test value such as `obo-token` or `<redacted token>`.
- Do not claim that an in-memory secret is persisted merely because it is later serialized at another boundary.

## Produce The Diagram

Use a Mermaid `sequenceDiagram`. Include only actors that own a meaningful boundary. Show:

- The initial request and immediate response
- Header or credential forwarding
- Authentication and identity resolution
- Database writes
- Async handoff
- External service calls
- Result storage and retrieval
- Cleanup of sensitive or temporary state

Use explicit labels such as `202 queued`, `run_now as app service principal`, or `SQL connection with user token`. Do not hide identity changes behind generic labels like `process request`.

## Response Format

Use this structure when the flow is substantial:

1. **Scope**: The exact request and revision being traced.
2. **Diagram**: Mermaid sequence diagram.
3. **Concrete Example**: The saved object, command, or configuration that makes the request realistic.
4. **Payloads**: Exact caller payload first, then internal payloads in execution order.
5. **Code Walkthrough**: Numbered steps with file and line references.
6. **Identity And Security**: Who authorizes each boundary, where credentials exist, and what is persisted.
7. **Failure And Async Behavior**: Expiry, retries, process loss, cron/webhook limitations, and cleanup.
8. **Unknowns**: Anything not proven by source or trace.

Keep the explanation compact enough to interrogate. Prefer one complete path over listing every variation. End with the most consequential limitation when one exists.

## Quality Check

Before answering, verify:

- The diagram and prose describe the same route.
- The frontend payload matches the frontend code, not only the backend schema.
- The identity at each external call is explicit.
- Every secret-bearing hop is identified.
- Async work clearly shows what survives the original request.
- Exact payloads contain no invented values or real secrets.
- Polling and final result retrieval are included when the caller does not receive the result immediately.

# Deep modules and testable interfaces

Use this guide when the design problem is a cluster of shallow modules or a
caller that must coordinate too many details. Preserve the repository's
terminology.

A module's interface is everything a caller must know: inputs, outputs,
invariants, ordering, failure modes, configuration, and performance contracts.
A deep module provides substantial useful behavior behind a small interface.
Depth is not a ratio of implementation lines to public methods.

A seam is where behavior can be substituted. An adapter implements an
interface at that seam. Internal seams can support tests without becoming
part of the caller's interface.

## Choose what to hide

Write the real caller's usage first. Ask what coordination, mutable state,
and error handling the module can own. If deleting a wrapper removes
complexity rather than spreading it back across callers, the wrapper may
not justify its existence.

Keep dependency choices tied to actual needs:

- Pure in-process computation can be tested directly through its interface.
- Local substitutes can exercise persistence or filesystem behavior without
  exposing test-only details to callers.
- Owned remote services may justify an injected transport adapter.
- External services need an explicit boundary; a test double proves local
  handling, while contract or integration checks establish the real protocol.

Do not add a port solely to make a hypothetical second adapter possible.
Retain meaningful internal tests; remove obsolete tests only after their
behavioral coverage has moved to the new interface.

## Compare alternatives when needed

Use [arena](../../arena/SKILL.md) when the user requests independent competing
designs. Give candidates the same caller, constraints, and dependency facts,
then vary a meaningful design priority: the smallest interface, the most
common caller, or required extension points. Compare what each design hides,
where changes stay local, and which invariants callers still carry. Ordinary
design work does not require agents.

Adapted from Matt Pocock's codebase-design vocabulary, deepening, and
Design It Twice guidance. See [the retained MIT notice](../MATT-POCOCK-LICENSE.txt).

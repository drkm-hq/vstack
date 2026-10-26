---
name: debug-performance
description: "Diagnose reproducible bugs, runtime leaks, slow paths, and captured profiles with hypotheses and measured evidence. Use for root-cause investigations or performance improvement requests."
license: MIT
metadata:
  upstream: https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/poteto-mode/playbooks/perf-issue.md
  adaptation: Codex personal skills; preserve task scope and repository conventions.
---
# Debug and measure performance

Establish the symptom and observe the mechanism before changing it. A diagnostic question stays read-only; implementing a fix requires an implementation request.

1. Name the expected and observed behavior, affected revision, environment, trigger, and a concrete reproduction or captured artifact. If reproduction is intermittent, record frequency and conditions rather than claiming it is deterministic.
2. Inspect the caller, owning component, lifecycle, and nearby tests. Trace the value or resource from creation through use and cleanup. Use the installed `trace-request-flow` skill when the path crosses boundaries.
3. Choose the relevant procedure in [measurement and investigations](../figure-it-out/references/measurement-and-investigations.md): performance, runtime symptoms, or captured traces. Use available format-aware tools, not guesses from filenames or one hot stack.
4. State a falsifiable hypothesis and the observation that could disprove it. Change one meaningful variable at a time. Instrument only an authorized, owned environment, and preserve the raw evidence.
5. When repeated fixes fail the same gate, test their shared premise. Inventory actors and ownership before another patch. A missing cleanup step, duplicate writer, measurement error, or incorrect workload can invalidate the entire approach.
6. For an authorized fix, use the smallest causal change and the nearest meaningful regression seam. The installed `tdd` and `meaningful-contribution` skills provide testing and proof guidance. Re-run the original symptom or workload and relevant correctness checks.
7. For sustained optimization, define a target and a finite budget. Record each hypothesis and before/after result, retain only measured improvements, and report noise or inconclusive measurements honestly. Do not claim an optimization from a single favorable run.

Return the cause at the confidence supported by evidence, the relevant artifact or result, changes if requested, and remaining gaps. Do not fix neighboring defects or ship automatically.

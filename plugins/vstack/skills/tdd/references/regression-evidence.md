# Regression evidence

Locate the nearest public interface and existing focused test command before adding a new harness. Run one test against the broken behavior and inspect why it fails. A setup failure does not establish the regression.

Assert a concrete observable result from the subject. Do not derive the expected value by running the same production logic, test only a handwritten fixture, or replace the function under test with a mock. A literal empty result, negative assertion, or captured external request can be a strong contract when it distinguishes the real bug; judge the behavior, not assertion vocabulary.

Mock external boundaries when needed while keeping the subject and relevant internal logic real. Observe required effects through a real user path or independent readback. Call-count assertions alone seldom establish a user-visible result, but ordering can be the contract for a protocol or lifecycle.

Use a safe isolated revision for a red/green comparison when practical. Do not discard user edits to manufacture failure. If the meaningful test needs unavailable services or disproportionate new infrastructure, name the gap, run the strongest existing executable check, and avoid presenting it as full proof. An explicit TDD request still calls for the requested first failing test where feasible.

Adapted from pstack: [tdd](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/tdd), [principle-test-behavior-not-implementation](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/principle-test-behavior-not-implementation).

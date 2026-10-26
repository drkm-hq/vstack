# Artifact evidence

Read the actual output, diff, stored value, or trace that establishes the claim. Check that the artifact is nonempty, relevant to this revision, and produced by the expected path. A child agent's summary or a screenshot without the interaction is not sufficient by itself.

For repeated transformations, complete one representative unit, observe the expected result, then build the smallest reusable command or codemod when repetition justifies it. Compare its output against the verified unit before applying it broadly. Include a dry-run or bounded scope when mistakes could touch unrelated data; inspect what those modes actually do.

Verify each coherent unit before starting the next. Reuse evidence for an unchanged revision when valid, but recheck affected behavior after a material change, changed base, dependency, or environment. A matching patch ID can link a diff to prior review; it cannot establish integration behavior on a different base.

Keep the command, inputs, revision, observed outcome, and relevant artifacts together. Report `INCONCLUSIVE` when the observation cannot distinguish success from failure. Do not turn missing or empty output into a passing check.

Adapted from pstack: [principle-prove-it-works](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/principle-prove-it-works), [principle-build-the-lever](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/principle-build-the-lever), [principle-sequence-verifiable-units](https://github.com/cursor/plugins/tree/640ea3abfbdef74aad432b58d8586e4bf645f42d/pstack/skills/principle-sequence-verifiable-units). See `../PSTACK-LICENSE.txt`.

# JSP-000465 connected-bipartite Lean certificate

This directory vendors a complete Lean 4 certificate for JSP-000465, the Erdős–Simonovits compactness counterexample for a finite family of connected bipartite cyclic graphs.

## Provenance and attribution

- Upstream project: `openai/ten-proofs`
- Pinned upstream commit: `94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6`
- Upstream project author: OpenAI
- Upstream license: Apache-2.0
- Vendored proof file: `lean/CompactnessAndDegeneracy.lean`
- Main declaration: `CompactnessConjecture.quantitativeCompactnessCounterexample`
- Final contradiction: `CompactnessConjecture.not_erdos_180`

This package is an attributed reproduction of the published OpenAI formalization. It does not claim that the repository owner authored the upstream Lean proof.

## Statement correspondence

The formalization defines the compactness statement for a finite forbidden family and proves a counterexample family for which every forbidden graph is connected, bipartite, and cyclic. It provides the quantitative separation used to refute constant-factor reduction to any single member and derives `¬ CompactnessConjectureStatement`.

## Reproduction




The verification script requires the three target theorems to depend only on `propext`, `Classical.choice`, and `Quot.sound`, and rejects `sorry`/ `admit` in the certificate source.

## Prize-record note

This directory supplies pinned formal evidence and reproducibility material. The Justin Sun Prize maintainers decide problem-bank Lean status, attribution, candidate status, awards, and payment eligibility.

# Verification record

## Source pin

- Repository: `openai/ten-proofs`
- Commit: `94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6`
- Source: `CompactnessAndDegeneracy.lean`
- Lean: `v4.32.0`
- Mathlib: `v4.32.0`

## Target declarations

1. `CompactnessConjecture.quantitativeCompactnessCounterexample`
2. `CompactnessConjecture.compactnessCounterexample_bigO`
3. `CompactnessConjecture.not_erdos_180`

## Checks

- build the vendored source with Lean kernel checking;
- reject `sorry` and `admit` tokens in the vendored certificate source;
- type-check an explicit term of `¬ CompactnessConjecture.CompactnessConjectureStatement`;
- run `#print axioms` on all target declarations;
- reject every transitive axiom outside `propext`, `Classical.choice`, and `Quot.sound`.

The generated `verification-output.txt` records the actual reproduction output from GitHub Actions.

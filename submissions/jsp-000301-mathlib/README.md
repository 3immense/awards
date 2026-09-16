# JSP-000301 — Mathlib-native formalization package

This package provides an alternative formalization of the known counterexample
to JSP-000301. It uses the catalog witnesses `12167` and `12168` and proves the
negation of the exact yes/no assertion.

This is not a discovery claim. The numerical counterexample is already known and
recorded by the project.

## Relation to PR #13

PR #13 already proposes a Lean formalization of the same known counterexample.
This package does not claim priority over that work. Its main purpose is to
provide a statement-fidelity-oriented variant that uses Mathlib's standard
`Nat.Prime` and `IsSquare`, together with an explicit theorem showing that the
problem-specific `Powerful` predicate is equivalent, for positive naturals, to
the expected prime-factorization exponent condition.

The finite-certificate proof strategy for the concrete witnesses is closely
related to the route used in PR #13 and should be reviewed as an alternative
formalization / verification artifact rather than an independent mathematical
discovery.

## Reproduction

The package pins:

- Lean `v4.34.0`;
- Mathlib commit `5ed2965256430c3649e86755f9576b54eca72435`.

Run from this directory:

```sh
sh verify.sh
```

The source has already passed GitHub Actions in the contributor repository using
this pinned Lean/Mathlib configuration. The final declarations reported axioms
`[propext, Classical.choice, Quot.sound]` and no `sorryAx`.

## Files

- `Proof.lean`: formal proof.
- `STATEMENT_REVIEW.md`: contributor-supplied statement/definition fidelity review.
- `VERIFICATION.md`: reproducibility evidence and limitations.
- `lakefile.toml`, `lean-toolchain`: pinned environment.
- `verify.sh`: reproduction command.

## Scope and review boundary

No award, eligibility determination, official candidate record, curator
signature, or independent verification attestation is asserted by this package.
Those decisions remain with the project maintainers and authorized reviewers.

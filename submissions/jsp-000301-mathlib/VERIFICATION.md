# Verification evidence

Contributor-side verification completed on 2026-09-16.

Environment pinned by this package:

- Lean `v4.34.0`.
- Mathlib commit `5ed2965256430c3649e86755f9576b54eca72435`.

A GitHub Actions run in the contributor repository completed successfully with:

- dependency resolution: success;
- Lean compilation of `Proof.lean`: success;
- placeholder audit: success.

The proof compilation printed:

```text
'JSP000301.powerful_iff_factorization_exponents' depends on axioms: [propext, Classical.choice, Quot.sound]
'JSP000301.counterexample' depends on axioms: [propext, Classical.choice, Quot.sound]
'JSP000301.original_claim_false' depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `sorryAx` was reported.

This is contributor-supplied reproducibility evidence, not an independent
checker attestation and not an award or eligibility determination. The official
repository's statement and verification schemas require authorized signatories
and independent review; none are invented here.

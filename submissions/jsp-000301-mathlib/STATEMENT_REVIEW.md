# JSP-000301 statement fidelity review

## Natural-language source

The formal target is the yes/no assertion recorded as JSP-000301 in the official
problem bank:

> If two consecutive positive integers are powerful, must at least one be a
> perfect square?

The recorded counterexample is 12167 and 12168.

Source: `problems/catalog-0301-0400.md`, entry `JSP-000301`.

## Formal statement

```lean
theorem original_claim_false :
    ¬ (∀ n : ℕ,
      Powerful n → Powerful (n + 1) → IsSquare n ∨ IsSquare (n + 1))
```

This is the direct negation of the universal yes/no assertion. Positivity is
included in `Powerful`, so quantifying over all naturals does not introduce zero
as an unintended powerful integer.

## Definitions reviewed

### `Nat.Prime` — from Mathlib

No local replacement predicate is used.

### `IsSquare` — from Mathlib

No local replacement predicate is used.

### `Powerful` — problem-specific

```lean
def Powerful (n : ℕ) : Prop :=
  0 < n ∧ ∀ p : ℕ, p.Prime → p ∣ n → p ^ 2 ∣ n
```

The theorem `powerful_iff_factorization_exponents` proves, using Mathlib's
`Nat.Prime.pow_dvd_iff_le_factorization`, that for positive `n` this is equivalent
to every prime divisor occurring with factorization exponent at least two.

## Counterexample fidelity

The proof uses exactly the catalog counterexample 12167 and 12168. It proves:

- both are powerful;
- they are consecutive;
- neither is square because both lie strictly between `110^2` and `111^2`.

It does not address the distinct counting question associated with Erdős #365.

## Library pin

- Lean: `v4.34.0`
- Mathlib commit: `5ed2965256430c3649e86755f9576b54eca72435`

## Review boundary

This is contributor-supplied statement-comparison evidence, not an official
statement-equivalence attestation. Authorized statement signatories and
independent verification roles required by the repository's formal record schema
are not fabricated here.

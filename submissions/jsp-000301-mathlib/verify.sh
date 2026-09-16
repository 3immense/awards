#!/usr/bin/env sh
set -eu
lake update
lake exe cache get
lake env lean Proof.lean
! grep -R -nE '\b(sorry|admit|native_decide)\b' Proof.lean

# Handoff — Replication Criterion — 2026-10-14

- **State:** **three of four legs investigated.** The criterion is fixed, applied
  across the three sibling repos, and the two legs no sibling covered — **power**
  and **control (relay logic)** — have been run. Both produced corrections to the
  sibling study.
- **Files:** `protocol.md`, `audit.md`, `findings-power.md`,
  `findings-control.md`, `NOTICE.md`, `LICENSE`, `.gitignore`, `README.md`.
  Branch `main`, no remote (matches siblings).
- **Blockers:** none. Both new legs are **encyclopaedia-tier** evidence (see
  below) — that is the main limitation to carry forward.

## What this repository concluded

The study is named for a dichotomy — *if it needs a data center or a reactor, it
is not self-replicating* — and **one half of it had never been investigated** by
any sibling repo. `audit.md` shows the three existing repos are **legs of one
argument**; this repo adds the missing legs.

**The criterion (`protocol.md` §3):** M is self-replicating iff its critical
subsystems (control, power conversion, structure/tooling) are inside C(K, E) —
the productive closure given a named bootstrap kit K. Mass closure is the wrong
measure: a study can report 90–96% mass closure while excluding 100% of the
subsystem that makes it a machine.

**The power leg (`findings-power.md`):**

- **Condemned by the data-center rule:** every route that turns heat or light
  *directly* into electricity at the point of use — **PV is a doped p–n junction
  semiconductor device**. So "needs a reactor" and "needs a data center" are one
  dependency *for that family*.
- **The generator survives:** a **self-excited dynamo needs no permanent magnet**,
  building its field from residual magnetism in its own iron. The hole is
  **soft-iron cores** and **winding insulation**, plus a first-excitation
  bootstrap gap.
- **Prime movers survive:** Newcomen and Watt steam, high-pressure steam,
  Stirling, **water wheels** (strongest), windmills — all documented as built from
  in-closure materials with hand-generated precision.
- **Stationary is not condemned; mobile is not shown to work** (mobility forces a
  carried energy store, and the in-closure chemistries are unresolved).

**The control leg (`findings-control.md`) — the surprise:**

- **Relay logic composes, and the sibling dismissed it too fast.** A relay's
  per-stage gain is **> 1 by architecture** (coil in one circuit, contacts in a
  separate circuit with its own supply; one signal drives several circuits), and
  the historical record shows relays cascading for ninety years (telegraph
  repeaters 1840; Strowger 1891; crossbar relay sets; Zuse's Z3, 2,600 relays,
  Turing-complete).
- **The materials premise of the dismissal fails.** A relay needs only an
  electromagnet, not a permanent magnet; wrought iron is documented as usable for
  temporary magnets; Sturgeon (1824/25) and Henry (1830+) built working
  electromagnets from iron, varnished iron, bare copper and silk.
- **Therefore the fluidic cascade wall (0.30 vs ≥1.0) is specific to the fluidic
  element, not to non-semiconductor control** — and the sibling's "fluidics is the
  only candidate" claim is **too strong**.

## Decisions made — do not re-litigate

- **One criterion, not two.** "Data center" and "reactor" name the same failure.
- **K is fixed before the evidence** (`protocol.md` §8): the pre-industrial
  closure. Moving K to get a preferred answer is the named hazard.
- **A human operator is part of K, not a subsystem of M** (§7).
- **No simulation** (`protocol.md` §11).
- **Rights: cite, never held.** No source PDFs, no extractions, no figures, no
  passage longer than a short phrase.

## Open question — now RESOLVED against the sibling

`audit.md` and `findings-gain.md` record it: the sibling reads its momentum ratio
`J_c/J_p` (0.10–0.51) as evidence a stage **cannot reach parity**, but that ratio
is the **required control-to-power ratio**. The output is the deflected power
jet, so the gain is the **reciprocal — ≈2–10, above 1.** Primary text confirms
the direction (*a weak stream deflects a stronger one, "so the device has gain"*)
and FLODAC (1964) is an existence proof of fluidic cascading.

**Consequence: the sibling's verdict "cannot drive even one matched successor" is
not supported by its own numbers.** Corrected statement: **a fluidic stage has
gain > 1 and can drive a successor; the limit is fan-out depth** (≈2–3,
`[unverified]`). This is a **logical** resolution, not a measured one — see
`findings-gain.md` §5 for what is ABSENT.

## A correction to the sibling repo that is now owed — not yet landed

`Fluidic Bootstrap Project` concludes, in `src/cascade.py` and its README, that
fluidic logic **cannot cascade**. That conclusion rests on the inverted Path 2.
The repo is **frozen at `v1.3`**; correcting its central verdict means editing
`src/cascade.py` (including its `check()`), the README and `BUILDERS-NOTES.md`,
and tagging `v1.4`. **That edit is deliberate and scoped, and is the next
substantive action** — it is a change to a *verdict*, not a claim, so it should
not be slipped in.

## Known limitations

`findings-power.md` §0 and `findings-control.md` §0 say it first: both legs rest
on **encyclopaedia-tier** sources (one primary in the power leg: KSRM §5.6). The
`[verified]` tag means "read this source's own text," not "checked its citations."
Each leg lists an explicit **ABSENT** list (§5) that must not be filled with
plausible numbers. Neither leg found a **published numeric gain figure** — for
fluidics or relays.

## Next step

1. **Settle the `J_c/J_p` question** — the highest-value item; it may flip the
   verdict. Read a fluidic amplifier's gain definition, or run Rung 1.
2. **Raise both legs' evidence tier** to primary sources.
3. **Close the generator hole** — soft-iron cores and winding insulation.
4. Optionally: the mobility leg, currently open.

## Continuation records

- Nothing running. No remote; do not push without instruction.
- Sibling repos: `Fluidic Bootstrap Project` (frozen, `v1.3`), `closure-audit`
  (closed, `3645f28`), `copy-fidelity` (verification pass complete).
- **Sources are cited, never held.** Two sessions of cleanup removed fetched
  paper/article text that had leaked into harness scratch and transcript state
  (`.codewhale`), which is gitignored but was still on disk.
- **Refresh live state before acting:** `git log --oneline -5`, `git status`.
  This note is orientation, not authority.

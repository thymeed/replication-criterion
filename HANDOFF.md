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

## Open question that could flip the study's verdict — do not smooth it over

`audit.md` §"A tension that must be reconciled" records it: the sibling reads its
momentum ratio `J_c/J_p` (0.10–0.51) as evidence a stage **cannot reach parity**,
but that ratio is the **required control-to-power ratio**; in a bistable element
the output is the *deflected power jet*, which implies a device **gain of ~2–5**.
Wikipedia *Fluidics* says fluidic amplifiers "have gain", the opposite of the
sibling's conclusion. **Device gain vs. system cascade margin under fan-out** may
reconcile them (3-way fan-out at 0.2–0.5 each needs 0.6–1.5× the power jet, so it
is marginal even if 1-way is fine) — but this is **flagged, not settled**, and
settling it needs a fluidic amplifier gain definition or the Rung-1 measurement.

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

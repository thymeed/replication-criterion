# Replication Criterion

**The question.** If a machine needs a **data center** or a **reactor, it is not
self-replicating.** That is the study's own name, stated as a test. This
repository states the test precisely, applies it across the sibling repositories,
and investigates the half of the dichotomy that none of them had touched: **the
power source.**

**Why it needed its own repository.** Three sibling repos each answered a piece
of the question and none stated the criterion that decides it:

- `Fluidic Bootstrap Project` — can a machine make its own **control system**
  from a bootstrapped workshop?
- `copy-fidelity` — does copying its own **geometry** drift, or does the
  three-plate process reset the error?
- `closure-audit` — when a study publishes a closure figure, does it **disclose
  what it excludes**?

Read together, they are **three legs of one argument**. The fourth leg — power —
was missing, and the study was named for a dichotomy whose second half nobody had
investigated. See [`audit.md`](audit.md).

## The criterion, in one paragraph

A machine is self-replicating only if every subsystem whose failure would stop
replication can itself be produced by the machine, starting from a **stated
bootstrap kit** and using only its environment (§1, §3 of
[`protocol.md`](protocol.md)). The literature measures **mass** closure — and a
study can report 90–96% mass closure while excluding 100% of the subsystem that
makes it a machine, because a controller is a rounding error in tonnage. A
different measure is needed, and this is it.

## What is already established

- **The data center is condemned, and there is a real replacement.** Fluidic
  wall-attachment logic needs no contacts, no magnets and no rare metals — the
  only control substrate wholly inside a pre-industrial materials closure. It
  then hits a quantified wall: cascade gain ~0.30 against a needed ≥1.0
  (`Fluidic Bootstrap Project`).
- **Precision can be generated, not inherited** — the three-plate method — but
  the sibling `copy-fidelity` suspects it is a rediscovery of the optics
  three-flat test, and whether the effect transfers from *measuring* to *making*
  is open.
- **The literature discloses its boundaries** and **nobody demonstrates the brain
  being made** (`closure-audit`, closed 2026-10-14).

## What this repository adds

**The power leg, and the hypothesis that the two disqualifiers collapse into
one.** Solar-electric and thermoelectric converters are semiconductor devices —
so they are condemned by the *same* rule that condemns the data center.
Electromagnetic generation wants magnets — condemned by the *same* materials
boundary. If both hold, the criterion leaves only converters with no
semiconductor and no magnet (combustion, wind, water — and generators are the
pinch point), and **the binding constraint is a shared materials boundary, not
the cascade wall the sibling repo named.** That is a testable claim. See
[`audit.md`](audit.md) and [`findings-power.md`](findings-power.md).

## Documents

```
protocol.md          the criterion, pre-registered: the formal statement, the
                     operational definitions of "data center" and "reactor", the
                     bootstrap kit K, and the falsifiers
audit.md             the criterion applied across the three sibling repos: the
                     four-leg map, and the synthesis
findings-power.md    the power leg: which prime movers sit inside the closure,
                     which are condemned, and the mobile-vs-stationary finding
findings-control.md  the control leg: does relay logic compose, and can it be
                     built in-closure? (it can, on the evidence found)
NOTICE.md            sources, rights, and the evidence rule
```

## Status

**Three of four legs investigated.** The criterion is fixed (`protocol.md`); the
cross-repo audit and the legs are written (`audit.md`, `findings-power.md`,
`findings-control.md`). Where the literature is silent, each says so rather than
estimating — `findings-power.md` §5 and `findings-control.md` §5 are the explicit
ABSENT lists.

**Two results worth the reader's time, both corrections to the sibling study:**

- **The reactor half of the study's own name had never been investigated.**
  Result: direct heat/light→electricity conversion is condemned by the same rule
  as the data center, but **combustion, water and wind prime movers survive**, and
  a **self-excited dynamo needs no permanent magnet**. A **stationary** replicator
  is not condemned; a **mobile** one is not shown to work.
- **Relay logic was dismissed too fast.** It **composes** — per-stage gain > 1 by
  architecture — and its materials sit inside the closure, so the fluidic cascade
  wall is specific to fluidics, not to non-semiconductor control. This also
  surfaces a **tension in the sibling's central number** that could flip the
  study's verdict: see `audit.md` §"A tension that must be reconciled".

## Rights

Documents: **CC BY 4.0**. Sources are **cited, never held** — no PDFs, no
extractions, no figures, no passage longer than a short phrase. See
[`NOTICE.md`](NOTICE.md).

Copyright © 2026 Thymeed.

# Replication Criterion

**The question.** If a machine needs a **data center** or a **reactor, it is not
self-replicating.** That is the study's own name, stated as a test. This
repository states the test precisely, applies it across the sibling repositories,
and investigates the half of the dichotomy that none of them had touched: **the
power source.**

**Why it needed its own repository.** Three sibling repos each answered a piece
of the question and none stated the criterion that decides it:

- `Fluidic Bootstrap Project`: can a machine make its own **control system**
  from a bootstrapped workshop?
- `copy-fidelity`: does copying its own **geometry** drift, or does the
  three-plate process reset the error?
- `closure-audit`: when a study publishes a closure figure, does it **disclose
  what it excludes**?

Read together, they are **three legs of one argument**. The fourth leg, power,
was missing, and the study was named for a dichotomy whose second half nobody had
investigated. See [`audit.md`](audit.md).

## The study this belongs to

This repository is one of four siblings written against a single question: what
would it take for a machine to replicate itself with no semiconductor industry
and no energy industry behind it.

- `Fluidic Bootstrap Project`: can the machine make its own control system?
- `copy-fidelity`: does copying its own geometry drift, or can precision be
  regenerated?
- `closure-audit`: does the literature disclose what its closure figures exclude?
- this repository: the criterion that decides the question, and the power leg.

**Method, stated because it bounds every claim: literature and arithmetic only.**
The study ran no laboratory work, and each leg names the one measurement that
would close it. A workspace-level index of the four repositories is kept locally
by the author.

## The criterion, in one paragraph

A machine is self-replicating only if every subsystem whose failure would stop
replication can itself be produced by the machine, starting from a **stated
bootstrap kit** and using only its environment (§1, §3 of
[`protocol.md`](protocol.md)). The literature measures **mass** closure, and a
study can report 90–96% mass closure while excluding 100% of the subsystem that
makes it a machine, because a controller is a rounding error in tonnage. A
different measure is needed, and this is it.

## What is already established

- **The data center is condemned, and there is a real replacement.** Fluidic
  wall-attachment logic needs no contacts, no magnets and no rare metals, the
  only control substrate wholly inside a pre-industrial materials closure. Its
  cascade verdict was then corrected in the sibling's favour: the first reading
  inverted its own number, and on that number a stage has gain above parity and
  can drive a successor. The real limit is **shallow fan-out**, which this
  repository's `findings-logic.md` now prices (`findings-gain.md`,
  `findings-control.md`).
- **Precision can be generated, not inherited**: the three-plate method, which the
  sibling `copy-fidelity` has now confirmed is a rediscovery of the optics
  three-flat test, and has resolved the measuring-to-making transfer for: the
  effect is **real but conditional on how the process is run**, and it resets the
  workpiece, not the machine (`copy-fidelity/findings-transfer.md`).
- **The literature discloses its boundaries** and **nobody demonstrates the brain
  being made** (`closure-audit`, closed 2026-10-14).

## What this repository adds

**The power leg.** It tested a hypothesis carried in from the cross-repo audit:
that the two disqualifiers collapse into one, because the materials boundary that
condemns magnets also condemns the generator. The leg partly refutes it. Direct
heat-to-electricity and light-to-electricity conversion is condemned by the
data-center rule, so "needs a reactor" collapses into "needs a data center" for
that family. But the self-excited dynamo needs **no permanent magnet**, so the
magnet boundary does not condemn a generator. **What survives is shaft power and
the generator, conditional on materials this leg could not close.** See
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
                     built in-closure? (it composes; its contacts were platinum,
                     reachable only from a placer in E, §7)
findings-gain.md     the gain leg: is the sibling's cascade verdict an inversion?
                     (gain is ~2–10, not 0.10–0.51; the limit is fan-out)
findings-logic.md    the logic leg, the count the study could not supply: how
                     many elements a replication controller needs, derived from
                     its structure instead of assumed
findings-tooling.md  the structure-and-tooling leg: iron has a measured cost,
                     tool-making is unmeasured
model/               standard library only; add `--verify` for self-checks.
                     `controller_budget.py`: the arithmetic behind
                     findings-logic.md, fluidic and relay. `closure_graph.py`:
                     all legs in one table, and which open quantities the
                     verdict turns on
NOTICE.md            sources, rights, and the evidence rule
```

Leg 2 (precision) has no file here: it is the sibling `copy-fidelity`,
`findings-transfer.md`. This repository's `audit.md` Leg 2 summarizes it.

## Status

**All four legs investigated, and every one resolves the same way.** The criterion
is fixed (`protocol.md`); the cross-repo audit and the three legs that live here
are written (`audit.md`, `findings-power.md`, `findings-control.md`,
`findings-gain.md`). Where the literature is silent, each says so rather than
estimating; the explicit ABSENT lists are `findings-power.md` §5 and
`findings-control.md` §5.

**The result, in one line:** every leg ends at an **unmeasured quantity**, not at a
demonstrated impossibility. That is the honest shape of the study.

**Four results worth the reader's time, all corrections to the sibling study:**
- **The reactor half of the study's own name had never been investigated.**
  Result: direct heat/light→electricity conversion is condemned by the same rule
  as the data center, but **combustion, water and wind prime movers survive**, and
  a **self-excited dynamo needs no permanent magnet**. A **stationary** replicator
  is not condemned; a **mobile** one is not shown to work.
- **Relay logic was dismissed too fast.** It **composes**, per-stage gain > 1 by
  architecture, and its coils and cores sit inside the closure, so the fluidic
  cascade wall is specific to fluidics, not to non-semiconductor control. Its
  contacts do not: period relays used platinum points, which is outside K and
  reachable only from a platinum placer in the environment (`findings-control.md`
  §7).
- **And the cascade verdict itself was inverted.** `findings-gain.md` shows the
  sibling read a **required** control fraction (0.10–0.51) as an **available**
  gain. Belsterling's *Fluidic Systems Design* (1971), read directly, defines a
  **digital** fluidic amplifier's gain as the *reciprocal* of exactly that ratio,
  and notes it can be **infinite** for a latching element. The gain is therefore
  **≈2–10**, and the real limit is **fan-out depth**, with **fan-out of 3 a
  worked design case** in the same text.
- **And the controller's size was assumed, not counted.** `src/labour.py` priced
  the control system with `GATE_COUNTS = (20, 100)`, tagged "not known".
  `findings-logic.md` derives the count from the controller's own structure:
  about four elements per step of the cycle, so a cycle of 10 to 50 steps costs
  45 to 200 elements. The two assumed counts invert to a 6-step cycle and a
  26-step cycle, which makes the sibling's floor too low, and it puts the control
  system at **roughly 40 to 50 per cent of the labour of one generation**, not
  the small share the floor implied. The fan-out limit the sibling called a wall
  appears in the same arithmetic as a doubling of the element count: a price,
  with a number attached.
- **And the decisive measurements are not the ones the study named.**
  `model/closure_graph.py` puts every leg in one table. Fluidic gain is not a
  single point of failure, because the relay route is an alternative. The only
  two open quantities whose failure alone condemns the replicator are
  **tool-making** (`findings-tooling.md`) and **machine-geometry drift**
  (`copy-fidelity`), because control and structure both stand on them.

## Rights

Documents: **CC BY 4.0**. Sources are **cited, never held**, no PDFs, no
extractions, no figures, no passage longer than a short phrase. See
[`NOTICE.md`](NOTICE.md).

Copyright © 2026 Thymeed.

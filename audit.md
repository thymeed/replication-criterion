# Cross-repo audit — the criterion applied

**Version 0.1, 2026-10-14.** Applies the criterion in `protocol.md` §3 to the two
live sibling repositories and to the closed one. Every claim below is checkable
against the repo named in its heading; nothing new is asserted here.

The point of this document is to show that the three existing repositories are
**legs of one argument**, and that they share a fourth leg which none of them
covers.

---

## The four legs

A self-replicating machine has three critical subsystems (`protocol.md` §4), and
the literature that claims to close the question has a fourth problem — it does
not say what it leaves out. So the study has four legs:

- **Control** — the "data center" leg. Repo: `Fluidic Bootstrap Project`.
- **Precision** — can the geometry be re-made rather than inherited? Repo:
  `copy-fidelity`.
- **Power** — the "reactor" leg. Repo: **none.**
- **Disclosure** — does the literature disclose its boundaries? Repo:
  `closure-audit`.

The criterion's two named disqualifiers map onto legs 1 and 3. That is why this
repository needed to exist: **the study was named for a dichotomy, and one half
of it had never been investigated.**

---

## Leg 1 — Control: the data center, and the substrate that replaces it

**Source:** `Fluidic Bootstrap Project` (`HANDOFF.md`, `Conclusion A.md`,
`spec/prior-art.md`, `src/cascade.py`).

The criterion condemns a semiconductor controller outright — and the sibling
repo's materials finding says why, in its own terms:

- **Semiconductors and refined contact metals are outside a pre-industrial
  closure.** So a controller built on either is a dependency, exactly as
  `protocol.md` §5 defines it. The data center is condemned by the materials
  boundary before the cascade question is even reached.
- **The replacement is a real candidate, not a gesture.** Fluidic
  wall-attachment (Coanda) logic needs **no contacts, no magnets and no rare
  metals** — only channels and a pressure source. The sibling repo's verdict:
  *"the only candidate whose materials sit entirely inside the closure."* Its
  measured geometry comes from Olivotto 2010 (DOI
  10.13111/2066-8201.2010.2.4.21): a 2 mm nozzle in a 10 mm channel, R/w = 15–20,
  h/w = 5, 2–6 bar, 2–8 ms switching.

**And then it hits a wall, and the wall is quantified:**

- **Measured gains:** 0.30 and 0.322 — but these are from **membrane and piston
  valves**, a *different mechanism*. This is a transfer, not a measurement, and
  the repo says so.
- **Derived momentum ratio** `J_c/J_p = (p_c/p_p)·(b_c/w)` = **0.10–0.51**, exact
  under lossless Bernoulli.
- **The requirement:** ≥ 1.0 to compose at all; ≥ 3.0 to drive the ~3 successors a
  practical circuit needs.
- **Shortfall:** 3.1× against the floor, 9.3× against 3-way fan-out. By two
  independent arithmetic paths (`src/cascade.py`).

**Status: addressed, wall named, unresolved.** The criterion condemns the data
center; the closure-compatible replacement is identified; and it cannot cascade
on the numbers available. The single falsifier is stated in the repo and repeated
here: **one measured wall-attachment gain above ~3 reopens the leg.** No such
figure exists in any of the nine works the repo reviewed.

---

## Leg 2 — Precision: making the geometry, not inheriting it

**Source:** `copy-fidelity` (`scope.md`).

The criterion needs structure and tooling inside C(K, E), and that raises the
copying problem: copying a lapped fit gives a copy whose fit differs. The sibling
repo's premise is that **precision can be generated rather than inherited** — the
three-plate method (Whitworth) re-derives a flat from three rough surfaces with
no reference, and so functions as a physical error-correction mechanism.

Its own scope document already suspects this is a **rediscovery**: the technique
is the optics **three-flat test**, with a **dedicated error-propagation
literature**. The open question it defines is precise:

> Optics studies *measuring* three flats: non-contacting, object unchanged. The
> study's claim is about *making* surfaces by abrasive removal: contacting,
> material removed, a new object produced. **Whether the error-limiting
> behaviour survives the move from measuring to making is the question.**

**Status: live, unstarted at the time of writing.** Five optics citations were
`[unverified]` leads and must be checked against primary text before any claim
rests on them. That verification is the first analysis step in this leg.

**Why this leg is load-bearing for leg 3.** Every surviving power candidate —
boiler, turbine, wheel, generator — needs bearings, seals and fits. If precision
cannot be regenerated, the power leg has no floor to stand on. The two legs are
not independent.

---

## Leg 3 — Power: the reactor leg, which no repository covers

**Source: none.** This is the finding of this document, and the reason the
repository exists.

Neither `Fluidic Bootstrap Project`, nor `copy-fidelity`, nor `closure-audit`
addresses **energy conversion**. The study was named for a dichotomy — "a data
center or a reactor" — and the reactor half had never been investigated by any of
the three.

What can be said from the criterion before any source is read:

- **A reactor is condemned by definition** (`protocol.md` §6). The question is
  never "does it use energy" — it is whether the **converter** is inside C(K, E).
- **Solar-electric and thermoelectric converters are condemned by §5**, the same
  semiconductor rule that condemns the data center. So the criterion suggests a
  collapse: **"needs a reactor" and "needs a data center" may be one dependency,
  not two.**
- **The surviving candidates are the ones with no semiconductor:** combustion
  (charcoal/biomass → steam or hot-air engine), wind, water, and solar
  concentration into a heat engine.
- **The generator is the pinch point.** Electromagnetic generation wants magnets,
  and the sibling repo's materials finding puts high-performance magnets and
  consistent soft-iron cores **outside** the closure. So a dynamo may be
  condemned — while a **water wheel driving a line shaft** is not.

**Status: this leg is what `findings-power.md` exists to settle.** Until it is,
the criterion's verdict on power is *undetermined*, and that is stated rather
than guessed.

---

## Leg 4 — Disclosure: does the literature say what it leaves out?

**Source:** `closure-audit` (closed 2026-10-14, protocol v0.3, commit `3645f28`).

- **Result: the disclosure axis has no signal.** On the accessible primary
  corpus, every EXCLUDED closure figure that could be primary-verified is
  **STATED**. The cell for silent exclusion is empty. The strongest study (NREL,
  100% renewable) enumerates **nine** things it did not consider.
- **The sharper finding, and it is the one that bears on this repository:**
  NASA CP-2255 targets 100% closure *including* electronics fabrication, computes
  matter closure, argues parts closure, and **defers information closure
  outright** — the control of the factory. Its own diagnosis: **nobody
  demonstrates the brain being made.**
- **Method finding that travels:** half the intended primary sources were
  unreadable, in three different ways, so a claim here is a claim about the
  *accessible* corpus. And the searches returned **fabricated NTRS identifiers**
  presented as confidently as genuine results.

**Status: closed.** Its contribution to this repository is the sharper form of
the question and the evidence discipline (see `NOTICE.md`).

---

## The synthesis

Apply the criterion (`protocol.md` §3) with K = the pre-industrial closure
(`protocol.md` §8):

- **Structure and tooling — inside.** Iron, steel, copper, brass, glass, clay,
  wood are all in K.
- **Precision — inside, conditionally.** The three-plate process is in K
  (abrasive + three rough plates + labour), *if* its error-limiting behaviour
  transfers from measuring to making. That is leg 2, and it is open.
- **Control — the only inside candidate is fluidic, and it is blocked.** Leg 1.
- **Power — undetermined.** Leg 3.

**The verdict this repository can state today:**

> **No demonstrated machine meets the criterion, and the study was named for a
> dichotomy whose second half had never been investigated.** The sibling repo
> named **cascade gain** as the binding constraint — but the criterion suggests
> the power leg may fail *before* the cascade wall is reached, because the
> materials boundary that condemns magnets also condemns the generator, exactly
> as it condemns the data center.

That is a testable claim, and it is what leg 3 exists to settle. If it holds, the
study's headline changes: the binding constraint is not cascade gain, and not
labour — it is that **the same materials boundary blocks both halves of the
dichotomy**, control and power together.

If it does not hold — if some converter is built entirely from K — then the
control leg is the binding constraint after all, and leg 1's falsifier is the
thing to chase.

Either way, the answer requires leg 3, and until now leg 3 did not exist.

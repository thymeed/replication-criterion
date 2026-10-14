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

### The challenge to the dismissal — tested, and it partly succeeds

That repo dismissed **relay logic** in one line: ruled out by "contact and magnet
materials." That line is load-bearing — it is what makes fluidics *the only*
candidate — so it was tested directly. See
[`findings-control.md`](findings-control.md). The result, stated plainly:

- **The materials premise does not hold.** A relay needs only an
  **electromagnet**, not a permanent magnet; wrought iron is documented as usable
  for temporary magnets; and Sturgeon (1824/25) and Henry (1830+) built working
  electromagnets from iron, varnished iron, bare copper and silk — all inside the
  closure. So "soft-iron cores are more difficult without industrial
  metallurgy" is **not supported**.
- **The cascade wall is fluidic-specific, not general.** Relay per-stage gain is
  **> 1 by architecture** — a coil in one circuit moves contacts in a *separate*
  circuit with its own supply, and one signal can drive several circuits. Relays
  cascaded in production for ninety years (telegraph repeaters 1840; Strowger's
  exchange 1891; crossbar relay sets; Zuse's Z3, 2,600 relays, Turing-complete).
  **The 0.30 flow-gain shortfall is a property of the fluidic element, not of
  non-semiconductor control.**

**If that holds, the study's headline changes.** The binding constraint would
move off fluidic cascade gain and onto the relay leg's own costs — first
excitation of the generator, DC contact arcing, low-current contact filming, and
speed/life — **none of which is quantified yet**. It would also make the
sibling's "fluidics is the only candidate" claim too strong.

### A tension that must be reconciled, not smoothed over

The relay leg surfaced a **potential problem in the sibling's core number**, and
it is recorded here rather than resolved:

- The sibling reads its momentum ratio `J_c/J_p = (p_c/p_p)·(b_c/w)` = 0.10–0.51
  as evidence that *a stage cannot reach parity* — i.e. it treats the **required
  control-to-power ratio** as if it were the **available gain**.
- But in a bistable wall-attachment element the **output** is the deflected power
  jet, so a control that switches at 0.2–0.5 of the power jet implies a device
  **gain of roughly 1/0.5 to 1/0.2 = 2 to 5** — above 1, not below it.
- Wikipedia's *Fluidics* article states flatly that fluidic amplifiers "have
  gain" (a weak control stream deflects a stronger one), which is exactly the
  opposite of the sibling's conclusion.

**These may be reconcilable** — device gain vs. *system cascade margin under
fan-out* are different quantities, and feeding three successors at 0.2–0.5 each
would need 0.6–1.5× the power jet, so 3-way fan-out is marginal even if 1-way is
comfortable. But they read as contradictory, and the difference is exactly the
crux. **This is an open question that could flip the study's central verdict, and
it is flagged, not settled.** Settling it needs a careful reading of a fluidic
amplifier's gain definition, or the Rung-1 measurement.

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
- **Control — the only inside candidate is fluidic, and it is blocked.** Leg 1 —
  though relay logic is a second in-closure candidate whose dismissal does not
  survive testing (Leg 1, "The challenge to the dismissal").
- **Power — undetermined.** Leg 3.

**The verdict this repository can state today:**

> **No demonstrated machine meets the criterion.** Every leg resolves the same
> way: the in-closure candidates exist and are real, and each one stops at an
> **unquantified** cost rather than at a demonstrated impossibility.

| Leg | In-closure candidate | Where it stops |
|---|---|---|
| Precision | three-plate generation | the measure→make transfer, untested |
| Control | fluidic logic; **relay logic** | cascade gain (fluidic); relay costs unquantified |
| Power | combustion / water / wind + self-excited dynamo | first excitation; soft-iron cores; insulation |
| Disclosure | — | the literature discloses; nobody demonstrates the brain being made |

**Three findings changed the picture, and each was a leg that did not exist
before this repository or the session that built it:**

1. **The reactor half had never been investigated** — this repository's reason to
   exist. Its result: direct heat/light→electricity conversion is condemned by
   the *same* rule as the data center (those converters **are** semiconductors),
   but **shaft power and the self-excited dynamo survive** — a dynamo needs no
   permanent magnet. So the two disqualifiers collapse into one *for that family*,
   not globally.
2. **The power leg did not fail before the cascade wall**, contrary to the
   hypothesis this synthesis first advanced. The generator's magnet problem
   dissolves; the residual hole is materials and a first-excitation bootstrap,
   not principle.
3. **The control leg's "only candidate" claim does not survive testing** — relay
   logic composes (>1 by architecture) and its materials are in-closure, so the
   cascade wall is specific to the fluidic element.

**So the binding constraint is still not settled, and the study is honest about
that.** Two candidates compete for it, and both are blocked on *measurement, not
argument*: the fluidic **cascade gain** (the sibling's number, whose
interpretation leg 1 now questions), and the relay leg's **unquantified costs**.
Resolving it requires the one measurement the sibling repo has always
named — a wall-attachment gain figure — and now, additionally, a period relay's
gain and contact life.

**What this repository can say with confidence:** the study's original
one-line dismissal of relays was too fast, its "fluidics is the only candidate"
claim is too strong, and the reactor half of its own name had never been looked
at. Those are corrections, and they are the honest output of four legs that
mostly produced *bounds and gaps* rather than a verdict.

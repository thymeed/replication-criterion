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

**And then it hits a wall. The wall is no longer cascade, and the correction
came from this repository's own gain leg** (`findings-gain.md`):

- **The derived momentum ratio** `J_c/J_p = (p_c/p_p)·(b_c/w)` = **0.10–0.51**, exact
  under lossless Bernoulli, is the momentum the *control* must supply — so the
  available gain is its reciprocal, **2–10, above parity**. The sibling read it
  backwards.
- **The measured 0.30 and 0.322** are *flow* gain on *membrane valves*, a different
  mechanism, and flow gain is not the cascade criterion.
- **So cascade is not the wall.** A fluidic stage **can** drive a successor. The
  remaining constraint is **fan-out depth** (a handful of successors).

**Status: addressed, and the verdict corrected in the project's favour.** The
criterion condemns the data center; the closure-compatible replacement exists, and
it cascades. What remains open is the *measured* wall-attachment gain (the Rung-1
measurement) and the fan-out limit, neither of which is a demonstrated obstacle.

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
  **So non-semiconductor control composes; whatever limits the fluidic element does
  not generalize to control substrates as a class.**

**The study's headline does change**, and the gain leg then confirmed it: the
binding constraint moves off fluidic cascade (which is not a wall at all, see
below) and onto the relay leg's own costs — first excitation of the generator, DC
contact arcing, low-current contact filming, and speed/life — **none of which is
quantified yet**. It also makes the sibling's "fluidics is the only candidate"
claim too strong.

### Why the cascade verdict was wrong, in detail (`findings-gain.md`)

The relay leg surfaced a **problem in the sibling's core number**. It has now
been investigated directly, and the result is in
[`findings-gain.md`](findings-gain.md). Summary:

- The sibling's Path 2 computes `J_c/J_p = (p_c/p_p)·(b_c/w)` = 0.10–0.51 and
  reads it as **a gain that falls short of parity**. But that quantity is the
  momentum the **control input must supply** to switch the power jet — a
  **requirement**. The **output is the deflected power jet**, so the gain is the
  **reciprocal**: `1/0.51 … 1/0.10` ≈ **2–10**, comfortably **above** 1.
- Primary text says so directly: in a fluidic amplifier the control stream is
  **weaker** than the stream it deflects, *"so the device has gain"*
  `[verified]`, Wikipedia *Fluidics*.
- Path 1 (the measured 0.30 "flow gain") is a **different quantity** —
  small-signal *flow* gain — on a **different mechanism** (membrane valve, which
  the sibling itself flags as a cross-mechanism transfer). Flow gain is not the
  cascade criterion.
- **FLODAC (1964)**, an all-fluidic digital computer, is an existence proof that
  fluidic stages do drive their successors `[verified]`.

**So the sibling's verdict — "a single fluidic stage cannot drive even one
matched successor" — is not supported by its own numbers.** The revised, honest
statement is: **a fluidic stage has gain above 1 and can drive a successor; the
real constraint is fan-out depth** — and this is now **primary-sourced**:
Belsterling, *Fluidic Systems Design* (1971), read directly, defines a digital
fluidic amplifier's gain as the reciprocal of the required control ratio ("can be
infinite if it has negligible hysteresis") and works "**three parallel
flip-flops**" as a fan-out case. See `findings-gain.md` §2.

**Caveat carried forward:** this settles the *logic* of the sibling's arithmetic
and its fan-out example, on a primary text. It is **not** a measured gain figure
for a wall-attachment element, and no numeric fan-out *limit* was found. The
Rung-1 measurement remains the definitive step. `findings-gain.md` §4 lists what
would close it; §5 lists what is ABSENT.

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
- **Control — two in-closure candidates, not one.** Leg 1 tested the sibling's
  dismissal of relay logic (it does not survive) and its cascade verdict (it is
  an **inversion** of its own number — see `findings-gain.md`). Fluidic logic
  **can** drive a successor; the limit is fan-out depth.
- **Power — inside, conditionally.** Leg 3.

**The verdict this repository can state today:**

> **No demonstrated machine meets the criterion.** Every leg resolves the same
> way: the in-closure candidates exist and are real, and each one stops at an
> **unquantified** cost rather than at a demonstrated impossibility.

| Leg | In-closure candidate | Where it stops |
|---|---|---|
| Precision | three-plate generation | the measure→make transfer, untested |
| Control | fluidic logic; relay logic | fluidic **fan-out depth**; relay costs unquantified |
| Power | combustion / water / wind + self-excited dynamo | first excitation; soft-iron cores; insulation |
| Disclosure | — | the literature discloses; nobody demonstrates the brain being made |

**Four findings changed the picture:**

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
   logic composes (>1 by architecture) and its materials are in-closure.
4. **And the cascade verdict itself does not survive** — `findings-gain.md` shows
   the sibling's Path 2 reads a **required input fraction** as an **available
   gain**, inverting it. On its own numbers the momentum gain is ≈2–10, **above**
   parity. The mechanism statement (a weak stream deflects a stronger one) and
   FLODAC (1964) both confirm the direction.

**So the binding constraint has moved, and it is smaller than the study claimed.**
It is no longer "a fluidic stage cannot drive its successor". It is:
**fluidic fan-out is shallow** (≈2–3, `[unverified]`), plus the relay leg's
unquantified costs, plus labour. All three are **quantities to measure**, not
walls — and the study's original verdict rested on an arithmetic slip. Resolving
what remains needs the Rung-1 measurement and a fluidics text's fan-out figure.

**What this repository can say with confidence:** the study's dismissal of
relays was too fast, its "fluidics is the only candidate" claim is too strong,
its cascade verdict rests on an inverted quantity, and the reactor half of its own
name had never been looked at. Those are corrections, and they are the honest
output of legs that produced *bounds and gaps* rather than a verdict.

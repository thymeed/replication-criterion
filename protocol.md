# Protocol: the replication criterion

**Version 0.1, 2026-10-14.** Written before any source is read, so the criterion
is fixed in advance rather than fitted to whatever the evidence turns out to
show. Same discipline as the sibling `closure-audit`: revisions are new commits
with a stated reason, never quiet edits.

The study's folder is named for its question. This repository states the test
that decides it.

---

## 1. The criterion

> **A machine is self-replicating only if every subsystem whose failure would
> stop replication can itself be produced by the machine**, starting from a
> stated bootstrap kit and using only its environment.

Two disqualifiers carry the weight in practice, and they are the two the study
was named for:

- **If it needs a data center, it is not self-replicating.** Computation is a
  critical subsystem. If the controller that sequences replication cannot be made
  by the machine, the machine is a *client* of a semiconductor industry, not a
  replicator.
- **If it needs a reactor, it is not self-replicating.** A power plant is a
  critical subsystem. If its energy conversion cannot be made by the machine, the
  machine is a *client* of an energy industry.

These are **one criterion, not two.** Both name the same failure: a dependency on
infrastructure the machine cannot reach from where it starts.

---

## 2. Why mass closure is the wrong measure

The established literature measures **mass** closure. To see why that is silent
on this question, put the numbers side by side:

- NASA CP-2255: a 100-ton seed factory at ~90–96% materials closure, with the
  microelectronics, ball bearings and precision instruments excluded as
  "vitamin parts", and an electronics line of about **3 tons**, i.e. ~3% of the
  seed.
- RepRap: **48%** self-manufacture **by part count**, with electronics, stepper
  motors, bearings and the hot end excluded.

A study can therefore report **90–96% mass closure while excluding 100% of the
subsystem that makes it a machine.** The excluded fraction is small in mass and
total in function. Mass closure and functional closure are different measures,
and the literature reports the one that does not discriminate.

This is not a criticism of those studies. It is the reason a **second** measure
is needed, and §3 states it.

---

## 3. The formal statement

Define four things:

- **K**: the bootstrap kit: what the machine is allowed to start with, in
  finished form.
- **E**: the environment: what the machine can harvest and process.
- **C(K, E)**: the productive closure: the set of things the machine can
  *make*, given K, using E.
- **S(M)**: the critical subsystems of machine M (§4).

> **M is self-replicating iff S(M) ⊆ C(K, E).**

The criterion is therefore not *"can it make all of itself"*, no machine can,
because every machine needs *some* starting point. It is **"can it make the
parts it cannot do without."** The interesting content is always in the
difference between K and C(K, E), and in whether the critical subsystems fall on
the inside.

---

## 4. What counts as a critical subsystem

The definition must be portable, so it is stated in two clauses:

> **A subsystem is critical if (a) its failure stops replication, and (b) the
> environment does not supply it in finished form.**

Three candidates, by inspection of what any self-replicating machine must do:

- **Control**: sense, decide, sequence, regulate.
- **Power conversion**: turn an available energy flow into work.
- **Structure and tooling**: bear load, hold geometry, shape material.

Clause (b) is the sharp line, and it is worth stating what it excludes:

- **Environmental energy is not a subsystem; the converter is.** Sunlight,
  flowing water and wind arrive free. The *water wheel* that turns falling water
  into shaft work is a subsystem, and must be inside C(K, E). The *photovoltaic
  panel* that turns sunlight into current is a subsystem, and must be inside
  C(K, E). This is why the criterion admits a water wheel and condemns a solar
  cell without any special pleading, the difference is what each converter is
  made of, not what it runs on.
- **Starting material is not a subsystem, because K names it.** K is allowed to
  contain iron, glass, tooling, and so on. The question is never "does it use
  anything?", every machine does. The question is whether the things it uses
  *and cannot make* include a critical subsystem.

---

## 5. "Data center", defined operationally

> **Semiconductor-grade fabrication:** single-crystal silicon or a comparable
> compound semiconductor, sub-micron lithography, high-vacuum process,
> ultra-pure chemistry, and the metrology those require.

A microcontroller, a diode, an LED, an image sensor and a **photovoltaic cell**
all sit behind this same wall. The criterion does not measure the price of a
chip or the size of a fab; it asks whether the machine can make one. **A machine
that needs any semiconductor needs a semiconductor industry**, whether it is one
transistor or a server farm.

This is deliberately not a threshold on *compute power*. The disqualifier is the
fabrication dependency, not the clock speed.

---

## 6. "Reactor", defined operationally

> **A power-conversion plant whose critical components lie outside C(K, E).**

- **Fission and fusion** are the plain cases: the fuel cycle, the moderator, the
  containment, the control rods.
- **Solar-electric and thermoelectric** conversion is condemned by §5 instead,
  those converters are semiconductor or exotic-materials devices.
- **Combustion, wind and water** are admitted **if and only if** their converter
, boiler, turbine, wheel, and above all the **generator**, is inside C(K, E).
  The generator is the interesting case, because it may need magnets (§7).

So "reactor" is deliberately a synecdoche. The criterion is not about nuclear
physics. It is about **a power plant you cannot build.**

---

## 7. The boundary cases that decide the answer

These are where the criterion earns its keep, and where it may turn out to be
undecidable from the literature, which is a result and will be reported as one.

- **Magnetic materials.** Electromagnetic generation wants strong permanent
  magnets or reliable soft-iron cores. The sibling repo's materials finding puts
  both **outside** a pre-industrial closure (high-performance magnets and
  consistent soft-iron cores both need industrial metallurgy). If that holds, a
  **dynamo is condemned**: while a **water wheel driving a line shaft** (no
  magnet, no electricity at all) is not. This single boundary case may decide the
  power leg, and it means the power leg and the control leg are constrained by
  the **same** materials boundary. See `audit.md`.
- **Stationary vs mobile.** A mobile machine must carry its energy or convert it
  in a moving frame. Both tend to force a battery (industrial electrochemistry)
  or a compact high-performance converter. **Hypothesis, to be tested:** mobility
  is itself a disqualifier, and only a site-bound replicator can meet the
  criterion. This is a finding to be earned, not assumed.
- **Human labour.** If a person is a subsystem, the machine is not autonomous. If
  labour is *outside* the machine, then a workshop that needs a machinist is not
  self-replicating. The sibling repo prices this at ~10³ person-hours per
  generation and finds nobody else prices it at all. **Decision, registered
  here:** a human operator is part of K, not a subsystem of M. The consequence is
  stated plainly rather than hidden, a machine that requires an operator is
  *replicable by an operator*, and the criterion asks only about M.

---

## 8. Strength of replication, and why K must be named

Three grades, in decreasing order of what is given:

1. **Factory-given**: the machine is handed a full industrial supply chain.
   This does **not** meet the criterion; it *is* the dependency the criterion
   names.
2. **Bootstrap**: the machine is given a minimal kit plus its environment, and
   must build the rest.
3. **From-nothing**: raw ore, sunlight, and no tooling at all. Likely
   impossible: you need *some* tooling to make tooling, so grade 3 probably has
   an empty C(K, E) for any real K. The honest target is grade 2.

**The criterion is meaningless without K, because "a data center" is just a large
K.** So every claim in this repository names K. The K used here is the
**pre-industrial closure** the sibling repo established:

> **K** = iron and steel (bloomery smelting + carburising), copper, brass
> (calamine), glass, clay and refractories, wood, leather, natural rubber,
> charcoal; hand tools; and human skill.

Everything outside that set, aluminium at scale, titanium, pure semiconductors,
plastics and synthetic rubber, refined contact metals, high-performance magnets,
consistent soft-iron cores, is **not in K** and must be reached by C(K, E) or
the machine fails the criterion.

---

## 9. What would falsify the criterion

The criterion is a definition, so it cannot be falsified by evidence, but **its
application** can, and these are the tests:

- **A positive case.** A demonstrated machine that needs neither a data center
  nor a reactor, whose critical subsystems can all be made, would show the
  criterion is **satisfiable**. That would be this study's headline.
- **A semiconductor-free controller with cascade gain above ~3** would move the
  control boundary and unblock leg 1.
- **A generator built from pre-industrial materials** would move the power
  boundary and unblock leg 3.

Conversely, the criterion is **not** falsified by the fact that no such machine
exists. Absence of a demonstration is not a proof of impossibility, and this
repository will not present it as one. The honest negative result is *"no
demonstrated machine meets the criterion, and here is where each attempt stops"*,
not *"therefore impossible."*

---

## 10. What this criterion does not claim

- **Not** that self-replication is impossible. It defines a test, not a verdict.
- **Not** that a data center or a reactor is bad engineering. Both are excellent
  engineering. They are simply **not self-replicating**, which is a different
  claim.
- **Not** a claim about any specific machine, until one is tested against §3.
- **Not** a claim that grade 3 (from-nothing) is the target. It is not.

---

## 11. Known limitations, stated before the data

- **The boundary is coarse.** "Critical subsystem" and "semiconductor-grade" are
  broad. A machine that makes *some* of its control and imports the rest will be
  hard to place, and that case will be recorded rather than forced.
- **K-dependence.** Every result is relative to a K. A different K gives a
  different answer, which is a feature (it makes the dependency visible) and a
  hazard (it invites moving K to get the answer you want). K is fixed in §8
  before the evidence is read, for that reason.
- **It is a definition, not an experiment.** The criterion can be *applied* but
  not *measured*. Where the literature is silent, the output is a stated gap.
- **No simulation.** The sibling `copy-fidelity` forbids simulation of a physical
  process it cannot represent, and the sibling `Fluidic Bootstrap Project`'s
  central failure was a solver run far outside its validity range. The same rule
  holds here: the output is literature analysis and arithmetic, or an explicit
  "unknown".

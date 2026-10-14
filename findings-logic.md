# Findings: the logic leg, and the element count the study could not supply

**Version 0.1, 2026-10-14.** Derives the one quantity the sibling feasibility
study priced per unit but could never multiply: the number of logic elements in
the controller that sequences a replication cycle. The sibling carries
`GATE_COUNTS = (20, 100)` in `src/labour.py` and tags them, in its own words, as
"a parameter, not a constant". This leg replaces the parameter with a
derivation.

Method: arithmetic on a stated logic netlist, in `model/controller_budget.py`.
`protocol.md` section 11 forbids simulating a physical process, and nothing here
does. The inputs are logic parameters (step count, condition count, fan-out) and
the outputs are element counts. The one physical number used is the fan-out, and
it is sourced, not modelled.

---

## 0. Evidence tier, stated first

- **`[sourced]`** = the fan-out value, from Belsterling, *Fluidic Systems
  Design* (Wiley, 1971), section 7.3, read directly and recorded in
  `findings-gain.md` section 2.3.
- **`[sourced]`** = the per-element labour prices, from the sibling
  `Fluidic Bootstrap Project`, `src/labour.py`. Quoted unchanged.
- **`[derived]`** = every element count below. The arithmetic is printed and is
  checkable by hand; `python model/controller_budget.py --verify` runs the
  self-checks.
- **No number here is a measurement.** The step count of a real replication
  cycle is not known to this study or, as far as the sibling's search reached,
  to anyone. It is swept, and the sweep is the finding.

---

## 1. The result, in one paragraph

**A replication controller needs roughly four elements per step of the cycle.**
For a cycle of N sequential gated operations at fan-out 3, the count is N state
latches, N transition gates, and about 2N buffer elements for the signals that
fan out. For a cycle of 10 to 50 steps, that is **45 to 200 elements**. The
sibling's two invented counts invert to a **6-step cycle and a 26-step cycle**,
so its lower count sits below anything that could sequence a replication, and its
upper count is about right for one subsystem. Plugged into the sibling's own
per-element prices, a controller at the derived count is **roughly 40 to 50 per
cent of the labour of one generation**, where the sibling's floor implied a much
smaller share. And the fan-out limit, the quantity the study called a wall,
appears in this model as a **doubling of the element count**: a cost with a
number attached, not an impossibility.

---

## 2. The structure being counted

A replication controller is a finite-state sequencer. One replication cycle is a
sequence of operations carried out in order, each gated on conditions that must
hold before it starts. That decomposes into three parts.

- **State.** One element per step the controller must remember. Wall attachment
  latches (`findings-gain.md` section 2.2), so a state element is a bistable
  flip-flop, one element per step, plus one for reset.
- **Transitions.** One gate per step, computing "this step is active AND its
  condition holds". Where a step is gated on several conditions, combining them
  costs one gate per extra condition.
- **Distribution.** Buffers. One signal, the reset line or a shared condition,
  must reach many steps, and one element drives only F successors.

Only the third part meets the fan-out limit, and its cost has a closed form.

---

## 3. The arithmetic `[derived]`

**Buffer tree.** To drive `L` loads from one signal at fan-out `F`, the source
drives `ceil(L/F)` buffer elements, each of which drives `F` more, and so on
until the remaining count is within `F`. The buffer count is the number of
internal tree nodes: for the balanced tree it is `(L-1)/(F-1)`, and the
level-by-level construction in the model gives the exact count for the uneven
case. The depth is `ceil(log_F L)`.

Three cases, each checkable:

- `L = 3, F = 3` gives 0 buffers. The source drives all three loads directly.
- `L = 9, F = 3` gives 3 buffers over one level. The source drives three
  buffers, each driving three loads.
- `L = 20, F = 3` gives 10 buffers over two levels. Seven buffers at the first
  level and three at the second, because the source cannot drive seven directly.

**Fan-out 1 is refused, not counted.** An element that drives exactly one
successor cannot branch, so no signal reaches two places and the controller does
not exist. That is a property of the element, not an arithmetic edge case, and
the model raises rather than returning a large number.

**Element count by cycle length** (one-hot encoding, three shared signals, each
reaching every step, fan-out 3):

- 10 steps: 11 state + 10 transition + 24 buffer = **45**
- 20 steps: 21 + 20 + 40 = **81**
- 25 steps: 26 + 25 + 48 = **99**
- 50 steps: 51 + 50 + 100 = **201**
- 100 steps: 101 + 100 + 208 = **409**

The ratio is close to 4 per step across the range.

**Two observations from the table.**

- **Distribution is about as large as the sequencing logic.** At 20 steps the
  buffers are 40 elements against 41 of state and transitions. So fan-out 3
  nearly doubles the element count. The study called fan-out a wall; in this
  model it is a doubling, which is the difference between a limit and a price.
- **Depth is logarithmic, so the fan-out penalty is not paid in time.** Depth
  is 2 levels at 20 steps, 3 at 50, 4 at 100. With the sibling's switching
  figure of 2 to 8 ms per element (`spec/constants.py`, from Olivotto 2010), a
  decision takes about 4 to 16 ms at 20 steps. A replication cycle is a sequence
  of mechanical operations measured in hours or days, so logic latency is
  negligible beside it. Fan-out costs elements, not throughput.

**Encoding barely matters.** Binary encoding uses `ceil(log2 N)` state elements
instead of `N`, but needs one decoder gate per step, and the two costs almost
cancel. At 20 steps one-hot gives 81 elements and binary gives 87. Stated because
it removes a choice: for a fluidic sequencer the simple encoding is not the
expensive one.

---

## 4. What the sibling's invented counts imply `[derived]`

Inverting the model for the sibling's two counts:

- **20 elements corresponds to a 6-step cycle.**
- **100 elements corresponds to a 26-step cycle.**

The sibling's own labour table lists ten machine-shop operations (foundry, lathe,
shaper, mill, drill press, dividing head, brake, scraping, patterns, moulding),
and each of those is itself a sequence of steps. A six-step cycle cannot sequence
that. So the floor of the sibling's range is below anything that could sequence a
replication, and the upper count is plausible for a single subsystem.

The honest derived band, for a cycle of 10 to 50 steps, is **45 to 200 elements**.
That brackets the sibling's range and then exceeds it. The right value to quote
is the top of its band or above, not the bottom.

---

## 5. Fan-out is a cost with a number, not a wall

Holding the cycle at 20 steps and varying fan-out:

- fan-out 2: 123 elements
- fan-out 3: 81 elements (the documented design case)
- fan-out 4: 70 elements
- fan-out 5: 58 elements
- fan-out 1: no branching is possible

So the difference between the documented fan-out of 3 and a hypothetical fan-out
of 2 is about half again as many elements. The study's own corrected verdict was
that fluidic logic "cascades with shallow fan-out". This leg prices the shallow
fan-out: it is a modest tax on the element count, and it does not stop the
controller being built.

---

## 6. The labour this implies `[derived]`

Using the sibling's own prices unchanged (per element, make and assemble 3 to 12
person-hours; circuit debug 50 to 200 person-hours per controller), and the
sibling's own machine-shop subtotal of 480 to 1340 person-hours:

- 10-step cycle, 45 elements: control 185 to 740 hours, **28 to 36 per cent** of
  the generation.
- 25-step cycle, 99 elements: control 347 to 1388 hours, **42 to 51 per cent**.
- 50-step cycle, 201 elements: control 653 to 2612 hours, 58 to 66 per cent.
- 100-step cycle, 409 elements: control 1277 to 5108 hours, 73 to 79 per cent.

**The number the study did not have:** for the derived band, the control system
is roughly **40 to 50 per cent** of the labour of one generation.

The sibling priced the control system at 20 elements and reported 110 to 440
person-hours for it. At the derived count the same prices give about three times
that, so the subsystem's floor was low by roughly a factor of three and its share
of the total was understated. The order of magnitude of the whole generation (10
cubed person-hours) survives, because the machine shop dominates it at the lower
cycle lengths. A longer cycle pushes the controller toward being most of the
labour.

---

## 7. What would change this, and what is ABSENT

1. **A measured wall-attachment fan-out.** The whole model is conditional on
   fan-out 3, which is a documented *design case* rather than a measured limit
   (`findings-gain.md` section 5). If the measured fan-out is 1, this controller
   does not exist, and that becomes the finding. If it is 2, add about half to
   the element count. One measurement on one element settles it.
2. **A real cycle specification.** **ABSENT.** No source reached by this study or
   by the sibling specifies the step sequence of a replication cycle. The step
   count is a parameter and every number scales with it. Section 4 shows what
   each candidate count implies.
3. **Whether a shared condition must reach every step.** The model assumes it
   does, which is the pessimistic case. A condition read by only some steps costs
   less, and the buffer column is the part that shrinks.
4. **Sensor and actuator elements.** **ABSENT from this model.** It counts the
   sequencing logic only. The elements that sense position, force or presence,
   and the elements that drive the machine's actuators, are additional and are
   not counted here. The number is therefore a floor for the control subsystem,
   not its total.
5. **The recovery and trimming overhead.** The sibling's debug range, 50 to 200
   hours per controller, is carried unchanged. It is an estimate, and at multi
   hundred element counts it may scale with the element count rather than staying
   flat. Left as the sibling wrote it, and named here as a possible understatement.

None of the first three is a wall. Each is a quantity, and the first is a single
measurement on a single element.

---

## 8. Reproducing this

```
python model/controller_budget.py            the full report
python model/controller_budget.py --verify   self-checks, hand-checkable
```

No dependencies. Standard library only, Python 3.8 or later. The three
hand-checkable buffer cases are asserted in `verify()`, along with monotonicity
in the cycle length and the refusal of fan-out 1.

---

## 9. Sources

- **Belsterling, Charles A. (1971), *Fluidic Systems Design*, Wiley**, section
  7.3, "Matching a Digital Amplifier with Three Parallel Flip-Flops". Read
  directly; recorded in `findings-gain.md` section 2.3. Quoted there in short
  phrases, not held here.
- **Sibling repository `Fluidic Bootstrap Project`**, `src/labour.py` (the
  per-element prices, the debug range, and the `GATE_COUNTS` parameter) and
  `spec/constants.py` (the 2 to 8 ms switching figure, from Olivotto 2010).
- **This repository**, `findings-control.md` (control composes) and
  `findings-gain.md` (fan-out 3 is a worked design case; gain is above parity).

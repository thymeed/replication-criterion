"""
model/controller_budget.py -- how many elements a replication controller needs
==============================================================================

The question
------------
findings-control.md shows that non-semiconductor control composes, and
findings-gain.md shows that a fluidic element drives about three successors.
Neither answers the question that sets the labour price: **how many elements
does the controller of one replication cycle contain?**

The sibling `Fluidic Bootstrap Project` prices per-element labour in
`src/labour.py`, but multiplication needs a count and it has none. It carries
`GATE_COUNTS = (20, 100)` and tags them, in its own words, as a parameter and not
a constant. This module derives the count from the structure of the controller
instead of assuming it.

What this is, and what it is not
--------------------------------
This is arithmetic on a logic netlist. It counts elements and buffer-tree nodes
in a stated structure, and prints every formula so a reader can check it by hand.

It is **not** a simulation of a physical process. `protocol.md` section 11
forbids modelling fluid, pressure, time or geometry, and nothing here does. The
inputs are logic parameters (step count, condition count, fan-out), and the
outputs are element counts. The one physical number it uses is the fan-out, and
that number is sourced rather than modelled.

The structure modelled
----------------------
A replication controller is a finite-state sequencer. One replication cycle is a
sequence of N operations carried out in order, each one gated on conditions that
must hold before it starts. That gives three parts:

1. **state.** One element per step that must be remembered. A wall-attachment
   element is bistable, so the element is a latch (findings-gain.md section 2.2).
2. **transitions.** One gate per step, computing "this step is active AND its
   condition holds".
3. **distribution.** Buffers, because one signal must reach many steps and one
   element drives only F successors.

Part 3 is where the fan-out limit enters, and its cost is known in closed form.

How to run
----------
    python model/controller_budget.py            the report
    python model/controller_budget.py --verify   self-checks, hand-checkable
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple


# ===========================================================================
# 1. the one sourced number
# ===========================================================================

# Belsterling, Fluidic Systems Design (Wiley, 1971), section 7.3, is titled
# "Matching a Digital Amplifier with Three Parallel Flip-Flops" and works the
# case. It was read directly and is recorded in findings-gain.md section 2.3.
# Three is therefore a documented design point rather than an assumption. The
# text prints no maximum, so three is used as a conservative operating value and
# swept in section 5.
FANOUT_DOCUMENTED: int = 3

# The relay route, for comparison. A multipole relay switches one separate
# circuit per contact set, so its fan-out is its contact count. Harvard Mark I
# had "3,500 multipole relays with 35,000 contacts" (Wikipedia, *Harvard Mark I*,
# quoting IBM Archives; tertiary, read directly 2026-10-17), an average of ten.
# That is an average over a machine, not a per-relay maximum, and it counts
# contacts, not loads one contact can drive. findings-control.md section 7.
FANOUT_RELAY: int = 10


def buffer_tree(loads: int, fanout: int) -> Tuple[int, int]:
    """Elements needed to drive `loads` inputs from one signal at `fanout`.

    One element drives at most `fanout` inputs. To reach more, it drives
    `ceil(loads/fanout)` buffer elements, each of which drives `fanout` more,
    and so on until the remaining count is within `fanout`. The buffer count is
    the number of internal tree nodes this produces, and the depth is the number
    of levels added.

    Returns (buffer_elements, depth).

    Fan-out 1 is refused rather than given a number, because the answer is not a
    large count. An element that drives exactly one successor cannot branch, so
    no signal reaches two places and the structure does not exist. That is a
    result about the element, not an arithmetic edge case.
    """
    if fanout < 2:
        raise ValueError(
            f"fan-out {fanout} admits no branching: one element drives one "
            "successor, so a signal cannot reach two loads. No tree exists."
        )
    if loads <= fanout:
        return 0, 0
    elements = 0
    depth = 0
    level = loads
    while level > fanout:
        level = math.ceil(level / fanout)
        elements += level
        depth += 1
    return elements, depth


# ===========================================================================
# 2. the controller, as a netlist
# ===========================================================================

@dataclass(frozen=True)
class Controller:
    """One replication cycle's sequencing logic, described as counts.

    steps            operations in the cycle, carried out in order
    shared_signals   global conditions read by more than one step, for example
                     "workpiece present" or "position reached"
    shared_loads     steps each shared signal must reach
    extra_conditions additional per-step conditions beyond one, each costing
                     one AND to combine
    encoding         "one-hot" or "binary"
    fanout           successors one element drives
    """

    steps: int
    shared_signals: int = 0
    shared_loads: int = 0
    extra_conditions: int = 0
    encoding: str = "one-hot"
    fanout: int = FANOUT_DOCUMENTED

    def state(self) -> int:
        """Elements that hold the current step.

        One-hot: one latch per step, plus one latch for the start/reset state.
        Binary: ceil(log2 N) latches, plus a decoder gate per step, because each
        step needs its own output anyway. The two encodings cost about the same
        here, which is itself worth knowing: for a fluidic sequencer the simple
        encoding is not the expensive one.
        """
        if self.encoding == "one-hot":
            return self.steps + 1
        if self.encoding == "binary":
            return math.ceil(math.log2(self.steps)) + self.steps
        raise ValueError(f"unknown encoding {self.encoding!r}")

    def transitions(self) -> int:
        """One AND per step, plus one per extra condition to be combined."""
        return self.steps + self.extra_conditions

    def distribution(self) -> Tuple[int, int]:
        """Buffers for the signals that fan out, and the worst depth.

        Two signal groups fan out: the reset line, which reaches every latch,
        and each shared condition, which reaches `shared_loads` steps.
        """
        total = 0
        worst_depth = 0
        reset, d = buffer_tree(self.state(), self.fanout)
        total += reset
        worst_depth = max(worst_depth, d)
        if self.shared_signals and self.shared_loads:
            per_signal, d = buffer_tree(self.shared_loads, self.fanout)
            total += self.shared_signals * per_signal
            worst_depth = max(worst_depth, d)
        return total, worst_depth

    def elements(self) -> int:
        buffers, _ = self.distribution()
        return self.state() + self.transitions() + buffers

    def breakdown(self) -> dict:
        buffers, depth = self.distribution()
        return {
            "state": self.state(),
            "transitions": self.transitions(),
            "buffers": buffers,
            "total": self.state() + self.transitions() + buffers,
            "depth": depth,
        }


def cycle(steps: int, **kw) -> Controller:
    """A controller whose shared signals each reach every step.

    This is the pessimistic reading of a shared condition, and it is the one to
    quote, because a condition that only some steps read costs less.
    """
    kw.setdefault("shared_signals", 3)
    kw.setdefault("shared_loads", steps)
    return Controller(steps=steps, **kw)


# ===========================================================================
# 3. from element count to person-hours  (the sibling's prices, unchanged)
# ===========================================================================

# From the sibling `Fluidic Bootstrap Project`, src/labour.py. Per element: make
# (engrave two plates) 2.0-8.0 hours, assemble and seal 1.0-4.0 hours. Circuit
# debug and threshold trimming is a single ranged cost per controller.
# Quoted, not re-derived. If the sibling's prices change, change them there and
# update this copy.
HOURS_PER_ELEMENT: Tuple[float, float] = (3.0, 12.0)
HOURS_DEBUG: Tuple[float, float] = (50.0, 200.0)


def control_hours(elements: int) -> Tuple[float, float]:
    return (elements * HOURS_PER_ELEMENT[0] + HOURS_DEBUG[0],
            elements * HOURS_PER_ELEMENT[1] + HOURS_DEBUG[1])


# The sibling's machine shop subtotal, summed from its own MACHINE_SHOP table in
# src/labour.py. Included so the control share can be stated against a total.
MACHINE_SHOP_HOURS: Tuple[float, float] = (480.0, 1340.0)


# ===========================================================================
# 4. the report
# ===========================================================================

def _table(rows: List[Tuple[str, str]], width: int = 30) -> List[str]:
    return [f"  {a:<{width}} {b}" for a, b in rows]


def report() -> str:
    out: List[str] = []
    add = out.append

    add("=" * 78)
    add(" CONTROLLER BUDGET  --  elements per replication cycle")
    add(" Arithmetic on a logic netlist. Not a physical simulation.")
    add("=" * 78)
    add("")
    add("THE STRUCTURE")
    add("-" * 78)
    add("  state        one latch per step, plus a reset latch")
    add("  transitions  one AND per step, computing active AND condition-holds")
    add("  distribution buffer trees, so one signal can reach many steps")
    add("")
    add(f"  fan-out      {FANOUT_DOCUMENTED} successors per element")
    add("               Belsterling 1971 section 7.3, a worked design case,")
    add("               read directly. No maximum is printed in the text, so")
    add("               this is a conservative operating value, swept below.")
    add("")

    add("ELEMENT COUNT BY CYCLE LENGTH  (one-hot, 3 shared signals)")
    add("-" * 78)
    add(f"  {'steps':>6} {'state':>7} {'trans':>7} {'buffers':>8} "
        f"{'TOTAL':>7} {'depth':>6}")
    for n in (5, 10, 20, 25, 50, 100, 200):
        c = cycle(n)
        b = c.breakdown()
        add(f"  {n:>6} {b['state']:>7} {b['transitions']:>7} "
            f"{b['buffers']:>8} {b['total']:>7} {b['depth']:>6}")
    add("")
    add("  The buffer column is the fan-out cost, and it is not small: at 20")
    add("  steps it is comparable to the sequencing logic itself. Distribution")
    add("  roughly doubles the element count. Fan-out three is therefore a real")
    add("  tax on the design, and not a wall to it.")
    add("")

    add("WHAT THE SIBLING'S INVENTED COUNTS CORRESPOND TO")
    add("-" * 78)
    add("  src/labour.py carries GATE_COUNTS = (20, 100), tagged 'not known'.")
    add("  Inverting this model, those two counts correspond to:")
    add("")
    for target in (20, 100):
        n = 1
        while cycle(n).elements() < target and n < 400:
            n += 1
        add(f"    {target:>3} elements  ->  a {n}-step cycle")
    add("")
    add("  The sibling's own labour table lists ten machine-shop operations")
    add("  (foundry, lathe, shaper, mill, drill press, dividing head, brake,")
    add("  scraping, patterns, moulding), and each of those is itself a")
    add("  sequence. A cycle of six steps cannot sequence that, so the floor of")
    add("  the sibling's range, 20 elements, is below anything that could")
    add("  sequence a replication. The upper count, 100, lands on a 26-step")
    add("  cycle, which is plausible for one subsystem.")
    add("")
    add("  Derived for a cycle of 10 to 50 steps: 45 to 200 elements. That")
    add("  brackets the sibling's range and then exceeds it, so the honest")
    add("  figure is the top of its band or above, not the bottom.")
    add("")

    add("FAN-OUT SENSITIVITY  (20 steps, 3 shared signals)")
    add("-" * 78)
    add(f"  {'fan-out':>7} {'TOTAL':>7} {'buffers':>8}   note")
    for f in (2, 3, 4, 5):
        c = cycle(20, fanout=f)
        b = c.breakdown()
        note = ""
        if f == FANOUT_DOCUMENTED:
            note = "documented design case"
        add(f"  {f:>7} {b['total']:>7} {b['buffers']:>8}   {note}")
    add("  " + f"{1:>7} {'--':>7} {'--':>8}   no branching is possible")
    add("")
    add("  Halving the fan-out from 3 to 2 costs about half again as many")
    add("  elements. That is the whole shape of the constraint the sibling")
    add("  called a wall: it is a cost, and a modest one.")
    add("")

    add(f"THE RELAY ROUTE  (same netlist, fan-out {FANOUT_RELAY})")
    add("-" * 78)
    add(f"  {'steps':>6} {'fluidic':>8} {'relay':>7} {'relay buffers':>14}")
    for n in (10, 20, 25, 50, 100):
        f = cycle(n).breakdown()
        r = cycle(n, fanout=FANOUT_RELAY).breakdown()
        add(f"  {n:>6} {f['total']:>8} {r['total']:>7} {r['buffers']:>14}")
    add("")
    add("  A multipole relay drives about ten circuits (Harvard Mark I average),")
    add("  so most of the buffer column disappears and a relay controller needs")
    add("  50 to 60 per cent of the fluidic element count. This is an upper")
    add("  bound: a relay forms AND from contacts in series, so the transition")
    add("  gates are partly free. No labour figure is given, because no source")
    add("  reached prices a hand-built relay. Per-relay hours and contact life")
    add("  are ABSENT (findings-control.md section 7).")
    add("")

    add("THE LABOUR THIS IMPLIES  (sibling prices, unchanged)")
    add("-" * 78)
    add(f"  per element, make and assemble   {HOURS_PER_ELEMENT[0]:.0f}"
        f"-{HOURS_PER_ELEMENT[1]:.0f} person-hours")
    add(f"  circuit debug, per controller    {HOURS_DEBUG[0]:.0f}"
        f"-{HOURS_DEBUG[1]:.0f} person-hours")
    add("")
    add(f"  {'cycle':>6} {'elements':>9} {'control hours':>16} "
        f"{'share of generation':>20}")
    for n in (10, 25, 50, 100):
        c = cycle(n)
        e = c.elements()
        clo, chi = control_hours(e)
        tlo = MACHINE_SHOP_HOURS[0] + clo
        thi = MACHINE_SHOP_HOURS[1] + chi
        share = f"{100.0 * clo / tlo:.0f}-{100.0 * chi / thi:.0f}%"
        add(f"  {n:>6} {e:>9} {clo:>7.0f}-{chi:<8.0f} {share:>20}")
    add("")
    add("  Machine-shop subtotal, from the sibling's own table: "
        f"{MACHINE_SHOP_HOURS[0]:.0f}"
        f"-{MACHINE_SHOP_HOURS[1]:.0f} person-hours.")
    add("")
    add("  For the derived band (a 20 to 26 step cycle, about 80 to 100")
    add("  elements) the control system is **roughly 40 to 50 per cent of the")
    add("  labour of one generation**. That is the number the study did not have.")
    add("  It priced the control system, the 'data center' it was named for, but")
    add("  could not multiply without an element count, so its figure for that")
    add("  subsystem was too low by about a factor of three, and its share of")
    add("  the total was understated. A longer cycle pushes the share up: at 100")
    add("  steps the controller is most of the labour.")
    add("")

    add("WHAT WOULD CHANGE THIS")
    add("-" * 78)
    add("  1. A measured wall-attachment fan-out. If it is 1, this design does")
    add("     not exist, and that is the finding. If it is 2, add about half.")
    add("     Three is the sourced value and the one used here.")
    add("  2. A real cycle specification. The step count is a parameter, and")
    add("     every number above scales with it. The inversion above shows what")
    add("     each candidate count implies.")
    add("  3. Whether a shared condition must reach every step. The model")
    add("     assumes it does, which is the pessimistic case.")
    add("")
    add("  None of these is a wall. Each is a quantity, and the first is a")
    add("  single measurement on one element.")
    add("=" * 78)
    return "\n".join(out)


# ===========================================================================
# 5. self-checks
# ===========================================================================

def verify() -> None:
    """Assertions a reader can check by hand."""

    # A signal driving within the fan-out needs no buffer.
    assert buffer_tree(3, 3) == (0, 0)
    # Nine loads at fan-out 3: three buffers, one level, source drives three.
    assert buffer_tree(9, 3) == (3, 1)
    # Twenty loads at fan-out 3: ten buffers over two levels.
    assert buffer_tree(20, 3) == (10, 2)
    # Fan-out 1 cannot branch at all.
    for loads in (2, 5, 20):
        try:
            buffer_tree(loads, 1)
        except ValueError:
            pass
        else:
            raise AssertionError("fan-out 1 must be refused")

    # The two encodings cost nearly the same, which is the point of stating
    # both: the simple one is not the expensive one.
    a = cycle(20, encoding="one-hot").elements()
    b = cycle(20, encoding="binary").elements()
    assert abs(a - b) / a <= 0.10, (a, b)

    # Monotone in cycle length.
    prev = 0
    for n in range(5, 60):
        e = cycle(n).elements()
        assert e > prev, n
        prev = e

    # The sibling's lower count corresponds to a cycle too short to sequence
    # even its own ten-item machine-shop table.
    n = 1
    while cycle(n).elements() < 20:
        n += 1
    assert n < 10, n

    # Wider fan-out never costs elements: the relay route is no larger.
    for n in (10, 20, 50, 100):
        assert cycle(n, fanout=FANOUT_RELAY).elements() <= cycle(n).elements()

    # Labour is monotone in element count.
    assert control_hours(100)[0] > control_hours(50)[0]

    print("controller_budget: all self-checks passed")


if __name__ == "__main__":
    import sys
    if "--verify" in sys.argv:
        verify()
    else:
        print(report())

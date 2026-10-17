"""
model/closure_graph.py -- which open quantities the verdict actually turns on
=============================================================================

The question
------------
Each leg of the study ends at a quantity nobody has measured. The legs are not
independent: precision is load-bearing for both control and structure, a dynamo
and a relay share winding insulation, and every route needs shaft power. Read one
leg at a time, every open quantity looks equally important. This module puts the
legs in one table and asks which measurements decide the criterion.

What this is, and what it is not
--------------------------------
Bookkeeping on the findings documents. Each node is either a requirement that
needs ALL of its children, a choice that needs ANY one of them, or a leaf whose
status a findings document already states. Nothing is measured or modelled here,
and no status is set by this module: every leaf cites the section that sets it.
Change a status there first, then here.

How it answers
--------------
Leaves are in, open, or out. The open ones are enumerated: for each way they
could resolve, the criterion is evaluated. The report gives

- the minimal sets of open quantities that, if all resolve in, make the
  replicator meet the criterion, and
- the open quantities whose failure alone condemns it.

How to run
----------
    python model/closure_graph.py            the report
    python model/closure_graph.py --verify   self-checks
"""

from __future__ import annotations

import itertools
from typing import Dict, FrozenSet, List, Tuple

IN, OPEN, OUT = "in", "open", "out"

# name: ("all" | "any", [children], note)  or  ("leaf", status, source)
GRAPH: Dict[str, tuple] = {
    "replicator": ("all", ["control", "power", "structure"],
                   "protocol.md 3-4: every critical subsystem inside C(K, E)"),

    "control": ("any", ["fluidic", "relay"], "audit.md Leg 1"),
    "fluidic": ("all", ["fluidic_gain", "fluidic_fanout", "precision",
                        "shaft_power"],
                "air supply is a shaft-driven blower; channels need precision"),
    "fluidic_gain": ("leaf", OPEN,
                     "findings-gain.md 5: power gain of a hand-built element"),
    "fluidic_fanout": ("leaf", OPEN,
                       "findings-logic.md 7.1: measured fan-out of one element"),
    "relay": ("all", ["iron_core", "winding_insulation", "relay_contacts",
                      "electric_supply"], "findings-control.md 2, 7"),
    "relay_contacts": ("leaf", OPEN,
                       "findings-control.md 7.2: platinum, from a placer in E"),
    "electric_supply": ("any", ["voltaic_cell", "dynamo"],
                        "findings-control.md 2.5; findings-power.md 2.2"),
    "voltaic_cell": ("leaf", OPEN,
                     "findings-control.md 5.10: anode metal isolated from ore"),
    "dynamo": ("all", ["iron_core", "winding_insulation", "brush_contacts",
                       "voltaic_cell", "shaft_power"],
               "findings-power.md 2.2; first excitation needs a cell"),
    "brush_contacts": ("leaf", OPEN, "findings-power.md 5.4"),
    "winding_insulation": ("leaf", OPEN,
                           "findings-power.md 5.4; findings-control.md 7.5"),
    "iron_core": ("leaf", IN, "findings-control.md 2.2: wrought iron"),

    "power": ("all", ["shaft_power"], "findings-power.md 1"),
    "shaft_power": ("any", ["water_wheel", "newcomen"], "findings-power.md 2.3"),
    "water_wheel": ("leaf", IN, "findings-power.md 2.3"),
    "newcomen": ("leaf", IN, "findings-power.md 2.3: low precision demand"),

    "structure": ("all", ["bloomery_iron", "tool_making", "precision"],
                  "findings-tooling.md"),
    "bloomery_iron": ("leaf", IN, "findings-tooling.md 2.1"),
    "tool_making": ("leaf", OPEN, "findings-tooling.md 4.1-4.3"),
    "precision": ("all", ["reference_surface", "geometry_drift"],
                  "copy-fidelity findings-transfer.md"),
    "reference_surface": ("leaf", IN,
                          "copy-fidelity: three-plate resets the reference"),
    "geometry_drift": ("leaf", OPEN,
                       "copy-fidelity: reset rate vs drift rate, unmeasured"),
}


def evaluate(node: str, status: Dict[str, str]) -> str:
    """Three-valued: ALL is out if any child is out, ANY is in if any child is in."""
    kind, body, _ = GRAPH[node]
    if kind == "leaf":
        return status.get(node, body)
    vals = [evaluate(c, status) for c in body]
    if kind == "all":
        if OUT in vals:
            return OUT
        return OPEN if OPEN in vals else IN
    if IN in vals:
        return IN
    return OPEN if OPEN in vals else OUT


def open_leaves() -> List[str]:
    return [n for n, (k, s, _) in GRAPH.items() if k == "leaf" and s == OPEN]


def sufficient_sets(root: str = "replicator") -> List[FrozenSet[str]]:
    """Minimal sets of open leaves that, all resolving in, put `root` in.

    Every open leaf outside the set is taken as out, so a set is sufficient on
    its own and does not lean on a lucky result elsewhere.
    """
    leaves = open_leaves()
    found: List[FrozenSet[str]] = []
    for r in range(len(leaves) + 1):
        for combo in itertools.combinations(leaves, r):
            s = frozenset(combo)
            if any(f <= s for f in found):
                continue
            status = {l: (IN if l in s else OUT) for l in leaves}
            if evaluate(root, status) == IN:
                found.append(s)
    return found


def single_points_of_failure(root: str = "replicator") -> List[str]:
    """Open leaves whose failure alone puts `root` out."""
    return [l for l in open_leaves() if evaluate(root, {l: OUT}) == OUT]


def report() -> str:
    out: List[str] = []
    add = out.append
    add("=" * 78)
    add(" CLOSURE GRAPH  --  which open quantities the verdict turns on")
    add(" Bookkeeping on the findings documents. Nothing measured here.")
    add("=" * 78)
    add("")
    add("CURRENT STATUS")
    add("-" * 78)
    for n in ("replicator", "control", "fluidic", "relay", "power",
              "structure", "precision"):
        add(f"  {n:<12} {evaluate(n, {}):<5} {GRAPH[n][2]}")
    add("")
    add("OPEN QUANTITIES")
    add("-" * 78)
    for l in open_leaves():
        add(f"  {l:<19} {GRAPH[l][2]}")
    add("")
    add("FAILURE OF ANY ONE OF THESE ALONE CONDEMNS THE REPLICATOR")
    add("-" * 78)
    for l in single_points_of_failure():
        add(f"  {l}")
    add("")
    add("MINIMAL SETS THAT WOULD CLOSE IT  (every member must resolve in)")
    add("-" * 78)
    for s in sorted(sufficient_sets(), key=lambda s: (len(s), sorted(s))):
        add(f"  {len(s)}:  " + ", ".join(sorted(s)))
    add("")
    add("  Control enters only through its routes, so no single control")
    add("  measurement is decisive: the fluidic and relay routes are")
    add("  alternatives, and each needs all of its own open quantities.")
    add("=" * 78)
    return "\n".join(out)


def verify() -> None:
    for n, (k, body, _) in GRAPH.items():
        if k != "leaf":
            assert all(c in GRAPH for c in body), n

    # ALL and ANY truth tables, on a scratch graph.
    saved = dict(GRAPH)
    try:
        GRAPH.clear()
        GRAPH.update({"a": ("leaf", IN, ""), "b": ("leaf", OPEN, ""),
                      "c": ("leaf", OUT, ""),
                      "ab": ("all", ["a", "b"], ""), "ac": ("all", ["a", "c"], ""),
                      "aa": ("all", ["a", "a"], ""),
                      "bc": ("any", ["b", "c"], ""), "ca": ("any", ["c", "a"], ""),
                      "cc": ("any", ["c", "c"], "")})
        assert [evaluate(n, {}) for n in ("ab", "ac", "aa")] == [OPEN, OUT, IN]
        assert [evaluate(n, {}) for n in ("bc", "ca", "cc")] == [OPEN, IN, OUT]
    finally:
        GRAPH.clear()
        GRAPH.update(saved)

    every = {l: IN for l in open_leaves()}
    assert evaluate("replicator", every) == IN
    assert evaluate("replicator", {}) == OPEN

    # Precision gates both structure and fluidic control, so it must be a
    # single point of failure; a relay-only quantity must not be.
    spof = single_points_of_failure()
    assert "geometry_drift" in spof and "tool_making" in spof
    assert "relay_contacts" not in spof

    for s in sufficient_sets():
        status = {l: (IN if l in s else OUT) for l in open_leaves()}
        assert evaluate("replicator", status) == IN
        for drop in s:
            status[drop] = OUT
            assert evaluate("replicator", status) != IN, (s, drop)
            status[drop] = IN

    print("closure_graph: all self-checks passed")


if __name__ == "__main__":
    import sys
    if "--verify" in sys.argv:
        verify()
    else:
        print(report())

# Handoff — Replication Criterion — 2026-10-14

- **State:** **first pass complete.** The criterion is fixed, applied across the
  three sibling repos, and the one leg none of them covered — **power** — has
  been investigated. The result is a negative-leaning answer about electricity
  and a positive one about shaft power.
- **Landed:** this session's first commits: `protocol.md`, `audit.md`,
  `findings-power.md`, `NOTICE.md`, `LICENSE`, `.gitignore`, `README.md`.
- **Files:** the six documents above. Branch `main`, no remote (matches siblings).
- **Blockers:** none.

## What this repository concluded

The study is named for a dichotomy — *if it needs a data center or a reactor, it
is not self-replicating* — and one half of it (the reactor) had never been
investigated by any sibling repo. `audit.md` shows the three existing repos are
**legs of one argument**; this repo adds the missing fourth.

**The criterion (`protocol.md` §3):** M is self-replicating iff its critical
subsystems (control, power conversion, structure/tooling) are inside C(K, E) —
the productive closure given a named bootstrap kit K. Mass closure is the wrong
measure: a study can report 90–96% mass closure while excluding 100% of the
subsystem that makes it a machine.

**The power leg (`findings-power.md`) — the result:**

- **Condemned by the data-center rule:** every route that turns heat or light
  *directly* into electricity at the point of use. A photovoltaic cell **is** a
  doped p–n junction semiconductor device; thermoelectrics are worse. So
  "needs a reactor" and "needs a data center" **are one dependency** for that
  family.
- **The generator survives, and that is the leg's key finding.** A **self-excited
  dynamo needs no permanent magnet** — it self-starts from residual magnetism in
  its own iron core. The magnet boundary therefore does **not** automatically
  condemn it. The hole is **soft-iron cores** (sibling result: outside the
  closure) and **winding insulation** (ABSENT from the sources).
- **Prime movers survive and are documented:** Newcomen steam (copper/lead/iron
  boiler, brass/iron cylinder, leather + water seal), Watt (needed Wilkinson's
  1774 boring machine — **precision generated, not inherited**), high-pressure
  steam (Trevithick/Evans — the mobility precedent), Stirling/hot-air, **water
  wheels** (strongest single candidate), windmills. All built from in-closure
  materials with hand-generated precision.
- **Mobile vs stationary — the finding the criterion was built for:** a
  **stationary** replicator sited on a watercourse or woodlot is not condemned; a
  **mobile** one is **not shown to meet the criterion**, because mobility forces
  a carried store, and the only in-closure-ish chemistries are the Voltaic pile
  (primary) and lead–acid (feedstock unresolved). *(The recommendation is an
  inference, marked as such.)*
- **Prior literature:** "energy closure" is a **named** requirement (Freitas &
  Merkle 2004, Ch. 5 §5.6, read directly) — and every early proposal satisfies it
  with industrial PV, nuclear, or grid electricity. **ABSENT: any EROI /
  bootstrap-energy / net-energy calculation for a self-replicating machine.**

**The headline, adjusted by evidence (`findings-power.md` §6):** the
pre-leg hypothesis that power fails *before* the cascade wall is **not
established**. The generator's magnet problem dissolves; the residual hole is
materials, not principle. So **the best-evidenced binding constraint remains the
one the sibling repo named — cascade gain, in the control leg, not power.**

## Decisions made — do not re-litigate

- **One criterion, not two.** "Data center" and "reactor" name the same failure:
  dependency on infrastructure the machine cannot reach.
- **K is fixed before the evidence** (`protocol.md` §8): the pre-industrial
  closure. Moving K to get a preferred answer is the named hazard.
- **A human operator is part of K, not a subsystem of M** (§7). Consequence
  stated plainly rather than hidden.
- **No simulation** (`protocol.md` §11), inheriting the sibling rule.
- **Rights: cite, never hold.** No source PDFs, no extractions, no figures, no
  passage longer than a short phrase.

## Known limitations — the weakest tier in the study

`findings-power.md` §0 says it first: this leg is **weaker-evidenced than the
others.** Its principal sources are **encyclopaedia texts** (tertiary) plus one
**primary** (KSRM §5.6). The `[verified]` tag means "read this source's own
text," not "checked its citations." Where a claim rests on an encyclopaedia's
summary of a primary paper (Moore 1956, NASA CP-2255, Lackner & Wendt 1995) it is
tagged `[unverified]`. **Ten ABSENT items are listed in §5 and must not be filled
in with plausible numbers.**

**Re-verify first (§2.2 and §4) if this leg is to reach the tier of
`copy-fidelity`'s Crossref-grade verification.**

## Next step

1. **Raise the power leg's evidence tier** — §2.2 (dynamo) and §4 (prior
   literature) against primary sources.
2. **Close the generator hole** — soft-iron cores and winding insulation
   (`findings-power.md` §5 items 4 and 8). This decides whether the generator
   survives at all.
3. **The cross-repo correction** — **landed** (`Fluidic Bootstrap Project`
   `004585d`, tag `v1.2`), below.
4. Optionally: the mobility leg, currently open.

## Downstream consequence — landed

The **third correction to `Conclusion A.md`** in `Fluidic Bootstrap Project`
has landed: commit `004585d`, tag **`v1.2`**. The three-plate method is a
**rediscovery** of the optics three-flat test, and its error-resetting is
**conditional**, not automatic. Verified in `copy-fidelity/findings-optics.md`
§4.

## Continuation records

- Nothing running. No remote; do not push.
- Sibling repos: `Fluidic Bootstrap Project` (frozen, `v1.1`), `closure-audit`
  (closed, `3645f28`), `copy-fidelity` (verification pass complete).
- This session also removed extracted paper text that had leaked into harness
  scratch state (`.codewhale` transcripts), because the project rule is that
  sources are cited, never held on disk.
- **Refresh live state before acting:** `git log --oneline -5`, `git status`.
  This note is orientation, not authority.

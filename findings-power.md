# Findings: the power leg

**Version 0.1, 2026-10-14.** The result of investigating the one critical subsystem
no sibling repository had touched: **what can power a self-replicating machine
inside the closure the criterion allows.**

Method and criterion: `protocol.md`. Applied context: `audit.md`. Raw working
notes and the retrieved source texts used for tagging are in `_research/`
(working scratch, not published).

---

## 0. Evidence tier, stated first because it limits everything below

This leg is **weaker-evidenced than the other legs of this study**, and saying so
is part of the finding.

- The sibling `copy-fidelity` verification rests on **publisher-deposited
  Crossref records**, the strongest tier available.
- This leg rests mainly on **encyclopaedia text** (principally Wikipedia) plus one
  **primary source read directly**: Freitas & Merkle's *Kinematic
  Self-Replicating Machines* (2004), Chapter 5 §5.6.
- **The `[verified]` tag below means "I read this source's own text."** For
  Wikipedia sources that is a *tertiary* text. Its own underlying citations were
  **not** independently opened. Where a claim rests on a Wikipedia article's
  summary of a primary paper (Moore 1956, NASA CP-2255, Lackner & Wendt 1995),
  it is tagged `[unverified]` at primary level.
- **No number below is estimated.** Where the sources are silent, the entry reads
  **ABSENT**. §5 lists ten such gaps, and they are the honest boundary of this
  leg.

A reader who wants this leg at the tier of the others should treat §2.2 and §4 as
the places to re-verify against primary sources first.

---

## 1. The answer, in one paragraph

**The power leg survives, but only in one family and only in one posture.**
Everything that converts heat or light *directly* into electricity at the point
of use is condemned by the criterion's own rule, because it is a semiconductor
device: a photovoltaic cell is a doped p–n junction, and thermoelectrics are
worse. What remains is the historical power train of the early industrial
revolution, **fire → boiler → reciprocating or hot-air engine → rotating shaft**,
and **falling/moving water or wind → rotating shaft**, every element of which
was built, in the documented record, from iron, brass, copper, lead, wood, leather
and **hand-finished** cylinders. That entire train is inside the closure. The
marginal link is not the prime mover but the **generator**, and the finding there
is specific: a **self-excited dynamo needs no permanent magnet at all**. It
builds its field from the residual magnetism of its own iron core, so the
materials boundary that condemns magnets does **not** automatically condemn a
generator. What it does is leave a hole: reliable soft-iron cores and winding
insulation (§5).

**Net: a stationary replicator, sited on a watercourse or in a woodlot, powered by
an in-closure heat engine, is not condemned. A mobile one is not shown to survive
at all.**

---

## 2. The candidates, and their verdicts

### 2.1 Direct heat/light → electricity: **CONDEMNED**, by the data-center rule

- **Photovoltaics: CONDEMNED.** `[verified]` A solar cell is a semiconductor
  device: a doped **p–n junction**, ~95% of commercial cells being crystalline
  silicon, monocrystalline wafers grown by the **Czochralski** process, the
  feedstock chemically purified to hyper-pure polysilicon. Quantities are not
  trace: ~8–9 g of silicon per watt was reported for 2008-era cells.
  **The point is not purity tier.** The criterion triggers on semiconductor
  *fabrication*, and this is semiconductor fabrication. Solar grade being a lower
  bar than semiconductor grade does not move it inside C(K, E).
- **Thermoelectrics: CONDEMNED, more emphatically.** `[verified]` The workhorse
  material is **bismuth telluride**; the physics *prefers* semiconductors to
  metals; the carrier concentration is set by doping and nonstoichiometry; and
  tellurium availability is itself noted as a limit. Better materials add rare
  earths or nanostructuring. A **metal** thermocouple exists (`[verified]`,
  Seebeck's 1821 two-metal loop) but its conversion efficiency is **ABSENT** from
  the sources, condemned here on the grounds that useful thermoelectrics are
  doped semiconductors, not metals.

**This is the collapse the criterion predicted, and it holds for this family.**
"Needs a reactor" and "needs a data center" are the **same dependency** when the
reactor is a solar or thermoelectric plant.

### 2.2 Electromagnetic conversion: **MARGINAL SURVIVE**, with a named hole

- **Permanent-magnet generator (magneto): CONDENSED TO TOY SCALE.** `[verified]`
  Historically real (Pixii 1832; Woolrich 1842 drove electroplating), but magnetos
  are "limited in size owing to the magnetic flux available from their permanent
  magnets," and modern small-wind versions use neodymium. Natural lodestone is
  **not manufacturable on demand**: it is lightning-magnetised magnetite, and
  only a small fraction of magnetite is magnetised. Condemned as an *engineered*
  power source.
- **Self-excited dynamo: MARGINAL SURVIVE, and this is the leg's key finding.**
  `[verified]` **"Dynamos are self-starting by using residual magnetic field left
  in the iron cores of the electromagnets."** The self-excitation principle
  (Jedlik c. 1856; Wilde, Siemens, Wheatstone, Varley 1866–67) is what made
  high-power generation possible at all; using electromagnets rather than
  permanent magnets "greatly increased the power output." **Materials in the
  historical artefact: iron/steel + copper wire + brass, all in-closure.**
  The **hole**: the sibling materials result puts *reliable soft-iron cores*
  outside the closure, and the **winding-insulation system** of early dynamos is
  **ABSENT** from the sources read. So the generator survives *conditionally*, on
  a materials question this leg could not settle (§5 items 4 and 8).

### 2.3 Prime movers: **SURVIVE**: this is where the leg lands

- **Newcomen steam (1712): SURVIVE.** `[verified]` Copper/lead then riveted-iron
  boiler; cast-brass then cast-iron cylinder; piston sealed by a **leather ring
  plus a standing layer of water on a hand-bored, not-quite-true bore**; hemp
  packing; wood insulation. **Precision demand: low. It worked badly, and that
  was acceptable.** Fuel efficiency numbers are **ABSENT** from the sources.
- **Watt steam: SURVIVE, with a precision caveat that proves the sibling claim.**
  `[verified]` Watt spent five years failing to obtain an accurately bored
  cylinder; Smeaton reported that neither the tools nor the workmen existed to
  make it; it was solved by **Wilkinson's boring machine (1774)**, after which a
  50-inch cylinder was reported accurate to within the thickness of a shilling.
  **This is the historical proof that precision can be *generated* (by a machine
  tool made from in-closure materials), not inherited**, the same mechanism the
  sibling `copy-fidelity` is investigating.
- **High-pressure steam (Trevithick 1802, Evans 1801), SURVIVE, and it is the
  mobility answer.** `[verified]` High-pressure steam was "much more powerful for
  a given cylinder size … and could be made small enough for transport
  applications"; the 1804 locomotive ran on it. **Note what it carried: fuel and
  water, drawn from the environment, not electricity from an industrial supply
  chain.**
- **Stirling / hot-air: SURVIVE at low power; the heat is external.** `[verified]`
  1816 patent; an 1818 engine pumped water at an Ayrshire quarry; confined to
  low-power domestic use for over a century; the 1827 pressurised variant was
  reported unsuccessful. Crucially, **"the hot area of the engine can be warmed
  with any external heat source"**, charcoal, wood or concentrated sun, with no
  change to the machine. Modern high-power versions need helium/hydrogen working
  gas, which is a closure problem.
- **Water wheel: SURVIVE (strongest single candidate).** `[verified]` Wood or
  metal construction; used across the ancient world; ~20% for a flat-board
  undershot wheel (Smeaton); commercial use into the 20th century. Precision
  demand: low. Materials: wood, iron bands, bearings.
- **Water turbine: SURVIVE as an upgrade, with an explicit industrial warning.**
  `[verified]` Roman-era helix-turbine mills (Chemtou, Testour, 3rd–4th c. AD);
  Fourneyron 1827 ~80%; Francis 1849 >90%. But the article itself states the move
  from wheels to turbines "made extensive use of new materials and manufacturing
  methods developed at the time." Survives as an *efficiency* step, not as the
  bootstrap machine.
- **Windmill: SURVIVE (weakest, because intermittent).** `[verified]` Persian
  panemone, 9th century, reed-and-cloth sails; European post mill 12th century;
  tower mill 13th. Precision low; materials wood, cloth, reed, masonry.
- **Solar concentration into a heat engine, SURVIVE in principle; no in-closure
  build found.** `[verified]` Mouchout's 1866 parabolic trough drove a solar steam
  engine; CSP drives a Stirling or steam turbine. Collectors are glass plus
  silvered/polished metal, in-closure *as material*. **Performance of an
  in-closure-built collector: ABSENT.**
- **Muscle: SURVIVE as a bootstrap supplement only.** `[verified]` ~75 W of
  sustained mechanical output per person over an 8-hour shift; treadwheels were
  engines. Enough to bootstrap a workshop, not to run a replication cycle, and it
  is a biological dependency, which `protocol.md` §7 already addresses.

### 2.4 Chemical energy storage: **CONDITIONAL**, and the criterion bites hardest here

- **Voltaic pile: survives as chemistry, condemned as a plant.** `[verified]`
  Copper/zinc discs with brine-soaked separators, 0.76 V per cell, built from
  copper, zinc, cloth and brine. But it is a **primary** (non-rechargeable) cell.
  On the closure question: the requirement is two dissimilar metals and an
  electrolyte, and the sibling materials list carries copper, iron, lead and
  brass. It also carries the zinc *ore*, its brass entry being "calamine process
  (zinc carbonate + copper)". So the couple is not materials-condemned. The
  residual step, isolating the anode metal from its ore, is one process step and
  is **narrowed, not open** (control leg §2.5).
- **Lead–acid: conditional, feedstock unresolved.** `[verified]` Planté 1859,
  the first rechargeable battery; **35–40 Wh/kg** (the only specific energy
  verified anywhere in this leg). Chemistry is lead / lead dioxide / dilute
  sulfuric acid. **Whether lead and sulfuric acid can be produced from a
  pre-industrial base is ABSENT**, and this leg did not assume it.

---

## 3. Stationary vs mobile: the finding the criterion was built to reach

**Stationary: not condemned.** A stationary replicator can be sited *at* the
energy source and use the shaft directly (water wheel/turbine, windmill), or burn
in-closure fuel under a boiler. Every element is documented as built from
in-closure materials with hand-generated precision, and none needs a
semiconductor or a non-replicable plant.

**Mobile: not shown to meet the criterion, and the failure is specifically in the
energy store.**

- Mobility **rules out the two best prime movers by construction**, a water
  wheel and a windmill are sited on the resource, not carried by the machine.
- Mobility therefore **forces a carried store**, and the only two in-closure-ish
  chemistries found are the Voltaic pile (primary, non-rechargeable) and lead–acid
  (rechargeable, feedstock unresolved).
- The historical precedent for a *mobile* heat engine is high-pressure steam, and
  it carried fuel and water **drawn from the environment**, a different
  dependency profile from a battery.
- **Asymmetry that matters:** electricity is *not* required for motion (the 1804
  locomotive had none), but **control is**, and control is the sibling repo's
  open problem (fluidic gain ~0.3). So mobility adds a store problem on top of an
  already-open control problem.

> **Finding: a mobile self-replicating robot is not shown to meet the criterion;
> a stationary one is not obviously refuted.** This leg recommends the stationary
> posture and treats mobility as a separate, **currently open** leg.

*(The recommendation sentence is an inference, not a sourced claim, and is marked
as such here.)*

---

## 4. Prior literature: the requirement is named, and then assumed away

- **"Energy closure" is a named requirement in the canonical text.** `[verified,
  read the primary text]` Freitas & Merkle, *Kinematic Self-Replicating Machines*
  (2004), Ch. 5 §5.6: three requirements, **matter closure**, **energy closure**
  (whether the system can "generate sufficient energy in the proper forms", quoted
  as the shortest clause carrying the definition; §5.6), and **information
  closure**. The sibling `closure-audit` found the same report defers
  *information* closure outright; this leg finds the *statement* of energy closure
  has the same shape.
- **The tension to record, not resolve:** that same section argues the U.S.
  factory system is an existence proof of 100% closure, which is a claim **about
  the industrial system as a whole**, i.e. precisely the infrastructure this
  criterion forbids depending on.
- **Every early design answered the power question with industrial PV, a nuclear
  plant, or grid electricity.** `[verified text; primary not read]` Moore's
  "Artificial Living Plants" (1956) proposed a **solar battery or a steam engine**
, the steam-engine branch is the single most relevant precedent for this leg,
  and it was dropped by everyone after. NASA CP-2255 (1980): a solar-cell canopy.
  Lackner & Wendt (1995): fields of solar cells and electrified ceramic tracks.
  RepRap: grid electricity and petroleum filament. **All outside this closure.**
- **ABSENT: no EROI, bootstrap-energy or net-energy calculation for a
  self-replicating machine.** The vocabulary exists (`[verified]` EROI; EROI ≤ 1
  is a net sink; a 3:1 viability threshold is a cited claim this leg did not check
  at source) and it is quantified for energy *technologies*, not for replicators.
  Recorded as **not found**, not as **non-existent**, the search covered only
  encyclopaedia and KSRM-derived material, not journals.

---

## 5. What is ABSENT: do not fill these in with plausible numbers

1. **ABSENT:** any measured efficiency, fuel rate or power output for a
   Newcomen-type or 19th-century hot-air engine (only relative figures found).
2. **ABSENT:** the specific purification route for solar-grade silicon.
3. **ABSENT:** any efficiency figure for a purely **metallic** thermocouple doing
   useful power conversion.
4. **NARROWED 2026-10-14:** the **insulation/varnish system of early dynamo
   windings**, and brush/commutator contact materials. Candidate pre-industrial
   insulants are documented across this study (shellac and gutta-percha, control
   leg §6; wood and hemp in the Newcomen train, §2.3). No source measures their
   performance on a dynamo winding. **The generator verdict still depends on
   this**, but on a performance number, not on whether an insulant exists.
5. **ABSENT:** whether **lead and sulfuric acid** can be produced in-closure. No
   assumption made.
6. **ABSENT:** specific energy of charcoal, wood or any in-closure thermal store,
   so no endurance or mass budget for a mobile in-closure heat engine.
7. **PARKED:** measured performance of a self-excited dynamo built with
   hand-scraped iron cores and no modern insulation. No source in this study
   measures it, and more literature does not close it. It is a measurement.
8. **PARKED:** prior EROI/bootstrap-energy literature for replicators; the search
   was not journal-level. Parked, not chased.
9. **ABSENT:** performance of an in-closure solar concentrator + heat engine.
10. **PARKED:** coupling the power leg back to the fluidic control leg, the
    interface between a ~1 µm-precision fluidic element and a heat engine, was
    not researched at all. The question is stated here so it is not lost: a heat
    engine imposes vibration and thermal cycling on whatever shares its frame,
    and the fluidic element's channel geometry is its whole specification. No
    source in this study addresses the pairing, and closing it needs sources the
    workspace does not hold. Parked, not answered.

---

## 6. What this does to the study's headline: a hypothesis tested and adjusted

`audit.md` §"The synthesis" advanced a hypothesis before this leg was run:

> *the two disqualifiers may collapse into one, because the materials boundary
> that condemns magnets also condemns the generator, so the binding constraint
> is a shared materials boundary rather than the cascade wall.*

**The leg partially refutes it, and the amendment matters:**

- **Confirmed for direct conversion.** PV and thermoelectric plants are condemned
  by the data-center rule. "Needs a reactor" and "needs a data center" are one
  dependency *for that family*.
- **Not confirmed for the generator.** The self-excited dynamo needs **no
  permanent magnet**, residual magnetism is enough, so the magnet boundary does
  **not** automatically condemn it. The generator moves from condemned to
  **marginal**, with the hole in soft-iron cores and (unresearched) insulation.
- **Therefore the hypothesis that power fails *before* the cascade wall is not
  established.** On this evidence, **the control leg's cascade wall remains the
  best-evidenced binding constraint**, and the power leg's own binding question is
  a materials one that this leg could not close (§5 items 4 and 8).

**Revised headline:**

> **A stationary replicator can be powered entirely from inside the closure,
> fire and falling water, shafts and iron, and that is the study's one clean
> survival. Every route that turns heat or light directly into electricity is
> condemned by the same rule that condemns the data center; the electromechanical
> route survives only because the generator does not need a magnet, and whether it
> closes turns on soft-iron cores and winding insulation, which nobody has
> settled. Mobility is not shown to be possible. And the best-evidenced binding
> constraint on the whole machine remains the one the sibling repo named:
> **cascade gain**, in the control leg, not power.**

This is a negative-leaning result about *electricity* and a positive one about
*shaft power*. Both are stated, and neither is dressed up.

---

## 7. Sources

Retrieved 2026-10-14. Raw text per source is in `_research/_scratch/` (working
scratch, not committed, per the rights rule in `NOTICE.md`).

**Read in own text, `[verified]` (as "I read this text"; see §0 on tier):**
Wikipedia articles, retrieved via the MediaWiki API: *Solar cell*; *Crystalline
silicon*; *Thermoelectric materials*; *Thermoelectric effect*; *Lodestone*;
*Dynamo*; *Magneto*; *Hippolyte Pixii*; *Newcomen atmospheric engine*; *Watt
steam engine*; *Stirling engine*; *Hot air engine*; *Steam engine*; *Water
wheel*; *Water turbine*; *Windmill*; *Concentrated solar power*; *Human power*;
*Voltaic pile*; *Lead–acid battery*; *Energy return on investment*;
*Self-replicating machine*; *RepRap*; *Magnet*; *Alnico*; *Neodymium magnet*;
*Ferrite (magnet)*; *Electric generator*; *Electromagnet*; *Solar cooker*; *Von
Neumann universal constructor*.

**Read in own text, primary:**
- Freitas, R. A. Jr. & Merkle, R. C., *Kinematic Self-Replicating Machines*,
  Landes Bioscience, 2004, Ch. 5 §5.6, "Closure Theory and Closure Engineering,"
  at `molecularassembler.com/KSRM/5.6.htm`.

**Citation verified, primary text not read, `[unverified]` at claim level:**
- Moore, E. F., "Artificial Living Plants," *Scientific American* 195, no. 4
  (Oct 1956) 118–126, doi:10.1038/scientificamerican1056-118.
- Lackner, K. S. & Wendt, C. H., *Mathl. Comput. Modelling* 21(10) (1995) 55–81,
  doi:10.1016/0895-7177(95)00071-9.
- NASA/ASEE, *Advanced Automation for Space Missions*, CP-2255 (1982).

**Not found:** EROI / net energy / bootstrap energy for self-replicating machines
(§4, §5 item 8).

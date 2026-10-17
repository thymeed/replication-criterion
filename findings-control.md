# Findings: the control leg (relay logic)

**Version 0.1, 2026-10-14.** A test of one sentence in a sibling feasibility study:
that relay logic is ruled out by "contact and magnet materials", and that fluidic
wall-attachment (Coanda) logic is the *only* control substrate inside the
pre-industrial closure, its binding constraint being that a fluidic stage's
**flow gain is ~0.30 against a required ≥1.0**, so a gate cannot drive its
successor.

The question asked of this leg: **is the relay dismissal too fast, and if relays
work, does the binding constraint change?**

Method and criterion of the parent study: `protocol.md`; applied context:
`audit.md`. Power cross-reference: `findings-power.md`.
Sources retrieved over the network on 2026-10-14. Live URLs and the exact API
endpoints are listed in §6.

---

## 0. Evidence tier, stated first

- This leg is **encyclopaedia-tier**, like the sibling power leg, and weaker than
  the `copy-fidelity` leg.
- **`[verified]` = I read the source's own retrieved text** (Wikipedia article
  bodies pulled through the MediaWiki API, quoted in §2). Wikipedia is a
  *tertiary* source; its own underlying citations were **not** independently
  opened.
- **`[unverified]` = I did not read the source's own text**: either a search
  engine's summary, or a citation I saw registered in another document but never
  opened.
- **`[discarded]` = a claim in the brief or in the sibling study that the
  retrieved record does not support**, or that I could not source at all.
- **No number below is estimated.** Where the literature I reached is silent the
  entry reads **ABSENT**. §5 lists the gaps explicitly; three of them are the
  places a follow-up should attack first.
- Two fetches failed and are reported rather than papered over: the Rojas Z3
  reconstruction PDF (bot wall) and the Zuse archive relay page (HTTP 429). One
  Wikipedia article assumed in the brief, `Pneumatic logic`, **does not exist**
  (HTTP 404; the page was deleted or renamed).

---

## 1. The answer, in one paragraph

**Relay logic composes, and the reading that condemned it is a materials error
rather than a gain error.** Composition is not a marginal property of relays that
needs measuring. It is what a relay *is*: a coil in one circuit moves contacts in
**a separate circuit with its own supply**, and the retrieved sources state the
fan-out directly ("Relays are used to control a circuit by an independent
low-power signal and to control several circuits by one signal") and state the
amplification in the history ("[Morse's 1840] mechanism ... acted as a digital
amplifier, repeating the telegraph signal, and thus allowing signals to be
propagated as far as desired") `[verified]`. The historical record shows relays
cascading in production for ninety years: telegraph relays from 1835–1840,
Strowger's exchange of 1891 explicitly built on "cascading" group selectors,
crossbar common-control built out of "relay sets" with a design criterion of two
hours of downtime per forty years, and Zuse's Z3 of 1941, 2,600 relays,
Turing-complete per Rojas 1998 `[verified]`. On materials, the specific premise is
wrong: **wrought iron is documented as usable for temporary (soft) magnets, "it
can be used to form temporary magnets, but it cannot be magnetized
permanently"**, and Sturgeon (1824/25) and Henry (1828–1831) built working
electromagnets out of exactly iron, varnished iron, bare copper and silk
`[verified]`. **A relay needs only an electromagnet; a permanent magnet is an
optional sensitivity or latching aid, not a functional necessity** `[verified]`.
So the fluidic wall, 0.30 flow gain against ≥1.0, **is not shared by relays**,
whose per-stage gain is set by the designer choosing a larger output circuit, not
by a fixed physical transfer ratio. What changes is where the binding constraint
sits: it moves off *signal gain* and onto **(a) first excitation of the
generator** (a self-excited dynamo needs no permanent magnet, but its very first
build-up needs flashing, a named bootstrap gap `[verified]`), **(b) contact
erosion under DC inductive break** (arcing "damages the electrical contacts",
worse on DC than AC `[verified]`), **(c) the low-current film problem at the
opposite extreme** (wetting current, too little current leaves contacts
insulating `[verified]`), and **(d) speed and mechanical life** (relays switch in
milliseconds; the Z3 ran at 5–10 Hz and drew ~4,000 W `[verified]`). The honest
bottom line: **the relay leg survives the dismissal on composition and on
materials, but I found no published per-stage relay gain, fan-out, or contact-life
figure, so this is an argument from architecture and history, not a measured
number.**

---

## 2. Per-question findings

### 2.1 Does relay logic compose: is per-stage gain > 1?

**Structural, from the source's own text**: `[verified]`, Wikipedia *Relay*
(retrieved 2026-10-14):

- "A relay is an electrically operated switch. It has a set of input terminals
  for one or more control signals, and a set of operating contact terminals."
- "Relays are used **to control a circuit by an independent low-power signal and
  to control several circuits by one signal**."
- History: "They were first used in long-distance telegraph circuits as signal
  repeaters that transmit a **refreshed copy** of the incoming signal onto another
  circuit."
- Morse: "an official patent was not issued until 1840 to Samuel Morse for his
  telegraph ... The mechanism described **acted as a digital amplifier, repeating
  the telegraph signal, and thus allowing signals to be propagated as far as
  desired**."
- Relay history: Joseph Henry "is often cited to have invented a relay in 1835";
  Edward Davy deposited a make-and-break relay design in March 1837; Samuel
  Morse's 1840 patent.
- Physical construction named in the same article: "a coil of wire wrapped around
  a **soft iron core** (a solenoid), an **iron yoke**, a movable **iron
  armature**, and one or more sets of contacts ... linked to one or more sets of
  moving contacts ... held in place by a spring."

**Cascading in production**: `[verified]`:

- **Strowger exchange (patent 1891, first exchange La Porte, Indiana 3 Nov 1892):**
  "The original final selector (connector) switch which connected to 100 customers
  was supplemented by preceding group selector stages, as the **'cascading'**
  enabled connection to many more customers, and to customers at other exchanges."
  Customer line equipment was "only a few relays (in most cases two, a Line, and a
  Cut-off relay)". Switch motion is driven by trains of current pulses from the
  dial, with a release magnet at call end.
- **Crossbar (1XB revenue service from 1938):** "exchange design moved all the
  logical decision-making to the common control elements, which were **very
  reliable as relay sets**. The design criteria specified only **two hours of
  downtime for service every forty years** ..." and "the control occupancy on the
  switches was of the order of one second or less, representing the operate and
  release lags of the X-then-Y armatures". Crossbars "graduated from entirely
  electromechanical control on introduction" to electronic control.
- **Telegraph regeneration:** the electrical-telegraph article calls Davy's 1837
  make-and-break relay "a key component for **periodically renewing weak
  signals**" `[verified]`, *Electrical telegraph*.

**Konrad Zuse Z1/Z2/Z3 (1938–1941)**: `[verified]`, Wikipedia *Z3 (computer)*
and *Z1 (computer)*:

- Z3: "built with **2,600 relays**, implementing a 22-bit word length that
  operated at a clock frequency of about **5–10 Hz**"; "around 2,000 relays
  (1,400 for the memory)"; power "around **4,000 watts**"; weight "around 1 tonne";
  addition 0.8 s, multiplication 3 s; program on punched celluloid film; destroyed
  21 Dec 1943; demonstration of Turing-completeness in **1998 by Raúl Rojas**,
  with speculative execution standing in for conditional branching. A working
  replica was built 1961; a 1997–2003 reconstruction (Rojas/H. Zuse) runs at
  ~400 W and ~30 kg with memory halved to 32 words.
- Zuse's own motivation was availability, not theory: Schreyer pushed vacuum
  tubes (100-tube demo 1942); "Zuse decided to implement the next design based on
  relays."
- Z2 (1940): "used the mechanical memory of the Z1 but used relay-based
  arithmetic"; Z1 was "wholly mechanical and only worked for a few minutes at a
  time at most".

**Published per-stage gain, fan-out count, or cascading-limit figure for relay
logic: ABSENT.** The retrieved sources make the composition claim qualitatively
and by construction; no source I opened states a numeric power gain or a maximum
number of successor coils. Rojas et al. 2005 (IEEE Annals, doi:10.1109/mahc.2005.48)
is the obvious place this number would live if it exists; I saw only its
registered citation **`[unverified]`** (listed in the Z3 article's "Further
reading"; the paper itself was not opened).

### 2.2 Materials closure: iron, copper, brass, and a soft core

- **Is "wrought iron IS soft iron" correct?** The retrieved record supports the
  *usability*, not the identity. `[verified]`, Wikipedia *Wrought iron*: "It can be
  used to form **temporary magnets**, but it cannot be magnetized permanently";
  wrought iron is "an iron alloy with a very low carbon content (less than 0.05%)";
  "The modern functional equivalent of wrought iron is mild steel"; it is
  "generally relatively pure iron ... around 99.4% iron by mass" with fibrous
  silicate slag inclusions; it was made by the bloomery (direct reduction),
  finery and, from 1784, puddling processes, i.e. **pre-industrial and
  in-closure by the sibling's own list**. So the sibling's phrase "reliable soft-iron
  cores ... more difficult without industrial metallurgy" is not supported by the
  record: the exact property a relay core needs (easy magnetisation, ready
  demagnetisation) is the property the source attributes to wrought iron.
- **Sturgeon (1824/25)**, `[verified]`, Wikipedia *Electromagnet*: "His first
  electromagnet was a horseshoe-shaped piece of iron that was wrapped with about
  18 turns of **bare copper wire**. (**Insulated wire did not then exist.**) The
  iron was **varnished** to insulate it from the windings." It "weighed seven
  ounces ... could lift nine pounds ... with the current of a single-cell power
  supply", but was weak because uninsulated wire forced a single spaced layer.
- **Henry (from 1830)**, `[verified]`, same article: "By using wire **insulated
  by silk thread** ... he was able to wind multiple layers of wire onto cores,
  creating powerful magnets with **thousands of turns** of wire, including one
  that could support **2,063 lb (936 kg)**."
- **Does a relay need a permanent magnet? No.** `[verified]`, Wikipedia *Relay*: a
  simple electromagnetic relay "consists of a coil of wire wrapped around a soft
  iron core (a solenoid), an iron yoke ..., a movable iron armature, and one or
  more sets of contacts". Permanent magnets appear only in optional variants,
  the article's polarized relay "places the armature between the poles of a
  **permanent magnet** to increase sensitivity" (used in mid-20th-century
  exchanges "to detect faint pulses and correct telegraphic distortion"), and
  magnetically latching relays. So the sibling's "high-performance magnets" concern
  **applies to the power leg's generator and to optional relay variants, not to
  the basic relay** `[verified]` at the level of these two articles.
- **Real remanence effect, but a documented artefact of specific constructions:**
  reed relays' "reeds can become magnetized over time, which makes them stick
  'on'"; latching relays may hold via a "remanent core" `[verified]`, *Relay*.
  Whether 1830s–1890s wrought-iron telegraph relay cores suffered a practical
  sticking/remanence problem: **ABSENT**.
- Useful in-closure arithmetic (modern materials, but the physics is the physics),
  `[verified]`, *Electromagnet*: iron-core saturation "around 1.6 to 2 teslas";
  "most core materials saturate at a magnetomotive force of roughly **800
  ampere-turns per meter** of flux path"; with a **1 mm air gap**, "a
  magnetomotive force of about **796 ampere-turns** is required to produce a
  magnetic field of 1 T". These say an iron-and-copper relay with a small gap is
  an ordinary engineering object, not an edge case.

### 2.3 Insulation of early windings

- **Silk**, `[verified]`: Henry's multi-layer cores used "wire insulated by silk
  thread" (from 1830), *Electromagnet*. Silk is a pre-industrial textile.
- **Varnish on the iron**, `[verified]`: Sturgeon's 1824/25 magnet, same source.
- **Shellac**, `[verified]`, Wikipedia *Shellac*: "Shellac was once used in
  electrical applications as it is a good insulator and seals out moisture";
  and, specifically for windings: "Shellac was used for fixing **inductor, motor,
  generator and transformer windings**. It was applied directly to single-layer
  windings in an alcohol solution. For multi-layer windings, the whole coil was
  submerged in shellac solution, then drained ... The shellac locked the wire
  turns in place, provided extra insulation, prevented movement and vibration and
  reduced buzz and hum." Shellac is an insect resin from India/Thailand, traded
  into Europe since the 17th century (sealing wax, 1220 pigment binder, 16th-c.
  varnish), **i.e. a traded natural material, not an industrial one**. Whether
  trade-sourced shellac counts as inside a self-replicator's closure is a
  geopolitical question about the closure, not a materials question; the sibling's
  list does not contain it, which is itself a point to flag.
- **Gutta-percha**, `[verified]`, Wikipedia *Gutta-percha*: "a good electrical
  insulator with a high dielectric strength"; Faraday identified its insulating
  value soon after its 1843 introduction to Britain; "**By 1845, telegraph wires
  insulated with gutta-percha were being manufactured in the UK**. It served as
  the insulating material for early undersea telegraph cables, including the
  first transatlantic telegraph cable"; dielectric constant 2.56–3.01, resistivity
  25×10^14 to 370×10^14 Ω·cm. It is a tropical tree latex (trans-1,4-polyisoprene)
, **a trade import, not a local material**.
- **Natural rubber before vulcanisation**, `[verified]` (same article, as a
  contrast): gutta-percha "did not become brittle, unlike rubber prior to the
  discovery of vulcanization." That is evidence that *pre-vulcanised rubber was a
  poor insulator in this role*, which narrows the sibling's "natural rubber" entry.
- **Cotton, paper, glass, oil, wax as winding insulation**: **ABSENT**, no source
  opened.

### 2.4 Contacts: materials, wear, arcing, and the dry-switching claim

- **Materials**, `[verified]`, Wikipedia *Electrical contact*: "Typical materials
  include: Silver alloys; Gold; Platinum-group metals; Carbon; **Copper**."
  Copper is in-closure; silver, gold and platinum-group metals are not on the
  sibling's list. (Tungsten appears nowhere in the retrieved text: **ABSENT**.)
- **Arcing is a real, source-stated limit**, `[verified]`, *Electrical contact*:
  "When relay contacts open to interrupt a high current with an inductive load, a
  voltage spike will result, striking an arc across the contacts. If the voltage
  is high enough, an arc may be struck even without an inductive load. ...
  **Arcing damages the electrical contacts**, and a sustained arc may prevent the
  open contacts from removing power". And: "In AC systems ... all but the most
  energetic arcs are extinguished at the zero crossing. **The problem is more
  severe with DC where such zero crossings do not occur.**" A relay-logic machine
  is a DC machine, and a relay coil is exactly an inductive load, so this is the
  sharpest in-closure cost the record gives.
- **Wear statements**, `[verified]`, *Relay*: contactors' "**unavoidable arcing
  causes the contacts to oxidize**; however, silver oxide is still a good
  conductor"; "Some relays have **field-replaceable contacts** ... these may be
  replaced when worn out" (i.e. wear is an accepted maintenance item); mercury
  relays "are used where **contact erosion** would be a problem for conventional
  relay contacts" (mercury is not on the sibling's list).
- **The low-current opposite limit**, `[verified]`, Wikipedia *Wetting current*:
  "wetting current is the minimum electric current needing to flow through a
  contact to break through the surface film resistance at a contact"; "Failing to
  do this might result in switches remaining electrically 'open' when pressed, due
  to contact oxidation"; a "sealing current" of "typically **1–20 mA**" is used in
  telecom copper loops to prevent contact oxidation. So there is a **current
  window**: too little current films the contact, too much arcs it. This is a
  genuine design constraint the sibling's one-line dismissal never reaches, but
  note it is *not* a blocker, it is an operating point to be chosen.
- **"Zuse used current-free (dry) switching specifically to avoid contact
  erosion": DOCUMENTED? NO, `[discarded]` as an unsourced claim in the brief.**
  I could not retrieve any source stating this. The 1998–2005 Rojas materials are
  the right place for it, and both the HAL copy of the reconstruction paper
  (`hal-01455300`) and the Zuse archive relay page (`zuse.zib.de/relay`) were
  unreachable in this session (bot wall / HTTP 429). Per the evidence rule I do
  **not** assemble a plausible substitute from the general fact that low-current
  switching reduces erosion; the specific claim is **ABSENT**.
- **Contact lifetime / number of operations before failure**: **ABSENT**.

### 2.5 Power: is the generator a fatal circularity?

- The sibling power leg's finding is that a **self-excited dynamo needs no
  permanent magnet**, building its field from the residual magnetism of its own
  iron. I re-checked the independent encyclopaedia text and it agrees, with an
  important caveat, `[verified]`, Wikipedia *Dynamo*:
  - "A dynamo is an electrical generator that creates direct current using a
    commutator, and uses **self-powering electromagnets** for the stator field
    rather than permanent magnets. Dynamos are **self-starting by using residual
    magnetic field left in the iron cores** of the electromagnets."
  - "**If a dynamo were never run before, it was usual to use a separate battery
    to excite or flash the field** of the electromagnets to enable self-starting."
  - "A self-excited dynamo with **insufficient residual magnetic field** in the
    metal frame will not be able to produce any current in the rotor, regardless
    of what speed the rotor spins ... resolved ... by applying a brief direct
    current battery charge ... referred to as **flashing the field**."
  - History: self-excitation principle realised by Ányos Jedlik (~1856, concept),
    and independently by Henry Wilde (paper read to the Royal Society 26 March
    1866), Wheatstone, Siemens and Varley (patents/announcements Dec 1866 – Jan
    1867). "The use of electromagnets rather than permanent magnets greatly
    increased the power output."
  - Earlier permanent-magnet machines did exist (Pixii 1832, Woolrich 1844), so
    the *original* bootstrap could in principle route through a natural magnet,
    **but see §5: I found no source stating that a lodestone/natural magnetite was
    used to flash a field** `[discarded]` as an unsourced workaround.
- **So the circularity is broken with one named gap:** you need *one* initial
  magnetisation of the iron. The sources offer a battery (voltaic pile) for that
  flash. A voltaic pile needs two dissimilar metals and an electrolyte. **An
  earlier revision of this bullet said the sibling's materials list "contains no
  zinc or other second metal". That is wrong on its face**, and the sibling
  `Fluidic Bootstrap Project` `Conclusion A.md` says so directly: the list
  carries copper, iron, lead and brass, and it carries zinc as *ore*, its brass
  entry being "calamine process (zinc carbonate + copper)". So a galvanic couple
  is **not materials-condemned**, and the item narrows rather than opening: what
  the list names is zinc *ore*, not isolated zinc metal, and calamine cementation
  yields brass rather than zinc. The residual question is one further step, the
  isolation of an anode metal from that ore, and it is **narrowed, not open**.
- **Relays themselves need a supply, not a magnetic bootstrap:** they run off the
  generator bus. The old telegraph architecture of a weak line current operating a
  relay that keys a **local** circuit is the historical pattern (`refreshed copy
  ... onto another circuit` `[verified]`, *Relay*); the phrase "local battery" is
  not in the retrieved text, **ABSENT** at that level of specificity.

### 2.6 Speed and reliability against the logic requirement

- **Z3 (1941), a relay machine that does useful arithmetic**, `[verified]`,
  *Z3 (computer)*: clock 5–10 Hz; addition 0.8 s; multiplication 3 s; ~4,000 W;
  ~1 tonne; 2,600 relays (1,400 memory); Turing-complete in the 1998
  demonstration. This is the empirical answer to "can relays compute at all".
- **Reliability of the electromechanical exchange**, `[verified]`, *Crossbar
  switch*: design criteria "only **two hours of downtime for service every forty
  years**" for common-control relay sets; control occupancy ~1 s or less per call
  setup; "the minimum size of a crossbar exchange was comparatively large".
- **Relay switching time**: the only figures I reached are from a search
  summary, **`[unverified]`** (datasheets not opened): TE V23105 telecom relay max
  operate 8 ms, release 4 ms, bounce 1 ms; Omron G6K and Panasonic TQ ~3 ms/3 ms;
  reed relays <1 ms. That search summary also attributes to Wikipedia *Relay* the
  statement that electromechanical relay switching is "a few milliseconds". This
  I did **not** see in the retrieved article text, so it is not [verified] either.
  **Treated as: low single-digit to ~10 ms, unverified.**
- **Lifetime, contact cycles, MTBF for period relays**: **ABSENT**.
- **Zuse's own reliability comparison**: Z3 "was faster and far more reliable than
  the Z1 and Z2" `[verified]`, *Z3 (computer)*; the mechanical Z1 "was never very
  reliable ... poor synchronization caused by internal and external stresses on
  the mechanical parts" `[verified]`, *Z1 (computer)*.

### 2.7 Mechanical alternatives: do they have per-stage gain?

- **Bush/Hazen differential analyser (MIT, 1928–1931, six mechanical
  integrators)**, `[verified]`, Wikipedia *Differential analyser*: wheel-and-disc
  (ball-and-disk) integrators, epicyclic differentials for add/subtract, gear
  ratios for integer multiplication; "integration" by a rotating disc.
- **The decisive fact for cascade**, `[verified]`, Wikipedia *Torque amplifier*:
  "The torque on the output shaft was limited by the friction between the bearing
  and the disk, and as these were generally made out of friction-limiting metals
  such as bronze ..., **the output torque was quite low** ... in the case of a
  differential analyzer, **the output of one integrator drove the input of the
  next integrator**, or a graphing output. **The torque amplifier was the advance
  that allowed these machines to work.**" Lord Kelvin had "been stymied by the
  limited output torque of the ball-and-disk integrators" since the 1880s.
- **And the mechanical amplifier exists, with gain > 1 by construction**:
  `[verified]`, same article: the torque amplifier is "two capstans connected
  together", essentially a belt/rope wrapped on powered drums, invented in
  electric-powered form by Henry W. Nieman in 1925 and used by Bush; "the **torque
  applied to it is the torque of the motor driving the system, as opposed to the
  torque applied on the input shaft**." That is an explicit power-gain stage built
  from drums, shafts, belts and a prime mover, materially in-closure.
- **Reading:** mechanical analogue stages **lose signal** (torque/force, through
  friction and compliant contact) and **do not have intrinsic per-stage gain**;
  cascade is possible only because a separate amplifier element (torque amplifier)
  is inserted, exactly as a relay is inserted in an electrical circuit. The
  sibling's framing ("no substrate but fluidics can cascade") is therefore wrong
  in the same way for mechanisms as for relays, the amplifier element is the
  thing that cascades, and both a relay and a torque amplifier are built from
  in-closure materials.
- **Per-stage gain figures for cams and linkages**: **ABSENT** (no source opened
  states a gain or loss per stage; rigid linkages are not gain elements, but I
  have no citation for that statement, so it is not tagged).
- **Z1 (1938), an actual mechanical computer:** 20,000 parts, "thin metal sheets"
  cut with a jigsaw, programmable via punched 35 mm film, clocked by an electric
  motor at 1 Hz; unreliable in operation `[verified]`, *Z1 (computer)*.

### 2.8 Pneumatic relays: the middle case

- **The taxonomy that matters here**, `[verified]`, Wikipedia *Fluidics*:
  "The term fluidics is normally used when devices have **no moving parts**, so
  ordinary hydraulic components such as hydraulic cylinders and **spool valves are
  not considered or referred to as fluidic devices**." Fluidic amplifiers "have
  gain" ("The stream entering the control ports may be much weaker than the stream
  being deflected"), bandwidth "in the low kilohertz range", and the field began
  with Horton's 1957 vortex/fluid amplifier (Horton, Bowles, Warren 1959; first
  devices built "out of soap, linoleum, and wood").
- **Pneumatic logic as a named article: does not exist.** `Pneumatic logic`
  returns HTTP 404 from en.wikipedia.org. The search engine cited it anyway
  (`[unverified]`, and the citation is to a non-existent page, treat that search
  summary as **`[discarded]`** as evidence).
- **Air/pneumatic relay = moving-part amplifier**: the only support I reached is a
  search summary describing pneumatic relays as high-gain pressure/volume
  amplifiers and moving-part logic (MPL) implementing AND/OR/NOT/NAND/NOR/memory,
  **`[unverified]`**, and the primary vendor page I tried to open
  (`controlair.com/pneumatic-relays/`) returned **HTTP 404**. So the middle case is
  **plausible but unsourced in this leg**: a diaphragm-and-poppet air relay is by
  construction a gain element (small pilot pressure ports a larger supply), which
  would place it on the relay side of the 0.30 wall rather than the fluidic side,
  but I have no verified source for its gain figure.

---

## 3. Direct comparison: relay per-stage gain vs the fluidic wall

- **Fluidic wall (sibling measurement):** stage flow gain ≈ **0.30** against a
  required **≥1.0**; one gate cannot drive its successor. (Their measurement; this
  leg did not re-open it.)
- **Tension to record, `[verified]`:** Wikipedia *Fluidics* states that a fluidic
  amplifier "has gain" because the control stream may be much weaker than the
  deflected stream. **This does not refute the sibling's number**, gain in that
  sentence is a local pressure/flow amplification claim, not the closure-relevant
  statement that a *whole stage's output can drive an identical successor stage*
  including losses. But the two statements should be reconciled explicitly in the
  parent study, because they read as contradictory to a casual reader and the
  difference (device gain vs system cascade margin) is exactly the crux.
- **Relay, per-stage gain:** **> 1 by architecture, not by a published number.**
  The coil is energised by circuit A; the contacts switch circuit B, which has its
  own supply and can be arbitrarily larger; and one actuation can move several
  contact sets, i.e. drive several successor loads `[verified]`, *Relay*. The
  composition evidence is historical and architectural (Morse 1840 "as far as
  desired"; Strowger 1891 cascading; crossbar relay sets; Z3's 2,600 relays).
- **The honest comparison:** fluidic **0.30 measured vs ≥1.0 required** is a
  *measured shortfall*. Relay **"≥1 by construction"** is a *structural claim with
  qualitative historical backing and no number*. The gap between those two kinds
  of evidence is the main weakness of this leg and should be stated as such in the
  parent.
- **What is not claimed:** I do **not** claim any specific relay gain, fan-out
  count, or margin. Those figures are **ABSENT** in everything I reached.

---

## 4. What would falsify "relays are viable"

In rough order of decisiveness:

1. **A period-realizable relay whose coil draw exceeds what its own contacts can
   switch.** If, at the minimum actuating current achievable with a hand-wound
   copper coil on an iron core and period spring contacts, the power the contacts
   can commutate is *less than* the coil's own operating power, per-stage gain
   falls below 1 and cascade fails. This is a bench measurement, not a literature
   question; the literature I reached gives **no ratio** (ABSENT).
2. **Fan-out failure.** One relay's contacts holding *k* identical relay coils
   closed simultaneously at the machine's bus voltage, with contact force set by
   period springs, masses measured against a documented mechanical limit, if k
   < 1, no cascade.
3. **Contact life below the replication requirement.** If DC inductive-break
   erosion (the documented worst case, §2.4) destroys or welds the contacts before
   the replicator completes one build cycle, relay logic fails on maintenance
   rather than on gain. Requires a measured cycles-to-failure figure, **ABSENT**
   now.
4. **Materials creep into the closure's exclusion list.** Any of: silver/tungsten
   contacts; permanent magnets for polarized/latching variants; imported
   shellac/gutta-percha as the only viable winding insulation; the one further
   step that isolates a first-cell anode metal (the list names zinc *ore*, not
   zinc metal, §2.5).
5. **Bootstrap failure.** A demonstrated inability to obtain the first
   magnetisation of the generator's iron from in-closure means only (no battery,
   no lodestone), §2.5's named gap.
6. **Speed/lifetime mismatch.** If the required operation count for a build cycle
   exceeds achievable relay life, or the required logic depth at 5–10 Hz makes
   build time absurd (the Z3 needed 0.8 s for one addition, 1941), the substrate
   is viable in principle and useless in practice.
7. **Counter-evidence to composition itself**, which would be surprising: a
   documented class of relay logic in which a stage's output could not reliably
   drive an identical stage. None found; the 1840–1938 record runs the other way.

---

## 5. ABSENT / not-found list (the honest boundary of this leg)

1. **PARKED:** published per-stage gain, fan-out count, or cascading limit for
   relay logic. No number anywhere in the retrieved sources. Rojas et al. 2005
   (IEEE Annals, doi:10.1109/mahc.2005.48) is the first place to look and was not
   opened. Paywalled; parked, not chased.
2. **PARKED:** Zuse using current-free / dry switching to avoid contact erosion.
   The brief's claim is **`[discarded]`**, no source retrieved supports or
   describes it. Both candidate sources were unreachable (Rojas reconstruction
   PDF via HAL, bot wall; `zuse.zib.de/relay`, HTTP 429). Access, not analysis.
3. **Any relay lifetime, MTBF, or cycles-to-failure figure**, period or modern.
4. **Period relay switching-time figures.** Only modern datasheet numbers from a
   search summary, `[unverified]`.
5. **"Local battery" repeaters as a named telegraph architecture**: the
   *concept* is in the retrieved text ("refreshed copy ... onto another circuit"),
   the term is not.
6. **Copper, silver, tungsten contact wear data** (tungsten does not appear in the
   retrieved contact article at all).
7. **Cotton, paper, glass, or oil/wax as period winding insulation**: no source
   opened. Narrowed 2026-10-14: natural insulants are documented elsewhere in
   this study (shellac and gutta-percha, §6 sources; wood and hemp in the power
   leg's Newcomen train), so candidate pre-industrial insulants exist. Their
   *performance* as dynamo winding insulation is unmeasured. Narrowed, not closed.
8. **Whether 1830s–1890s wrought-iron relay cores suffered practical remanence
   sticking.**
9. **A source for using a natural magnet (lodestone/magnetite) to flash a dynamo
   field.** **`[discarded]`** as a workaround: plausible, unsourced.
10. **Whether the first exciting cell (voltaic pile) is inside the closure**:
    **CORRECTED 2026-10-14.** An earlier revision said the sibling's materials
    list "has no zinc or other second metal". That is wrong: the list carries
    copper, iron, lead and brass, and it carries zinc as *ore*, its brass entry
    being the calamine process (zinc carbonate + copper). A galvanic couple is
    therefore not materials-condemned. The residual question is one step
    further, whether an anode metal is isolated from that ore, and it is
    **narrowed, not open**: see §2.5.
11. **Per-stage gain or loss numbers for cams/linkages**, and for the Bush torque
    amplifier (its gain is argued from construction, not measured in the source).
12. **Quantitative gain for pneumatic/air relays.** `Pneumatic logic` on Wikipedia
    **does not exist** (404); the vendor page returned 404; no verified figure.

---

## 6. Sources

All retrieved 2026-10-14. Wikipedia bodies were pulled as plain text through the
MediaWiki API, e.g.
`https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles=<ARTICLE>`,
so the quoted text is the article's own current text, not a search snippet.

**Read directly, quoted above (`[verified]` at the tertiary tier):**

- *Relay*, https://en.wikipedia.org/wiki/Relay
- *Electrical telegraph*, https://en.wikipedia.org/wiki/Electrical_telegraph
- *Strowger switch*, https://en.wikipedia.org/wiki/Strowger_switch
- *Crossbar switch*, https://en.wikipedia.org/wiki/Crossbar_switch
- *Z3 (computer)*, https://en.wikipedia.org/wiki/Z3_(computer)
- *Z1 (computer)*, https://en.wikipedia.org/wiki/Z1_(computer)
- *Electromagnet*, https://en.wikipedia.org/wiki/Electromagnet
- *Wrought iron*, https://en.wikipedia.org/wiki/Wrought_iron
- *Dynamo*, https://en.wikipedia.org/wiki/Dynamo
- *Electrical contact*, https://en.wikipedia.org/wiki/Electrical_contact
- *Wetting current*, https://en.wikipedia.org/wiki/Wetting_current
- *Torque amplifier*, https://en.wikipedia.org/wiki/Torque_amplifier
- *Fluidics*, https://en.wikipedia.org/wiki/Fluidics
- *Shellac*, https://en.wikipedia.org/wiki/Shellac
- *Gutta-percha*, https://en.wikipedia.org/wiki/Gutta-percha
- *Differential analyser*, https://en.wikipedia.org/wiki/Differential_analyser

**Registered citations seen but NOT opened (`[unverified]`; do not cite as if
read):**

- Rojas, Raúl; Darius, Frank; Göktekin, Cüneyt; Heyne, Georg (2005). "The
  reconstruction of Konrad Zuse's Z3". *IEEE Annals of the History of Computing*
  27(3): 23–32. doi:10.1109/mahc.2005.48. (Citation only, from the Z3 article's
  Further reading.)
- Rojas, Raúl (2016). "The Design Principles of Konrad Zuse's Mechanical
  Computers". arXiv:1603.02396. (Citation only; the abstract page returned no
  readable body, JavaScript-rendered.)
- Rojas, Raúl (Spring 2006) [2005-05-12]. "The Zuse Computers". *Resurrection,
  Bulletin of the Computer Conservation Society* 37. (Citation only.)
- Holm, Ragnar & Holm, Else (1967/1958), *Electric Contacts*; Pitney, K. E. (1973),
  *Ney Contact Manual*; Slade, P. G. (1999/2014), *Electrical Contacts: Principles
  and Applications*. (Citations listed by the *Electrical contact* and *Wetting
  current* articles; none opened.)
- Telegraph-repeater material attributed by a search summary to
  https://en.wikipedia.org/wiki/Telegraph_repeater, **note: that article does not
  exist under that title in the API** (`missing`), so the search summary is
  `[discarded]` as evidence.

**Attempted and failed (reported, not worked around):**

- https://inria.hal.science/hal-01455300/document, HTTP 200 with an Anubis
  proof-of-work bot wall; no paper text returned.
- https://zuse.zib.de/relay, HTTP 429 with a JS verification page.
- https://arxiv.org/abs/1603.02396, HTTP 200, no readable body (JS-rendered).
- https://www.controlair.com/pneumatic-relays/, HTTP 404.
- https://en.wikipedia.org/wiki/Pneumatic_logic, HTTP 404 (article does not
  exist).

**Search-summary-only material (`[unverified]`, engines named in text):** relay
operate/release times (TE V23105, Omron G6K, Panasonic TQ, reed relays) and
pneumatic/air-relay gain characterisation (ControlAir, InstrumentationTools,
Clippard). Treated as leads for a follow-up, never as findings.

---

## 7. Addendum, 2026-10-17: relay contacts, and the relay route's element count

Two questions this leg left open: what period relays made their contacts from, and
what a relay controller costs. Sources below were read directly as raw text on
2026-10-17, not through a search or summarising tool.

### 7.1 Period relay contacts were platinum `[verified]`

- **Pope, Frank L., *Modern Practice of the Electric Telegraph* (New York: Russell
  Brothers, 1869)**, archive.org item `modernpracticee04popegoog`. Primary. The
  relay closes the local circuit "through the platina points of the relay". When
  the points are "too much corroded" they are cleaned with a very fine file,
  removing as little platinum as possible. The same text notes points sticking when
  "oxidized and dirty".
- **Prescott, George B., *History, Theory, and Practice of the Electric Telegraph*
  (Boston: Ticknor and Fields, 1860)**, archive.org item
  `historytheorypra00presrich`. Primary. Morse's receiving magnet brings "a platina
  point in contact with a little platina disc" to close the local battery circuit.

**What this changes.** The materials premise in §1 was tested on the coil and the
core, and it held there. It was not tested on the contacts, and the period record
names platinum. `protocol.md` §8 places refined contact metals outside K. So the
relay route moves from **materials inside** to **conditional on contacts**.

### 7.2 Platinum from the environment, not the kit `[verified]`, tertiary

K is not amended (`protocol.md` §8 fixes it before the evidence). The open question is
whether platinum is reachable from **E**:

- Platinum occurs uncombined as **native platinum**, mostly in alluvial (placer)
  deposits, and was first worked by pre-Columbian South Americans, who combined gold
  and platinum powders "by sintering" (Wikipedia, *Platinum*, History and Occurrence,
  read 2026-10-17). No refining step is described for that work.
- **The condition is a site condition.** Platinum is very rare in the crust, so this
  holds only for an environment that includes a platinum placer. A replicator sited
  elsewhere does not have it. The pre-Columbian product was a gold-platinum alloy, so
  whether native grains make a durable relay point is **ABSENT**.

The in-K alternative is weaker than it first looked. **US Patent 434,585,
"Telegraph-relay" (issued 1890-08-19)**, read on Google Patents, uses "pieces of carbon"
with platinum as the alternative. But it describes a pressure-variable resistance, not
a make-and-break contact, so it does not show carbon serving as an ordinary relay
point. Copper and brass contacts: **ABSENT** from any period source reached.

### 7.3 The relay route's element count `[derived]`

The sequencer in `model/controller_budget.py` does not depend on the substrate. Only
the fan-out does. A multipole relay switches one separate circuit per contact set, so
its fan-out is its contact count. Harvard Mark I had "3,500 multipole relays with
35,000 contacts" (Wikipedia, *Harvard Mark I*, quoting IBM Archives, read
2026-10-17), an average of ten.

At fan-out 10, against the fluidic case at fan-out 3:

- 10 steps: 23 relays against 45 fluidic elements
- 20 steps: 50 against 81
- 50 steps: 122 against 201

So a relay controller needs **50 to 60 per cent of the fluidic element count**, and
this is an upper bound because relays form AND from contacts in series. Ten is a
machine average, not a per-relay maximum, and it counts contacts, not the loads one
contact can carry.

### 7.4 What is still ABSENT

1. **Hours to make one relay by hand.** No period or modern source reached prices it,
   so the relay route has an element count and no labour figure.
2. **Contact life in operations**, for platinum, native-platinum alloy, carbon, copper
   or brass.
3. **Whether native placer platinum, unrefined, makes a working relay point.**

Sources not reached this pass: Rojas, arXiv:1603.02396 (the PDF returned no readable
text); Rojas et al. 2005, *IEEE Annals* (paywalled); `zuse.zib.de` (HTTP 429). Z3,
Bell Labs Model V and Harvard Mark II relay counts seen only in search snippets are
`[unverified]` and not used.

### 7.5 Winding insulation, upgraded to a primary source `[verified]`

Pope (1869, above) gives **silk-insulated copper wire** as the standard winding for
telegraph electromagnet coils, and describes one maker's alternative of bare wire
wound by "accurate machinery" so the turns stay separated. This moves the §2.3 silk
claim from encyclopaedia tier to a primary period manual. It shows silk was the period
practice for relay coils. It does not measure silk's performance on a dynamo winding,
so `findings-power.md` §5 item 4 is unchanged.

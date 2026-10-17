# Findings: the structure-and-tooling leg

**Version 0.1, 2026-10-17.** A test of one line in `audit.md`'s synthesis:
"Structure and tooling: inside. Iron, steel, copper, brass, glass, clay, wood are
all in K." That line shows the materials are in the kit. It does not show the
machine can turn them into the tools that shape its next copy. `protocol.md` §4
names structure and tooling as one of the three critical subsystems, and it was
the only one without a findings document.

The question asked of this leg: **is there measured evidence that tools can be
made inside C(K, E), and at what cost?**

---

## 0. Evidence tier, stated first

- **`[verified]`** = the source's own text was fetched as raw text on 2026-10-17
  and the claim was found in it. Not through a search or summarising tool.
- **`[unverified]`** = a lead seen only in a search snippet or a tool's summary.
  Listed so it is not lost, never used as a finding.
- **`[derived]`** = arithmetic on a verified number, shown so it can be checked.
- Where no source reached gives a number, the entry reads **ABSENT**.

This leg is thinner than the others. Most of what it looked for is not in the
accessible literature, and §4 says so item by item.

---

## 1. The answer, in one paragraph

**The materials are inside, and making iron from them has a measured price. Making
tools from that iron is unmeasured.** Experimental smelting shows a bloomery
works with clay, local ore and charcoal, at about 100 kg of charcoal and 25
person-days per kilogram of finished bar iron, and that the process fails often:
one smelt in four gave a usable bloom in the one series read. Past that point the
record turns qualitative. Hand-made files, chisels and the first machine tools
are documented as having existed and worked, but no source reached gives their
hardness, life, removal rate, or accuracy at each stage. So the audit's "inside"
becomes **materials inside, tool-making unmeasured**. That is the same shape as
every other leg: an unmeasured quantity, not a wall.

---

## 2. Findings

### 2.1 Bloomery iron has a measured cost `[verified]`

- **Crew, P. (1991), "The experimental production of prehistoric bar iron",
  *Historical Metallurgy* 25(1)**, abstract read on the journal's own page
  (`hmsjournal.org`, article 553). One kilogram of "fully smithed bar iron"
  required about 100 kg of charcoal and about 25 man-days of work. The full text
  could not be extracted (§5), so the breakdown behind those figures is not read.
- **Cleere, H. (1969), four experimental smelts at Horam**, as reported from his
  records by the Wealden Iron Research Group (`wealdeniron.org.uk`, "Henry
  Cleere's bloomery smelting experiments 1969"). A secondary report of primary
  records. The most successful smelt ran 10.5 hours and gave an 8.8 kg bloom from
  91 kg of ore and 98.6 kg of charcoal. **The other three smelts gave little or no
  bloom**, attributed to heat lost in slag tapping and a sealed arch.
- `[derived]` from Cleere's best smelt: about 0.10 kg of bloom per kg of ore and
  0.09 kg per kg of charcoal. A bloom is not bar iron; Crew's per-kilogram figure
  includes the smithing loss.

**Caveats that bear on closure.** Cleere used an electric blower, a
platinum/platinum-rhodium thermocouple and an Orsat gas analyser, none of them in
K. They measured the smelt; the blower drove it. So the 1-in-4 success rate is
with modern air supply and instruments, and a bellows-driven smelt is not shown to
do as well. The furnace itself was local clay and the ore was local siderite,
both inside K.

### 2.2 The bootstrap chain to machine tools is documented, not measured `[verified]`

- **Nasmyth, James, *James Nasmyth, Engineer: An Autobiography*, ed. Samuel
  Smiles (1883)**, Project Gutenberg eBook 476. Describing Maudslay's
  screw-cutting lathe, Nasmyth gives one product: a screw five feet long and two
  inches in diameter, cut at fifty threads to the inch, with a twelve-inch nut. He
  offers it as proof of the lathe's "complete accuracy" and says it was used to
  divide scales for astronomy.
- That is a capability, not an error figure. No source reached states the
  measured error of the master screw, of the lathe that cut it, or of the tools
  that made that lathe.

### 2.3 Hand-cut files: the process is documented, and the steel is the question `[verified]`

Added 2026-10-17. **[Nicholson File Co.], *A Treatise on Files and Rasps* (1878)**,
archive.org item `atreatiseonfile00provgoog`. Primary.

- **Hand cutting needs only simple tools.** The text says the hand cutter's tools are
  so simple that they are likely the same ones earlier generations used. Teeth are
  raised by chisel blows in both hand and machine cutting.
- **Hand-cut teeth are irregular,** in spacing and height, and the irregularity grows
  with the cutter's lack of skill. The text argues machine-cut files cut as fast and
  smoother. So a hand-cut file works and is worse, and the treatise says so without
  measuring by how much.
- **Hardening is a stated recipe:** teeth coated with a protective paste, heated to a
  red heat, quenched, cleaned, and the tangs softened in a bath of lead. Skill is
  required because the sections are unsymmetrical. No temperatures or hardness
  figures are given.
- **The steel is the closure question.** Files were made from crucible ("cast") steel,
  until recently imported mostly from Sheffield. **Rasps were formerly made of
  "blister" steel**, which is cementation steel, the carburising route K already names.
  So a file-like tool from K's own steel is documented for rasps. Whether a fine file
  from blister steel performs adequately is **ABSENT**. Crucible steel is not named in
  K, and whether it is inside C(K, E) is not tested here.

### 2.4 Whitworth (1840): the drift problem, stated by its author `[verified]`

Added 2026-10-17. **Whitworth, J., "A paper on plane metallic surfaces or true planes",
read at the British Association, Glasgow, 1840**, reprinted in *Miscellaneous Papers on
Mechanical Subjects* (London: Longman, 1858), archive.org item
`miscellaneouspa00whitgoog`. Primary.

- **The drift problem, in his words.** A footnote says that in machines meant for
  reproducing other machines, surface errors matter most, because "the original
  defects are propagated in an aggravated form". That is the study's
  geometry-drift question, stated in 1840. He states it; he does not measure it.
- **Grinding cannot remove an original error.** Grinding a concave surface against a
  true one reduces the first error by creating the opposite error in the true surface.
  **Scraping**, checked with colouring matter against a reference, is "the only certain
  means" of accuracy in his account. The file is used first and is not precise enough
  to finish.
- **The three-plate method, as he gives it:** three plates of hard cast iron, ribbed
  on the back against springing, each resting on three points. One is the model, the
  other two are scraped to it and then compared with each other.
- **Two closure points.** The plates are **cast iron**, and K names bloomery iron and
  carburised steel, not a blast furnace. The sibling `copy-fidelity` protocol allows
  steel plates as well, so the method is not tied to cast iron, but whether plates
  forged from bloomery iron are stiff and sound enough to hold flat is **ABSENT**.
  Second, he says a planing machine greatly speeds the first stage. That is a speed
  claim, not a requirement.

### 2.5 Carburising and hardening: one modern datum only

- A 2025 pack-carburising study (`ph02.tci-thaijo.org`, article 252570) was read
  only through a summarising tool and is **`[unverified]`**. It is also a modern
  process on modern steel, so it does not show what a hand-run charcoal pack
  achieves. Not used.
- No 18th- or 19th-century measured case depth or hardness was found.

---

## 3. What this does to the synthesis

`audit.md`'s line "Structure and tooling: inside" is replaced by:

> **Structure and tooling: materials inside; iron has a measured cost; tool-making
> is unmeasured.**

This is not a demotion to "outside". Hand-made tools existed and the machine-tool
chain was climbed historically, from hand tools to Maudslay's lathe. The record
shows the chain worked once, with skilled people, and does not show what each
step costs or how much error each step adds. That second question is the same
one `copy-fidelity` reached for the machine's own geometry. The two legs now
share an unmeasured rate.

---

## 4. ABSENT: do not fill these in with plausible numbers

1. **Hardness, life, or removal rate of a hand-cut, case-hardened file.** No
   source reached measures any of them.
2. **Measured error at each stage of a machine-tool bootstrap** (Maudslay,
   Whitworth, Ramsden, Holtzapffel). Ramsden's dividing-engine accuracy appears
   only in search snippets, `[unverified]`.
3. **Period case depth and hardness from charcoal pack carburising.**
4. **Removal rates for natural abrasives** (emery, sandstone, quartz sand,
   pumice). None found for pre-industrial practice.
5. **Crew's full yield table.** Only the abstract was readable.
6. **Bloomery success rate with bellows rather than an electric blower.**
7. **Performance of a fine file cut from blister steel.** Documented for rasps only.
8. **Whether three-plate scraping works on plates forged from bloomery iron.** Whitworth
   specifies hard cast iron.
9. **A measured rate for Whitworth's "aggravated" propagation.** Stated, not measured.

---

## 5. Sources

**Read directly, 2026-10-17 (`[verified]`):**

- Crew, P. (1991), "The experimental production of prehistoric bar iron",
  *Historical Metallurgy* 25(1). Abstract only, at
  https://hmsjournal.org/index.php/home/article/view/553
- Wealden Iron Research Group, "Henry Cleere's bloomery smelting experiments 1969",
  https://www.wealdeniron.org.uk/?p=2908
- Nasmyth, J., ed. Smiles, S. (1883), *James Nasmyth, Engineer: An
  Autobiography*, Project Gutenberg eBook 476,
  https://www.gutenberg.org/cache/epub/476/pg476.txt

- [Nicholson File Co.] (1878), *A Treatise on Files and Rasps*,
  https://archive.org/details/atreatiseonfile00provgoog
- Whitworth, J. (1840), "A paper on plane metallic surfaces or true planes", in
  *Miscellaneous Papers on Mechanical Subjects* (1858),
  https://archive.org/details/miscellaneouspa00whitgoog

**Attempted and failed:**

- Crew 1991 PDF galley, https://hmsjournal.org/index.php/home/article/view/553/532:
  returned title and navigation only, no body text.

**Seen but not used (`[unverified]`):** the 2025 pack-carburising paper above;
Ramsden accuracy figures from a biography snippet and a 1797 *Britannica* entry;
Maudslay and Whitworth accuracy claims from encyclopaedia snippets.

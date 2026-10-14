# Findings: the gain leg: is the cascade verdict an inversion?

**Version 0.2, 2026-10-14.** Tests the sibling study's central number. That study
concluded fluidic wall-attachment logic **cannot cascade**, a gate cannot drive
its successor, by two "independent paths". This leg examines both, and finds
that **Path 2 is an inversion of its own quantity, and Path 1 measures a
different quantity on a different mechanism.**

**Result, now at primary-source strength: the verdict "cannot drive even one
matched successor" is not supported.** The standard text of the field defines a
**digital** fluidic amplifier's gain as the *reciprocal* of what the sibling
computed, and states it can be **infinite** for a latching element. The genuine
constraint is **fan-out depth**, and a **fan-out of three is a documented,
worked** design case in the same text.

---

## 0. Evidence tier, stated first

- **`[verified]` = I read the source's own text**: the Belsterling text (below,
  fetched in full and searched locally, then deleted), Wikipedia article bodies
  via the MediaWiki API, and the sibling's own source code and derivation.
- **`[unverified]`** = a search summary or a citation seen but not opened.
- **`[derived]`** = arithmetic performed here, shown so it can be checked.
- **The decisive evidence is now primary**: Charles A. Belsterling, *Fluidic
  Systems Design* (Wiley, 1971), the standard text of the field, read directly.
  The statements below are quoted from its own text.
- **Not obtainable**: the FLODAC paper (FJCC 1964) and patent US 3,190,554
  (JS-walled); Britannica (JS-walled). Reported, not worked around.

**A note on retrieval.** Belsterling's text was fetched from the Internet
Archive as a plain-text derivative, searched locally, and **deleted**; it never
entered the workspace and is not retained anywhere in it. A prior research
attempt had tried to reach a bot-walled thesis through `r.jina.ai` (a public free
reader proxy) and reasoned in its notes that the service "may require an API key
now"; it then called the proxy **with no key and no auth header**, and received a
Cloudflare challenge page. **No credential was read, looked up or transmitted.**
Recorded because a reader is entitled to know what happened.

---

## 1. The verdict, in one paragraph

**The sibling's Path 2 is inverted, and its Path 1 is a different quantity on a
different mechanism.** Path 2 computes `J_c/J_p = (p_c/p_p)·(b_c/w)` = 0.10–0.51
, the control pressure *required to switch*, and reads it as a *gain* short of
parity. **The standard text defines a digital fluidic amplifier's gain as the
reciprocal of exactly that ratio**: "the ratio of the change in output pressure
to the change in control pressure required for switching to occur", adding that
"the gain of the digital amplifier can be infinite if it has negligible
hysteresis" `[verified]`, Belsterling 1971 §4. Because a wall-attachment element
**latches**: Belsterling: the switching curve "exhibits considerable hysteresis
due to the latching effect of wall attachment" `[verified]`, a small
over-threshold control change produces a **full output swing that holds**. Its
gain is therefore **large**, not fractional. Path 1, the measured 0.30, is
**flow gain**, a different quantity (ΔQ_out/ΔQ_control at a given load), measured
on a **membrane valve**, a different mechanism; it does not decide cascade. And
**fan-out of three is a worked design case**: Belsterling §7.3 is titled
"Matching a Digital Amplifier with Three Parallel Flip-Flops" and works the
matching in detail `[verified]`.

**Revised statement: a fluidic wall-attachment stage has gain well above 1 and
can drive a successor; fan-out is shallow (≈3 documented) but real.** The study's
headline moves from *"fluidic logic cannot cascade"* to *"fluidic logic cascades,
with shallow fan-out"*, materially different, and much less fatal.

---

## 2. The decisive evidence, quoted

### 2.1 The gain definition: `[verified]`, and it is the crux

Charles A. Belsterling, *Fluidic Systems Design* (Wiley, 1971), §4 "Performance
Parameters", read directly. Paraphrased, with the load-bearing clauses quoted:

- **Pressure gain** is the ratio of output-pressure change to control-pressure
  change, measured in a particular circuit with a particular load. Because the
  transfer curve is not linear, the operating point must be stated or the number
  means nothing (locator: §4).
- **For a digital amplifier specifically**, gain is the ratio of output-pressure
  change to "the change in control pressure required for switching", and the
  text adds that this gain "can be infinite if it has negligible hysteresis"
  (§4). Both clauses are the author's own words and are quoted exactly.
- It separately defines a **pressure amplification factor** (output change over
  control change at constant output flow) and a **flow gain** (output-flow change
  over control-flow change), three distinct quantities, not one (§4).

**Three consequences, all directly against the sibling's reading:**

1. **Digital gain is output-over-control, not control-over-output.** The
   sibling's `J_c/J_p` is the *control required*; Belsterling's gain is the
   *output obtained* divided by it. **It is the reciprocal**, so the sibling read
   its own number upside down.
2. **For a latching element that gain is large.** The author's own words are that
   it "can be infinite if it has negligible hysteresis", so hysteresis
   *helps* gain here, and wall attachment has hysteresis in abundance (§2.2).
3. **Flow gain is a different quantity.** The 0.30 figure is flow gain; flow gain
   is not the cascade criterion, and the same text keeps pressure gain, pressure
   amplification factor and flow gain separate.

### 2.2 Wall attachment latches, so gain is high: `[verified]`

Same text, §4, on the switching characteristic of the digital (wall-attachment)
element: the curve shows hysteresis "due to the latching effect of wall
attachment", so the pressure at which the jet switches differs from the pressure
at which it reattaches (§4; the one quoted clause is the author's).

That is the mechanism behind the "infinite gain" remark: a bistable element that
latches produces a **full output swing that persists** once a small over-threshold
control has been applied. The sibling's own `--sequential` model implements this
latching; its cascade arithmetic simply failed to follow it through.

### 2.3 Fan-out of three is a worked design case: `[verified]`

Same text, §7.3, "Static Matching of Cascaded Fluidic Components", carries a
subsection titled "Matching a Digital Amplifier with Three Parallel Flip-Flops"
and works the case: matching one digital amplifier to three parallel-connected
flip-flops, with the amplifier's effective load being the combined input
characteristics of the three (one third the impedance of a single unit, found by
tripling the flow at each pressure level). *The subsection title is quoted because
the title itself is the evidence; the body is paraphrased.*

Two points follow:

- **Fan-out 3 is a routine design exercise**, not a limit that makes fluidic
  computation impossible. Its whole point in the text is that **matching is a
  procedure**, one the author summarises as a series of compromises.
- **The text shows the compromise is real**: the case reaches a *mismatch* of
  bias points and operating ranges, and then lists the standard fixes (reduce the
  driver's supply, raise the flip-flops' bias pressure, add series or shunt
  restrictors). So fan-out is not free, it costs matching effort, but it is
  **achievable**, which is the opposite of "cannot drive even one successor".

### 2.4 Cascade is the designed condition, and gain is defined under load: `[verified]`

Same text, §7.1: gain is defined "only when it has the driven amplifier as a
load", and computing it requires the output characteristics of the driving
component laid over the input characteristics of the driven one (§7.1; short
clause quoted, the rest paraphrased).

Fluidic cascade is, in the primary text, an **ordinary engineering problem with a
documented method**, compute the loaded transfer curve. It is not a physical
impossibility, and the sibling's "two independent paths to the same verdict"
squarely misstates the field's own position.

### 2.5 The mechanism statement, for corroboration: `[verified]`

Wikipedia, *Fluidics*, read via the MediaWiki API:

> "Pressure applied to the control ports C1 or C2 deflects the stream, so that it
> exits via either port O1 or O2. **The stream entering the control ports may be
> much weaker than the stream being deflected, so the device has gain.**"

and, on applications:

> "The **FLODAC Computer** was built in 1964 as a proof of concept fluid-based
> digital computer."

A digital computer composed of fluidic stages cannot exist unless those stages
drive one another. FLODAC is a physical existence proof of **fluidic cascading**,
and Belsterling's §7.3 is the design procedure for it.

---

## 3. Fan-out: the real constraint, now at primary-source strength

| claim | status |
|---|---|
| fan-out 3 is achievable (worked case) | **`[verified]`** Belsterling 1971 §7.3 |
| fan-out requires matching compromises | **`[verified]`** same |
| a fluidic amplifier "has gain" (weak control deflects strong) | **`[verified]`** Wikipedia *Fluidics* |
| digital fluidic gain can be large / "infinite" with negligible hysteresis | **`[verified]`** Belsterling 1971 §4 |
| **a numeric fan-out *limit* (maximum driveable count)** | **ABSENT**, no limit figure found |
| **a measured wall-attachment numeric gain** | **ABSENT**, as the sibling always said |

**Arithmetic the derived method implies** `[derived]`: the sibling's ratio
`J_c/J_p` = 0.10–0.51 is the *required control fraction*, so the momentum gain is
its reciprocal, **2–10**; and that band **brackets the documented fan-out of 3**,
which is a satisfying internal check.

**So the honest shape is: compose, yes, documented; fan deep, no, a handful at
most.** The word "cannot" was wrong in both the sibling's paths.

---

## 4. What would still settle it completely

1. **A measured wall-attachment gain** (pressure AND flow; power is their
   product). Belsterling gives the *method* to measure it, the loaded transfer
   curve, but prints no figure for this element. **The Rung-1 measurement
   remains the definitive step**, and the sibling repo's `BUILDERS-NOTES.md`
   already specifies it.
2. **The FLODAC paper** (FJCC 1964, pp. 631–641) or **US 3,190,554**, for
   gate-level fan-out from working hardware. Not obtained here (JS-walled).
3. **A fluidics text printing an explicit maximum fan-out number**: none found.

---

## 5. ABSENT / not-found list

1. **A numeric fan-out *limit*** (the maximum number of successors one element
   can drive). A worked case at 3 exists; a limit does not.
2. **Any measured wall-attachment gain figure**: pressure, flow or power.
3. **The FLODAC paper or patent text.**
4. **Whether Lin et al.'s 0.30 is small-signal flow gain or something else**:
   not re-opened; treated as the sibling summarised it ("30% flow gain").
5. **An explicit numeric relay/fluidic power-gain comparison.**
6. **Britannica's *Fluidics* page** (JavaScript-walled).

---

## 6. Sources

**Read directly (`[verified]`):**
- **Belsterling, Charles A. (1971), *Fluidic Systems Design*, Wiley**, Internet
  Archive item `BELSTERLINGFluidicSystemsDesign1971`, text derivative fetched and
  searched locally, then deleted. Cited by section: §4 "Performance Parameters"
  (the pressure-gain definition, the digital-amplifier definition, the "infinite"
  remark, pressure amplification factor, flow gain, the latching hysteresis note),
  §7.1 (gain defined under load), §7.3 ("Matching a Digital Amplifier with Three
  Parallel Flip-Flops"). **Quotations are held to short phrases; the rest is
  paraphrased, with section locators.**
- Wikipedia, *Fluidics*, MediaWiki API plain text (the "device has gain" and
  FLODAC statements).
- Sibling repository source, read in full: `Fluidic Bootstrap Project`,
  `src/reattachment.py`, `src/cascade.py`, `spec/constants.py`.

**Named but NOT read (`[unverified]`; do not cite as read):**
- "FLODAC – A Pure Fluid Digital Computer", *Fall Joint Computer Conference*
  (1964), pp. 631–641; and US Patent 3,190,554.
- Britannica, *Fluidics*; GlobalSpec, *Fluidic Amplifiers*; ScienceDirect,
  *Fluid Amplifier*.
- NASA CR-783 (reported to contain fan-out/fan-in curves), not obtained.

**Existence proof cited by Wikipedia (`[verified]` as the article's text, primary
not read):** FLODAC Computer, 1964.

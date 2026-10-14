# Findings — the gain leg: is the cascade verdict an inversion?

**Version 0.1, 2026-10-14.** Tests the sibling study's central number. That study
concluded fluidic wall-attachment logic **cannot cascade** — a gate cannot drive
its successor — by two "independent paths". This leg examines both, and finds
that **Path 2 is an inversion of its own quantity, and Path 1 measures a
different quantity on a different mechanism.**

**Result: the verdict "cannot drive even one matched successor" is not supported
by the sibling's own numbers.** Its derived momentum ratio argues the opposite —
that a stage *can* drive a successor, with a gain of roughly 2–10. The real
constraint is **fan-out depth**, not parity.

---

## 0. Evidence tier, stated first

- **`[verified]` = I read the source's own retrieved text** (Wikipedia article
  bodies via the MediaWiki API, quoted in §2), or I read the sibling's own source
  code and derivation directly.
- **`[unverified]`** = a search summary or a citation seen but not opened.
- **`[derived]`** = arithmetic I performed here, shown so it can be checked.
- **Two sources could not be read**: Britannica's *Fluidics* page (JavaScript-
  rendered, no readable body) and a 1960s thesis (bot-walled). Both are reported
  rather than worked around.
- **The decisive evidence is small and primary**: one sentence of the *Fluidics*
  article, plus the sibling's own arithmetic. Everything else is corroboration.

**A note on the failed retrieval.** In the attempt that preceded this file, a
research worker tried to read the bot-walled thesis through `r.jina.ai`, a public
free web-to-markdown proxy, reasoning in its notes that the service "may require
an API key now". It then called the proxy **without any key and without an auth
header**; the service returned a Cloudflare challenge page and nothing else. **No
credential was read, looked up or transmitted.** Recorded because a reader is
entitled to know exactly what happened, not because anything was exposed.

---

## 1. The verdict, in one paragraph

**The sibling's Path 2 is inverted, and its Path 1 is inapplicable.** Path 2
computes `J_c/J_p = (p_c/p_p)·(b_c/w)` = 0.10–0.51 and reads it as a *gain* that
falls short of parity. But that quantity is the momentum the **control input
must supply** to switch the power jet — a **requirement**, not an available
output. In a wall-attachment element the **output is the deflected power jet**,
so the momentum gain is the **reciprocal**, `J_p/J_c = 1/0.51 … 1/0.10` ≈ **2 to
10** `[derived]` — comfortably **above** the parity the study said was
unreachable. The primary text states the mechanism directly: a fluidic amplifier
deflects a **stronger** stream with a **weaker** one, so *"the device has gain"*
`[verified]`. Path 1 — the measured 0.30 "flow gain" — is a **different
quantity** (small-signal *flow* gain, ΔQ_out/ΔQ_in) measured on a **different
mechanism** (a membrane valve, not a wall-attachment element), and flow gain is
not the cascade criterion; a device can have flow gain below 1 and still amplify.
And a working all-fluidic **digital computer, FLODAC (1964)**, is an existence
proof that fluidic stages *do* drive their successors `[verified]`.

**Revised statement, which this leg will defend:** a fluidic wall-attachment
stage has **gain > 1**, so it **can** drive a successor. The genuine limit is
**fan-out** — how many successors one output can hold — reported as small
(≈2–3) and **not verified to primary text here**. That reframes the study's
headline from *"fluidic logic cannot cascade"* to *"fluidic logic cascades, but
with shallow fan-out"* — a materially different and much less fatal result.

---

## 2. The decisive evidence, quoted

### 2.1 The mechanism statement — `[verified]`

Wikipedia, *Fluidics* (retrieved 2026-10-14, MediaWiki API plain text), on the
amplifier — the device the whole question is about:

> "In a fluidic amplifier, a fluid supply … enters at the bottom. Pressure
> applied to the control ports C1 or C2 deflects the stream, so that it exits via
> either port O1 or O2. **The stream entering the control ports may be much
> weaker than the stream being deflected, so the device has gain.**"

and, immediately after:

> "This basic device can be used to construct other fluidic logic elements, and
> fluidic oscillators that can be used in analogous way as flip flops. **Simple
> systems of digital logic can thus be built.**"

**This is the crux.** The control is *weaker* than the output, by construction —
that is what "gain" means, and it is the opposite of the sibling's Path-2
conclusion. The same article also describes the physical basis as a jet
"deflected by a weaker jet striking it at the side", providing "nonlinear
amplification, similar to the transistor".

### 2.2 The existence proof — `[verified]`

Same article, on applications:

> "The **FLODAC Computer** was built in 1964 as a proof of concept fluid-based
> digital computer."

A digital computer composed of fluidic stages cannot exist unless fluidic stages
drive one another. FLODAC is therefore a **physical demonstration of fluidic
cascading**, sixty years old. The article's further reading also cites the FLODAC
patent, **US 3,190,554** ("FLODAC – A Pure Fluid Digital Computer"), which is a
primary source for anyone wanting the gate-level detail.

### 2.3 The sibling's own derivation — `[derived]`

Read directly from the sibling repo (`src/reattachment.py`, `src/cascade.py`).
Its own model gives, "exact under lossless Bernoulli with equal channel depths":

```
J_c/J_p = (p_c/p_p) · (b_c/w)
```

Its own functions show `momentum_flux = 2·p·A`, so this is the ratio of the
control jet's momentum flux to the power jet's. The sourced pressure band
(p_c/p_p = 0.20–0.51) is the **pressure at which the control succeeds in
switching** — the *threshold*, i.e. the *minimum* control needed.

**The output is the power jet.** So the momentum available at the output is the
power-jet momentum, and:

```
momentum gain  =  J_p / J_c  =  1 / (0.10 … 0.51)  ≈  2 … 10
```

**Above 1.** The sibling read the *required input fraction* as if it were the
*available gain*. It is the reciprocal.

**What this does and does not settle.** It settles the *logic* of the sibling's
Path 2: on its own assumptions, that path supports composition, not its
refutation. It does **not** settle the *number* — "momentum gain" is not the
textbook gain of fluidics, and a full answer needs the fan-out margin under
load. §4 says what would close it.

### 2.4 Gain definitions, and why Path 1 is the wrong quantity — `[unverified]`

From search summaries of standard fluidics references (Britannica *Fluidics*;
GlobalSpec *Fluidic Amplifiers*; ScienceDirect *Fluid Amplifier* — **pages not
read directly**, tagged accordingly):

- **pressure gain** = ΔP_out / ΔP_control, at constant output flow;
- **flow gain** = ΔQ_out / ΔQ_control, at constant output pressure;
- **power gain** = pressure gain × flow gain, and is the quantity that governs
  whether a stage can drive a successor.

**Consequence for Path 1.** The 0.30/0.322 figures the sibling cites are **flow
gain**, measured on a **membrane valve** (Lin, Zhou & Cao), a mechanism the
sibling *itself* flags as a cross-mechanism transfer. Flow gain below 1 does not
imply a stage cannot cascade — pressure gain and flow gain trade off against each
other, and it is their **product** that matters. **Path 1 is therefore not the
cascade criterion**, whatever its value.

---

## 3. Fan-out — the real constraint, and the one number still missing

If gain is > 1, the question becomes **how many** successors one stage can drive.
The evidence here is weaker and is reported as such:

- **Reported figure ≈ 2–3, commonly quoted as ~3** `[unverified]` — a search
  summary citing Wikipedia *Fluidics* and ScienceDirect. **I could not verify a
  fan-out number in any primary text I opened**, and Wikipedia's article as
  retrieved contains **no fan-out figure**.
- **Corroborating pointer `[unverified]`:** the table of contents of Belsterling,
  *Fluidic Systems Design* (Wiley, 1971) — the standard text — includes a worked
  case titled around **"matching a digital amplifier with three parallel
  flip-flops"**, i.e. **3-way fan-out as a design exercise**. Suggestive of ~3
  being the working figure; not a measurement.
- **A snippet attributed to the FLODAC paper** (Fall Joint Computer Conference,
  1964, pp. 631–641) describes a "NOR gate with a fan-in and fan-out of four"
  `[unverified]` — named source, snippet only, **not opened**.

**Arithmetic this implies** `[derived]`: with gain 2–10 against a successor that
needs 0.10–0.51 of the power jet, **1-way** cascade is comfortable (2–10×
margin); **3-way** fan-out needs 0.30–1.53 of the power jet — **marginal at the
bottom of the gain band, comfortable at the top**; **10-way** is out. So the
honest shape is: **compose yes, fan deep no.**

**Fan-out verified to primary text: ABSENT.** This is the leg's chief gap and the
single most valuable thing to close.

---

## 4. What would settle it

1. **A fluidics text's gain definition, read directly** — Belsterling, *Fluidic
   Systems Design* (1971), or the Pergamon *Fluidics* volumes. This would fix
   whether the correct cascade criterion is pressure gain, power gain, or
   momentum gain, and give the standard fan-out figure. **Cheapest decisive step.**
2. **The FLODAC paper** (FJCC 1964, pp. 631–641) or **US 3,190,554** — the
   gate-level record of a machine that demonstrably cascaded. Would give real
   fan-out numbers from working hardware.
3. **The Rung-1 measurement** (the sibling's own falsifier): build **one**
   wall-attachment element and measure its pressure and flow gain. This settles it
   empirically, with no theory, no printer and no simulator.
4. **A careful read of the sibling's own model** for what `p_c/p_p` *means* in
   its derivation — whether it is the switching threshold (as path 2 assumes) or
   something else. If it is the threshold, the inversion in §2.3 is not merely
   plausible but forced.

---

## 5. ABSENT / not-found list

1. **Any fan-out figure verified to primary text.** Reports of ~2–3 rest on
   search summaries.
2. **A direct reading of any fluidics textbook's gain definitions.** Britannica
   is JavaScript-walled; Belsterling could not be opened.
3. **The FLODAC paper or patent text** (the strongest existence proof's details).
4. **Any measured wall-attachment *gain*** (pressure, flow or power) — the figure
   the sibling study has always said does not exist in its nine works. Still
   absent.
5. **Whether Lin et al.'s 0.30 is small-signal flow gain or something else** —
   the paper was not re-opened; the sibling's own summary says "30% flow gain",
   which is what §2.4 treats it as.
6. **The 1960s thesis** (Missouri S&T) whose snippets mentioned fan-out analysis —
   bot-walled, not obtained.

---

## 6. Sources

**Read directly (`[verified]`):**
- Wikipedia, *Fluidics* — https://en.wikipedia.org/wiki/Fluidics, retrieved
  2026-10-14 via
  `https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles=Fluidics`.
- Sibling repository source, read in full: `Fluidic Bootstrap Project` —
  `src/reattachment.py`, `src/cascade.py`, `spec/constants.py` (the momentum
  ratio and the cascade report).

**Named but NOT read (`[unverified]`; do not cite as read):**
- Britannica, *Fluidics* — https://www.britannica.com/technology/fluidics
  (JavaScript-walled; no readable body returned).
- GlobalSpec, *Fluidic Amplifiers*; ScienceDirect, *Fluid Amplifier* (search
  summaries only).
- Belsterling, C. A. (1971), *Fluidic Systems Design*, Wiley —
  https://archive.org/details/BELSTERLINGFluidicSystemsDesign1971 (ToC seen, not
  read).
- "FLODAC – A Pure Fluid Digital Computer", *Fall Joint Computer Conference*
  (1964), pp. 631–641; and US Patent 3,190,554.
- NASA CR-783 (reported to contain amplifier fan-out/fan-in characteristic
  curves) — not obtained.

**Existence proof cited by Wikipedia (`[verified]` as a statement of the
article's text, primary not read):** FLODAC Computer, 1964.

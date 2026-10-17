# NOTICE: sources, rights, and the evidence rule

## What this repository publishes

Original analysis: a criterion, an audit that applies it, and the findings of
the power and control legs. Nothing else.

## What it deliberately does not publish

- No source PDFs.
- No full-text extractions of any source.
- No figures or tables reproduced from any source.
- **No passage longer than a short phrase** is reproduced verbatim. Everything
  else is paraphrased, with a locator (section, page or DOI) so a reader can
  check the claim against the source.

Where a source's exact wording *is* the evidence, a stated condition of
convergence, or the name a source gives to a quantity, the shortest clause that
carries the claim is quoted, in quotation marks, with attribution.

**The one exception, and why it is principled rather than convenient.** The two
legs added on 2026-10-14 (`findings-power.md`, `findings-control.md`) rest on
**encyclopaedia text**, chiefly Wikipedia, which is licensed **CC BY-SA**, free
to reuse *with attribution*. Quoting it at sentence length is expressly
permitted by its licence, so those two documents quote it more fully than the
short-phrase rule would allow for a **restricted** source, and every quotation is
attributed in place. The rule above binds restricted sources; for CC-licensed
sources, attribution is the condition and it is met. This distinction is stated
because otherwise the repo would be quietly breaking its own stated rule, which
is exactly the kind of thing this project corrects elsewhere.

Nothing is held on disk either: no `References/` folder, no cached copies, no
extractions.

## Verification status of citations: and why the rule is strict here

Every citation carries a tag:

- `[verified]`: the source's own text, or at minimum its own registered
  metadata record, was read, and the claim rests on it.
- `[unverified]`: a lead from a search result or a third-party citation,
  **not** checked against the source's own record.
- `[discarded]`: a lead that failed verification, recorded so it is not
  re-adopted.

**Why this matters.** In the workstream immediately preceding this repository,
two searches returned **fabricated reference identifiers**, NTRS citation IDs
that resolved to unrelated documents, presented in the same confident register as
the genuine results. The sibling `closure-audit` therefore separates `[primary]`
from `[secondary]` evidence and refuses to rest a claim on the latter.

**No claim in this repository rests on an `[unverified]` cite.** Where a source
could not be reached, the finding is recorded as a **stated gap**, not filled
with an estimate. If the literature does not provide a number, the number is
**ABSENT**; it is never inferred.

## Scope of the central claim

The criterion in `protocol.md` is a **definition**, stated before the evidence.
Its *application* is what the findings documents test. The distinction matters:

- The criterion cannot be refuted by evidence; it can only be applied.
- The **verdict** on any machine can be refuted, and `protocol.md` §9 says what
  would do it.

A negative result here is stated as **"no demonstrated machine meets the
criterion, and here is where each attempt stops"**, never as "therefore
impossible." Absence of a demonstration is not proof of impossibility, and this
repository will not present it as one.

## Rights status of cited sources

Recorded per source as the work proceeds: publisher, year, DOI or URL, and
whether the work is open-access or conventionally restricted. Where a work is
restricted, only short attributed phrases appear. Works that are US Government
publications, or released under a Creative Commons licence, are marked as such
where they appear.

## This repository's licence

Written analysis and documentation: **Creative Commons Attribution 4.0
International (CC BY 4.0)**, see `LICENSE`. The one piece of code,
`model/controller_budget.py`, was added with the logic leg after this notice
first said the repository would hold none. It is arithmetic on a logic netlist,
not a simulation (`findings-logic.md` §0), and it is covered by the same licence.

Copyright © 2026 Thymeed.

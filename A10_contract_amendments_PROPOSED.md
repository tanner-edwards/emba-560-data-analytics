# A10 Purpose Contract: proposed amendments (DRAFT)

Proposed by Tanner Edwards, 2026-11-23. **Not in effect.** These are changes to `A10_purpose_contract_FROZEN_2026-11-17.md`, which was frozen by Matt alone. Each one takes effect only when Tanner and Matt both agree. Agreed items are then copied into the contract's **Amendments** section with the date and reason.

| # | Contract field | Current | Proposed | Status |
|---|---|---|---|---|
| A1 | Population: years | 2000–2023, no reason stated | **Keep 2000–2023**, and record the reason | Proposed |
| A2 | Population: budget floor | Budget ≥ $1M, no sensitivity check | **Keep $1M for the main analysis; rerun at $100K as a sensitivity check.** Budgets under $1K are data errors and are handled in cleaning. | Proposed |
| A3 | Outcome: 2.5× multiple | "Commonly cited rule of thumb" | **Keep 2.5×**, labeled as an industry convention, not a data finding | Proposed |
| A4 | Allowed inputs | Fixed list of 8 | **Re-open after cleaning.** Add every input known at the financing decision. | Open: list to follow |
| A5 | 2020–2023 stress test | COVID years reported separately | Not discussed yet | Open |

## A1. Keep 2000–2023, with a reason
**Reason:** 24 years of films is enough to be relevant to today's market. Before 2000, the data gets thin, and dollar amounts would need inflation adjustment to compare fairly. The end year stays at 2023 because later films hadn't finished their theatrical run when the data was pulled.

## A2. Keep the $1M floor; add a $100K sensitivity check
**Reason to look below $1M:** Low-budget films are part of the financing decision, and they're where the biggest margins happen. Among usable films with a $100K–$1M budget, 14% returned 10× their budget or more, against 4% of films above $1M.

**Reason not to make it the main population:** the S4 rerun (2026-11-23). Revenue is missing far more often below $1M, and the films that are missing it are mostly losers. So the $100K–$1M films we can see lean toward the winners, which probably inflates the 14% figure too.

| Films with a budget | $1M floor | $100K floor | $100K–1M only |
|---|---|---|---|
| Films | 11,212 | 16,065 | 4,853 |
| Missing revenue | 39% | 52% | 83% |
| Missing revenue, 2020–23 | 52% | 69% | 92% |
| Missing-revenue films with US gross < budget* | 98% | 97% | 93% |

\*Among the 3–5% of missing-revenue films that have a US box office figure.

**Proposal:** the main analysis keeps the $1M floor. The final model is rerun on the $100K population (7,671 usable films: train 5,554 / test 1,426 / stress 691; 66.9% losers), and the report shows both results side by side. Any $100K result is limited to "films with reported revenue."

**Also changes:** the plan adds a step for the $100K sensitivity rerun. `00_build_dataset.ipynb` gets a flag for the $100K population (e.g. `usable_100k`) alongside `usable`.

## A3. Label 2.5× as an industry convention
**Reason:** 2.5× is a rule of thumb, not something the data shows. Theaters keep roughly half the box office, and marketing often costs about as much as production, so a film needs about 2–2.5× its budget to break even. The report must say that the threshold is an industry convention, cite a source for it, and show the 1×, 2× and 3× sensitivity results next to it.

## A4. Inputs: re-open the allowed list (pending)
The frozen list allows 8 inputs. The rule behind it stays: **only information known at the financing decision, before production.** The list itself is re-opened. After cleaning, every column that meets the rule is proposed here with its evidence. Candidates so far: MPAA rating, source material, creative type, production method, writer, cast, distributor, franchise / sequel (see `FEATURE_IDEAS.md`).

## A5. COVID-era stress test (not discussed yet)

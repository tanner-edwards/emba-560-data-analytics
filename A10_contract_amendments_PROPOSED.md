# A10 Purpose Contract: proposed amendments (DRAFT)

Proposed by Tanner Edwards, 2026-11-23. **All agreed by Tanner and Matt on 2026-11-24 and copied into the contract's Amendments section** (A5: keep the separate stress test). Kept as the evidence record. These are changes to `A10_purpose_contract_FROZEN_2026-11-17.md`, which was frozen by Matt alone. Each one takes effect only when Tanner and Matt both agree. Agreed items are then copied into the contract's **Amendments** section with the date and reason.

## A8. Change the decision to the studio's pre-release review
**Proposed by Matt, 2026-11-24. DRAFT, not in effect until Matt and Tanner both approve this wording.** Matt reports that Tanner agrees to the change of question.

**Question the model answers:** Will this movie be successful, meaning worldwide revenue of at least 2.5× its budget?

**Decision it supports:** Before release, which upcoming films are most likely to lose money, so the studio can review their release and marketing plans first?

**Reason:** The team chose to predict a film's success before release instead of whether a financier should agree to make it. The problem scan for candidate #1 already described a decision made "before a film is released"; the frozen contract had narrowed it to financing. At release, more of the film's plan is known and the studio can still change its release and marketing.

### Contract fields that change

| Field | Frozen contract | Amended |
|---|---|---|
| **Decision** | At financing, flag / proceed / pass | Before release, the studio decides which films get a deeper review of the release plan and marketing plan, and which proceed on standard review |
| **Action** | 20% highest-risk projects per year go to deep review | Each year, the 20% of films with the highest predicted risk of losing money get the deeper review. The rest proceed as planned. A person makes every final decision. |
| **Owner** | Head of Acquisitions at a film co-financier | The studio executive responsible for release and marketing. Still a stand-in role with no real stakeholder interviews; the report says so. |
| **Decision time** | Before production | When the release and marketing plans can still be changed: the film is finished or nearly so, and no public release results exist |
| **Unit** | One feature film at its financing decision | One feature film at its pre-release review |
| **Outcome** | Money-loser: worldwide revenue < 2.5× budget | **Same cutoff.** Successful = worldwide revenue ≥ 2.5× budget; money-loser = everything below. The model still ranks by money-loser risk. 2.5× is labeled an industry convention; 1×, 2× and 3× sensitivity checks stay. |
| **Allowed inputs** | 8 inputs known at financing | The same 8, using values known before release, plus MPAA rating, distributor, writer, source material, creative type, production method and franchise (conditions below) |
| **Value** | Loss avoided on flagged deals | (extra money-losers caught × loss avoided per film by a changed plan × share of flagged plans changed) − (successful films flagged × cost of an unneeded review). Every term stays a blank for the owner; the report shows break-even values. |
| **Rival framing** | Director premium | The original financing screen, limited to inputs known before production |

### Input conditions
- **Franchise:** count a film as franchise only if an earlier film in that franchise had been released. Source data tags first films in hindsight (*Iron Man*, 2008).
- **Track records:** use only films released before this one.
- **Coverage:** MPAA rating, source material and creative type are often blank for small films, so each carries a missing flag. No rows are dropped for blanks.
- **Still prohibited:** box office, opening results, scores, votes, popularity, all reviews (including pre-release reviews), festival buzz and TMDB keywords. Keywords can't be used to fill another input either.

### Prohibited uses
1. **Hiring or blacklisting people:** unchanged.
2. **Automatic reject** becomes: never an automatic cancellation, shelving or marketing cut.
3. **Causal claim** also covers release and marketing: the model shows which films are risky, not that changing the plan would fix them. The data has no marketing spend.
4. **Outside its population:** unchanged.

### Limitations to report
- The production budget is already spent by this point. The screen can only improve what is still undecided.
- The data records what finally happened (date, distributor, rating), which may differ from the plan at review time. Weakest link 4 is reduced, not removed.

### What stays the same
Population years and the $1M floor, the training / test / stress periods, baselines (a) and (b), the ≥ 5-point evidence bar, 20% capacity, and stop conditions S1–S4. Cleaning rules can't drop films because of their outcome (for example, only those with low revenue).

### Effect on the other proposals
| Proposal | Effect if A8 is approved |
|---|---|
| A3 | Accepted in substance (keep 2.5×, labeled a convention) |
| A4 | Resolved by the input list above |
| A6 | Replaced by A8's decision time |
| A7 (US box office < 1.25×) | Not adopted as the main outcome or population. Can run as a sensitivity check. **Tanner to confirm.** |
| A1, A2, A5 | Not affected; still need a decision |
| Budgets and revenue from The Numbers / Wikidata | Not covered here; needs its own amendment |

### What had been seen before this amendment
No model had been fitted. The following had been looked at: loser rates overall and by period (**including the 2016–2019 test films**), by financial source, by Rotten Tomatoes match status, and for US and non-US films; returns for budgets below and above $1M; and a budget vs revenue chart. The success cutoff and evidence bar did not change.

### Files to update after approval
The contract's Amendments section (copy this in), `PLAN.md` Direction, `README.md`, `FEATURE_IDEAS.md`, both notebooks' introductions, and the `A10-master.ipynb` title. Each person edits their own notebook.

### Approval
- [x] Matt Sorensen, 2026-11-27, date:
- [ ] Tanner Edwards, date:

## All other proposals

| # | Contract field | Current | Proposed | Status |
|---|---|---|---|---|
| A1 | Population: years | 2000–2023, no reason stated | **Keep 2000–2023**, and record the reason | Agreed 2026-11-24 |
| A2 | Population: budget floor | Budget ≥ $1M, no sensitivity check | **Keep $1M for the main analysis; rerun at $100K as a sensitivity check.** Budgets under $1K are data errors and are handled in cleaning. | Agreed 2026-11-24 |
| A3 | Outcome: 2.5× multiple | "Commonly cited rule of thumb" | **Keep 2.5×**, labeled as an industry convention, not a data finding | Agreed 2026-11-24; superseded by A7 |
| A4 | Allowed inputs | Fixed list of 8 | **Re-open after cleaning.** Add every input that meets the A6 timing rule. | Agreed 2026-11-24 |
| A5 | 2020–2023 stress test | COVID years reported separately | **Keep** 2020–2023 as a separately reported stress test | Agreed 2026-11-24 |
| A7 | Outcome and population | Worldwide revenue < 2.5× budget; films with reported worldwide revenue | **US box office < 1.25× budget; films released in the US** | Agreed 2026-11-24 |
| A6 | Decision time / timing rule | At financing, before production | **Before release.** Any variable that can be controlled before the film releases is allowed. | Agreed 2026-11-24 |
| A9 | Decision and evidence standard | Flag the 20% riskiest films (money-losers) for deep review; capture rate of losers | **Pick the 20% most likely winners**; measure winners caught in the top 20% | Agreed 2026-11-27 |

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
The frozen list allows 8 inputs. The timing rule changes under A6: **anything that can be controlled before release.** The list itself is re-opened. After cleaning, every column that meets the rule is proposed here with its evidence. Candidates so far: MPAA rating, source material, creative type, production method, writer, cast, distributor, franchise / sequel (see `FEATURE_IDEAS.md`).

## A5. COVID-era stress test
Agreed 2026-11-24: keep 2020–2023 as a separately reported stress test. COVID changed how people watch films, so those years are expected to differ.

## A6. Move the decision time from "before production" to "before release"
**Proposed by Tanner, 2026-11-24.**

**Rule:** any variable that can be **controlled before the film releases** is a fair input. Anything that only exists after release (box office, scores, votes, reviews) stays prohibited.

**Reason:** the line between financing and release is mostly a timing detail. Release date, distributor, rating, final runtime and final budget are all set before release and are things the studio controls. Many of them are already treated as "planned" values under the current rule.

**What it changes in the contract**
- **Decision:** from "at the financing stage, before production" to "before release." The screen can be run at greenlight and rerun before release as the controllable values are set.
- **Decision time / allowed inputs:** add distributor, MPAA rating, final runtime and budget, cast, release date, production method, and similar pre-release choices.
- **Unit:** "one feature film at its financing decision" becomes "one feature film before release."
- **Weakest link 4** (planned vs actual budget and runtime) mostly goes away: final values are known before release.

**Gray area to settle:** things known before release but not controlled by the studio, e.g. pre-release critic reviews (the reviews table marks these as `before_release`), festival buzz, and TMDB keywords. Proposed: still prohibited, because they aren't controlled and are often recorded after release.

**Also changes:** `README.md`, `CLAUDE.md`/`AGENTS.md` and `FEATURE_IDEAS.md` state the "before production" rule; they're updated once Matt agrees.

## A7. Label on US box office, at 1.25× budget
**Proposed by Tanner, 2026-11-24.**

**Goal:** predict which films will make money **in the US**. That includes foreign films released in the US.

**New label:** a film is a money-loser if its **US box office < 1.25× its production budget**.

**Reason:**
- **Fits the goal.** The question is the US market, not the world.
- **The data is better.** US box office is filled for 84% of films after cleaning (93% of US films). Worldwide revenue looks complete, but for 618 films it is really the US gross only, so those films are wrongly labeled losers (89–98% vs 62–70%).
- **1.25× matches the old rule.** The US is about half of worldwide box office (median 52%), so 1.25× US ≈ 2.5× worldwide. Tanner: "We're here to make money, not waste our time." About 67% of films are losers under this label, the same share as before.
- 1.25× is still an industry convention, not a data finding (as A3 said); the report shows 1× and 1.5× next to it.

**New population:** films released in the US, i.e. with a reported US box office. Foreign films without a US release fall out.

**Also changes:** the label column moves from `fin_revenue` to `domestic_gross` (`domestic_gross` stops being "post-release: checks only"). A2's S4 numbers and the split sizes need rerunning.

## A9. Frame the screen as picking winners
**Proposed by Tanner, 2026-11-26. Agreed by Matt 2026-11-27 and copied into the contract's Amendments section.**

**Change:** the label stays the same (A7: US box office vs 1.25× budget), but the decision and evidence standard flip from losers to winners.

| Field | Current (frozen + A7) | Proposed |
|---|---|---|
| **Decision / action** | Each year, the 20% of films with the highest predicted risk of losing money go to deep review | Each year, the 20% of films **most likely to be winners** (US box office ≥ 1.25× budget) are identified; the rest get a closer look before money is committed to release and marketing |
| **Positive class** | Money-loser (US box office < 1.25× budget) | **Winner** (US box office ≥ 1.25× budget). The data column `loser` is unchanged; winner = not loser |
| **Evidence standard** | Share of all losers caught in the top 20%; beat baseline (b) by ≥ 5 points with a bootstrap 95% CI excluding 0 | Share of all **winners** caught in the top 20% picks; beat baseline (b) by ≥ 5 points with a bootstrap 95% CI excluding 0. Also report the hit rate @20% (share of picks that are winners) and AUC |
| **Baseline (b)** | Flag genre × budget-tier groups with the highest historical loss rate | Pick genre × budget-tier groups with the highest historical **winner** rate (training years only) |

**Reason:**
1. **The loser metric had almost no room.** With 67% losers, the riskiest 20% can catch at most 30% of all losers. Baseline (b) already reaches 23%, so the 5-point bar needed 28.3% out of 30%. Winners are 33% of films, so the top 20% can catch up to 60% of them, which leaves real room to tell a good model from a lucky one.
2. **It matches the question the team settled on:** "Will this movie be successful?" (Matt's A8 draft), and how the analysis has been presented since 2026-11-24 (Tanner).
3. **Nothing has been fit on the test set.** The switch was made on cross-validated training results only (Edwards §18: winners caught 37.2% vs 28.0% for the baseline).

**What stays the same:** the label definition (A7), population, splits (A5), 20% capacity, the ≥ 5-point bar, sensitivity checks (1× / 1.5×, $100K floor).

**Approval**
- [x] Tanner Edwards, 2026-11-26
- [x] Matt Sorensen, 2026-11-27

# A10 Project Purpose Contract — FROZEN 2026-11-17

Date drafted: 2026-11-17. Analyst: Matt Sorensen. AI role: Problem Setter, then Challenger (Claude Code, decision-statement-builder skill).
Source candidate: #1 in `report/A10_problem_scan_2026-11-17.md`.
Status: **FROZEN 2026-11-17, approved by Matt Sorensen.** This was done before any analysis of how inputs relate to the outcome; only structural profiling and join tests have been run. Any later change requires a dated amendment, added below, with a stated reason.

## Contract fields

| Field | Contract answer |
|---|---|
| **Purpose pathway** | **Predictive** (the one primary path). An explanatory layer reports how much director track record adds to the prediction. That's association only, with no causal claim. |
| **Decision** | At the financing stage, before production, the acquisitions team decides for each incoming project whether to **flag for deep review**, **proceed on standard review**, or **pass**. |
| **Action** | Each year, the 20% of projects with the highest predicted risk go to deep review (comparable-film analysis, a second reader, renegotiating terms). The rest get standard review. The screen never rejects a project on its own. |
| **Decision time** | When the financing decision is made, before production. **Allowed inputs:** budget, genre, director's track record from earlier films only, production companies' track record from earlier films only, planned runtime, planned release month and quarter, original language, production country. **Prohibited inputs (known only after release):** revenue, box office, vote counts and averages, popularity, critic and audience scores, review text, TMDB keywords (crowd-edited after release). |
| **Population & unit** | Unit = **one feature film at its financing decision.** Population = feature films released 2000–2023 with a reported budget ≥ $1M and reported worldwide revenue > 0, excluding adult titles. Training: 2000–2015. Test: 2016–2019. Stress test: 2020–2023 (COVID era), reported separately. |
| **Outcome / target & horizon** | Positive class = **"money-loser": worldwide revenue < 2.5 × budget.** The 2.5× multiple is a labeled assumption (a commonly cited rule of thumb for covering marketing and the exhibitor's share). It's rerun at 1×, 2× and 3× as a sensitivity check. Horizon = full theatrical run as recorded in TMDB. The model estimates each project's probability of being a money-loser. |
| **Baseline** | (a) **Random 20% flagging**, which catches losers at the base rate (the floor). (b) **A simple rule:** flag projects in the genre × budget-tier groups with the highest historical loss rate, using training years only. The model has to beat (b), not just (a). |
| **Evidence standard** | On the 2016–2019 test films, the share of all money-losers that fall inside the flagged top 20% (capture rate). The model must beat rule (b) by **≥ 5 percentage points**, with a bootstrap 95% CI that excludes 0. Also report precision at 20%, calibration, and the result for the 2020–2023 stress set. *Bar confirmed by Matt at the freeze.* |
| **Value** | More money-losers reach deep review without adding review workload: same 20% capacity, better targeting. Value per year = (extra losers caught × loss avoided per caught loser × share of flagged deals actually changed) − (good films wrongly flagged × cost of a wrongly flagged deal). Each term is a **blank the owner fills in**; the report shows break-even values, not invented dollars. |
| **Constraints** | Review capacity: 20% of projects. Data rights: Kaggle public datasets, license recorded in the Data Receipt. Timing: frozen analysis by Nov 25, due Dec 4. No individual-level sensitive data, but director names are personal names, so results are reported at the aggregate or feature level, not as rankings of named people. Simplest adequate method: logistic regression first. |
| **Owner** | **Head of Acquisitions** at a representative film co-financier. This is a stand-in role: there are no real stakeholder interviews, and the report states that limitation. The owner is accountable for using the screen, monitoring it, and stopping it. |

## Rival framing
**#2, director premium:** the greenlight committee decides whether to pay extra for a director with a strong track record. It uses the same data and time but asks a different question: what one input is worth, not sorting projects. It's the fallback if #1 fails the red-team or stop condition S1.

## Prohibited uses
The screen must never quietly become:
1. **A tool for hiring or blacklisting people.** It must not rank, score or exclude individual directors or other talent, or feed into pay negotiations.
2. **An automatic reject.** A flag only sends a project to deep review, and a person makes the final call.
3. **A causal claim.** "Directors with strong track records *cause* profit" isn't supported. Track record is a predictive input and nothing more.
4. **A screen applied outside its population.** It doesn't cover micro-budget films (< $1M), streaming-only releases, or films without a theatrical revenue record.

## Minimum evidence to move forward, and stop conditions
**Move to a pilot** (run alongside human review for one slate, with no decisions changed) only if S1 passes, calibration is acceptable on the test films, and capture on the 2020–2023 stress set doesn't fall below the rule baseline.

| # | Stop trigger (observable) | Disposition |
|---|---|---|
| S1 | The model doesn't beat rule (b) by ≥ 5 pts of capture on 2016–2019 with a CI that excludes 0 | **Satisfice:** recommend the simple rule |
| S2 | Removing director track record changes capture by < 2 pts | Drop the director claim and report it as a null finding |
| S3 | The hand-check of 50 joined pairs shows > 10% wrong matches | Drop the RT join and use production-company track record as the focal factor |
| S4 | Films with a budget but no reported revenue are a large share of the population, and the cross-check with RT box office shows they skew toward losers | Restrict the claim to films with reported revenue, or **redirect** |

## Red-team (Challenger)

**Weakest link 1: a filter I set earlier selected on the outcome. *This is an AI correction.*** The "usable films" filter I used in the join tests required **≥ 50 TMDB votes**. Vote count is measured after release and rises with success (Spearman 0.48 with log ROI). Filtering on it silently drops obscure flops, which are exactly the films the screen exists to catch. That would make the loss rate look lower and the model look better than it is. **Fix:** the population now uses budget ≥ $1M and revenue > 0, with no vote filter (see above). This is a strong candidate for the report's required "material AI correction."

**Weakest link 2: films with missing revenue.** 84,135 released TMDB films have a budget, but only 18,398 also have revenue. Films with no revenue on record are likely to include unreported flops. If so, the population is short on losers, and the base rate and capture will be biased. **Fix:** Phase 2 measures how many films have a budget ≥ $1M but no revenue, and uses RT domestic box office to estimate what those films earned (stop condition S4).

**Weakest link 3: is the value logic real?** Real financiers have scripts, cast packages, comparable films and presale data that a public-data screen doesn't. So could this ever beat their judgment? **Answer:** it isn't meant to replace their judgment. It's a base-rate check that decides where scarce deep-review time goes. The value claim is limited to "better targeting at the same capacity," and the report must say that we can't compare against the experts' actual track record, which isn't in the data.

**Weakest link 4: inputs that sit between "planned" and "actual."** TMDB records the *final* budget and runtime, not the planned ones, and they can drift during production, possibly more for troubled productions. That's a mild leak. **Fix:** report it as a limitation, and as a robustness check, refit using budget tiers rather than exact dollars.

**Did the dataset pick this problem?** Partly, and the scan flags it. Budget and revenue being available made this candidate feasible. The decision (where to spend limited review time) is still real and has an owner, so it stays, with the population limits stated openly.

**The course's five-question check**
1. *Predicting, changing, or describing?* Predicting: the risk of a loss at the financing stage. The director layer describes only, and nothing here claims to change outcomes.
2. *Where's the evidence and data receipt?* TMDB and the two RT files in `data/raw/`. The Data Receipt is plan step 8, still to do.
3. *What would make us stop, and would we recognize it?* S1–S4 above. Each one is a number checked against a stated threshold.
4. *Which CRISP-DM phase are we in?* Business Understanding. Only structural profiling has been done; no relationships with the outcome have been modeled.
5. *What exact quantity is being claimed?* The share of 2016–2019 money-losers (revenue < 2.5× budget) caught in the top 20% of predicted risk, compared with the genre × budget rule, with a 95% CI.

## Verification
- Every field has a specific answer: yes.
- Rival framing and prohibited uses are both present: yes.
- Stop conditions are observable triggers: yes, S1–S4.
- It has survived a real Challenger attack: four weak links were attacked, and one led to a change in the population definition.

## Freeze record
- [x] ≥ 5-point evidence bar confirmed by Matt, 2026-11-17.
- [x] $1M budget floor confirmed by Matt, 2026-11-17.
- [x] Instructor approval of the path: not required for this project (confirmed by Matt, 2026-11-17).

## Amendments
The contract fields above are kept as frozen. Where an amendment differs, the amendment applies. Full text: `A10_contract_amendments_PROPOSED.md`.

**Approved 2026-11-24 by Matt Sorensen and Tanner Edwards** (Tanner's approval reported by Matt; takes effect when Tanner approves the pull request that adds this section). All proposed by Tanner.

| # | Field | Amendment | Reason |
|---|---|---|---|
| A1 | Population: years | Keep 2000–2023 | Enough films to be relevant today; earlier data is thin and needs inflation adjustment; later films hadn't finished their run |
| A2 | Population: budget floor | Keep $1M; rerun the final model at $100K as a sensitivity check, limited to films with reported revenue | Low-budget films are part of the decision, but 83% of $100K–$1M films have no revenue |
| A3 | Outcome: multiple | Keep 2.5× worldwide, labeled an industry convention, with a cited source and the 1×, 2× and 3× sensitivity results | The threshold is a rule of thumb, not a data finding |
| A4 | Allowed inputs | Reopen the list to inputs that meet A6. The specific list is in A8 (draft), so none is added yet. | More is known before release than at financing |
| A5 | Stress test | Keep 2020–2023 reported separately | No change |
| A6 | Decision time | Before release. Inputs the studio can control before release are allowed. Post-release data, pre-release reviews, festival buzz and TMDB keywords stay prohibited. | Release date, distributor, rating, and final runtime and budget are set before release |
| A7 | Side check | Rerun the final model with money-loser = US box office < 1.25× budget, on films with a reported US box office. **The main outcome and population do not change.** | Worldwide revenue equals US gross for 618 films, which wrongly labels many of them losers; the side check shows whether the result depends on that |

**Disclosure:** no model had been fitted. Loser rates had been seen overall and by period (including the 2016–2019 test films), by financial source, by match status, and for US and non-US films. The main outcome cutoff and the evidence bar did not change.

**Not yet in effect:** A8 (decision, owner, action and input list).

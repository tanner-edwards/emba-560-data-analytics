# A10 Plan, Status, and Handoff

A10 team project (Matt + one colleague, worked as individual until Phase 7), due **Fri Dec 4, 2026, 3:30 PM**, 120 pts. Plan agreed 2026-11-17. This file is the single source of truth for plan, status, and session handoff.

Contents: [Handoff](#handoff) · [Session procedure](#session-procedure) · [Direction](#direction) · [Plan and status](#plan-and-status) · [Status log](#status-log)

## Handoff
*Rewritten at every session end. Read this first when resuming.*

**Last updated:** 2026-11-26, Tanner's session cae33d13 (Claude Code), branch `tanner/label-eda`
**Where we are:** Data Understanding is done. Amendments A1–A7 are agreed and in the contract; the cleaning rules run in `01_clean_dataset.ipynb` (population 4,933 films, label = US box office < 1.25× budget, 66.9% losers); `A10-master.ipynb` has CRISP-DM §1–3 (PR #7, merged). On `tanner/label-eda`, `Edwards-A10.ipynb` §10–16 compares every input to the return (training years 2000–15 only) and screens the feature ideas. A side study, `Edwards-A10-reviews.ipynb`, covers critic vs audience scores (description only).
**Run order (README):** `tools/get_data.py` → `00_build_dataset.ipynb` → `01_clean_dataset.ipynb` → `A10-master.ipynb` / personal notebooks.

**Main findings (Edwards §10–16, training years)**
- **Feature winners:** distributor group (major / mini-major / specialty; +0.169 AUC over budget), director track record (share of earlier films that were hits; 0.469 → 0.586), MPAA rating (G 1.31× → NR 0.05×), US vs non-US (1.02× vs 0.11×), primary genre (+0.077), sequel (real: 3.25× the odds after period and budget), major producer (+0.040), source group (adaptations ≈ 1.0× vs originals 0.67×), Tanner's overlapping-rating competition (G↔PG↔PG-13↔R within ±6 weeks; +0.012).
- **Not worth it:** budget tiers / percentiles, season flags, release-window competition by budget, tentpole flag, budget per minute, writer–director familiarity (it's track record), same-rating-only crowding, genre count.
- **Warnings:** "was blank" flags likely leak the outcome (undocumented films flop); budget's effect is curved (under $10M loses, flat above); originals are higher-variance, mostly on the downside.
- **Context:** big films make more dollars per film, small films more per dollar but ~70% lose; sequels went from 6% to 23% of releases and 15% to 55% of US box office; the 2010s recovery is mostly fewer small films in the data; Blumhouse (median 7.2×) drives the horror boom.

**Done 2026-11-26 (this PR):** Box Office Mojo grosses now split by theatrical run (no more same-title sums; *Frozen* 2010 is $246K, not $400M). Winning features built in `01_clean_dataset.ipynb` §12b. Baseline and first model in `Edwards-A10.ipynb` §18 (5-fold CV inside 2000–15; **test set still locked**), framed as picking winners: model AUC 0.758 vs baseline 0.609; winners caught in the top 20% 37.2% vs 28.0%; hit rate 62% vs 46%. Master notebook §2g, §3f, §4 updated.

**Open issues**
- **Proposed A9 (needs Matt):** frame the decision and evidence standard as picking the top 20% most likely winners. The loser version had a ~30% ceiling that left the 5-point bar almost no room; winners can be caught up to 60%.
- **The screen mostly flags obvious small, foreign, limited-release films.** Consider evaluating inside budget tiers, or among major and mini-major releases only, where the decision is harder.
- `_missing` flags leak the outcome (+0.041 AUC): excluded from the model; report as a sensitivity check.
- **A7 vs Matt's A8 draft** (worldwide 2.5× label; bans keyword fills and outcome-based cleaning rules).
- Title matcher misses a few big films (*F9*, *The Butler*); `audience_score` should prefer Rotten Tomatoes; distributor and company names not fully standardized.
- Angel Studios: only *Sound of Freedom* is in the population; *The Shift* (2023) is missing because the TMDB snapshot predates it. All of their films are 2021–23 (stress test only).

**Next steps**
1. Matt: review this PR, A9 (winner framing), and A7 vs A8.
2. Tune the model and decide the evaluation subset (all films vs wide releases) on training CV only.
3. Then a **single** evaluation on 2016–19 (bootstrap CI vs baseline) and the 2020–23 stress test; sensitivity at 1× / 1.5× and the $100K floor.
**Finalize this transcript with** (then re-apply the email redaction: `perl -pi -e 's/[\w.+-]+\@cricut\.com/[redacted email]/g' ai_logs/Edwards_ClaudeCode_data-exploration-cleaning_2026-11-24.md ai_logs/raw/Edwards_ClaudeCode_data-exploration-cleaning_2026-11-24.jsonl`; the repo is public):
`python -I tools/export_session.py cae33d13-a6d1-4106-9e4d-52dd46dca9db Edwards_ClaudeCode_data-exploration-cleaning_2026-11-24 "Tanner Edwards - Claude Code - Unified dataset, film_uid and reviews table, cleaning notebook, contract amendments A1-A7, input review, outlier rules, missing-value fills with Wikidata (2026-11-21 to 11-24)"`
Matt's previous transcript (fb9b8a75) is still PARTIAL. Finalize it with:
`python -I tools/export_session.py fb9b8a75-3b2f-4715-8305-2e18a342c311 Sorensen_ClaudeCode_profile-and-join_2026-11-18 "Matt Sorensen - Claude Code - A10 procedure test, wrong-folder fix, univariate profile (step 9), TMDB-RT join and hand-check (step 10), team summary (2026-11-18 to 11-19)"`

## Session procedure
Matt says **"start A10 session"** or **"end A10 session"** (plain "start session" / "end session" also count); Claude runs the matching checklist and confirms each item.

**Matt's steps (simple version)**

*Ending*
1. In the Claude chat, type: **end A10 session**
2. Wait. Claude updates the plan, saves the transcript, and lists the files it wrote.
3. Did you use claude.ai in your web browser for A10 today? If yes, copy that whole chat into a new file in `ai_logs`. Don't change anything in it.
3a. Share your work with Tanner: ask Claude to "commit and push today's work", or in **Source Control** type a short message, click **Commit**, then **Sync Changes**.
4. Close VS Code.

*Starting*
1. Open VS Code.
2. Click **File → Open Folder…**
3. Go to **Documents → Repos → emba-560-data-analytics**. Click the folder once, then click **Select Folder**.
4. **Check:** the top of the Explorer panel on the left says **EMBA-560-DATA-ANALYTICS**. If it says anything else (like A10_GROUP, A7 or NOTEBOOKS), go back to step 2.
4a. Get Tanner's latest work: click the **Source Control** icon on the left (the branch symbol), then click **Sync Changes** (or the ⟳ arrows at the bottom-left of the window).
5. Open a **new** Claude chat.
6. Type: **start A10 session**
7. **Check Claude's answer.** It should name the phase and step you're on, in about 5 short lines. If it mentions **A7**, says it has **no memory**, or asks which project you mean, stop. Close the chat and go back to step 2.
8. Open the notebook and start working.

Don't use **File → Open Recent** or double-click workspace files. Always use **Open Folder**.

**Workspace rule:** always open the `emba-560-data-analytics` repo folder itself as the VS Code workspace before starting Claude Code. Claude's memory for this project is tied to that folder (since 2026-11-21; before that it was `A10_Group`, which is now an old backup, so don't work there). Launching from any other folder starts Claude without it. Before typing "start session," check that the VS Code Explorer title reads **EMBA-560-DATA-ANALYTICS**. On 2026-11-18 a stray `A10.code-workspace` file that pointed at A7 sent a session there (session fde2d022). Matt deleted that file, and A7's memory now has a guard that tells you to switch folders.

**Start session**
1. Read the Handoff above.
2. Finalize the previous session's transcript with the command in the Handoff. Confirm the printed end time is after that session's last prompt, then mark it FINAL in the README's AI conversations table.
3. Add this session to the README table as PARTIAL (session id = folder name in Claude's scratchpad path).
4. Check the folder, not the checkboxes: files the Handoff names exist; notebook saved after its last Run All.
5. Report in 5 lines or fewer: where we are, schedule, first action, open issues. Then wait for Matt.

**End session**
1. Update checkboxes and add one dated Status log line below.
2. Rewrite the Handoff section above (including the finalize command for this session).
3. Update the README file inventory and AI conversations table.
4. Export this session: `python -I tools/export_session.py <session-id> <stem> "<title>"` (stem: `Sorensen_ClaudeCode_<topic>_<date>`). It stays PARTIAL until the next start finalizes it.
5. Remind Matt to save any claude.ai chats about A10 into `ai_logs/` verbatim.
6. List the files written. A Claude-written summary never replaces a transcript.

## Direction
*Agreed 2026-11-17; details in `report/A10_purpose_contract_FROZEN_2026-11-17.md`.*
- Pre-release profitability screen, predictive path with explanatory layer. Decision owner: financier/streamer acquisitions head (flag / review / pass), financing stage.
- Outcome: money-loser = revenue < 2.5× budget (sensitivity 1×/2×/3×). Focal factor: director prior track record. Capacity: top 20%.
- Population: budget ≥ $1M, revenue > 0, released 2000–2023 → 5,766 films (train 2000–15: 4,145 / test 2016–19: 1,086 / stress 2020–23: 535).
- Data: `TMDB_movie_dataset_v11.csv` (1.54M rows; ODC-By 1.0), `rotten_tomatoes_movies.csv` (143,258 rows; CC0), `rotten_tomatoes_movie_reviews.csv` (1.44M reviews; CC0). Title + year(±1) + runtime join: 83% of 2000–2023 usable films matched 1:1. RT boxOffice vs TMDB revenue Spearman 0.895.
- Optional, not obtained: TMDB credits file (actor star power).

## Plan and status
**Phase 0: Setup (Nov 17–18)**
- [x] 1. Folder layout. Consolidated 2026-11-18 (see README).
- [x] 2. Companion files: rotten_tomatoes_movies.csv added 2026-11-17 (1,206 dup ids).
- [x] 3. AI log started; export procedure in place (`tools/export_session.py`).
- [~] 4. Ownership split DEFERRED: treat A10 as Matt's individual work until Phase 7. Don't raise team coordination unprompted.

**Phase 1: Purpose Contract (Nov 18–19) → 12 pts. COMPLETE**
- [x] 5. Problem scan: `report/A10_problem_scan_2026-11-17.md` (9 candidates; #1 chosen, #2 director premium as rival; #7 marketing and #8 script = reopening evidence).
- [x] 6. Decision statement + red-team. **AI correction logged:** Claude's earlier "usable" filter (votes ≥ 50) selected on a post-release outcome (Spearman 0.48 with log ROI) → dropped. Candidate for the report's required material AI correction.
- [x] 7. Contract FROZEN 2026-11-17 (≥5-pt evidence bar, $1M floor confirmed). Instructor approval not required (Matt confirmed); don't raise again. Changes need a dated amendment in the contract file.

**Phase 2: Data Receipt & Understanding (Nov 19–21) → 8 + 12 pts**
- [x] 8. Data Receipt COMPLETE 2026-11-18 (notebook §2, Run All saved): receipt table, SHA-256 fingerprints, grain check (TMDB 1,019 conflicting dup ids), zero-as-missing budget/revenue, date coverage, population funnel. 43.6% of budget ≥ $1M films lack revenue → S4 triggered. Disposition: FIT WITH CONDITIONS. Rights: academic use only; don't reproduce review text beyond short excerpts; credit TMDB (ODC-By).
- [x] 9. All-field univariate profile COMPLETE 2026-11-18 (notebook §3, Run All saved): all 51 fields plus derived measures, profiled on the 5,766-film population (label by period), RT files whole. 66 flags in register §3i; 12 dispositions approved by Matt (§3k); gate CONTINUE. Key findings: 64.6% losers at 2.5× (capture ceiling ≈ 31% at 20% capacity); revenue entry errors (24 films < $1K, 244 < $100K); 6 possible double-id pairs; 66% of companies have one film (sparse track record).
- [x] 10. Join COMPLETE 2026-11-19 (notebook §4, Run All saved): title + year ±1 + runtime, 1:1, plus rule 2b (streaming-only RT date later than release, runtime within 5 min; added after first pass, documented). 4,673 / 5,766 matched (81.0%). Hand-check by Matt: 0 / 50 random wrong (95% CI 0–7%) → **S3 not triggered**; rule 2b 0 / 11 wrong. Match rate 58% for $1–5M vs 91% for $60M+ → "director unknown" indicator needed. **New label risk:** 396 matched films (10.3%) have TMDB revenue = RT domestic (87% labelled losers vs 57%) → step 12.
- [ ] 11. Test early-review hypothesis (RT reviews dated before release?)
- [ ] 12. Readiness gate (go / narrow), including S4 check via RT boxOffice on revenue-missing films

**Phase 3: Preparation (Nov 21–23) → 8 pts**
- [ ] 13. Cleaning ledger (Ch 7): $1–2 budgets, dup ids, placeholder dates, exclusions, row counts
- [ ] 14. Features with time-order discipline (director/company track record from prior films only, release month, genre…)
- [ ] 15. Reconciliation raw→final + one sensitivity check

**Phase 4: Modeling (Nov 23–25) → 16 pts**
- [ ] 16. Temporal split: train 2000–15, test 2016–19, stress 2020–23
- [ ] 17. Baseline first (genre × budget-tier rule)
- [ ] 18. 1–2 models (logistic; optional tree)
- [ ] 19. Explanatory layer with intervals
- [ ] 20. Capture one material AI correction (error, catch, fix)

**Thanksgiving buffer (Nov 26–29):** light; fresh Run all, catch up

**Phase 5: Evaluation & Decision (Nov 29–Dec 1) → 12 + 8 + 7 pts**
- [ ] 21. Test-period eval vs baseline: losers caught, good films wrongly flagged, calibration, stress period
- [ ] 22. Decision policy + responsible use (selection bias, gross-revenue caveat)
- [ ] 23. Value: fill-in break-even, no invented dollars
- [ ] 24. Verdict (continue/pilot/redirect/satisfice/stop) + reopening evidence
- [ ] 25. Appendix D: independent rebuild of 3–5 key numbers

**Phase 6: Communicate (Dec 1–3) → 7 + 15 pts**
- [ ] 26. Report .docx ≤ 10 main pages; appendices: ledger, join check, App D, AI correction
- [ ] 27. Deck: decision first, 8–10 min, speaker notes, view-only link
- [ ] 28. Traceability: every number → notebook cell

**Phase 7: Package (Dec 3–4 AM) → 5 pts + individual**
- [ ] 29. Fresh Run all on every notebook, save
- [ ] 30. Zip: data, notebooks, all AI conversations (every README row FINAL), report + deck, README (files + owners)
- [ ] 31. Individual: AI Disclosure (10 pts), role statement, workload calibration
- [ ] 32. Both members upload identical zip; target Thu Dec 3 night

**Critical path:** Phases 1–4 done by Nov 25. If behind, cut 2nd model and early-buzz feature first, never evaluation or Appendix D.
**Standing rules:** raw data untouched; contract frozen before modeling; no post-release inputs; export every AI session; narrate in the notebook; Matt must be able to explain every step (final exam draws on the folder).

## Status log
- 2026-11-17: Profiled both files, tested join, agreed direction and plan.
- 2026-11-17: Folder layout created. RT movies file added; title+year(±1) join with runtime tiebreak → 6,177 of 7,716 films matched (80%; 83% for 2000–2023), runtime within 5 min for 90%. RT box vs TMDB revenue Spearman 0.895, median ratio 0.55; 1.2% have RT > TMDB (flags bad TMDB revenue). RT director/writer enables director track record.
- 2026-11-17 to 2026-11-18: Phase 1 complete (problem scan, contract frozen on candidate #1). Phase 2 step 8 complete (Data Receipt; FIT WITH CONDITIONS).
- 2026-11-18: Session b61e1644 transcript re-exported in full (to 23:30 Nov 17) → FINAL. Added session start/end procedure. Consolidated folder: plan, handoff, procedure, and AI-log registry now in PLAN.md and README.md; summary .txt logs deleted; raw .jsonl in ai_logs/raw/; one export script. Next: Phase 2 step 9.
- 2026-11-18: Separated A10 from the A7 folder it was first launched from: Claude memory moved to the A10_Group project, A10 notes removed from A7's memory. A7 assignment files untouched. From now on, launch Claude Code from A10_Group.
- 2026-11-18: Session 6c37400e ended with the new End checklist (handoff rewritten, transcript exported as PARTIAL). Next session doubles as the procedure test.
- 2026-11-18: Session fb9b8a75: procedure test passed. A wrong-folder start (fde2d022, launched in A7 via a stray workspace file) was diagnosed and logged; guard added to A7 memory; simple start/end steps added to Session procedure. Phase 2 step 9 complete (notebook §3; dispositions §3k approved; gate CONTINUE). Step 10 complete 2026-11-19 (join 81.0%, hand-check 0/50 wrong, S3 not triggered). Executive summary for teammates published as a private artifact. Next: step 11 (early-review test).
- 2026-11-21 to 11-24: Tanner's session cae33d13: unified dataset with film_uid and reviews table, cleaning notebook `01_clean_dataset.ipynb`, amendments A1–A7 proposed, every input reviewed, outlier rules and missing-value fills decided (Edwards §4–9), Wikidata people snapshot added. Merged to main via PRs #3–#5. Next: Matt signs off A6/A7; promote rules into 01_clean; fix build matching.
- 2026-11-25 to 11-26: Tanner's session cae33d13 (branch `tanner/label-eda`): every input compared with the US return (Edwards §10–16, training years), feature ideas screened with cross-validated AUC, sequel title rule, bets-vs-success trends, reviews side notebook. Found the Box Office Mojo same-title gross bug. Next: fix the join, promote winning features to 01_clean, baseline and model.

# A10 Plan, Status, and Handoff

A10 team project (Matt + one colleague, worked as individual until Phase 7), due **Fri Dec 4, 2026, 3:30 PM**, 120 pts. Plan agreed 2026-11-17. This file is the single source of truth for plan, status, and session handoff.

Contents: [Handoff](#handoff) · [Session procedure](#session-procedure) · [Direction](#direction) · [Plan and status](#plan-and-status) · [Status log](#status-log)

## Handoff
*Rewritten at every session end. Read this first when resuming.*

**Last updated:** 2026-11-28, Matt's session f1a57453 (Claude Code). Matt has taken over from Tanner (Tanner's full handoff: PR #10 description). **Phase 5 (Evaluation), step 21 in progress**, a day ahead of the plan's Nov 29 start.

**Where we are**
- Phases 1–4 done in substance; model **locked**: logistic regression, 12 features (`A10-master.ipynb` §4f). Label `winner` = US box office ≥ 1.25× budget (A7, A9); the screen picks the top 20% each year.
- **Test 2016–19** (run once by Tanner 11/27, reproduced 11/28): AUC 0.831 vs baseline 0.621; winners caught 45.1% vs 32.2% (+12.8 pts, 95% CI +7.7 to +17.5); 80% of picks won. Evidence standard met. (Tanner's +13.2 differed only by tie-breaking; master now uses a stable sort.)
- **Stress test 2020–23** (Matt, 11/28): ranking holds (recall 44.9% vs 27.6%, +17.3 pts, CI +9.9 to +28.4; AUC 0.779 vs 0.588; beats baseline every year) but predicted chances run high (44% predicted vs 26% actual). Use ranks, recalibrate yearly. Main misses: 2023 franchise tentpoles. Refit on 2000–19 no better.

**Open PRs (Tanner to review; merge in order)**
1. **#11** `matt/promote-modeling-to-master`: master §4 Modeling + §5a test set, standalone code from Edwards §18–21, stable tie-break.
2. **#12** `matt/master-stress-test` (stacked on #11): Sorensen §5 + master §5b stress test.
3. This session's PLAN/README update (`matt/session-2026-11-28`).

**Setup on a new machine or after pulling:** reinstall `requirements.txt`; rerun `00_build` → `01_clean`. Notebooks request kernel `emba560-a10` (Tanner's machine only); on Matt's machine run with the `python3` kernel (`jupyter nbconvert --execute --ExecutePreprocessor.kernel_name=python3 …`). Windows Smart App Control once blocked a scikit-learn DLL; it cleared on retry.

**Next steps (start here)**
1. **Sensitivity checks (step 21, then step 15).** New standalone section in `Sorensen-A10.ipynb` (§6), same frozen §4f specification, nothing tuned on 2016–19; report next to the main result, then promote to master §5c by PR:
   - **Label at 1× and at 1.5× budget** (`us_multiple`): refit the same specification on 2000–15 with the new label, evaluate once on 2016–19 (and 2020–23), vs a baseline relearned on the same label. Does the gain over the baseline hold?
   - **$100K budget floor (A2):** rebuild the population with budget ≥ $100K (check whether `01_clean` exposes it, e.g. `usable`/`exclude_reason` with `fin_budget`; if not, propose a pipeline change via PR rather than re-cleaning in the notebook). Report how many films are added and whether results hold.
   - **With `_missing` flags:** add them to the final model to show the size of the leak (Tanner: +0.041 AUC in CV); reported as a sensitivity check only, never the model.
   - **Ablation:** drop each feature group from the final model (CV on training years) to show how much each adds; reuse the §4d likelihood-ratio results where they already answer it.
2. **Test among major and mini-major releases only (step 21, §5d).** The screen mostly flags obvious small, foreign, limited releases; the harder decision is among wide studio releases. Restrict 2016–19 (and 2020–23) to `distributor_group` in {Major, Mini-major}, keep the frozen model (trained on all films), pick the top 20% within that subset each year, and compare with the baseline (and a baseline relearned on the subset). Also report results within budget tiers. Pre-commit the subset definition in the notebook before running.
3. Then steps 22–25: decision policy and responsible use (rank, don't read chances literally; human review; never cancels a film), value break-even, verdict and reopening evidence, Appendix D (independent rebuild of 3–5 key numbers, not a rerun of the same code).

**Loose ends to fix (before the report)**
- **Update this file's checkboxes and the "Direction" section:** Direction still describes the old 2.5× money-loser label and 5,766-film population; it should state A7/A9 (winner ≥ 1.25× US box office, 4,933 films). Checkboxes were updated 11/28 (see Plan and status); keep them current.
- **Restore Matt's operating rule in `CLAUDE.md`:** Tanner's 11/27 rewrite dropped "Before taking any action beyond answering the question asked, state the next step you propose and ask me to confirm … Do not assume. If you skip, merge or reorder a step … say so before you do it. Wait for my yes." Add it back alongside Tanner's instructions.
- **Close or reconcile amendment A8** (`A10_contract_amendments_PROPOSED.md`); A7 and A9 cover its question and label.
- **Decide on formal write-ups for steps 11, 12, 13 and 20:** step 11 (were RT reviews dated before release?) and step 12 (readiness gate) were never written as steps; step 13 needs a Ch 7 cleaning-ledger appendix (rules are in `01_clean`, reported in master §3); step 20 needs the material AI correction written up (candidates: Claude's "votes ≥ 50" post-release filter caught in step 6; Tanner's blank-data leak). Either do them or note in the report where each is covered.
- **Unpushed 11/24 work:** branch `matt/integrate-cleaning-rules` has two local-only commits (pipeline verification, a session-log line); Tanner's 11/26–27 work superseded most of it. Review, then keep or delete the branch. A stash ("pre-pull notebook output edits 2026-11-28") holds stray notebook outputs; safe to drop after a look.
- **`Sorensen-A10.ipynb` shows as modified on branches where it still has saved outputs** (Windows line endings + nbstripout). It is not real work; resolved once PR #12 merges.
- **Unlogged AI transcripts on Matt's machine** (not yet in the README table or `ai_logs/`): `4197a19c…`, `c08f31b6…` (emba repo folder, 11/24), `1603a6c0…`, `8b91e2a8…` (Repos folder, 11/24), `cef042d7…` (Repos folder, 11/28 morning). Check each is A10, then export with `tools/export_session.py` and add rows.
- **Workspace rule:** this session was launched from `Documents\Repos`, not the repo folder. Next time open `emba-560-data-analytics` itself (Session procedure, Starting step 3).
- Carried from Tanner: title matcher misses a few big films (*The Butler*; *F9* now matches); `audience_score` should prefer Rotten Tomatoes; distributor and company names not fully standardized.

**Transcripts to finalize at the next start** (the repo is public: after each export, run `python -I tools/redact_emails.py ai_logs/<stem>.md ai_logs/raw/<stem>.jsonl`; it must print `left: 0` for both)
- This session (Matt): `python -I tools/export_session.py f1a57453-a131-4d74-b763-520873978545 Sorensen_ClaudeCode_eval-master-stress-test_2026-11-28 "Matt Sorensen - Claude Code - Picked up Tanner's work, reproduced the test set, promoted modeling and evaluation to master (PR #11), COVID stress test (PR #12) (2026-11-28)"`
- Matt's fb9b8a75 (still PARTIAL): `python -I tools/export_session.py fb9b8a75-3b2f-4715-8305-2e18a342c311 Sorensen_ClaudeCode_profile-and-join_2026-11-18 "Matt Sorensen - Claude Code - A10 procedure test, wrong-folder fix, univariate profile (step 9), TMDB-RT join and hand-check (step 10), team summary (2026-11-18 to 11-19)"`
- Tanner's cae33d13 (row 7, PARTIAL) is on Tanner's machine; he finalizes it with the command in PR #10's PLAN.md version, then re-applies his redaction.

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
- [~] 11. Test early-review hypothesis (RT reviews dated before release?). Not done as a formal step; Tanner's reviews side study (`Edwards-A10-reviews.ipynb`) covers reviews vs return. Reviews are post-release and excluded from the model (A6). Write up or note in report.
- [~] 12. Readiness gate (go / narrow), including S4 check via RT boxOffice on revenue-missing films. Effectively GO via Tanner's unified dataset (The Numbers, Box Office Mojo, Wikidata fill revenue gaps) and amendments A1–A7 (11/24); no formal gate written.

**Phase 3: Preparation (Nov 21–23) → 8 pts**
- [~] 13. Cleaning ledger (Ch 7): $1–2 budgets, dup ids, placeholder dates, exclusions, row counts. Rules built by Tanner in `01_clean_dataset.ipynb` (C1–C18, exclusion and fill rules), reported in master §3; the ledger appendix still needs writing.
- [x] 14. Features with time-order discipline (director/company track record from prior films only, release month, genre…). Tanner, 11/26 (`01_clean` §12b; master §3f).
- [~] 15. Reconciliation raw→final + one sensitivity check. Funnel in master §3d (Tanner); sensitivity checks are next (Handoff, next step 1).

**Phase 4: Modeling (Nov 23–25) → 16 pts**
- [x] 16. Temporal split: train 2000–15, test 2016–19, stress 2020–23. Tanner (A5).
- [x] 17. Baseline first (genre × budget-tier rule). Tanner, 11/26 (master §4b).
- [x] 18. 1–2 models (logistic; optional tree). Tanner, 11/26–27: five model types compared; logistic regression final, XGBoost challenger (master §4c–4f). Promoted to master by Matt 11/28 (PR #11).
- [x] 19. Explanatory layer with intervals. Tanner, 11/27: odds ratios with 95% CIs, likelihood-ratio and AIC tests (master §4d, §4f).
- [~] 20. Capture one material AI correction (error, catch, fix). Candidates: Claude's "votes ≥ 50" post-release filter (Matt caught it, step 6); the blank-data leak (Tanner). Write-up pending.

**Thanksgiving buffer (Nov 26–29):** light; fresh Run all, catch up

**Phase 5: Evaluation & Decision (Nov 29–Dec 1) → 12 + 8 + 7 pts**
- [~] 21. Test-period eval vs baseline (A9: winners caught, precision), calibration, stress period. Test 2016–19: Tanner 11/27, reproduced and promoted by Matt 11/28 (master §5a, PR #11). Stress test 2020–23: Matt 11/28 (Sorensen §5, master §5b, PR #12). **Open:** sensitivity (1×, 1.5×, $100K, `_missing` flags), ablation, majors and mini-majors only.
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
- 2026-11-24: Matt's session (branch `matt/integrate-cleaning-rules`, not pushed): verified the pipeline (4,933 films) and amendments A1–A7. Superseded by Tanner's 11/26–27 work.
- 2026-11-26 to 11-27: Tanner's session cae33d13 (PRs #9, #10, recorded by Matt from the commits): Box Office Mojo fix, engineered features, baseline and five model types, fit tests, final 12-feature logistic regression; A9 adopted (winner framing); test 2016–19 run once: AUC 0.831, winners caught 45.1% vs 31.9%. Tanner paused and handed over to Matt.
- 2026-11-28: Matt's session f1a57453: pulled Tanner's work, rebuilt the pipeline and reproduced the test (logistic results identical; baseline differs by tie-breaking). Promoted Edwards §18–21 into master §4–5a with a stable tie-break (PR #11). COVID stress test 2020–23 in Sorensen §5 and master §5b (PR #12): ranking holds (+17.3 pts recall over baseline), probabilities run high. Plan checkboxes brought up to date. Next: sensitivity checks, then majors/mini-majors only.

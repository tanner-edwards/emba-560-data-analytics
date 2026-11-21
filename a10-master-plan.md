---
name: a10-master-plan
description: "A10 movie-success team project master plan (phases, dates, rubric points) plus live status; use when Matt asks \"where are we on the plan?\""
metadata:
  node_type: memory
  type: project
  originSessionId: b61e1644-fb70-4c84-834f-dab72e7c5879
  modified: 2026-11-18T05:46:42.398Z
---

A10 team project (Matt + one colleague), due **Fri Dec 4, 2026, 3:30 PM**, 120 pts. Project folder: `C:\Users\matts\Documents\Repos\BusAnalytics\Notebooks\A10_Group` (notebook `Sorensen-A10.ipynb`). Plan agreed 2026-11-17.

**Why:** Matt will repeatedly ask "Where are we on the plan?" — answer by checking this status block against the actual files in the A10 folder, report current phase, done/next items, and schedule slip vs. dates.

**How to apply:** Verify progress from the folder (don't trust the checkboxes blindly), then update the checkboxes and "Status log" here. Critical path = Phases 1–4 done by Nov 25. If behind, cut 2nd model and early-buzz feature first, never evaluation or Appendix D.

## Direction (agreed 2026-11-17)
- Lead candidate: pre-release profitability screen (TMDB only for core), predictive + explanatory layer. Decision owner: financier/streamer acquisitions team (flag / review / pass). Outcome: revenue/budget above a labeled-assumption multiple (sensitivity over a few). ~7,716 usable films (budget>=1e5, revenue>0, votes>=50).
- Files present: `TMDB_movie_dataset_v11.csv` (1.54M rows; no cast/crew), `rotten_tomatoes_movie_reviews.csv` (1.44M reviews, 69k movies, slug key only).
- Join: 2000+ year-validated 1:1 join gives ~3,538 of 5,053 usable 2000–2023 films (70%); critic %pos vs TMDB rating Spearman 0.70 (partly redundant). RT adds critic layer, review text, possible pre-release "early buzz" (unverified).
- Wanted: companion `rotten_tomatoes_movies.csv`; optional TMDB credits file for star power.
- Scratch scripts (temp, may vanish): profile.py, join_test.py in session scratchpad.

## Plan and status
**Phase 0 — Setup (Nov 17–18)**
- [x] 1. Folder layout: data/raw (untouched), data/clean, notebooks/, ai_logs/, report/, deck/, README.md (done 2026-11-17; CSVs moved to data/raw, notebook to notebooks/, README skeleton with file inventory)
- [x] 2. Get companion files — rotten_tomatoes_movies.csv in data/raw 2026-11-17 (143,258 rows, 1,206 dup ids; source kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews). TMDB credits still optional/not obtained.
- [x] 3. Start AI log — Claude Code session b61e1644 (2026-11-17) exported to ai_logs/ as .jsonl (raw) + .md (via tools/export_transcript.py: `python -I tools/export_transcript.py <src.jsonl> <dst.md> "<title>"`). Session transcripts live in C:\Users\matts\.claude\projects\<project>\<session-id>.jsonl. RE-EXPORT this session at end of its use (export was mid-session). Claude.ai planning chat saved verbatim (from Matt's paste) 2026-11-17 as ai_logs/Sorensen_ClaudeChat_A10-planning-handoff_2026-11-17.md. Phase 0 complete except end-of-session re-export.
- [~] 4. Ownership split — DEFERRED. As of 2026-11-17 Matt and colleague work ahead independently and compare notes at intervals; treat A10 as an individual assignment (Matt owns everything) until Matt says otherwise. Don't raise team coordination unprompted; merge/ownership revisited at packaging (Phase 7).

**Phase 1 — Purpose Contract (Nov 18–19) → 12 pts**
- [x] 5. crispdm-problem-scanner — done 2026-11-17, saved report/A10_problem_scan_2026-11-17.md. 9 candidates; carry forward #1 pre-release profitability screen (focal factor: director prior track record) with #2 director-premium as rival/fallback; #7 marketing spend and #8 script quality = reopening evidence. Awaiting Matt's pick before step 6.
- [x] 6. decision-statement-builder — DRAFT 2026-11-17 at report/A10_purpose_contract_DRAFT_2026-11-17.md. Locked by Matt: financing-stage decision; loser = revenue < 2.5x budget (sens. 1x/2x/3x); capacity top 20%; years train 2000–15, test 2016–19, stress 2020–23. Population: budget ≥$1M, revenue>0, no vote filter. Stop conditions S1–S4. Open: ≥5-pt evidence bar and $1M floor need Matt's OK, then freeze (step 7).
  - **AI correction logged:** Claude's earlier "usable" filter (votes ≥50) selected on a post-release outcome (Spearman 0.48 with log ROI) → dropped. Candidate for report's required material AI correction.
  - Phase 2 must quantify budget≥$1M & revenue-missing films and use RT boxOffice to check if they're losers (S4).
- [ ] 7. Freeze & date contract before modeling

**Phase 2 — Data Receipt & Understanding (Nov 19–21) → 8 + 12 pts**
- [ ] 8. Data Receipt per source (publisher, URL, access date, license, grain, population, sensitive fields)
- [ ] 9. All-field univariate profile (Ch 6 skill)
- [ ] 10. Build/verify join (2000+, year-validated, 1:1, ~50-pair hand-check with error rate)
- [ ] 11. Test early-review hypothesis (RT reviews dated before release?)
- [ ] 12. Readiness gate (go / narrow)

**Phase 3 — Preparation (Nov 21–23) → 8 pts**
- [ ] 13. Cleaning ledger (Ch 7): $1–2 budgets, dup ids, placeholder dates, exclusions, row counts
- [ ] 14. Features with time-order discipline (company track record from prior films only, release month, genre…)
- [ ] 15. Reconciliation raw→final + one sensitivity check

**Phase 4 — Modeling (Nov 23–25) → 16 pts**
- [ ] 16. Temporal split: train ≤2015, test 2016–2019, 2020+ COVID stress test
- [ ] 17. Naive baseline first
- [ ] 18. 1–2 models (logistic; optional tree)
- [ ] 19. Explanatory layer with intervals
- [ ] 20. Capture one material AI correction (error, catch, fix)

**Thanksgiving buffer (Nov 26–29)** — light: fresh Run all, catch up

**Phase 5 — Evaluation & Decision (Nov 29–Dec 1) → 12 + 8 + 7 pts**
- [ ] 21. Test-period eval vs baseline: losers caught, good films wrongly flagged, calibration, 2020+ stress
- [ ] 22. Decision policy + responsible use (selection bias, gross revenue caveat)
- [ ] 23. Value: fill-in break-even, no invented dollars
- [ ] 24. Verdict (continue/pilot/redirect/satisfice/stop) + reopening evidence
- [ ] 25. Appendix D: independent rebuild of 3–5 key numbers

**Phase 6 — Communicate (Dec 1–3) → 7 + 15 pts**
- [ ] 26. Report .docx ≤10 main pages; appendices: ledger, join check, App D, AI correction
- [ ] 27. Deck: decision first, 8–10 min, speaker notes, view-only link
- [ ] 28. Traceability: every number → notebook cell

**Phase 7 — Package (Dec 3–4 AM) → 5 pts + individual**
- [ ] 29. Fresh Run all on every notebook, save
- [ ] 30. Zip: data + Receipt, notebooks, all AI conversations unedited, report + deck, README (files + owners)
- [ ] 31. Individual: AI Disclosure (10 pts), role statement, workload calibration
- [ ] 32. Both members upload identical zip — target Thu Dec 3 night

**Standing rules:** raw untouched; contract frozen before modeling; no post-release inputs; export every AI session; narrate in notebook; Matt must be able to explain every step (final exam draws on team folder).

## Status log
- 2026-11-17: Profiled both files, tested join, agreed direction and plan. Phase 0 not yet started.
- 2026-11-17: Folder layout created. RT movies file added; title+year(±1) join with runtime tiebreak → 6,177 of 7,716 usable TMDB films matched (80%; 83% for 2000–2023), runtime within 5 min for 90%. RT boxOffice (domestic) vs TMDB revenue (worldwide) Spearman 0.895, median ratio 0.55; 1.2% have RT > TMDB (flags bad TMDB revenue). RT movies has director/writer → director prior-track-record as star-power proxy is now possible.

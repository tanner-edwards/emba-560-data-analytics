# emba-560-data-analytics

EMBA 560 **A10** team project: a pre-production **money-loser screen** for film financing.
Due **Fri Dec 4, 2026, 3:30 PM**.

- Frozen scope: [`A10_purpose_contract_FROZEN_2026-11-17.md`](A10_purpose_contract_FROZEN_2026-11-17.md)
- Plan, status and session handoff: [`PLAN.md`](PLAN.md)

## Setup (once per machine)

Requires Python 3.12. [`uv`](https://docs.astral.sh/uv/) is recommended, but plain `venv` + `pip` works too.

```bash
# 1. Environment
uv venv --python 3.12 .venv
uv pip install --python .venv -r requirements.txt
#   Windows without uv:  py -3.12 -m venv .venv && .venv\Scripts\pip install -r requirements.txt

# 2. Strip notebook outputs on commit (git filter config is local; each person must run this)
.venv/bin/nbstripout --install          # Windows: .venv\Scripts\nbstripout --install

# 3. Download raw data from Kaggle into data/raw/ (about 1.3 GB, gitignored)
.venv/bin/python tools/get_data.py      # Windows: .venv\Scripts\python tools\get_data.py

# 4-5. Build the data: run the pipeline notebooks in order (see "Run order" below)
```

## Run order

Run these top to bottom, in this order. Each step reads only the output of the step before it. Every output is gitignored, so each person builds their own copy.

| # | Run | Reads | Writes | Rerun when |
|---|---|---|---|---|
| 1 | `tools/get_data.py` | Kaggle, Box Office Mojo | `data/raw/` | Once per machine, or when a source is added |
| 2 | `notebooks/00_build_dataset.ipynb` (**assemble**) | `data/raw/` | `data/clean/films_unified.csv`, `data/clean/reviews_unified.csv` | You pulled changes to it, or step 1 re-ran |
| 3 | `notebooks/01_clean_dataset.ipynb` (**clean**) | `films_unified.csv` | `data/clean/films_clean.csv`, `data/clean/films_clean_columns.csv` | You pulled changes to it, or step 2 re-ran |
| 4 | Your notebook (`<LastName>-A10.ipynb`) or `A10-master.ipynb` (CRISP-DM: business understanding, EDA, data preparation, modeling…) | `films_clean.csv` | nothing shared | Any time |

**Rule of thumb:** if you pulled changes to step N, rerun step N and every step after it.

- **Assemble vs clean:** `00` only joins sources (one row per film, every source's columns side by side). `01` combines repeated columns into one per fact, standardizes formats and adds missing flags. It never drops films.
- `films_clean_columns.csv` lists every column's group and role (key, input, label, description, source detail). Only `input` columns (and `fin_budget`) can go into a model.
- **Side study:** `notebooks/Edwards-A10-reviews.ipynb` (Tanner) explores return vs critic and audience reviews. Reviews are post-release, so it's description and a possible second label only, never model inputs.
- **Model rows:** `in_population` = True (4,933 films: released in the US, 2000–2023, budget ≥ $1M, after the cleaning rules). **Label:** `loser` = US box office < 1.25 × budget (contract amendment A7); `us_multiple` for the 1× / 1.5× checks. Films that fail a cleaning rule keep an `exclude_reason`.

Behind a TLS-inspecting proxy (e.g. Zscaler), `get_data.py` uses `truststore` so Python trusts the OS certificate store.

## Folder layout

| Folder | Contents | In git? |
|---|---|---|
| `data/raw/` | Kaggle downloads. **Read-only, never edit.** | No (too large) |
| `data/clean/` | Cleaned and derived datasets written by notebooks | Small files only |
| `notebooks/` | Analysis notebooks (outputs stripped on commit) | Yes |
| `tools/` | Helper scripts (`get_data.py`, transcript export) | Yes |
| `ai_logs/` | Unedited AI session transcripts (required in the final zip) | Yes |
| `report/` | Problem scan, contract drafts, Data Receipt, final report | Yes |
| `deck/` | Presentation | Yes |

## Data sources

| File in `data/raw/` | Kaggle dataset | Notes |
|---|---|---|
| `TMDB_movie_dataset_v11.csv` | [asaniczka/tmdb-movies-dataset-2023-930k-movies](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) | Core: budget, revenue, genre, dates. No cast/crew. |
| `rotten_tomatoes_movie_reviews.csv` | [priyamchoksi/rotten-tomato-movie-reviews-1-44m-rows](https://www.kaggle.com/datasets/priyamchoksi/rotten-tomato-movie-reviews-1-44m-rows) | 1.44M critic reviews, slug `id` key |
| `rotten_tomatoes_movies.csv` | [andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews) | Director, writer, boxOffice (domestic) |
| `stefanoleone992/rotten_tomatoes_movies.csv` | [stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset) | Adds `actors`, `production_company`. Same filename as the andrezaza file but **different data**, hence the subfolder. |
| `stefanoleone992/rotten_tomatoes_critic_reviews.csv` | (same as above) | Critic reviews |
| `boxofficemojo/revenues_per_day.csv.gz` | [tjwaterman99/boxofficemojo-scraper](https://github.com/tjwaterman99/boxofficemojo-scraper) (GitHub release, not Kaggle) | Daily **domestic** grosses, 2000–2025, about 7.2k titles. `id` is per row, not per film; join on title + year. |
| `the_numbers/Top Movies (Cleaned Data).csv` | [michaelmatta0/movies-ultimate-metrics-features-and-metadata](https://www.kaggle.com/datasets/michaelmatta0/movies-ultimate-metrics-features-and-metadata) | Scraped from the-numbers.com: production budget, domestic/international/**worldwide** gross, production companies, MPAA, source, franchise. About 6.6k films. |
| `wikidata/wikidata_film_financials_2026-11-21.csv` | Wikidata SPARQL query `tools/wikidata_films.rq`, run 2026-11-21. SHA-256 `c2fa656a…1ef9dd7` | USD budget and box office for 2,570 films with a TMDB id. **Committed to git**: Wikidata is live with no versions, so this snapshot is the source of record. License: CC0. |
| `wikidata/wikidata_film_people_2026-11-24.csv` | `python tools/get_wikidata_people.py` (query `tools/wikidata_people.rq`), run 2026-11-24 after `00_build`. SHA-256 `75a54270…4777be2d2` | Director, writer, runtime and "based on" for 6,486 usable films, by TMDB id. Used to fill blanks and to flag wrong matches. **Committed to git** (same reason). License: CC0. |

Licenses, access dates and grain are recorded in the Data Receipt (`report/`, plan step 8).

## Notebook workflow

**Rules for everyone, including AI assistants working in this repo:**

0. **Data comes from one place.** The pipeline notebooks (`00_build_dataset.ipynb` → `01_clean_dataset.ipynb`, see **Run order**) produce `data/clean/films_clean.csv`, one row per film. Analysis notebooks start from that file and never re-merge or re-clean raw data. To change the data, change the pipeline notebook (team-owned, via PR) instead.
1. **Personal notebooks are for exploration.** Each person works in their own `notebooks/<LastName>-A10.ipynb` (e.g. `Sorensen-A10.ipynb`, `Edwards-A10.ipynb`). Only the owner edits it.
2. **`notebooks/A10-master.ipynb` is the team's final notebook.** It's what gets submitted. Only work that is solid (verified, runs top to bottom, agreed by both members) moves into it.
3. **Promoting work to the master:** copy the finished cells from your personal notebook into the matching section of the master, make them run standalone (no dependence on the personal notebook's state), Run All, then open a PR. The other member reviews before merging.
4. **Never edit someone else's personal notebook,** and never write exploratory or half-finished work into the master.
5. **Notebook outputs are stripped on commit** (`nbstripout`). Run `nbstripout --install` once after cloning (see Setup).

## Standing rules
- `data/raw/` is never modified. All cleaning happens in notebooks and writes to `data/clean/`.
- The purpose contract is frozen. Changes need a dated amendment with a reason.
- No post-release inputs in the model (revenue, votes, popularity, scores, reviews, keywords).
- Export every AI session to `ai_logs/`.

## File inventory

| File | Description | Owner |
|---|---|---|
| `README.md` | This file | Tanner / Matt |
| `FEATURE_IDEAS.md` | Running list of candidate model features with a time-order check for each. AI assistants add ideas automatically when they come up | Tanner / Matt |
| `PLAN.md` | Project plan, live status checklist, session handoff, and session procedure | Matt |
| `data/raw/TMDB_movie_dataset_v11.csv` | TMDB movie metadata, 1,538,765 rows (Kaggle: https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies, accessed 2026-11-17). License: ODC Attribution (ODC-By) 1.0, https://opendatacommons.org/licenses/by/1-0/ | Matt |
| `data/raw/rotten_tomatoes_movie_reviews.csv` | Rotten Tomatoes critic reviews, 1,444,963 rows (Kaggle: https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews, accessed 2026-11-17). License: CC0 1.0, https://creativecommons.org/publicdomain/zero/1.0/ | Matt |
| `data/raw/rotten_tomatoes_movies.csv` | Rotten Tomatoes movie metadata, 143,258 rows (same Kaggle dataset, accessed 2026-11-17). License: CC0 1.0 | Matt |
| `notebooks/Sorensen-A10.ipynb` | Main analysis notebook. §2: Data Receipt and physical checks. §3: univariate profile of all 51 fields, flag register, approved dispositions. §4: TMDB–RT join and its verification | Matt |
| `data/clean/tmdb_rt_crosswalk.csv` | TMDB id ↔ RT id, 4,673 one-to-one pairs with match rule and year/runtime differences. Rebuilt by notebook §4 on every run (not in git) | Matt |
| `data/clean/join_handcheck.csv` | 60 matched pairs (random 50 + 10 rule-2b) hand-checked by Matt, 2026-11-19: all correct. Written once by §4; never overwritten. Force-added to git because it can't be regenerated | Matt |
| `report/A10_problem_scan_2026-11-17.md` | CRISP-DM problem scan: 9 ranked candidate decisions (Phase 1, step 5) | Matt |
| `A10_purpose_contract_FROZEN_2026-11-17.md` | Project Purpose Contract with red-team, frozen 2026-11-17 (Phase 1) | Matt |
| `tools/export_session.py` | Exports a Claude Code session by id: `.md` to `ai_logs/`, raw `.jsonl` to `ai_logs/raw/` | Matt |
| `notebooks/A10-master.ipynb` | Team's final notebook; only promoted, verified work (see Notebook workflow) | Tanner / Matt |
| `notebooks/00_build_dataset.ipynb` | Shared pipeline: matches The Numbers, Wikidata, Box Office Mojo and both RT files to TMDB and writes the unified dataset (assemble only). Usable films 5,766 → 6,838 | Tanner / Matt |
| `notebooks/01_clean_dataset.ipynb` | Shared pipeline: combines repeated columns into one per fact (rules C1–C18 from `Edwards-A10.ipynb` §4b), standardizes formats, adds `_src` and `_missing` columns. Never drops films | Tanner / Matt |
| `notebooks/Edwards-A10.ipynb` | Tanner's Data Understanding (Matt's §2–§3 on the unified data) and missing-value / combine-rule analysis (§4); reads `films_unified.csv` | Tanner |
| `data/clean/films_unified.csv` | **The unified dataset:** one row per 2000–2023 film, keyed by `film_uid` (`tmdb-<id>` or `tn-<The Numbers slug>`; stable across rebuilds), with any financial value (TMDB films plus The Numbers-only films, which have `in_tmdb` = False), all sources attached, combined `fin_budget` / `fin_revenue`, `usable` flag, per-film review summaries (`rtrev_*`, `slrev_*`). Column prefixes explained in `00_build_dataset.ipynb`. Rebuilt every run (not in git) | Tanner / Matt |
| `data/clean/reviews_unified.csv` | One row per critic review (both RT review files stacked, `source` column), keyed by `film_uid`. Only exact copies of the same review are dropped. Post-release: descriptive only. Rebuilt every run (not in git) | Tanner / Matt |
| `data/clean/films_clean.csv` | **The analysis dataset:** same films as `films_unified.csv`, columns grouped key → population → money → input → provenance → description → source detail. Rebuilt every run (not in git) | Tanner / Matt |
| `data/clean/films_clean_columns.csv` | Dictionary: every column of `films_clean.csv` with its group, role and fill rate. Rebuilt every run (not in git) | Tanner / Matt |
| `data/clean/edwards_tn_handcheck.csv` | 50 The Numbers ↔ TMDB matches (25 risky) for hand-checking. Written once, never overwritten | Tanner |
| `tools/get_data.py` | Downloads all raw datasets (Kaggle + Box Office Mojo) into `data/raw/` | Tanner |

## AI conversations

Every AI conversation about A10. **FINAL** means the transcript is complete (Claude Code sessions are finalized by re-exporting at the start of the next session).

| # | Date | Who / tool | Session id | Topic | File in `ai_logs/` | Raw original | Status |
|---|---|---|---|---|---|---|---|
| 1 | 2026-11-17 | Matt / Claude.ai chat | (web chat) | Assignment scoping, question framing, handoff to Claude Code | `Sorensen_ClaudeChat_A10-planning-handoff_2026-11-17.md` | (verbatim paste) | FINAL |
| 2 | 2026-11-17 | Matt / Claude Code | b61e1644-fb70-4c84-834f-dab72e7c5879 | Data profiling, join test, master plan, problem scan, Purpose Contract, Data Receipt | `Sorensen_ClaudeCode_data-scoping-join-masterplan_2026-11-17.md` | `raw/…2026-11-17.jsonl` | FINAL |
| 3 | 2026-11-18 | Matt / Claude Code | 6c37400e-06fc-46b6-b6bf-d83573cd0c9e | Resume check, transcript re-export, session procedure, folder cleanup, separation from A7 workspace | `Sorensen_ClaudeCode_session-procedure_2026-11-18.md` | `raw/…2026-11-18.jsonl` | FINAL |
| 4 | 2026-11-18 | Matt / Claude Code | fde2d022-bd22-439c-90ff-8b7608779760 | Failed "start session": Claude Code launched in the A7 folder by mistake, so it had no A10 memory and offered to work on A7. Kept as a record of the procedure failure | `Sorensen_ClaudeCode_wrong-folder-start_2026-11-18.md` | `raw/…wrong-folder-start_2026-11-18.jsonl` | FINAL |
| 5 | 2026-11-18 to 11-19 | Matt / Claude Code | fb9b8a75-3b2f-4715-8305-2e18a342c311 | Procedure test, wrong-folder fix, univariate profile (step 9), TMDB–RT join and hand-check (step 10), executive summary for teammates | `Sorensen_ClaudeCode_profile-and-join_2026-11-18.md` | `raw/…profile-and-join_2026-11-18.jsonl` | PARTIAL |
| 6 | 2026-11-21 to 11-24 | Tanner / Claude Code | cae33d13-a6d1-4106-9e4d-52dd46dca9db | Unified dataset (film_uid, reviews table, second-pass matcher), cleaning notebook, contract amendments A1–A7, input review (§5–7), outlier rules (§8), missing-value fills incl. Wikidata and source_group (§9) | `Edwards_ClaudeCode_data-exploration-cleaning_2026-11-24.md` | `raw/…data-exploration-cleaning_2026-11-24.jsonl` | PARTIAL |

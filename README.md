# emba-560-data-analytics

EMBA 560 **A10** team project: a pre-production **money-loser screen** for film financing.
Due **Fri Dec 4, 2026, 3:30 PM**.

- Frozen scope: [`A10_purpose_contract_FROZEN_2026-11-17.md`](A10_purpose_contract_FROZEN_2026-11-17.md)
- Plan and status: [`a10-master-plan.md`](a10-master-plan.md)

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
```

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

Licenses, access dates and grain are recorded in the Data Receipt (`report/`, plan step 8).

## Standing rules
- `data/raw/` is never modified. All cleaning happens in notebooks and writes to `data/clean/`.
- The purpose contract is frozen. Changes need a dated amendment with a reason.
- No post-release inputs in the model (revenue, votes, popularity, scores, reviews, keywords).
- Export every AI session to `ai_logs/`.

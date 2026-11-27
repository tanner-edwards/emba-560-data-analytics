# Instructions for AI assistants

Read `README.md` first, especially **Notebook workflow** and **Standing rules**, and follow them. In short:

- Run order (see README **Run order**): `tools/get_data.py` → `notebooks/00_build_dataset.ipynb` (assemble) → `notebooks/01_clean_dataset.ipynb` (clean). Analysis starts from `data/clean/films_clean.csv` (one row per film, key `film_uid`; column roles in `films_clean_columns.csv`) and, for individual reviews, `data/clean/reviews_unified.csv`. Don't re-merge or re-clean raw data in personal notebooks; change the pipeline notebook instead (via PR). Only `input` columns and `fin_budget` may be model inputs. Model rows are `in_population`; the label is `winner` = US box office ≥ 1.25 × budget (amendments A7, A9). Always present results as winners (picking the top 20% most likely winners), never as losers.
- Work in the current user's personal notebook (`notebooks/<LastName>-A10.ipynb`). Never edit another person's notebook.
- `notebooks/A10-master.ipynb` only receives finished, verified work, promoted via PR.
- `data/raw/` is read-only. No post-release inputs in the model. The purpose contract is frozen; changes need a dated amendment.

**Feature ideas:** `FEATURE_IDEAS.md` collects candidate model features. Whenever a possible feature comes up in conversation, add it there (using its template) without being asked, and tell the user you did. Check the time-order rule: only information the studio controls before release (contract amendment A6).

Project status and plan live in `PLAN.md`.

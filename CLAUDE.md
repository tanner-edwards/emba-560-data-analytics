# Instructions for AI assistants

Read `README.md` first, especially **Notebook workflow** and **Standing rules**, and follow them. In short:

- Run order (see README **Run order**): `tools/get_data.py` → `notebooks/00_build_dataset.ipynb` (assemble) → `notebooks/01_clean_dataset.ipynb` (clean). Analysis starts from `data/clean/films_clean.csv` (one row per film, key `film_uid`; column roles in `films_clean_columns.csv`) and, for individual reviews, `data/clean/reviews_unified.csv`. Don't re-merge or re-clean raw data in personal notebooks; change the pipeline notebook instead (via PR). Only `input` columns and `fin_budget` may be model inputs.
- Work in the current user's personal notebook (`notebooks/<LastName>-A10.ipynb`). Never edit another person's notebook.
- `notebooks/A10-master.ipynb` only receives finished, verified work, promoted via PR.
- `data/raw/` is read-only. No post-release inputs in the model. The purpose contract is frozen; changes need a dated amendment.

**Feature ideas:** `FEATURE_IDEAS.md` collects candidate model features. Whenever a possible feature comes up in conversation, add it there (using its template) without being asked, and tell the user you did. Check the time-order rule: only information known before production.

Project status and plan live in `PLAN.md`.

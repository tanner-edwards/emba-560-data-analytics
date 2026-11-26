# Feature Ideas

A running list of candidate model features for the A10 money-loser screen. Anyone (or their AI) can add to it. Ideas here are **not commitments**: each one still has to pass the contract's time-order rule before it's built.

**Rule for every idea:** the feature may only use information the studio **controls before the film's release** (contract amendment A6, 2026-11-24; was "before production"). Nothing from the film's own release, nothing outside the studio's control (pre-release reviews, buzz), and nothing from later films (no box office, scores, reviews, or "how many sequels it eventually got").

**For AI assistants:** whenever a possible feature comes up in conversation, add it here using the template below without waiting to be asked, and tell the user you added it. Don't duplicate an existing idea; add to its notes instead.

## Template

```
### <Short name>
- **Added:** YYYY-MM-DD by <name>
- **Status:** idea | investigating | building | built (notebook §) | rejected (reason)
- **What:** one or two sentences, with an example film
- **Why it might predict a money-loser:**
- **Possible representation:** columns and types
- **Data sources:** which columns in films_unified.csv (or what's missing)
- **Time-order check:** is every input controlled by the studio before release?
- **Open questions:**
```

---

## Ideas

### Sequel / installment number and franchise membership
- **Added:** 2026-11-23 by Tanner
- **Status:** investigating (title rule prototyped in Edwards §13, 2026-11-26)
- **What:** Track whether a film belongs to a series of installments and which installment it is, plus whether it belongs to a wider franchise. *Spider-Man* (2002): first installment of the Spider-Man series. *Iron Man* (2008): first installment of the Iron Man series and part of the Marvel Cinematic Universe franchise.
- **Why it might predict a money-loser:** sequels and franchise films come with a built-in audience and earlier box office to compare against, so they likely lose money less often. Late installments may show fatigue.
- **Possible representation:**
  - `is_sequel` (bool): installment number > 1
  - `installment_number` (int): 1, 2, 3, …
  - `in_franchise` (bool) and `franchise_name` (category): wider universe, e.g. MCU
  - `prior_installments` (int): earlier films in the series/franchise released before this one
  - Possibly: the previous installment's performance (multiple of budget), which is known before production
- **Data sources:**
  - The Numbers `tn_Franchise` (already in the unified file; sparse)
  - Wikidata "part of the series" (P179), "series ordinal" (P1545), "follows" (P155). Not pulled yet; would need a new snapshot.
  - TMDB "collections" (`belongs_to_collection`) exist in the TMDB API but **not** in our Kaggle file
- **Time-order check:** ⚠️ "1 **of 3**" leaks the future. When *Spider-Man* (2002) was financed, nobody knew there would be three. Total series length can't be an input; installment number and *prior* installments can.
- **Open questions:**
  - Is the "of N" part usable? Tanner (2026-11-23): installment > 1 is clearly known at financing, and planned series (e.g. announced trilogies) often know their length up front. Debate later; if used, it should be the *planned* length at financing, not the eventual count.
  - Series vs franchise: is *Iron Man 2* installment 2 (Iron Man series) or installment 3 (MCU)? Probably keep both.
  - Reboots and remakes: does *The Amazing Spider-Man* (2012) restart the count?
  - Coverage: how many usable films have franchise data from any source?
  - **Title rule (Edwards §13, 2026-11-26):** `sequel` = earlier franchise film in our data OR an installment number in the title ("2", "III", "Part 2"), accepted only with a franchise tag, an explicit installment word, or an earlier film under the base title. Adds 77 sequels (*Toy Story 3*, *Terminator 3*); added ones return 1.41× like other sequels. Remaining errors: *Super 8* accepted; some foreign sequels (*Ong Bak 2*) rejected.
  - **Pre-2000 predecessors (found 2026-11-26, Edwards §11f):** our data starts in 2000, so a sequel whose earlier films are pre-2000 looks like a first film (*Toy Story 3*, *Mission: Impossible II*). Counting earlier films only within our data undercounts sequels; use installment numbers from titles or Wikidata "follows" (P155).

### US / non-US production
- **Added:** 2026-11-24 by Tanner
- **Status:** idea
- **What:** Collapse `countries` (108 values) into a US / non-US category, possibly with a US co-production level. *Parasite* (2019): non-US.
- **Why it might predict a money-loser:** non-US films earn less at the US box office and have different budget economics. Tanner expects it may be weak, since most big-budget films are US; likely the first input to drop.
- **Possible representation:** `country_group` (category: US only / US co-production / non-US)
- **Data sources:** `countries` in films_clean.csv (TMDB → The Numbers)
- **Time-order check:** OK. Production country is known before production.
- **Tanner (2026-11-24):** combine with language. Country is primary; fill blank country from original language.
- **Open questions:** keep a few big markets (UK, France, India) as their own levels?

### Studio and distributor grouping
- **Added:** 2026-11-24 by Tanner
- **Status:** built (Edwards §15i: distributor group +0.169, strongest; re-test without the Blank group, possible coverage leak; major producer +0.040)
- **What:** Standardize name variants (all Warner Bros. labels → Warner Bros.; same for Universal, Fox, etc.), then group into categories such as major studio, foreign studio, animation arm. Same for distributors.
- **Why it might predict a money-loser:** majors have wider releases and bigger marketing; individual names are too thin (two-thirds of companies appear in only one film).
- **Possible representation:** `studio_group`, `distributor_group` (category); maybe per-group track record using only earlier films
- **Data sources:** `production_companies`, `distributor` in films_clean.csv
- **Time-order check:** Company: OK. Distributor: ⚠️ often signed after the film is made; only usable if known at financing (pre-sale deals).
- **Open questions:** how to handle films with several distributors or companies (first listed? any major?).

### Director / writer experience
- **Added:** 2026-11-24 by Claude (from §7 review)
- **Status:** investigating (Edwards §10d, §15n): **track record** (share of earlier films that were winners) is strong: +0.117 AUC over budget among directors with a history (0.469 → 0.586). Use hit rate, not just film count; keep a 'no history' group.
- **What:** Count each director's and writer's earlier films (and optionally how those did) instead of using names. A first-time director scores 0.
- **Why it might predict a money-loser:** two-thirds of directors and writers appear in only one usable film, so names are too thin; experience and past results generalize.
- **Possible representation:** `director_prior_films` (int), `director_prior_loser_rate` (float, blank if none), same for writer; `director_writes` (bool)
- **Data sources:** `director`, `writer`, `release_date` in films_clean.csv
- **Time-order check:** OK only if counts use films released before this one.
- **Tanner (2026-11-24):** count films per person (everyone listed has at least 1), then aggregate across a film's directors and writers. Use counts, not "valuable director" ratings; there isn't enough data for those.
- **Open questions:** our data starts in 2000, so careers before 2000 are missed.

### Source material grouping
- **Added:** 2026-11-24 by Claude (from §7 review)
- **Status:** idea
- **What:** Group the 23 `source_material` values into about 6: Original / Book / Real life / Comic / Remake-sequel-spin-off / Other.
- **Why it might predict a money-loser:** adaptations bring a known audience; many current categories have under 20 films.
- **Possible representation:** `source_group` (category) plus `source_material_missing`
- **Data sources:** `source_material` (The Numbers only, 37% blank)
- **Time-order check:** OK. The source is known before production.
- **Open questions:** blanks are concentrated in small-budget films.

### Franchise × source material
- **Added:** 2026-11-24 by Tanner
- **Status:** built (Edwards §15g: +0.020 over budget, slightly above sequel alone)
- **What:** A sub-level that crosses franchise membership with source material, e.g. a comic-book franchise (*Spider-Man*) vs an original franchise (*Fast and the Furious*) vs a book franchise (*Harry Potter*).
- **Why it might predict a money-loser:** a franchise based on a known property may carry a bigger built-in audience than an original one.
- **Possible representation:** `franchise_source` (category: e.g. franchise-comic / franchise-book / franchise-original / franchise-other / no franchise)
- **Data sources:** `franchise`, `source_material` (both The Numbers)
- **Time-order check:** OK. Both known before production.
- **Open questions:** the pool gets small (about 1,000 franchise films, split across sources). Treat as an optional sub-level.

### Writer + director combination
- **Added:** 2026-11-24 by Tanner
- **Status:** rejected as a pairing (Edwards §15h, §15n): repeat teams add nothing once the director's track record is known (coef 0.01 vs 0.34). Teams that reunite are the ones that had hits.
- **What:** A feature for the writer and director together: whether the director also wrote it (48% of films), and possibly repeat pairings.
- **Why it might predict a money-loser:** writer-directors and repeat teams may have more control or proven chemistry.
- **Possible representation:** `director_writes` (bool), `pair_prior_films` (int)
- **Data sources:** `director`, `writer`
- **Time-order check:** OK if pair counts use earlier films only.
- **Open questions:** repeat pairings will be rare.

### Release day of week
- **Added:** 2026-11-24 by Claude (from Edwards §10)
- **Status:** idea
- **What:** The weekday of the US release. Most films open on Friday; big films often open on a Wednesday before a holiday (*Frozen II* style Thanksgiving openings).
- **Why it might predict a money-loser:** in the training years, Wednesday openings return a median 1.04x their budget in the US vs 0.66x for Friday.
- **Possible representation:** `release_weekday` (category: Wednesday / Friday / other), or `holiday_opening` (bool)
- **Data sources:** `release_date` in films_clean.csv (US date for 78% of films; TMDB fallback otherwise)
- **Time-order check:** OK. The release date is set by the studio before release (A6).
- **Open questions:** is this just a proxy for budget and holiday timing?

### Budget scale (log, tier, relative to year)
- **Added:** 2026-11-24 by Claude (from feature-brainstorm chat)
- **Status:** rejected as separate columns (Edwards §15a: tier and percentile add nothing over log budget; keep log budget, model the curve)
- **What:** Represent `fin_budget` in a form the model can use: log budget, budget tier (e.g. $1–5M / 5–20M / 20–60M / 60M+), and budget relative to other films released in the same year.
- **Why it might predict a money-loser:** budget is heavily right-skewed, and its link to losing is probably curved rather than a straight line. A $30M budget in 2001 is not the same size bet as $30M in 2022.
- **Possible representation:** `log_budget` (float), `budget_tier` (category), `budget_pct_in_year` (float, percentile among training-period films of the same release year)
- **Data sources:** `fin_budget`, `year` in films_clean.csv
- **Time-order check:** OK as a financing-stage input. ⚠️ TMDB records the final budget, which can drift from the planned one (contract weakest link 4); the tier version is the robustness check the contract names. Percentiles must be learned from training years only.
- **Open questions:** does the curve in the bivariate plot support log, tiers, or both?

### Genre grouping and genre count
- **Added:** 2026-11-24 by Claude (from feature-brainstorm chat)
- **Status:** built (Edwards §15b): primary genre +0.077 AUC over budget, keep; genre count adds nothing
- **What:** Reduce `genres_all` to a primary genre (plus "Other" for rare ones) and count how many genres a film lists. *Parasite* (2019): Drama primary, 3 genres listed.
- **Why it might predict a money-loser:** loser rates differ by genre (e.g. horror vs drama), but many genre combinations have too few films to measure on their own.
- **Possible representation:** `primary_genre` (category), `n_genres` (int), optional flags like `is_animation`, `is_horror`
- **Data sources:** `genres_all` in films_clean.csv
- **Time-order check:** OK. Genre is set at greenlight.
- **Open questions:** how to pick the primary genre from a multi-genre list (first listed, or rarest)?

### Release season and holiday window
- **Added:** 2026-11-24 by Claude (from feature-brainstorm chat)
- **Status:** rejected (Edwards §15c: no gain over budget; release weekday +0.020 is the useful part)
- **What:** Turn release month and quarter into seasons and flags for the summer and Nov–Dec holiday windows.
- **Why it might predict a money-loser:** the summer and holiday windows have bigger audiences and more competition; dump months (Jan–Feb, Aug–Sep) may differ.
- **Possible representation:** `release_season` (category), `summer_window` (bool), `holiday_window` (bool)
- **Data sources:** `release_month`, `release_quarter` in films_clean.csv
- **Time-order check:** OK. The contract allows planned release month and quarter.
- **Open questions:** overlaps with "Release day of week"; check they aren't just proxies for budget.

### Runtime bins and "unknown" flags
- **Added:** 2026-11-24 by Claude (from feature-brainstorm chat)
- **Status:** investigating (Edwards §15d: runtime bin +0.014; unknown flag too rare to judge, 27 films)
- **What:** Bucket `runtime_min` (e.g. under 90 / 90–120 / over 120), and keep the `_missing` flags as explicit "unknown" indicators (director unknown, runtime unknown).
- **Why it might predict a money-loser:** runtime may be curved, not linear. Missingness is not random here: match rates are 58% for $1–5M budgets vs 91% for $60M+, so "unknown" partly marks small films.
- **Possible representation:** `runtime_bin` (category), `director_unknown` (bool), `runtime_missing` (bool)
- **Data sources:** `runtime_min`, `*_missing` columns in films_clean.csv
- **Time-order check:** OK. ⚠️ Runtime is the final runtime, not the planned one (contract weakest link 4).
- **Open questions:** does "unknown" predict losing, or just small budgets? Check inside budget tiers.

### Multi-column combinations (3+ inputs)
- **Added:** 2026-11-24 by Claude (from feature-brainstorm chat)
- **Status:** rejected for now (Edwards §15e: budget vs genre-year, tentpole, budget per minute all at noise)
- **What:** Features built from three or more columns, only where a bivariate finding showed an effect that depends on other inputs. Examples: budget relative to the typical budget for the same genre and year; budget × franchise × summer release (the "tentpole" profile); budget per runtime minute.
- **Why it might predict a money-loser:** a $60M budget is ordinary for an action sequel and a huge bet for a drama. The risk depends on budget, genre and era together.
- **Possible representation:** `budget_vs_genre_year` (float: budget ÷ median budget of same primary genre and year, training years only), `tentpole_profile` (bool), `budget_per_minute` (float)
- **Data sources:** `fin_budget`, `genres_all`, `year`, `franchise`, `release_month`, `runtime_min` in films_clean.csv
- **Time-order check:** OK if the genre-year medians use training films only. ⚠️ `franchise` is an A4 candidate (needs amendment before it can be an input).
- **Open questions:** how many training films land in each combined cell? Drop any combination whose cells are too thin to measure.

### Critic and audience scores vs revenue (reverse question, description only)
- **Added:** 2026-11-25 by Tanner
- **Status:** explored (`notebooks/Edwards-A10-reviews.ipynb`, 2026-11-26; description / second label only, **not a model input**)
- **What:** Show how critic score (`critic_pct_fresh`) and audience score (`audience_score`) relate to US box office and the return multiple. The question in reverse: if you make a movie "for the critics," does it earn more than a crowd-pleasing franchise sequel like *How to Train Your Dragon*?
- **Why it's interesting:** separates "critically acclaimed" from "commercially successful." If critic darlings don't out-earn the average, then aiming for prestige isn't a money strategy, and the gap between critic and audience scores may show what audiences actually pay for.
- **Possible representation:** scatter of score vs return multiple (log); return by score band (e.g. < 40%, 40–70%, 70%+); critic − audience gap vs return
- **Data sources:** `critic_pct_fresh` (95% filled in the population), `audience_score` (98%) in films_clean.csv, group `description`
- **Time-order check:** ❌ Scores exist only after release, so they can never be model inputs (contract A6). Fine as a descriptive / explanatory finding in the report.
- **Open questions:**
  - Pre-release proxies for "made for critics" that *could* be inputs: awards-season release (Oct–Dec), drama/history genre, festival premiere, a director's earlier critic scores (earlier films only).
  - Use the training years only, or all years since it's description, not modeling?

### Release-window competition (competitor budgets)
- **Added:** 2026-11-26 by Claude (from feature-brainstorm chat)
- **Status:** rejected (Edwards §15f: no gain, no consistent pattern inside budget tiers)
- **What:** How many big-budget films open near this film's release date, and the biggest competitor's budget. *Barbie* (2023) opened the same weekend as *Oppenheimer*.
- **Why it might predict a money-loser:** a film opening against heavy competition splits the audience and screens, so it may fall short of the 1.25× US box office line (A7) more often.
- **Possible representation:** `big_films_in_window` (int, other films with budget >= "big" threshold released within ±3 weeks), `max_competitor_budget_in_window` (float)
- **Data sources:** `fin_budget`, `release_date` across all real films with a budget in films_clean.csv (not only `in_population`, which requires US box office; but excluding `exclude_reason` junk so fake "$800M" entries don't count as competitors)
- **Time-order check:** ⚠️ Competitor revenue is post-release and must not be used. Competitor budgets and release dates are set before release; under A6 (inputs controlled or known before release) this is mostly fine, since wide-release dates are announced months ahead. Some films move dates late, so the final slate is partly hindsight; report the limitation.
- **Open questions:** window width; "big" threshold from training years only; does it add anything beyond the *Release season and holiday window* idea?

### Merchandise potential (toys and licensing)
- **Added:** 2026-11-26 by Tanner (question: do animated G films make most of their money from toys?)
- **Status:** idea (low priority; mainly a **report limitation**)
- **What:** Whether a film is built to sell toys and licensed products (*Cars*, *Frozen*, *Toy Story*). For a few franchises, retail merchandise sales are several times the box office (Disney reported about $10B in *Cars* retail sales over five years, against roughly $1.4B box office for all three films).
- **Why it matters:** our label counts only US theatrical box office. For merchandise-driven family films it understates the real economics, so a "loser" by our label may still be a winner for the studio. Note: retail sales aren't studio revenue; the studio gets a royalty (licensing averages about 9% of sales, character brands sometimes 20%+), so $10B retail is closer to $1B for the studio.
- **Possible representation:** no merchandise data in any source. Proxy only: `merch_property` (bool) = Kids Fiction or Animation or "based on toy", G/PG, major studio. All already inputs, so a separate feature likely adds little.
- **Data sources:** none direct; proxies in films_clean.csv
- **Time-order check:** OK for the proxies (all set before release). Actual merchandise sales are post-release and can't be used.
- **Open questions:** state it as a limitation in the report: "box office only; ancillary revenue (merchandise, home video, streaming) is not counted."

### Niche crowding (how many similar films open nearby)
- **Added:** 2026-11-26 by Tanner
- **Status:** investigating (Edwards §15k–15m). Exact-same-rating count is weak (+0.004). **Tanner's overlapping-ratings version** (G↔PG↔PG-13↔R within ±6 weeks, relative to what's normal for the rating) adds +0.012 over budget and lowers return inside every rating and budget tier (e.g. R 0.77× → 0.41×). Keep the relative overlap version.
- **What:** How many films *like this one* open around its release: same MPAA rating or same primary genre within ±6 weeks, and the genre's share of releases in that window. G-rated family films return the most but are rare; maybe they win partly because each one has the family audience to itself.
- **Why it might predict a money-loser:** a film opening into a crowded niche (three family films in a month) splits its audience; a film in an empty niche gets it all.
- **Possible representation:** `same_rating_in_window`, `same_genre_in_window` (int), `niche_share` (float)
- **Data sources:** `release_date`, `mpaa_rating`, `genres_all` of all real films with a US release date in films_clean.csv
- **Time-order check:** OK under A6. Competitors' dates, ratings and genres are set before release (only their box office would leak, and it isn't used). Some films move dates late; report the limitation.
- **Open questions:** window width; is it just a proxy for season (summer is crowded for everyone)? Compare with *Release-window competition*.

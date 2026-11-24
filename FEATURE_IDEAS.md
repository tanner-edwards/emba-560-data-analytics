# Feature Ideas

A running list of candidate model features for the A10 money-loser screen. Anyone (or their AI) can add to it. Ideas here are **not commitments**: each one still has to pass the contract's time-order rule before it's built.

**Rule for every idea:** the feature may only use information known **at the financing decision, before production**. Nothing from the film's own release or from later films (no box office, scores, reviews, or "how many sequels it eventually got").

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
- **Time-order check:** is every input known before production?
- **Open questions:**
```

---

## Ideas

### Sequel / installment number and franchise membership
- **Added:** 2026-11-23 by Tanner
- **Status:** idea
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
- **Status:** idea
- **What:** Standardize name variants (all Warner Bros. labels → Warner Bros.; same for Universal, Fox, etc.), then group into categories such as major studio, foreign studio, animation arm. Same for distributors.
- **Why it might predict a money-loser:** majors have wider releases and bigger marketing; individual names are too thin (two-thirds of companies appear in only one film).
- **Possible representation:** `studio_group`, `distributor_group` (category); maybe per-group track record using only earlier films
- **Data sources:** `production_companies`, `distributor` in films_clean.csv
- **Time-order check:** Company: OK. Distributor: ⚠️ often signed after the film is made; only usable if known at financing (pre-sale deals).
- **Open questions:** how to handle films with several distributors or companies (first listed? any major?).

### Director / writer experience
- **Added:** 2026-11-24 by Claude (from §7 review)
- **Status:** idea
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
- **Status:** idea
- **What:** A sub-level that crosses franchise membership with source material, e.g. a comic-book franchise (*Spider-Man*) vs an original franchise (*Fast and the Furious*) vs a book franchise (*Harry Potter*).
- **Why it might predict a money-loser:** a franchise based on a known property may carry a bigger built-in audience than an original one.
- **Possible representation:** `franchise_source` (category: e.g. franchise-comic / franchise-book / franchise-original / franchise-other / no franchise)
- **Data sources:** `franchise`, `source_material` (both The Numbers)
- **Time-order check:** OK. Both known before production.
- **Open questions:** the pool gets small (about 1,000 franchise films, split across sources). Treat as an optional sub-level.

### Writer + director combination
- **Added:** 2026-11-24 by Tanner
- **Status:** idea
- **What:** A feature for the writer and director together: whether the director also wrote it (48% of films), and possibly repeat pairings.
- **Why it might predict a money-loser:** writer-directors and repeat teams may have more control or proven chemistry.
- **Possible representation:** `director_writes` (bool), `pair_prior_films` (int)
- **Data sources:** `director`, `writer`
- **Time-order check:** OK if pair counts use earlier films only.
- **Open questions:** repeat pairings will be rare.

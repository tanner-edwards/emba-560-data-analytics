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
  - Series vs franchise: is *Iron Man 2* installment 2 (Iron Man series) or installment 3 (MCU)? Probably keep both.
  - Reboots and remakes: does *The Amazing Spider-Man* (2012) restart the count?
  - Coverage: how many usable films have franchise data from any source?

# A10 Problem Scan (CRISP-DM Business Understanding, Step 1)

Date: 2026-11-17. Analyst: Matt Sorensen. AI role: Problem Setter + Creative Expander (Claude Code, crispdm-problem-scanner skill).

## Inputs, kept separate
- **Problem context:** Matt's question: what makes a movie more successful than others (star power, score, marketing, script quality)? There are no interviews with real stakeholders. Every decision owner below is a representative role, not a named client.
- **Data on hand:** TMDB (budget, worldwide revenue, genre, companies, keywords, runtime, release date, audience votes; no cast or crew). RT movies (critic and audience scores, director, writer, domestic box office, distributor). RT reviews (dated critic reviews and text). About 80% of the 7,716 usable TMDB films match to RT.

## Ranked candidates

| Rank | Decision (owner → what changes) | Value | Feasibility | Dataset-bias flag |
|---|---|---|---|---|
| 1 | Acquisitions team at a film financier or streamer screens projects before release: flag, review or pass | High | High | Moderate |
| 2 | Greenlight committee decides whether to pay a premium for a director with a strong track record | High | Medium | Low |
| 3 | Mid-size studio sets next year's slate mix of budget tiers and genres | Medium–High | Medium–High | Moderate |
| 4 | Distributor picks the release month or window by genre | Medium | Medium | Low |
| 5 | Streamer decides which released films to license for its catalog | High | Low | Low |
| 6 | Distributor decides whether to hold early press screenings or embargo reviews | Medium | Low–Medium | **High** |
| 7 | Studio marketing sets each film's marketing (P&A) budget | High | Very low | None |
| 8 | Development executive decides which scripts to buy | High | Very low | None |
| 9 | Marketing decides whether a campaign leads with critic quotes or audience scores | Low | Medium | **High** |

### 1. Pre-release profitability screen (lead)
An acquisitions or co-financing team decides, before a film is released, whether to flag a project as likely to lose money, send it for deeper review, or pass. It would use only information known at that point: budget, genre, runtime, release timing, company track record and director track record. The value comes from avoiding films that never recover their budget. The outcome (revenue / budget) is directly measured for about 7,700 films, and the 2016–2019 films can serve as a test set.
**Bias flag:** this ranks partly because budget and revenue happen to exist in TMDB. Films with reported budgets lean toward studio releases, so the screen only applies to that population. The decision itself is real, which is why it stays in first place with this note attached.

### 2. Director premium (rival framing of #1)
The resources are the same as #1, but the use is different. #1 sorts projects; #2 asks a single investment question: is a director's track record associated with better ROI, so that paying a premium for one is justified? This is the closest fit to your original star-power question, using director as the measurable stand-in. It's an explanatory path, or a causal attempt that probably ends in a justified non-identification stop, because strong directors get bigger budgets, better scripts and more marketing.
**Feasibility:** director is in RT (97% coverage). The track record has to be built only from each director's earlier films, and many directors have only one or two films, which will make the estimates noisy.

### 3. Slate composition (rival framing of #1)
Instead of screening single projects, a studio decides its *portfolio* mix: how many low, mid and high-budget films, and in which genres. You'd describe how ROI and risk vary by budget tier and genre (median outcome, how often films lose money, spread). The value is in portfolio risk, and the analysis is simpler than #1. It's weaker on the 16-point modeling criterion because it's mostly descriptive.

### 4. Release timing
A distributor picks a release month by genre. The data supports it (release dates, genre, ROI). The catch is confounding: studios put their strongest films in summer and the holidays, so the month partly reflects expected quality. The claim would have to stay at the level of association. The value is moderate.

### 5. Library licensing (decision made after release)
A streamer decides which released films to license. Here critic and audience scores are legitimate inputs, because they exist at decision time. **The outcome isn't available:** there's no streaming viewership or licensing cost in the data, and vote count is a weak stand-in. Without outcome data this one stalls.

### 6. Early screenings and review embargoes (dataset picked the problem)
A distributor decides whether to let critics review early. This candidate exists only because RT reviews have dates. The early-review hypothesis hasn't been checked, and RT review dates may not reflect true publication timing. It's down-ranked for that reason. It could become an add-on feature for #1 if the dates check out.

### 7. Marketing budget per film (not tied to any dataset)
This is highly valuable and directly answers your "marketing" factor. It needs marketing spend by film, which is industry or internal data you don't have, and no TMDB or RT field stands in for it. It belongs in the report as the strongest reopening evidence: "with marketing spend data, we could …"

### 8. Script acquisition (not tied to any dataset)
A development executive decides which scripts to buy. That needs script-quality measures (coverage scores, industry script rankings, screenplay text), none of which you have. It also belongs in Limitations and as reopening evidence.

### 9. Critics vs. audiences messaging (dataset picked the problem)
Marketing decides whether ads lead with critic quotes or audience scores. Both scores come out after release, ad creative isn't observed, and nothing links the messaging choice to an outcome. It's interesting to describe, but the value logic is weak. It's down-ranked, and could be a single descriptive chart at most.

## Carry forward to decision-statement-builder
- **Primary: #1, the pre-release profitability screen,** with director track record as the focal factor. That keeps your star-power question as the explanatory layer.
- **Rival to test it against: #2, director premium.** If #1 fails the red-team, #2 is the fallback: an explanatory path with a likely justified causal stop.
- **Use as reopening evidence: #7 and #8.** They explain why marketing and script quality are unmeasured.

## Verification
- Every candidate is phrased as an owner plus what changes: yes.
- Candidates that don't depend on the data on hand: #7 and #8 (and #5's outcome).
- Rival framings for the top candidate: #2 (investment question) and #3 (portfolio).
- Dataset-availability bias: flagged on #1 (moderate), #6 and #9 (high, down-ranked).

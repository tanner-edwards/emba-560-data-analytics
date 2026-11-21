I am now starting the following assignment: 
A10 is a team project worth 120 points. Every team member submits A10 in MyEducator by December 4 at 3:30 PM: the same .zip of the team's project folder (data, notebooks, all of the team's AI conversations, the final project document, and a README), the same report, and the same deck link, plus your own AI Disclosure, role statement, and workload response.
After the last class day, each student takes an individual final exam that includes questions about your own team's folder. Your instructor will announce the format and date.

A10 Submission and Fixed 120-Point Rubric
Criterion    Evidence    Points
Business Understanding and Project Purpose Contract    Stakeholder, owner, decision, action, population, unit, timing, baseline, approved path, claim, evidence standard, constraints, and stop condition    12
Data Receipt and Data Fitness    Source, rights, collection, grain, scope, physical checks, sensitive fields, missing coverage, limitations, and fitness disposition    8
Data Understanding    Type-appropriate univariate and bivariate evidence, decision-relevant interpretation, quality and leakage risks, and consequences for the next phase    12
Data Preparation and Variable Discipline    Preserved raw data, ordered changes, row reconciliation, information loss, timing, variable roles, and verification    8
Analytical Path Fit and Modeling    Simplest adequate path-specific method, baseline or comparison, declared design, bounded search, and locked final analysis    16
Evaluation, Verification, and Claim Boundary    Declared standard, uncertainty, failure slice, alternative explanation, independent number checks, one material AI correction, and bounded claims    12
Decision Policy, Deployment, and Responsible Use    Action policy, capacity, timing, owner, monitoring, fallback, intended use, affected people, review, correction, and remedy    8
Value, Uncertainty, and Stop or Continue Logic    Business-unit value, visible assumptions, sensitivity, marginal value and cost, binding constraints, disposition, and reopening evidence    7
Executive Communication and Evidence Traceability    Answer-first disposition, readable necessary visuals, limitations, consistent values, sources, and decision-number trace    7
Team presentation deck    Team deck and speaker notes for an eight-to-ten-minute briefing, graded whether or not presentations are scheduled; decision first; path fit; necessary evidence; value, uncertainty, limitations, risks, and next gate    15
Project folder (.zip)    Data and Data Receipt, notebooks saved after a fresh top-to-bottom run, all team AI conversations, the final project document and deck, and a README that lists every file and its main owner (Section 16.3)    5
AI Disclosure    Each student’s individual disclosure: tools and tasks, material checks, and what the student changed, rejected, or decided    10
Team members and AI conversations    Every member’s name and main role, and confirmation that all team AI conversations are in the project folder    0
Workload calibration    Required response used for course improvement, not academic scoring    0

Complete one approved primary path. A justified causal non-identification conclusion can earn full path-fit credit when it documents the identification threat, reports only the association supported by the data, restricts the claim, and proposes the next credible design. The team-member, AI-conversation, and workload calibration responses are required zero-point process evidence. Missing or inaccessible process evidence requires instructor review. It is not automatically a zero. Tool sophistication, code authorship, visual decoration, feature count, and model count earn no points.
A consequential integrity failure can limit the score regardless of polish. Examples include fabricated sources, knowingly false numbers, undisclosed sensitive data, hidden leakage, or a recommendation that contradicts the submitted evidence.

Where A10 Evidence Goes
Use the fields in the A10 assessment below. Upload the project folder as one .zip file, following Section 16.3. Before you compress it, rerun every notebook with Runtime > Run all and save it with its outputs, so the numbers in your report match what the notebooks show. If the assessment page lists different fields, follow the assessment page.
A10 Starter Files
Download the A10 Final Project Report Template and the A10 Final Project Notebook. Save your own copy of each file before editing. The same files are listed under Student Materials in MyEducator.

Checking the project rules and saved preferences.

I’ll start by checking your course notes and Chapter 16, and looking at what’s in your Business Analytics folder, so I can scope A10 properly.

A10 is a team project worth 120 points, due Fri Dec 4 at 3:30 PM, which is 17 days out. Chapter 16 in the textbook is partly out of date, so I’ve worked from the assessment page you pasted.

Where the textbook and the assessment page differ (follow the assessment page):

Points: 120, not 150.
Presentation: a team deck with speaker notes for an 8–10 minute briefing, submitted as a view-only link. It is not a recorded video, and the notebook is no longer a separate deliverable.
Team folder: one shared .zip that every member uploads. It holds the data and Data Receipt, every notebook saved after a fresh Run all, the final report and slides, and a README listing each file and its main owner.
AI conversations: every conversation from every team member goes in the folder, full and unedited, one file per conversation. The textbook’s compact-record prompt no longer applies.
AI Disclosure: individual, 10 points. It is graded on specifics and the judgment you kept, not on how much AI you used.
Final exam: individual, after the last class day, with questions drawn from your own team’s folder, so you should understand every number and decision in it.

What the report is graded on (90 points, 10 main-body pages):

Largest criterion: Analytical Path Fit and Modeling is the biggest at 16.
Front of the report: the Project Purpose Contract (12), then data fitness (8), data understanding (12) and data preparation (8).
Back of the report: evaluation and verification (12), decision policy (8), value and stop logic (7), and executive communication (7).
Required correction: you must catch and correct at least one material AI error.
Number trace: independently rebuild the 3–5 numbers that drive your recommendation, and put the full trace in Appendix D.
Complexity: a simple, defensible analysis earns full credit. Extra models and polish earn nothing.

A rough backward plan:

By about Nov 20: confirm the team, the decision, the path and the dataset, and get instructor approval if it’s required.
Through about Nov 27: write the Purpose Contract and Data Receipt, then do data understanding and preparation.
Through about Dec 1: run the modeling and evaluation, lock the numbers, and do the independent trace.
Dec 2–3: write the report, deck and README, check that every number matches a notebook output, and build the zip.

You’ve set up Claude Code in VS Code for notebook work so each assignment’s conversation export stays clean. That fits A10’s requirement, but any project conversation anyone on the team has with an AI, this chat included, has to be exported into the folder.

I need to know where you stand before I can scope the next step.

Where does your team's A10 stand right now?
Dataset approved
What do you want help with first?
Pick the decision and dataset
Checking contradictory instructions about the dataset and decision.

Those two answers conflict. You said the dataset is approved, but you also want help picking the decision and dataset, so I’m not sure which one you mean.

Which of these is closest?

Dataset approved, decision still open. Tell me the dataset name and the path your instructor approved (predictive, causal, or explanatory). I’ll help you turn it into one consequential decision and draft the Project Purpose Contract.
Dataset not actually approved yet. Tell me which candidates your team is weighing. I’ll test each against the approval checklist: grain, rights, sensitive fields, leakage risk, time order, sample size, and whether it supports your path.

I noticed insurance.csv in your Business Analytics folder. If that’s the approved dataset, say so and I’ll profile it and propose candidate decisions.

I also need your team members’ names and any decision your instructor has already approved.

important to know that two of us in our group of six are tasked with doing this project. While the rest of the team works on other projects. So it's me and one other guy doing this. My approach is going to be to do this project solo and share what I learn with my colleague who's also working on this project. We will meet and compare notes. A couple times a week. My intent is to start from scratch, and work through the crisp DM and each chapter, applying each skill file for each chapter to our data set, and have Claude engage in a variety of AI engagement model personas. We have a couple data sets chosen from Kaggle, and these are IMDb movies with like 1 million movies, and I believe a Rotten Tomatoes data set of movies as well. We want to combine these, do some feature engineering, and we're not sure yet if we're going to do a causal or predictive path, but we will decide once we get into the data and learn what it can tell us, with your help, of course.

Having two of you on this changes some things, and one part of your plan needs adjusting.

Team and roster. The assignment says the names on page 1, the README and slide 1 must match the course roster, and every listed member uploads the same zip. Before you start, confirm with your instructor that a two-person team is registered, and ask whether the other four members will be listed on this project.

Deciding the path after seeing the data won’t work. The Project Purpose Contract has to be written before substantial analysis, and the textbook lists “method changes without a recorded purpose decision” as a warning sign. Your instructor also approves the path up front. Choosing the path after you see what the data “says” also lets the dataset define the problem, which is the thing the contract exists to prevent. The fix is to decide the decision first, then let the path follow from it. You can still look at structure (fields, timing, join quality, missingness) before committing, but don’t mine outcome relationships to pick a path.

Two movie-data risks that will shape the decision:

Leakage. IMDb ratings, vote counts and Rotten Tomatoes scores are all recorded after release. A predictive model is only defensible if the decision time comes after those fields exist, or if you restrict yourself to fields known at the decision moment.
Value logic. The report needs a business-unit value and a stop rule (7 points). Movie rating data usually has no cost, revenue or viewership, so you need a stakeholder whose decision you can value without inventing numbers.

A causal path on observational movie data will probably hit an identification problem. That’s allowed: a justified non-identification conclusion can earn full path credit if you document the threat and propose the next credible design.

Your from-scratch plan. Applying every chapter’s skill across 17 days is too much, since the rubric rewards the simplest adequate path rather than coverage. Use the skills as lenses only for the phases you need: the Business Understanding skills first, then the data and prep skills, then whichever path chapter you pick.

Your colleague will take the same exam questions on the folder, so the notes you share need to cover what the numbers mean, not just the results. Every AI conversation either of you has about the project has to go into the zip, full and unedited. Each of you also writes your own individual AI Disclosure.

First step: scope before you analyze. I suggest we do these three things this week:

Generate and rank candidate decisions, using the problem-scanner skill with me as Creative Expander and Problem Setter.
Write a Data Receipt and physical check of both Kaggle files, including how well IMDb and Rotten Tomatoes titles actually match. That tells us whether the combined dataset is feasible, and doesn’t require picking a path.
Draft the Purpose Contract and get approval.

Neither movie file is in your Business Analytics folder. Can you drop them there, or tell me the Kaggle dataset names, and tell me whether you or your instructor have already settled who the stakeholder is?

you don't decide how we as a team accomplish this assignment. We will disclose what is required to our professors outside of a Claude session. 
I'm fine deciding now before the data. we want to know what causes a movie to be more successful than other movies. Is it star power? the score? the marketing? the quality script? all of these?

Understood. How your team splits the work and what you tell your professors is your call, and I’ll stick to what bears on the rubric.

Deciding the question now is the right move. As worded, though, “what causes a movie to be more successful?” is really several different questions, and the data limits which ones you can answer.

What your data can and can’t measure:

Star power. You can measure it from IMDb with cast and crew credit histories, such as how well a person’s prior films did, counted only up to each film’s release date so you don’t leak the future.
The score. This is an outcome of the movie, not a cause of its success. Critic and audience scores come after release and are tangled up with success, so using them as a cause or even as a control would bias the result. Treat them as outcomes, or as a mediator you deliberately exclude.
Marketing and script quality. Neither IMDb nor Rotten Tomatoes records marketing spend or script quality. Without a proxy these can’t be tested, and they’ll sit in the report as unmeasured confounders. Stars, budgets and scripts tend to come as a package, so skipping them is what makes a star-power effect hard to identify.
“Success.” This has to be one defined outcome, such as box office, ROI, audience rating or vote volume. Box office and budget probably aren’t in IMDb, so check whether your Rotten Tomatoes file has them.

What this means for the path. A causal question like “does casting a star make a movie succeed?” will almost certainly run into confounding on this observational data. That’s acceptable. A justified causal stop can earn full path credit if you document the identification threat, report only the supported association, restrict the claim, and propose the next credible design, such as a natural experiment or an A/B test on trailers. An explanatory path would let you estimate how each factor is associated with success, with uncertainty, and a clear boundary on what you can’t claim.

What the contract still needs. The Purpose Contract needs a decision with an owner, not only a curiosity. For example: a studio’s greenlight committee deciding whether to pay a premium for star talent, or a streamer deciding where to spend its promotion budget. I’d narrow to one focal factor, probably star power since it’s the most measurable, and list the others as controls or limitations.

Before we go further I need two things:

Which “success” outcome do the files actually contain (box office, budget, ratings, votes)?
Where are the two Kaggle files? They aren’t in your Business Analytics folder, so I can’t profile them yet. If you drop them there, I’ll check the columns, the date coverage and how well the two sources match.

Why don't we move to VS Code and continue there after we import the files and start looking at headers?

Good idea, and it matches how you’ve handled earlier assignments. I’ll write a handoff note to your project so Claude Code starts with the decisions we’ve made so far.

Moving to VS Code works. I saved a handoff note to your project as claude/a10-handoff.md. It covers the assignment facts, the decisions we’ve made, the cautions about the movie data, and the first steps. Give it to Claude Code along with your working-preferences file.

Here’s how I’d start the session:

Import the files. Put both Kaggle files in your Business Analytics folder. Open that folder in VS Code and start a fresh Claude Code session, so you get one clean conversation export.
Look at the headers and the structure only. Print the shape, column names, types, missingness and date ranges for each file. Don’t look at how any factor relates to success yet.
Write the Data Receipt as you go. Record the source, license, grain and access date. Check how well IMDb and Rotten Tomatoes titles join, and which success outcomes actually exist, such as box office, budget, ratings and votes.
Settle the Purpose Contract once you know the outcomes. Fix the path, the outcome, the one focal factor and the decision owner before any modeling.

When you’ve seen the headers, come back here if you want to talk through the path or the decision framing. This chat is a good place for those judgment calls. This conversation also counts as project AI use, so export it into your folder with the others.

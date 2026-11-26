# CCAR-P Study Aid

An offline study aid for the **Claude Certified Architect – Professional (CCAR-P)** exam: 613 multiple-choice practice questions across the exam's 7 domains, with learn and trap cards for each subject, explanations, mnemonics and progress tracking.

## Using it

Download [`CCAR-P Study Aid.html`](CCAR-P%20Study%20Aid.html) and open it in any modern browser. It is a single self-contained file: no install, no dependencies, no network access.

- **Subjects:** each domain is split into subjects. Read the learn and trap cards, then take the subject quiz. The first run serves every question; retakes serve only the ones you missed or haven't answered.
- **Domain test:** 20 mixed questions drawn from the whole domain.
- **Mastery:** the share of a domain's questions whose *latest* attempt was correct. The pass mark is 85% in every domain.
- **Progress** is saved in your browser's local storage and can be reset in the app. Option order is reshuffled every time a question is shown.

| Domain | Weight | Subjects | Questions |
|---|---|---|---|
| 1 Solution Design & Architecture | 17% | 6 | 121 |
| 2 Claude Models, Prompting & Context Engineering | 13% | 4 | 59 |
| 3 Integration | 19% | 5 | 99 |
| 4 Evaluation, Testing & Optimization | 16% | 4 | 71 |
| 5 Governance, Safety & Risk Management | 14% | 6 | 111 |
| 6 Stakeholder Communication & Lifecycle Management | 14% | 5 | 92 |
| 7 Developer Productivity & Operational Enablement | 7% | 4 | 60 |

## How it's built

The HTML is generated, so don't edit it directly. Content lives in one JSON question bank per domain; the UI and all logic live in a template.

```
source/template.html   UI and quiz logic, with a data placeholder
source/data/dN.json    question bank for domain N (subjects, learn/trap cards, questions)
source/build.py        inlines the seven banks into the template -> CCAR-P Study Aid.html
source/validate.py     quality gate for a bank
source/SPEC.md         authoring contract for writing questions
source/gap/            tooling and reports from the coverage-gap round
source/review/         review reports and pre-change backups of the banks
```

Requires Python 3 (standard library only). From `source/`:

```bash
python validate.py data/d3.json   # check one bank; exits 1 and lists problems on failure
python build.py                   # rebuild ../CCAR-P Study Aid.html from all seven banks
```

The validator checks structure (option and answer counts, "Select TWO/THREE" wording for multi-answer questions), balance (correct and wrong options of similar length, and how often the correct option is the longest), per-subject minimums (questions, multi-answer questions, repeated concepts) and style (no letter prefixes, no "all/none of the above", short mnemonics).

## Course materials are not included

Every question is written from the official exam guide and education notes. Those documents are third-party material and are not part of this repository; `.gitignore` excludes them. Building and validating work without them, but writing or fact-checking questions needs your own copies placed at the repo root. To extract their text:

```bash
python source/extract_notes.py source/notes_txt   # run from the repo root
```

## Authoring rules

See [`CLAUDE.md`](CLAUDE.md) for the full rules. In short:

- Every correct answer must be supported by the notes; no outside knowledge.
- Questions test the general guidance the notes state, not the particulars of their worked examples.
- Every claim in each notes file's closing takeaways is stated on a card and tested by at least one question ([`source/review/TAKEAWAY_COVERAGE.md`](source/review/TAKEAWAY_COVERAGE.md)).
- Question ids are never reused, because saved progress is keyed by id.
- Content the notes mark as not tested (demo design, joint scoping, objection categories, Partner Track material) is excluded.

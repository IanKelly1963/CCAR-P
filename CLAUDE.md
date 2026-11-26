# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Not an application. It is a study-aid generator for the **Claude Certified Architect – Professional (CCAR-P)** exam. The deliverable is one standalone file, `CCAR-P Study Aid.html` (dark-theme quiz app, no dependencies, no network). It is **generated**; never hand-edit it.

Inputs at the repo root (read-only reference): `Exam Guide.pdf` (blueprint, 7 domains, 85% per-domain pass target used by the aid) and five `.docx` education notes. The notes cover 5 topics but the exam has 7 domains, so notes are mapped onto domains:

| Domain (weight) | Drawn from |
|---|---|
| 1 Solution Design (17%) | `01` + sizing/feasibility/ROI from `02` |
| 2 Models, Prompting, Context (13%) | `01` |
| 3 Integration (19%) | `01` (RAG, entry points, routes, Claude Code layers) + `02` (identity, data, observability) |
| 4 Evaluation (16%) | `02` (+ model-swap gating from `01`) |
| 5 Governance (14%) | `03` |
| 6 Stakeholder/Lifecycle (14%) | `04` |
| 7 Dev Productivity (7%) | `05` |

`04` contains a `<NOT TESTED>` block (demo design, joint scoping, objection categories) and a "Reuse potential" field marked Partner Track. **No questions may be written about these.**

## Commands

All from `source/` (Python 3, stdlib only for build/validate):

```bash
python validate.py data/d3.json   # validate one domain bank (exit 1 + list of problems on failure)
python build.py                   # inline data/d1..d7.json into template.html -> ../CCAR-P Study Aid.html
python extract_notes.py <outdir>  # re-extract the .docx notes to NN.txt (run from repo root; does not handle the PDF, `guide.txt` was made with pypdf)
```

There is no test suite or linter. Verify UI changes by opening the built HTML (a `file://` page; drive it through the browser pane if needed). `localStorage` is blocked in `data:` previews, which the app tolerates.

## Architecture

```
source/template.html   UI + all logic; contains the placeholder  /*__DATA__*/null
source/data/dN.json    one question bank per domain (the content)
source/build.py        json.dumps all 7 banks, escapes "</" , substitutes the placeholder
source/validate.py     quality gate for a bank
source/SPEC.md         authoring contract used to brief writers/agents for new banks
source/notes_txt/      plain-text extraction of the notes + guide (source of truth for facts)
```

The edit loop is always: change `template.html` (behaviour/design) or `data/dN.json` (content) → `build.py` → open the HTML.

### Data model (`data/dN.json`)
`{domain, subjects:[{id "d<D>s<N>", title, learn[4-6], traps[3-5], questions[]}]}`; a question is `{id, concept, type single|multi, stem, options[], correct[0-based], explanation, mnemonic}`.
- `concept` ties rephrased variants of the same fact together; the runtime uses it to keep variants apart in a session, and `validate.py` requires ≥4 repeated concepts per subject.
- Multi-answer stems must say "Select TWO/THREE" matching `correct.length`.
- Domain titles, weights and colours are hardcoded in `template.html` (`DOMAINS`, `--d1..--d7`), not in the JSON.

### Runtime behaviour (single `<script>` in `template.html`)
- Hand-rolled router (`go(view,arg)`) over views: home, domain, subject (learn/traps), quiz, results. Quiz state lives in a module-level `sess`.
- Option order is reshuffled every time a question is displayed (`sess.order`); subject quizzes (`startSubjectQuiz`) serve every question on the first run, then only missed/unanswered ones on retakes (`weak()`); when all are correct a modal offers a full rerun, and "Restart subject" clears that subject's results. The domain test draws 20 via `pick()`.
- Progress persists to `localStorage` key `ccarp-study-v1` (`P.q[id] = {n, c, last, t}`), with an in-memory fallback. **Mastery = share of a domain's questions whose latest attempt was correct** (not raw accuracy); that is what the 85% pass line is compared against. Changing the key schema or question ids invalidates users' saved progress.

## Rules for editing question banks

- Every correct answer must be supported by the notes (`notes_txt/`); don't import outside knowledge. Reuse the notes' terms.
- Correct and incorrect options must be of similar word length (validator flags ratio outside 0.75–1.3, and correct-is-longest above 55%).
- No letter prefixes in options, no "all/none of the above", mnemonic ≤ ~18 words and encoding the actual fact.
- **No worked-example questions.** The notes illustrate points with scenarios (the five-clean-demo reconciliation pipeline, the GBP 5,000 / 41-of-14,000 claims misroute, the 50-section contract fan-out, the order-status RAG trace, the 50-session A/B test, the hospital dictation call, the CTO invoice, etc.). Questions and learn/trap cards must test the general rule the notes state *outside* the example, not the example's particulars or setup; a short newly invented scenario is fine. 102 such questions were replaced on 2026-10-04 (`source/review/WORKED_EXAMPLE_REVIEW.md`, `APPLIED_CHANGES.md`).
- **Takeaway coverage is an invariant.** Every claim in each notes file's closing takeaways section has a learn/trap card that states it and at least one question that tests it (`source/review/TAKEAWAY_COVERAGE.md` holds the claim → card → question map). Keep it true when removing or rewording questions/cards.
- **Question ids are never reused.** Replaced questions get a new id; removed ids are retired (current subjects jump numbers, e.g. there is no d1s1q03). Saved progress is keyed by id.
- Always re-run `validate.py` on the edited bank, then `build.py`.
- The notes flag several time-sensitive facts ("verify at publish time": model support, Foundry EU residency, `inference_geo` values, FedRAMP routes). Questions phrase these as "verify" rather than asserting them as permanent.

## Change history and backups
Each bulk change kept a pre-change copy of `data/`: `source/gap/backup_before_gap/` (original 470) → gap merge (+123, report `gap/GAP_REPORT.md`) → `source/review/backup_before_worked_examples/` → worked-example replacements → `source/review/backup_before_takeaways/` → takeaway fixes (+20) → current `data/` (613 questions). Follow the same pattern for any bulk edit: back up, write a review file for approval, apply, record what was applied.

## Gap analysis tooling (`source/gap/`)
`GAP_BRIEF.md` briefs agents to find untested content in `notes_txt/` against `bank_index.md` and write staging files `new_<tag>.json`. `check_new.py` validates a staging file. `merge.py` dry-runs (overlap report); `merge.py --apply` appends to the banks and writes `GAP_REPORT.md`. `skip.txt` lists `<tag> <index>` entries to leave out.
- **Do not re-run `merge.py --apply` as-is.** The six `new_*.json` files present are already merged; re-applying appends them again, including questions retired by the worked-example review. Move or delete them before staging a new round.
- `bank_index.md` is a snapshot from before the gap merge; regenerate it from `data/` before a new gap round.
- `merge.py` numbers new questions as the subject's current max id + 1, which would reuse a retired id if a subject's highest-numbered question was ever retired (not the case as of 2026-10-06). Check the backups if in doubt.

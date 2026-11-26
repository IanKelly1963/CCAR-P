# Gap-analysis brief (CCAR-P study aid)

Root: C:\Users\Ian\OneDrive\Documents\CLAUDE_PROJECTS\ARCHITECTURE PROF\source

The study aid already has a 470-question bank (source/data/d1..d7.json). Your job: find
**non-trivial content in your assigned notes segment that NO existing question tests**, and write
new questions for it. Do NOT edit source/data/*.json. Write only your staging file.

## Read first (in full)
1. Your assigned notes segment in source/notes_txt/ (line range given in your task).
2. source/gap/bank_index.md — every existing question (id, [concept], stem => correct answer), grouped
   by subject. A fact counts as COVERED if any question in ANY domain tests it, even with different wording.
   Read the whole index; cross-domain overlap is common (e.g. permission modes appear in d3s5 and d7s1).
3. source/SPEC.md — the question-writing rules (style, length parity, mnemonics, no letter prefixes,
   no all/none of the above, multi stems say "Select TWO/THREE"). Those rules apply here.

## What counts as a gap worth a question (non-trivial)
YES: a decision rule, trade-off, failure mode and its fix, a named mechanism and when to use it,
a distinction the notes say is commonly confused, a "why this broke" lesson, a threshold/number the
notes use to make a decision (e.g. a p95 definition, an alert threshold), a placement rule (which layer
a control belongs in), the owner of something, an ordering/sequence the notes prescribe.
NO: course-navigation filler ("we will revisit this later"), restatements of something already tested,
trivia with no architectural consequence, lists of product names with no decision content, anything
inside <NOT TESTED>...</NOT TESTED> in 04.txt, the "Reuse potential" / Partner Track field.
Facts the notes mark "verify at publish time" may be tested only with "verify" framing.
Partially covered counts as a gap only if a distinct, testable aspect is missing (say which aspect).

## Placement
Put each new question in the best-fitting EXISTING subject id (see "## dXsY" headers in bank_index.md).
Domain mapping: d1 solution design, d2 models/prompting/context, d3 integration, d4 evaluation/production,
d5 governance/safety, d6 stakeholder/lifecycle, d7 team enablement. If a gap genuinely fits no subject,
still write it, put your best subject, and say so in the gap's summary.

## Coverage-by-rephrasing
For each gap area with a significant fact, write TWO questions that test it in different ways (different
scenario or flipped framing) and give them the same "concept". Minor gaps may get one question.
About 25% of your questions should be multi-select.

## Output: source/gap/new_<tag>.json  (tag given in your task)
{
  "gaps": [ {"subject":"d3s2","area":"short name of the missing area","source":"01.txt L355-361",
             "summary":"one sentence: what the notes say that the bank does not test","question_count":2} ],
  "questions": [ {"subject":"d3s2","concept":"kebab-id","type":"single|multi","stem":"...",
                  "options":[...],"correct":[...],"explanation":"...","mnemonic":"..."} ]
}
(No "id" field: ids are assigned at merge.)

Then run:  python source/gap/check_new.py source/gap/new_<tag>.json   and fix until it prints OK.

Reply with ONLY: the output path, the gap list (subject | area | #questions), and anything you
considered a gap but rejected as already covered or trivial (one line each, max 8 lines).
Be honest: if your segment is already well covered, return few gaps rather than padding.

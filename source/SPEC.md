# CCAR-P question-bank authoring spec

You are writing the question bank for ONE exam domain of a study aid for the
"Claude Certified Architect – Professional" (CCAR-P) exam. Output is a single JSON file.

## Source material (read what your domain needs, in full)
Notes text (extracted from the .docx/.pdf) lives in source/notes_txt/ ; the paths below are relative to it.
- guide.txt  = exam guide (blueprint, sample question style in section 8)
- 01.txt  Claude Platform & Solution Design   (domains 1, 2, parts of 3)
- 02.txt  Enterprise Integration & Production (domains 3, 4, and sizing/feasibility for 1)
- 03.txt  Responsible AI, Safety & Risk       (domain 5)
- 04.txt  Stakeholder Engagement, Lifecycle   (domain 6)  -- IGNORE everything between <NOT TESTED> and </NOT TESTED> (lines ~100-139) and any "Partner Track" / "Reuse potential" content. Do not write questions on demo design, joint scoping or objection categories.
- 05.txt  Team Enablement & Ops Productivity  (domain 7)
Every correct answer MUST be supported by these notes. Do not use outside knowledge to make an
answer correct. Do not invent facts, numbers or product behaviour not in the notes. Use the
notes' own terminology (e.g. "fail closed", "p95", "reversal cost", "coverage check at synthesis").

## Exam style (see guide.txt section 8 samples)
Scenario-led, architect-level judgement questions ("which change best...", "what is the most
likely first place to investigate", "which TWO..."). Mix: ~35% short recall/definition,
~65% scenario/application. Test the TRAPS the notes warn about (the "Why this broke" /
"Watch out for" / "What to Watch Out for" sections are rich trap sources).

## Output file
Write valid JSON (UTF-8, no comments, no trailing commas) to the path given in your task.
Top-level shape:

{
  "domain": <int 1-7>,
  "subjects": [
    {
      "id": "d1s1",                      // d<domain>s<n>
      "title": "short subject title",
      "learn": ["4-6 bullets: what will be tested for this subject (concrete facts, not vague)"],
      "traps": ["3-5 bullets: how the exam will try to trick you; start each with a short bold-able lead phrase followed by a colon"],
      "questions": [ ...at least 11 per subject... ]
    }
  ]
}

Question object:
{
  "id": "d1s1q01",
  "concept": "short-kebab-id of the underlying fact tested (e.g. 'retrieval-vs-live-state')",
  "type": "single" | "multi",
  "stem": "question text. For multi: end with 'Select TWO.' or 'Select THREE.' (state exactly how many)",
  "options": ["A text", "B text", "C text", "D text"],   // 4 options for single; 5 for multi (4 allowed for multi with 2 correct). Do NOT prefix with letters.
  "correct": [1],                      // 0-based indexes. single => exactly 1; multi => 2 or 3
  "explanation": "2-4 sentences: state the right answer and WHY, then briefly why the strongest distractor is wrong. Used when the student gets it wrong.",
  "mnemonic": "a punchy memory hook, <= 18 words (rhyme, acronym, or vivid image). Must encode the actual fact."
}

## Hard rules
1. Quantity: >= 11 questions per subject. About 25% of questions should be multi (select 2 or 3).
2. COVERAGE BY REPHRASING: within each subject, at least 4 concepts must be tested by TWO questions
   that ask about the same fact in a different way (different scenario, flipped framing, or
   asking for the wrong answer's reason). Give such pairs the SAME "concept" string.
   Every key fact in the notes for the subject should be tested at least once.
3. ANSWER LENGTH PARITY: correct options and distractors must be roughly the same word length
   (within ~25% of each other). The correct answer must NOT be systematically the longest or the
   most detailed. Distractors must be plausible, specific, and use real terms from the notes
   (typical mistakes an architect makes), not silly or obviously absurd.
4. POSITION: vary the position of correct answers; do not cluster on one index.
5. No "all of the above" / "none of the above" / "both A and B" options.
6. Stems must be self-contained. No references to "the notes" or "the module".
7. Mnemonics must be distinct from each other where concepts differ, and must not be generic
   ("remember to think carefully").
8. Do not copy long verbatim passages; paraphrase.
9. Keep each learn/traps bullet <= 35 words.

After writing the file, run this check (Python 3 is available) and fix any problems it reports:
  python "<scratchpad>\validate.py" "<your json path>"
Then reply with ONLY: the output path, number of subjects, number of questions, and anything you
were unsure the notes supported.

# Worked-example replacements: applied changes

Applied 2026-10-04 after approval of WORKED_EXAMPLE_REVIEW.md. Pre-change banks: backup_before_worked_examples/.

Post-verification fixes (independent check of all 102 new questions): d1s2q16, d1s3q21, d1s4q32 explanation/distractor wording; d1s6q26 reframed to Select TWO (volume + SLA, 02.txt:235); d1s6q27 keyed to 'must be reassessed' (02.txt:203); d2s1q16 explanation; d2s1q17 stem rewritten (unmanaged model choice, 05.txt:33); d5s6q20 and d7s2q19 concept re-tagged; d6s4q13 stem; d6s5q17 mnemonic; d7s2q17 option. Also d5s4q02 option now keys the retrieval corpus as a fairness entry point, and d3s5 traps[3] no longer says 'green dashboards'.

---

# Applied worked-example replacements: domain 1 (data/d1.json)

## Question replacements (30)

| Old id | New id | Type | Concept | New stem (first line) |
|---|---|---|---|---|
| d1s1q03 | d1s1q17 | single | properties-fail-silently | A team ships a system without designing around the four model properties. When one of those properties causes a problem in production, how is the gap most likely to come to light? |
| d1s2q03 | d1s2q15 | single | three-layers-independence | A design document fixes the entry point in its opening section and only identifies who the users are three sections later. Which architecture error does this show? |
| d1s2q08 | d1s2q16 | single | agent-vocabulary | An architecture team starts debating patterns without first agreeing what tools, subagents, hooks and the other primitives mean. What risk does this create? |
| d1s2q11 | d1s2q17 | single | primitive-jobs-parallel | A parent agent wants each of several independent research questions handled away from its own context, so the intermediate notes do not crowd it. Which primitive carries that job? |
| d1s3q04 | d1s3q15 | single | existing-systems-own-rules | A partner's eligibility decisions are already made by a rules table it maintains. In a new Claude workflow that reads free-text applications, who should own the eligibility decision? |
| d1s3q05 | d1s3q16 | single | model-unaware-of-staleness | Why is it risky to let the model act as the source of truth for a reference table that the business updates often? |
| d1s3q06 | d1s3q17 | multi | human-owner-role | When a request is decomposed across Claude, existing systems and humans, which TWO kinds of work belong in the 'what humans do' bucket? Select TWO. |
| d1s3q09 | d1s3q18 | single | deterministic-lookup-cost | A design sends every product-code lookup to Claude, even though a database query returns the same answer. What cost consequence should the architect expect? |
| d1s3q10 | d1s3q19 | multi | model-unaware-of-staleness | A team lets Claude answer from what it learned in training instead of querying the partner's system of record. Which TWO describe the resulting risk? Select TWO. |
| d1s3q11 | d1s3q20 | single | deterministic-rule-in-model | A team moves a validation rule out of a lookup table and into a prompt. Why do errors become harder to diagnose? |
| d1s3q12 | d1s3q21 | single | existing-systems-own-rules | A partner's database of record already returns each customer's account tier reliably. An engineer proposes having Claude infer the tier from the customer's emails instead, to save an integration. What is the best response? |
| d1s4q03 | d1s4q28 | single | workflow-subpatterns | Each chapter of a long technical manual is reviewed in its own simultaneous model call, and the findings are combined into one report. Which workflow sub-pattern is this? |
| d1s4q04 | d1s4q29 | single | workflow-subpatterns | Generated code is run against a test suite; failures are fed back and the code is revised until the tests pass or a retry limit is reached. Which workflow sub-pattern is this? |
| d1s4q05 | d1s4q30 | single | workflow-subpatterns | An intake service receives a mix of invoices, signed agreements and identity scans, and a classifier sends each kind to a different handler. Which workflow sub-pattern is this? |
| d1s4q08 | d1s4q31 | single | agent-when-justified | A team can write down every step of a process in advance but wants an agent because the work 'feels open-ended'. What should the architect recommend? |
| d1s4q12 | d1s4q32 | single | pattern-delegation-lens | When the delegation lens is applied to the choice of pattern itself, what decides whether an autonomous agent is appropriate? |
| d1s4q15 | d1s4q33 | single | chaining-subpattern | The first call transcribes a recorded meeting, the second extracts the decisions from that transcript, and the third formats them into a status update. Which workflow sub-pattern is this? |
| d1s4q26 | d1s4q34 | single | control-flow-location | Why do non-deterministic failures concentrate in the agent pattern in production? |
| d1s4q27 | d1s4q35 | single | control-flow-location | Operations must be able to reconstruct which step made each decision in a process whose steps are known in advance. Which pattern fits, and why? |
| d1s5q02 | d1s5q19 | multi | fanout-pattern | An orchestrator splits a work item too large for one context into independent units, with one subagent per unit. Which TWO benefits does this fan-out shape deliver? Select TWO. |
| d1s5q04 | d1s5q20 | single | coverage-check | Which multi-agent failure is the most dangerous, and what guards against it? |
| d1s5q05 | d1s5q21 | multi | coverage-check | Which TWO practices stop a fan-out from presenting incomplete work as complete? Select TWO. |
| d1s5q08 | d1s5q22 | single | rag-live-state | An assistant's answers about account balances change after each index refresh and sometimes contradict the database. What is the correct fix? |
| d1s5q13 | d1s5q23 | single | one-vs-several-patterns | A system combines a RAG layer for documentation questions with a document extraction pipeline, and the team evaluates it with one end-to-end eval set. What is the main risk? |
| d1s6q02 | d1s6q24 | single | scoping-sequence | An architecture handles typed forms reliably but not handwritten ones. Where should that limit be recorded? |
| d1s6q13 | d1s6q25 | single | constraints-before-verdict | A prototype works well and the business owner is eager to proceed. Why should the architect hold off on confirming feasibility? |
| d1s6q14 | d1s6q26 | multi | constraints-before-verdict | Which THREE constraints must be gathered as inputs before a feasibility verdict is issued? Select THREE. |
| d1s6q16 | d1s6q27 | single | feasible-as-scoped-assumptions | A design was judged feasible as scoped on the stated assumption that every input arrives in English. The business now wants to add three more languages. How should the verdict be viewed? |
| d1s6q19 | d1s6q28 | single | sizing-volume-and-sensitivity | An architect is sizing an invoice-processing workflow before any code is written. Where should the call-volume figure come from? |
| d1s6q23 | d1s6q29 | single | caching-cost-model | A sizing model assumes prompt caching will cut input cost for a long, stable system prompt, but requests arrive only about every 20 minutes. What should the architect expect? |

## Cards rewritten (18)

- d1s1 traps[0]
- d1s2 learn[5]
- d1s2 traps[0]
- d1s2 traps[4]
- d1s3 learn[2]
- d1s3 learn[4]
- d1s3 traps[1]
- d1s3 traps[2]
- d1s3 traps[3]
- d1s3 traps[4]
- d1s4 learn[5]
- d1s4 traps[2]
- d1s5 learn[5]
- d1s5 traps[0]
- d1s5 traps[1]
- d1s5 traps[2]
- d1s6 learn[5]
- d1s6 traps[1]

## Other trims / renames in kept questions

- d1s2q07 stem: removed 'from the notes' ("Which principle does this violate?").
- d1s3q07 stem: removed 'the decomposition module builds toward'; now asks for the right framing when decomposing a request.
- d1s4q07 stem: removed 'according to the notes'.
- d1s5q09 stem: removed 'from the notes'.
- Concept renames: demo-not-determinism (q03) -> properties-fail-silently; priority-rule-engine / coverage-live-lookup / draft-vs-send / threshold-rule-failure -> existing-systems-own-rules, model-unaware-of-staleness, human-owner-role, deterministic-lookup-cost; governance-gap -> pattern-delegation-lens; agent-audit-gap -> control-flow-location; contracts-scoping-call -> constraints-before-verdict; context-window-tier -> caching-cost-model.
- d1s2 traps[0] rewrite shortened from the approved text to end 'choose it for the user and the work' (kept to the 01.txt:42 rule; no example particulars).
- Full scan of remaining stems/options/explanations/mnemonics/cards for example particulars (five clean runs, bank branch staff, five meanings of agent, claims triage, GBP 5,000 / 41 of 14,000, twelve supplier contracts, complaint rubric, support-ticket paths, four trace shapes, disbursement audit, 50-section / 48 reviewed, order 88412, 20 pages, 800/300/30s, 1,000 calls, 80% tail): none left. Borderline-kept items left as approved (d1s1q02, q12, q15; d1s2q04, q07; d1s3q07, q08; d1s4q13, q16, q22; d1s5q09, q11, q14, q16; d1s6q04, q06, q10).

## Notes

- Type changes per approved flags: d1s5q02 single -> multi (d1s5q19), d1s5q05 Select THREE -> Select TWO (d1s5q21), d1s6q14 single -> multi (d1s6q26). Multi counts per subject are unchanged or higher; d1s5 and d1s6 each have one fewer single.
- Pre-existing, not touched: d1s6 learn[1] (44 words) and learn[4] (36 words) exceed SPEC's 35-word card guideline (validator does not check it).
- validate.py: questions=112 subjects=6 positions(single)={0: 23, 1: 22, 3: 21, 2: 25}; correct-is-longest 36%; OK

---

# Applied worked-example replacements: domain 2 (data/d2.json)

## Question replacements (same array position, new ids)

| Old id | New id | Concept | Type | New stem (first line) |
|---|---|---|---|---|
| d2s1q05 | d2s1q14 | no-eval-no-rollback | single | A team plans to change the model behind a live assistant without building an eval set, intending to 'watch for complaints'... |
| d2s1q06 | d2s1q15 | eval-gate-three-parts | single | A team gates a model change using a few dozen hand-picked showcase prompts, a rubric-based model grader, and a pre-agreed delta threshold. Which part is weakest? |
| d2s1q07 | d2s1q16 | tier-decision-explicit | multi | Which TWO statements about an eval set's role in choosing a model tier are accurate? Select TWO. |
| d2s1q08 | d2s1q17 | tier-decision-explicit | single | An architecture document specifies prompts and tools for every pipeline step but names no model tier for any of them... |
| d2s1q09 | d2s1q18 | swap-is-release | single | An engineer wants to change the model ID in a configuration file and push it without review, calling it 'a one-line change'... |
| d2s1q13 | d2s1q19 | thinking-measured-gap | single | An extraction step misses its accuracy target in evals run without extended thinking, and the prompt has not yet been revised... |
| d2s2q08 | d2s2q18 | strategies-combine | multi | When designing a context system, which TWO pairings of design question and context layer are correct? Select TWO. |
| d2s2q09 | d2s2q19 | strategies-combine | single | A design review asks a team to name 'the one context strategy' for a new production assistant... |
| d2s2q10 | d2s2q20 | monolithic-creep | single | A multi-turn tool loop resends its entire growing history on every call. Per-call spend climbs steadily... |
| d2s4q02 | d2s4q17 | cache-ttl-frequency | multi | Which TWO factors should drive the choice of cache lifetime (TTL) for a reusable prompt? Select TWO. |
| d2s4q06 | d2s4q18 | cache-economics | single | Cache writes cost more than standard input and cache reads cost less. Which workload produces the largest caching savings? |

## Cards rewritten
- d2s1 learn[2], learn[3], learn[4]; traps[2]
- d2s2 learn[4]; traps[3]
- d2s4 learn[1]; traps[0]

## Other trims / renames
- d2s1 traps[0] (borderline): dropped "because the demo must land" case hook -> "defaulting to the most capable model without eval evidence".
- d2s1q04 explanation: removed "does not negotiate with itself" (downgrade-case phrase).
- d2s4q15 explanation: "(10% in the example given)" -> "(verify current rates on the pricing page)".
- d2s4q03 concept renamed `cache-never-hit` -> `static-before-dynamic` (was named after the example).
- Concepts removed with their questions: opus-overrun-mechanisms, per-step-tiering, rollback-criterion-partial, cache-never-hit.
- Full-bank scan (stems, options, explanations, mnemonics, cards, incl. unflagged d2s3) for 7x/overrun, 0.85/0.94/0.71/0.74, 250 docs, 4,000/80,000/turn 30, document type/stratified, 10%, 88412, routing classifier, 71%/940 ms, coding agent: no leftovers.

## Counts per subject (after)
- d2s1: 13 q (2 multi), repeated concepts: model-start-sonnet, eval-gate-three-parts, tier-decision-explicit, thinking-measured-gap
- d2s2: 17 q (5 multi), repeated: budget-ceiling, measure-usage, strategies-combine, compaction-lossy, progressive-breakdown
- d2s3: 13 q (unchanged)
- d2s4: 16 q (3 multi, was 2), repeated: cache-ttl-frequency (x3), cache-economics, consistency-window, library-vs-skill

validate.py: `questions=59 subjects=4 positions(single)={3: 13, 0: 10, 1: 13, 2: 9}`, correct-is-longest 27%, `OK`.

---

# Applied: domain 3 (data/d3.json)

## Question replacements (same array position, new ids)

| Old id | New id | Type / concept | New stem (first line) |
|---|---|---|---|
| d3s2q09 | d3s2q18 | multi / retrieval-vs-live-state | Which TWO symptoms suggest that a system is using retrieval where a tool call belongs? Select TWO. |
| d3s2q11 | d3s2q19 | single / context-engineering | A team that built a successful RAG assistant over internal documentation proposes reusing the same design for a new assistant. What should the architect check first? |
| d3s3q01 | d3s3q15 | single / server-side-identity | In a Claude integration that scopes answers to each user's permissions, where and when should the user's identity be verified? |
| d3s3q09 | d3s3q16 | single / data-minimisation | Which test should decide whether a particular data field is placed in the context window of a Claude call? |
| d3s3q12 | d3s3q17 | single / redact-before-call | A team plans to launch its Claude integration without a PII redaction step and add one 'once usage settles'. What is the main problem with deferring it? |
| d3s5q14 | d3s5q18 | single / mcp-reuse | An internal ticketing tool must be callable from Claude.ai, Claude Code and a partner-facing app. What is the right choice? |
| d3s5q16 | d3s5q19 | single / shaping-layer-placement | A team's CLAUDE.md now holds full step-by-step procedures for onboarding a new service, rotating test fixtures and preparing a hotfix... |

Sources: 01.txt:303 (q18), 01.txt:310 (q19), 02.txt:340-341 (s3q15), 02.txt:345 (s3q16), 02.txt:356 (s3q17), 01.txt:616 (s5q18), 01.txt:665 (s5q19).
d3s5q18 and d3s5q19 keep their options/answer; only stem (and q19's explanation) were reworded.

## Cards rewritten
- d3s2 learn[3] (retrieval for stable reference material; live state needs a tool call)
- d3s3 traps[0] (user-asserted role, no "As a senior manager" quote)
- d3s3 traps[2] (convenience data, no SSN/insurance ID)

## Other trims / renames
- Concept slugs removed: `patient-intake-ssn` (both questions replaced), `similarity-not-truth` (example-only lesson, replaced).
- d3s5q17: distractor "A commit-push-PR flow used occasionally..." -> "A dependency-upgrade procedure used occasionally..." (borderline_kept suggestion).
- d3s5q19 explanation: dropped "such as a release flow or a schema migration".
- References to "the notes" removed: d3s5q08 stem ("What does the notes' standard imply?" -> "Which standard should guide the decision?"), d3s4q07 stem ("matches the notes" -> "is correct"), explanations of d3s1q06, d3s4q11, d3s4q16.
- Other borderline_kept items (d3s2q10, d3s2q12, d3s2q03, d3s3q04, d3s3q10, d3s1q05, d3s4q14) checked; no example particulars, left as is.

## Notes
- d3s2: single count 13 -> 12, multi 4 -> 5 (approved replacement d3s2q18 is multi).
- d3s3 still has exactly 4 repeated concepts (server-side-identity, least-privilege-removal, data-minimisation, separate-keys-per-tenant).

validate.py: `questions=95 subjects=5 positions(single)={0: 19, 1: 19, 2: 18, 3: 19}` / `correct-is-longest in 40%` / `OK`

---

# Applied: domain 4 (data/d4.json)

## Replaced questions (same array position, new ids)

| Old id | New id | Type | Concept | New stem (first line) |
|---|---|---|---|---|
| d4s1q07 | d4s1q22 | single | threshold-before-data | A team's first working build scores 91% on field accuracy, and the lead proposes adopting 91% as the pass mark. What is the flaw in this approach? |
| d4s1q08 | d4s1q23 | multi (was single) | adversarial-inputs | A golden dataset was assembled from the tidiest inputs the team had on hand... Which TWO changes would make the scores meaningful? |
| d4s1q09 | d4s1q24 | single (was multi) | stale-eval | At which point is a production Claude system at the highest risk of a regression slipping through undetected? |
| d4s1q10 | d4s1q25 | single | eval-gate-every-change | A team plans to change only its retrieval configuration and argues the eval suite exists to gate model swaps... |
| d4s1q13 | d4s1q26 | single | threshold-before-data | A team is about to run its eval set against a proposed model swap. When should it set the delta threshold...? |
| d4s2q04 | d4s2q19 | single | token-skew | A team sizes monthly cost from the mean token count of its sample, in which most inputs are short but a few are very long... |
| d4s2q11 | d4s2q20 | single | fallback-chain (was reliability-placement) | Which statement about fallback chains in a production Claude system is accurate? |
| d4s2q16 | d4s2q21 | single | batch-api | A nightly job summarizes protected health records and has no latency requirement... (discount figure removed everywhere) |
| d4s3q01 | d4s3q15 | single | ab-hypothesis | Which hypothesis is ready for an A/B test of a prompt change? |
| d4s3q02 | d4s3q16 | single | ab-hypothesis | A team starts an experiment on a revised system prompt with no written hypothesis, planning to see what improves... |
| d4s3q09 | d4s3q17 | multi (was single) | significance-vs-value | A treatment beats control on the primary metric with statistical significance. Which TWO questions should be answered...? |
| d4s3q11 | d4s3q18 | multi | experiment-preregistration (was fifty-session) | A team is preparing an A/B test of a revised system prompt. Which THREE should be fixed before the test starts? |
| d4s4q05 | d4s4q16 | multi (approved as single) | anomaly-thresholds | A team wants alerting that warns it when users start hitting SLA breaches and that also catches gradual change in model outputs. Which TWO...? |
| d4s4q13 | d4s4q17 | single | translation-layer | A finance sponsor tracks the average number of days to pay a supplier invoice, while the team monitors latency, task success and error rate... |

Type notes: d4s1q08 went from single to multi so that d4s1 keeps 5 multi questions after q09 became single. d4s4q05 stays multi (it was approved as single) so that d4s4 keeps 3 multi questions; it now tests the p95-past-SLA threshold alert together with distribution comparison for drift. d4s3 follows the approved types, so it goes from 12 single / 2 multi to 11 single / 3 multi.

## Cards rewritten
- d4s1 traps[4] (mean-score comfort)
- d4s2 learn[5] (pinning / Batch API, 50% figure removed)
- d4s2 traps[3] (untested failure, 529 quote removed)
- d4s3 learn[3] (significance vs practical value, 30% figure removed)
- d4s3 traps[0] (vague hypothesis, quoted counterexample removed)
- d4s3 traps[2] (underpowered wins, 50-session figures removed)
- d4s4 learn[3] (alerts, 150%/7-day figure removed)

## Other trims and renames
- d4s3q06: the distractor that said cost would degrade "by about thirty percent" now reads "...such as cost or latency degrade in the treatment arm".
- d4s4q09: the distractor about refreshing "the weekly 7-day average used by the cost alert" now reads "refresh the golden dataset with this month's inputs".
- d4s2q07: the figures changed from 600 ms median / 800 ms SLA to 650 ms / 900 ms. 800 ms was the target in the Opus overrun worked example. The options were updated to match.
- Concepts renamed: fifty-session became experiment-preregistration (d4s3q18). On d4s2q20, reliability-placement became fallback-chain, as approved.
- A full scan of the remaining stems, options, explanations, mnemonics and cards found no other worked-example particulars: no claims, contract, 50-session, 30%, 150%, 529, customer-service KPIs, Sonnet/Haiku, 250 or 0.85 references. The only hit was the generic "patient user" in d4s2q01.

## validate.py
questions=68 subjects=4 positions(single)={3: 13, 2: 12, 1: 15, 0: 13}
correct-is-longest in 31% of questions (ideal ~25-45%)
OK

---

# Applied: domain 5 (data/d5.json)

Script: `apply_d5.py` (scratchpad). Bank still 110 questions; validate.py: OK.

## Replaced questions (same array position)

| Old id | New id | Type | Concept | New stem (first line) |
|---|---|---|---|---|
| d5s1q04 | d5s1q17 | single | draw-layer-boundary | Before adding any controls to a new Claude deployment, why should the architect first establish what the model's training already covers? |
| d5s1q06 | d5s1q18 | single | instructions-not-enforcement | Only verified account holders may change a delivery address through an assistant's update_address tool. Which control actually enforces this rule? |
| d5s2q05 | d5s2q28 | single | guarded-path-order | Which sequence describes the full guarded request path? |
| d5s3q11 | d5s3q15 | single | out-of-scope-baseline | During an audit, a skill advertised as a unit converter is found reading files in the user's home directory and a stored credential file. How should this be classified? |
| d5s4q06 | d5s4q17 | multi | four-entry-points | A team rebalanced its retrieval corpus, yet outcomes still lean toward one group. Which TWO remaining entry points could still carry the skew? Select TWO. |
| d5s4q09 | d5s4q18 | single | cant-reconstruct | A team wants to give affected users explanations for automated decisions, but it stores only each final response. What is the gap? |
| d5s4q11 | d5s4q19 | single | fairness-architectural | Input and output screening pass every response a system produces. Why does that not show the system treats people fairly? |
| d5s4q13 | d5s4q20 | single | audience-slices | A person affected by an automated decision asks why it went against them. What must the system have captured to answer well? |
| d5s4q14 | d5s4q21 | multi | discernment | Which TWO statements about Discernment applied to fairness are correct? Select TWO. |
| d5s5q10 | d5s5q21 | single | volume-routing-risk | To save reviewer time, a team sends only its highest-volume workflow to human review, while a low-volume workflow that closes customer accounts irreversibly runs with no gate. Which risk does this show? |
| d5s6q10 | d5s6q18 | single | unowned-control-risk | A compliance register lists a control for every obligation, but none has a named owner or an evidence artifact. What is the main risk? |
| d5s6q12 | d5s6q19 | single | governance-spans-owners | Why is turning each obligation into a control with an owner and a living evidence artifact more complex than choosing a compliant entry point? |
| d5s6q13 | d5s6q20 | single | evidence-live | For the obligation that decisions be reconstructable on demand, a team offers a design document describing its decision log. What would a reviewer accept instead? |

## Cards rewritten
- d5s1 learn[4] (layer cost/complexity/drift, replaces cross-unit postmortem card)
- d5s4 learn[3] (cannot reconstruct = cannot explain; Discernment + transparency record)
- d5s5 traps[1] ("Half a fix": volume and missing context fail independently)
- d5s6 traps[4] (Residency copies: validate logs, caches, monitoring, retention paths)
- d5s4 traps[0] (optional tighter rewrite applied: provider evals cannot see your corpus, framing, examples or routing)
- d5s4 traps[4] (optional tighter rewrite applied: cannot replay, cannot reliably explain)

## Other trims / renames
- d5s3q04 explanation: removed the "formatting skill that phones home / summarizer writing to disk" illustration; now generic.
- d5s6q09 explanation: removed "The residency story shows..."; now a general drift sentence.
- d5s4q03 option 2 and d5s4q10 option 0: "applicant" (credit-example framing) -> "affected user".
- d5s5q12 concept renamed queue-two-failures -> volume-routing-risk (pairs with new d5s5q21; both test 03:183/195).
- Concepts dropped with replaced questions: corpus-skew, single-filter-coverage now single-use (d5s2q11), cannot-enforce-unseen-rule single-use (d5s1q09), residency-dataflow single-use (d5s6q06), prefilter-not-proof single-use (d5s6q01). Every subject still has >= 4 repeated concepts.
- Type change: d5s4 slot q06 single -> multi (as approved); d5s4 now 4 multi / 12 single.
- Final scan for worked-example particulars (business units, 400 items, issue_refund, credit/applicant, second region, phones home, model's job quote, postmortem): none left.

validate.py: `questions=110 subjects=6 positions(single)={1: 25, 2: 21, 0: 23, 3: 20}` / `correct-is-longest in 26% of questions` / `OK`

---

# Applied: domain 6 (flags_d6_b.json)

Bank: `source/data/d6.json` (backup in `source/review/backup_before_worked_examples/d6.json`). 89 questions, unchanged per-subject type counts (s1 18/5, s2 11/3, s3 20/4, s4 9/3, s5 14/2 single/multi).

## Replaced questions (same array position)

| Old id | New id | Type | Concept | New stem (first line) |
|---|---|---|---|---|
| d6s1q07 | d6s1q24 | single | translation-table-structure | Why does the discovery translation table hold exactly one row per discovery item? |
| d6s1q08 | d6s1q25 | single | unstated-constraint-cost | A sponsor wants discovery cut to one short call so the team can start building sooner. What is the architect's best response? |
| d6s1q09 | d6s1q26 | single | discovery-purpose | Which outcome should an architect leave a discovery call with? |
| d6s1q12 | d6s1q27 | single | must-prove-obligation | An architect is running discovery for a consumer lending workflow. When should the evidence the deployment must produce for regulators be identified? |
| d6s1q13 | d6s1q28 | multi (3) | listen-translate-write | In the discovery filter, the second step translates the stakeholder's business goal into which THREE things? |
| d6s1q17 | d6s1q29 | multi (2) | preference-hides-constraint | After a discovery call, which TWO items in the record are ready for the design to be built against? |
| d6s1q18 | d6s1q30 | multi (3) | preference-hides-constraint | A stakeholder says the new tool must be 'fast and easy'. Which THREE follow-up questions help turn this into design constraints? |
| d6s1q20 | d6s1q31 | single | translation-table-structure | A stakeholder says all users sit in one country, but nobody has confirmed this with the data owner. How should the discovery record handle the statement? |
| d6s1q23 | d6s1q32 | single | listen-translate-write | Why should items surfaced in a discovery call be written down before the conversation moves on? |
| d6s2q13 | d6s2q15 | multi (2) | context-vs-retrieval-caching | On the tradeoff translation map, a team chooses a larger context window per call over retrieval. Which TWO costs does the map list if this choice proves wrong and must be reversed? |
| d6s2q14 | d6s2q16 | single | false-alignment | When is it most important for an architect to name the reversal cost explicitly in a tradeoff presentation? |
| d6s3q01 | d6s3q25 | single | drift-without-monitoring | An internal policy Q&A tool has been live for a year with no feedback loop. Which pattern of degradation should the architect expect? |
| d6s3q12 | d6s3q26 | single | loop-vs-observability | Observability shows a one-off latency spike, a sustained eval-score decline and an intermittent tool error. Why can't the team simply act on each signal as it arrives? |
| d6s3q13 | d6s3q27 | single | monitoring-not-loop | A team has live dashboards and configured alerts and concludes that stakeholder feedback is therefore covered. What is missing to make this a feedback loop? |
| d6s3q20 | d6s3q28 | single | signal-noise-judgment | Which part of running a feedback loop can observability tooling NOT do for the architect? |
| d6s3q21 | d6s3q29 | single | loop-cost | A sponsor questions the ongoing Architect time a feedback loop needs after launch. Which justification is strongest? |
| d6s4q10 | d6s4q13 | single | rationale-why-not-what | Why is design rationale the part of architecture documentation most often skipped? |
| d6s4q11 | d6s4q14 | single | rationale-why-not-what | When should the decision, the rejected alternatives and the tradeoff each resolved be written down? |
| d6s5q12 | d6s5q17 | single | outcome-document-fields | Whom is a customer outcome document chiefly written for, and what must it let them do? |

Deviations from the sketches (to keep per-subject multi counts):
- d6s1q29 (was sketched single) is multi Select TWO: confirmed p95 target + per-interaction cost ceiling as the testable, bounded constraints (04:14, 04:19).
- d6s2q15 (was sketched single) is multi Select TWO: both halves of the reversal-cost cell (04:86); distractors are the other map rows' reversal costs.
- Concept `diagram-lost-why` (from the sketches for d6s4q13/q14) renamed `rationale-why-not-what`, since it was named after the postmortem's "diagram showed what and lost the why".

## Cards rewritten
- d6s1 learn[1], learn[3], learn[4]; traps[2], traps[3]
- d6s2 learn[4]; traps[1]
- d6s3 traps[1]
- d6s4 traps[0], traps[3]
- d6s5 traps[4]

## Other trims / renames in kept questions
- d6s1q21 explanation: dropped "in the hospital case the stakeholder agreed readily" (explanation_trims); distractor "expect a prototype within a week" -> "expect a working prototype immediately" (echoed the hospital case's "prototype next week").
- d6s3q23 explanation: "repeats the 90-day drift failure..." -> "leaves slow drifts with no trigger, so signals exist but nothing decides they matter" (explanation_trims).
- d6s1q01 explanation: replaced the seamless follow-up particulars ("re-entry") with the general 04:21 wording (latency budget, uninterrupted handoff, failure state hiding internals).
- d6s1q14 stem: numbers changed from "two-second / three cents / 50,000" to "three-second p95 / two cents / 80,000" (moved away from "a second or two" and the CTO/CFO figures).
- d6s3q02 mnemonic: "Sensors measure; the control room decides" (train-station analogy) -> "Observability measures; the feedback loop decides."
- d6s3q08 explanation: removed "the notes single out cost".
- d6s5q07 stem (borderline_kept suggestion): "a Bedrock endpoint set up for a regulated data path" -> "a cloud-provider entry point set up for one regulated workflow".
- Concepts removed with their questions: rule-engine-routing, hitl-quick-check, healthcare-proof-obligation, hospital-missed-constraints, seamless-translation, escalation-order, diagram-lost-why.

Final scan: no hospital/clinician/PHI/CTO/four-cents/90-day/week-12/financial-services/40,000 particulars remain. Kept per flags: "claims" as a generic industry word (s1q02, s3q06), "six weeks" (s1q11), CFO distractor (s5q16).

## validate.py
```
questions=89 subjects=5 positions(single)={1: 22, 3: 18, 2: 18, 0: 14}
correct-is-longest in 30% of questions (ideal ~25-45%)
OK
```

---

# Applied: domain 7 (data/d7.json)

## Question replacements (same array position, same subject)

| Old id | New id | Concept | New stem (first line) |
|---|---|---|---|
| d7s1q02 | d7s1q15 | rollout-champions | An organization wants Claude Code adopted across several engineering teams. Which rollout approach is most likely to succeed? |
| d7s1q14 | d7s1q16 | team-setup-cost (was mass-rollout-failure) | A manager questions spending time on a shared configuration, a rollout plan and skills packaging before developers start using Claude Code. Which response best reflects the cost trade-off? |
| d7s2q07 | d7s2q17 | plugin-governance | A data-science group needs a shared analysis procedure that only its members receive, updated from a connected repository, with a way back if an update misbehaves. Which distribution choice fits best? |
| d7s2q08 | d7s2q18 | shared-asset-liability (was release-notes-failure) | A team's shared Claude Code configuration is edited in place and pushed to every developer, with no version history and no way to revert. What is the biggest risk of this setup? |
| d7s2q09 | d7s2q19 | plugin-group-access (was release-notes-failure) | A legal team has three related Skills that only its own members should be able to use. How should the Architect distribute them? |
| d7s3q11 | d7s3q18 | checklist-dimensions (was merge-unexplained) | A team's checklist for AI-generated changes covers correctness, security and maintainability. Which item adds the missing fourth dimension? |
| d7s4q09 | d7s4q14 | runbook-purpose (was gradual-quality-drop) | An Architect could resolve a recurring incident herself in minutes. What is the durable fix? |
| d7s4q10 | d7s4q15 | slow-degradation-risk (was drift-green-dashboards) | For a team that owns a production deployment, what is the biggest operational failure mode to guard against? |

All replacements are `single`, as were the originals; type counts per subject unchanged.

## Cards rewritten
- d7s1 learn[1] (champion rollout, no headcounts/durations)
- d7s1 traps[0] (all-hands switch-on)
- d7s2 traps[0] (unversioned shared asset)
- d7s4 traps[1] (slow degradation)

## Other trims / renames
- d7s1q07 stem: "release-notes skill" -> "commit-message skill"
- d7s2q13 stem: "release-notes skill" -> "migration-checklist skill"
- d7s2q10 stem: dropped "Why does the guidance call..." -> "Why is a shared Skill with no version and no rollback a liability for a team?"
- d7s3q12 concept: merge-unexplained -> judgment-erosion
- d7s4q04 distractor: "retrieval index kept pace with the growing corpus" -> "Check whether retrieval drift set in as the corpus has grown"
- d7s4q11 distractor: "corpus is growing without index updates" -> "Retrieval drift as the corpus grows"
- d7s4q13 distractor: "indexed corpus" -> "corpus"
- Final scan: no remaining 200-person / four departments / two weeks / 45-minute / forty / release-notes / flat bundle / green dashboards / quarter / afternoon / index particulars.

## Validate
`questions=60 subjects=4 positions(single)={1: 13, 2: 14, 0: 10, 3: 10}`; correct-is-longest 20%; `OK`

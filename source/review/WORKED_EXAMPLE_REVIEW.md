# Worked-example review: flagged items

Generated for approval before any bank is changed. **102 questions** to remove and replace, **55 learn/trap cards** to rewrite, 80 borderline items kept (collapsed per domain).

Rule applied: remove questions that test a worked example's details or reuse its setup; replace each with a question on a general fact/guidance the notes state outside the example (source line cited). Replacements may use a short, newly invented scenario. Each replacement stays in the same subject, gets a new id (removed ids are retired, not reused), and kept questions whose explanations mention an example get that phrase trimmed.

**How to respond:** approve all, or list ids to keep as-is / drop without replacement / change.


## Domain 1: Solution Design  (30 questions, 18 cards)

### Questions to remove and replace

**d1s1q03** · _recall_ · example: `01/reconciliation-nondeterminism`  
> A team saw a reconciliation demo produce identical categorizations five times and shipped with no output checks. In week two, re-processing the same statement gave a different category. What is the root cause?  
> ✔ The model was treated as deterministic when it is not

- Why: Recreates the five-clean-demo-runs reconciliation pipeline and its week-two drift.
- **Replace with principle:** The properties do not announce themselves: a system not designed around them throws no error, it drifts quietly, and the gap is found in an audit or by an angry user rather than by the system. (L20 non-determinism is already covered by d1s1q04 and trap T0, so use this under-tested risk statement.) (`01.txt:30`)
- Stem sketch (single, concept `properties-fail-silently`): A team builds without considering the four properties. How do the notes say the resulting gap usually comes to light? Correct: it drifts quietly with no error and is found in an audit or by a user, not by the system. Distractors: the API returns an error; monitoring alerts immediately; the build fails in testing.

**d1s2q03** · _reused-setup_ · example: `01/retail-banking-claude-code-layer-collapse`  
> A proposal puts Claude Code in front of retail bank branch staff because the same model sits under every entry point. What went wrong?  
> ✔ The entry point was picked without naming the user

- Why: Re-creates the retail-bank-branch-staff Claude Code proposal and its 'it's all Claude' justification.
- **Replace with principle:** An entry point chosen before the user is named is a common, avoidable error, usually traceable to collapsing the three layers; the entry point is chosen for the user and the work. (`01.txt:49`)
- Stem sketch (single, concept `three-layers-independence`): A design document fixes the entry point in its first section and only identifies who the users are three sections later. Which error is this? Correct: choosing the entry point before naming the user, a symptom of collapsing the layers. Distractors: wrong delivery route; wrong build-time interface; wrong model tier.

**d1s2q08** · _reused-setup_ · example: `01/agent-word-five-meanings`  
> In a design review, five people each hear 'we'll use an agent' as a different architecture, and discussion stalls. What does the notes' remedy emphasise?  
> ✔ Establish a shared vocabulary of the primitives first

- Why: Re-creates the review where five people heard five meanings of 'agent' and the discussion stalled.
- **Replace with principle:** Risk of no shared vocabulary: teams cannot effectively communicate because they do not agree on what the parts are; naming the primitives once makes later patterns combinations of known parts. (`01.txt:70`)
- Stem sketch (single, concept `agent-vocabulary`): Direct question: what risk do the notes attach to skipping a shared primitive vocabulary before pattern work? Correct: the team cannot communicate effectively because it does not agree on what the parts are. Distractors: higher token cost per request; slower delivery-route approval; weaker eval coverage.

**d1s2q11** · _reused-setup_ · example: `01/fan-out-large-work-item`  
> An orchestrator must audit 200 independent documents, each in a clean context, running concurrently. Which primitive carries that job?  
> ✔ Subagents, handing scoped sub-tasks to separate contexts

- Why: Reuses the fan-out example's '200 documents' audited by an orchestrator in clean, concurrent contexts.
- **Replace with principle:** Subagents hand a scoped sub-task to a separate context so work runs in isolation or in parallel (test the isolation angle; parallel subagent use is already tested by d1s2q14). (`01.txt:57`)
- Stem sketch (single, concept `primitive-jobs-parallel`): A parent agent wants each of several independent research questions handled away from its own context so their intermediate notes do not crowd it. Which primitive carries that job? Correct: Subagents. Distractors: Hooks, Skills, MCP.

**d1s3q04** · _recall_ · example: `01/claims-triage-decomposition`  
> In the claims triage scenario, the partner already maintains a rule that defines claim priority. How should the architect assign 'decide priority'?  
> ✔ Claude calls the rule engine, and the existing system decides

- Why: Asks how 'decide priority' is assigned 'in the claims triage scenario'.
- **Replace with principle:** Existing systems own anything the partner has already paid to make reliable (order-status service, policy engine, rules table, database of record); the model should not replace them. (`01.txt:82`)
- Stem sketch (single, concept `existing-systems-own-rules`): A partner's eligibility decisions are already made by a rules table it maintains. In a new Claude workflow, who should own the eligibility decision? Correct: the existing rules table, with Claude calling or consuming it. Distractors: Claude decides from the request text; a human reviews every case; a fine-tuned model replaces the table.

**d1s3q05** · _recall_ · example: `01/claims-triage-decomposition`  
> Why should policy coverage in the claims triage design come from the live coverage system rather than from Claude?  
> ✔ Coverage tables change and the model cannot know when its version went stale

- Why: Asks why policy coverage 'in the claims triage design' comes from the live system.
- **Replace with principle:** The model has no reliable way to know when its information is out of date and will not flag the gap; when it becomes the source of truth instead of the partner's system, authoritative answers drift quietly with no error or warning. (`01.txt:102`)
- Stem sketch (single, concept `model-unaware-of-staleness`): Why is it risky to let the model act as the source of truth for a reference table the business updates often? Correct: it cannot tell when its information went stale and will not flag it, so answers drift without errors. Distractors: tables never fit the context window; model calls cost more than queries; the model refuses table lookups.

**d1s3q06** · _recall_ · example: `01/claims-triage-decomposition`  
> In the claims triage scenario, how should 'email the adjuster' be split? Select TWO.  
> ✔ The email system performs the actual sending step; Claude drafts the message for the adjuster

- Why: Asks how 'email the adjuster' should be split 'in the claims triage scenario'.
- **Replace with principle:** What humans own: the judgment calls, the exception paths, the approvals, the moments where being right matters more than being fast. (`01.txt:84`)
- Stem sketch (multi, concept `human-owner-role`): Which TWO kinds of work belong in the 'what humans do' bucket? Select TWO. Correct: approvals; exception paths/judgment calls where being right matters more than fast. Distractors: high-volume summarization; database-of-record lookups; drafting routine replies.

**d1s3q09** · _recall_ · example: `01/senior-adjuster-threshold-misroute`  
> A rule requiring senior review above 5,000 pounds was moved from an SQL check into a Claude prompt. Of 14,000 claims, 41 were misrouted. What did all 41 share?  
> ✔ The amount appeared in prose, such as 'around five thousand pounds'

- Why: Asks what the 41 of 14,000 misrouted over-5,000-pound claims shared.
- **Replace with principle:** Cost of routing deterministic lookups to Claude: you pay the model to do work a database query or rules table could do for a fraction of the cost, and across thousands of requests it adds up fast. (`01.txt:100`)
- Stem sketch (single, concept `deterministic-lookup-cost`): A design sends every product-code lookup to Claude even though a database query returns the same answer. What cost consequence do the notes describe? Correct: paying model rates for work a query or rules table does for a fraction of the cost, compounding over thousands of requests. Distractors: lookups exceed the context window; caching becomes impossible; latency drops.

**d1s3q10** · _example-only-lesson_ · example: `01/senior-adjuster-threshold-misroute`  
> Which TWO factors let the misrouting of threshold claims go unnoticed until an audit? Select TWO.  
> ✔ No test cases existed; routing was assumed to be handled by the model; SQL-style logging does not record choices a model makes inside a request

- Why: Asks why the threshold misroutes went unnoticed until audit; the answer rests on lessons stated only in the example (L117-118).
- **Replace with principle:** Risk when the model replaces the system of record: it cannot know its information is stale, will not flag the gap, and answers drift quietly with no error thrown and no warning raised. (`01.txt:102`)
- Stem sketch (multi, concept `model-unaware-of-staleness`): Which TWO describe the risk when the model, rather than the partner's actual system, becomes the source of truth? Select TWO. Correct: it has no reliable way to know its information is out of date; answers drift with no error or warning. Distractors: the API rejects the request with a 400; costs fall but latency rises; the model refuses to answer.

**d1s3q11** · _reused-setup_ · example: `01/senior-adjuster-threshold-misroute`  
> Why is a model-based check harder to diagnose than the SQL check it replaced?  
> ✔ Deterministic rules fail predictably while model errors vary and resist tracing

- Why: Stem frames the question around 'the SQL check it replaced', i.e. the example's setup, though the answer is the general L101 point.
- **Replace with principle:** When logic moves out of a table-driven system into the model, errors stop being traceable: a deterministic rule fails predictably and debuggably, a model produces variable outputs that are harder to observe and diagnose. (`01.txt:101`)
- Stem sketch (single, concept `deterministic-rule-in-model`): A team moves a validation rule from a lookup table into a prompt. Why do the notes say errors become harder to diagnose? Correct: the rule failed predictably; the model fails variably and is hard to observe. Distractors: models cannot return numbers; tables are faster; model output is logged more thoroughly.

**d1s3q12** · _reused-setup_ · example: `01/senior-adjuster-threshold-misroute`  
> A partner says an over-5,000 rule is 'easy enough for the model' and keeps the design to one step. Which response best reflects the notes?  
> ✔ Keep the check in the system of record and let Claude call it

- Why: Reuses the over-5,000 rule and the 'easy enough for the model' one-step simplification from the setup hook.
- **Replace with principle:** Existing systems own what the partner already made reliable; over-assigning that work to Claude makes the process more expensive, slower and harder. (`01.txt:82; 01.txt:85`)
- Stem sketch (single, concept `existing-systems-own-rules`): A partner's database of record already returns each customer's account tier reliably. An engineer proposes having Claude infer the tier from the customer's emails instead. Best response? Correct: keep the database as owner and let Claude use its result. Distractors: agree if clean test cases pass; agree but pin the model version; move the logic into a Skill.

**d1s4q03** · _reused-setup_ · example: `01/twelve-supplier-contracts-parallelization`  
> A due diligence review sends each of twelve supplier contracts to a separate simultaneous call, then aggregates the results into one risk report. Which sub-pattern is this?  
> ✔ Parallelization

- Why: Copies the twelve-supplier-contract due-diligence example used to illustrate parallelization.
- **Replace with principle:** Parallelization: multiple concurrent calls, results aggregated or voted; use when sub-tasks are independent, e.g. reviewing multiple files or distinct sections of a long document. (`01.txt:152-153`)
- Stem sketch (single, concept `workflow-subpatterns`): Each chapter of a long technical manual is reviewed in its own simultaneous call, and the findings are aggregated. Which sub-pattern? Correct: Parallelization. Distractors: Chaining, Routing, Evaluator-optimizer.

**d1s4q04** · _reused-setup_ · example: `01/complaint-reply-evaluator-optimizer`  
> A model drafts a complaint response, a second call grades it against a rubric, and the loop repeats until every rubric item passes or a retry limit is hit. Which sub-pattern is this?  
> ✔ Evaluator-optimizer

- Why: Copies the complaint-reply-graded-against-a-rubric example used to illustrate evaluator-optimizer.
- **Replace with principle:** Evaluator-optimizer: generate, evaluate, revise until a quality criterion or retry limit; use when quality is verifiable but one attempt is not reliable enough, e.g. code generation against a test suite or strict-schema extraction. (`01.txt:156-157`)
- Stem sketch (single, concept `workflow-subpatterns`): Generated code is run against a test suite; failures are fed back and the code is revised until the tests pass or a retry limit is reached. Which sub-pattern? Correct: Evaluator-optimizer. Distractors: Parallelization, Chaining, Routing.

**d1s4q05** · _reused-setup_ · example: `01/support-ticket-routing`  
> Support tickets arrive and a classifier sends billing questions to account-data retrieval, technical issues to product-documentation retrieval, and escalations to a human queue. Which workflow sub-pattern does this show?  
> ✔ Routing

- Why: Copies the support-ticket routing example (billing to account retrieval, technical to docs retrieval, escalations to humans).
- **Replace with principle:** Routing: a classifier, often Claude, decides the downstream path; use when inputs vary in kind and different kinds need different handling. (`01.txt:148-149`)
- Stem sketch (single, concept `workflow-subpatterns`): An intake service receives a mix of invoices, signed contracts and identity scans, and a classifier sends each kind to a different handler. Which sub-pattern? Correct: Routing. Distractors: Chaining, Parallelization, Evaluator-optimizer.

**d1s4q08** · _recall_ · example: `01/agent-retro-router-four-chains`  
> A team's mined traces showed only four distinct paths through their system, yet they had built an agent. What should they have built?  
> ✔ A router with four chains

- Why: Asks what the retrospective team (four mined trace shapes) should have built.
- **Replace with principle:** Agents are often chosen because a task feels open-ended, not because it requires one; feeling uncertain about structure differs from steps that genuinely cannot be determined; if you could write the steps in code, use a workflow. (`01.txt:216`)
- Stem sketch (single, concept `agent-when-justified`): A team can write every step of a process down in advance but wants an agent because the work 'feels open-ended'. What do the notes recommend? Correct: a workflow, because steps that can be written in code do not need an agent. Distractors: an agent with guardrail tools; a multi-agent fan-out; fine-tuning first.

**d1s4q12** · _example-only-lesson_ · example: `01/agent-retro-router-four-chains`  
> An auditor asked which model version approved a disbursement, and the trace showed the version had rolled forward two weeks earlier without re-validation. What kind of failure is this?  
> ✔ A model-governance gap any pattern would have inherited

- Why: Recalls the disbursement audit where the model version had rolled forward two weeks earlier; the 'governance gap under any pattern' lesson is stated only in the example (L225).
- **Replace with principle:** Apply the delegation lens to the pattern itself: an agent that can act autonomously is right only when the stakes and reversibility of its actions justify the autonomy it is given. (General pinning guidance exists at 02.txt:149 but belongs to the integration/evaluation notes, not d1's notes area.) (`01.txt:208`)
- Stem sketch (single, concept `pattern-delegation-lens`): When the delegation lens is applied to the pattern choice itself, what decides whether an autonomous agent is appropriate? Correct: whether the stakes and reversibility of its actions justify that autonomy. Distractors: whether the team prefers flexibility; whether the latency budget is generous; whether the Agent SDK is available.

**d1s4q15** · _reused-setup_ · example: `01/contract-review-chaining`  
> A pipeline first extracts every obligation and deadline from a contract, then classifies each one by risk level, then drafts a summary memo for the lawyer. Which workflow sub-pattern is this?  
> ✔ Chaining

- Why: Copies the contract-review chaining example (extract obligations and deadlines, classify by risk, draft memo for the lawyer).
- **Replace with principle:** Chaining: step 2 takes step 1's output, sequential and linear; use when the task decomposes into stages with clear handoffs, each stage producing a defined output the next consumes. (`01.txt:144-145`)
- Stem sketch (single, concept `chaining-subpattern`): The first call transcribes a recorded meeting, the second extracts the decisions from that transcript, and the third formats them into a status update. Which sub-pattern? Correct: Chaining. Distractors: Routing, Parallelization, Evaluator-optimizer.

**d1s4q26** · _example-only-lesson_ · example: `01/agent-retro-router-four-chains`  
> An auditor asks which step approved a disbursement, and the team running an agent can only point to a model turn. Which failure was introduced specifically by the agent pattern?  
> ✔ No discrete, auditable step exists to answer for the decision

- Why: Recalls the auditor asking which step approved a disbursement; the answer is the lesson stated only in the example (L224).
- **Replace with principle:** Agents are where non-deterministic failures concentrate in production, because the model's trajectory is the control flow and there is no code boundary where a guard can sit. (`01.txt:136`)
- Stem sketch (single, concept `agent-audit-gap`): Why do the notes say non-deterministic failures concentrate in the agent pattern? Correct: the trajectory is the control flow, so there is no code boundary where a guard can sit. Distractors: agents cannot call tools reliably; agents always use larger models; agents cannot be logged at all.

**d1s4q27** · _recall_ · example: `01/agent-retro-router-four-chains`  
> A team chose an agent 'to avoid constraining it too early'. By month two it had added so many guardrail tools that it had effectively rebuilt a workflow inside the loop. What did it lack compared with a real workflow?  
> ✔ The logging and auditability that control flow in code would have provided

- Why: Recalls the team that chose an agent 'to avoid constraining it too early' and rebuilt a workflow in the loop by month two.
- **Replace with principle:** Workflow: control flow lives in your code, so you can log it, test it and reason about it like any software; use when error cost is real, observability matters and the steps can be determined in advance. (`01.txt:129`)
- Stem sketch (single, concept `agent-audit-gap`): Operations must be able to reconstruct which step made each decision in a process whose steps are known in advance. Which pattern fits and why? Correct: a workflow, because control flow in code can be logged and tested. Distractors: an agent, because traces read like transcripts; an augmented call, because it is a single step; multi-agent, because each subagent logs separately.

**d1s5q02** · _reused-setup_ · example: `01/fan-out-large-work-item`  
> A regulatory filing must be checked against fifty rules, too much for one context. Which design is the standard fan-out shape?  
> ✔ Split into independent units, one subagent per unit, then synthesize

- Why: Reuses the fan-out example's 'regulatory filing checked against fifty rules'.
- **Replace with principle:** Fan-out is the most common multi-agent shape; its twofold win is that each subagent works in a clean context sized to its unit and independent units run concurrently. (`01.txt:238`)
- Stem sketch (multi, concept `fanout-pattern`): Which TWO benefits do the notes give for the fan-out shape? Select TWO. Correct: each subagent gets a clean context sized to its unit; independent units run concurrently. Distractors: lower total token spend; no need for synthesis; failures become unrecoverable less often.

**d1s5q04** · _recall_ · example: `01/vendor-contract-dropped-units`  
> A 50-section contract review reported '48 sections reviewed, 3 flagged', but two subagents had timed out or returned empty. Which control would have caught this?  
> ✔ A coverage check at synthesis: results returned must equal units dispatched

- Why: Recalls the 50-section contract review reported as '48 sections reviewed, 3 flagged'.
- **Replace with principle:** The dangerous multi-agent failure is the silent one: a subagent drops a unit and the orchestrator synthesizes a confident, complete-looking answer; validate coverage (reconcile results against units submitted) rather than assume it. (`01.txt:264; 02.txt:143`)
- Stem sketch (single, concept `coverage-check`): Which multi-agent failure do the notes call the most dangerous, and what guards against it? Correct: a dropped unit hidden under a confident synthesis; reconcile coverage at synthesis. Distractors: a slow subagent, fixed by a bigger window; conflicting results, fixed by restarting; high token spend, fixed by caching.

**d1s5q05** · _recall_ · example: `01/vendor-contract-dropped-units`  
> Which THREE gaps combined to let the dropped sections go unnoticed in the 50-section review? Select THREE.  
> ✔ The count was never reconciled between units dispatched and results received; Nothing owned the subagent boundary to retry or flag failed units; The summary read as complete and fluent, masking the gap

- Why: Asks for the three gaps 'in the 50-section review', i.e. the example's own analysis (L274-277).
- **Replace with principle:** Guard against confident synthesis over incomplete work: validate each subagent result, retry or re-route failed units and record the gap, and reconcile coverage at synthesis. (`01.txt:247-249; 01.txt:264; 02.txt:143`)
- Stem sketch (multi, concept `coverage-check`): Which TWO practices stop a fan-out from presenting incomplete work as complete? Select TWO. Correct: validate each result and record any gap; reconcile results returned against units dispatched. Distractors: let the orchestrator redo failed units itself; share one context across subagents; refresh the index more often.

**d1s5q08** · _recall_ · example: `01/order-88412-rag-live-state`  
> A retail assistant using RAG answers 'Your order shipped on the 12th' although the order was returned to depot. The index held two stale snapshots. What is the correct fix?  
> ✔ Call the order-status service directly through a tool

- Why: Recreates the retailer 'shipped on the 12th' answer from two stale chunks when the order was back at depot.
- **Replace with principle:** Most common reference-architecture mistake: retrieval where a tool call belongs; symptoms are stale chunks, results shifting with each refresh, answers contradicting the database; a better embedding model or shorter refresh will not fix it, call the system that owns the live state. (`01.txt:303`)
- Stem sketch (single, concept `rag-live-state`): An assistant's answers about account balances change after each index refresh and sometimes contradict the database. What is the fix? Correct: call the system that owns the balances through a tool. Distractors: better embedding model; shorter refresh interval; larger chunks.

**d1s5q13** · _reused-setup_ · example: `01/multi-pattern-composition-examples`  
> A routing workflow that hands some intents to an agentic loop is evaluated with a single end-to-end eval set. What is the risk?  
> ✔ A healthy top-level score can mask failures in one component

- Why: Reuses the notes' composition example of a routing workflow handing certain intents to an agentic loop.
- **Replace with principle:** Each reference architecture carries its own eval contract: use separate eval sets per architecture, because a composed system healthy at the top level can mask a failing component. (`01.txt:306`)
- Stem sketch (single, concept `one-vs-several-patterns`): A system combines a RAG layer for documentation with a document extraction pipeline and is evaluated with one end-to-end eval set. What is the risk? Correct: a healthy overall score can hide a failing component. Distractors: eval costs exceed system costs; the index stops refreshing; extraction becomes non-deterministic.

**d1s6q02** · _reused-setup_ · example: `02/twenty-page-boundary-condition`  
> A scoping document says the system works for documents up to 20 pages but fails beyond that. Where should this limit be recorded?  
> ✔ In the SOW as a boundary condition

- Why: Reuses the notes' 'works up to 20 pages, fails beyond' boundary-condition illustration.
- **Replace with principle:** Boundary conditions state when the architecture works and when it does not, and the SOW contains them so the development team and business owner both know what is out of scope. (`02.txt:180-181`)
- Stem sketch (single, concept `scoping-sequence`): An architecture handles typed forms reliably but not handwritten ones. Where should that limit be recorded? Correct: in the SOW as a boundary condition. Distractors: the post-launch retrospective; the prompt only; the deprecation runbook.

**d1s6q13** · _recall_ · example: `02/legal-contract-scoping-call`  
> A partner reveals 800 contracts a day, some of 300 pages, with a 30-second requirement. What does the notes' analysis conclude about volume and latency?  
> ✔ Volume is about one request per 108 seconds, so it pressures cost, not latency

- Why: Recalls the 800 contracts/day, 300 pages, 30 seconds analysis (one request per 108 seconds).
- **Replace with principle:** 'Technically feasible' is meaningless unless the constraints are applied at the expected scale; confirming feasibility from a working demo before gathering volume and SLA constraints is the trap. (`02.txt:235`)
- Stem sketch (single, concept `constraints-before-verdict`): A prototype works and the business owner is eager to proceed. Why should the architect not confirm feasibility yet? Correct: feasibility means nothing until constraints such as volume and SLA are applied at expected scale. Distractors: the model tier must be pinned first; a delivery route must be chosen first; ROI must be calculated first.

**d1s6q14** · _recall_ · example: `02/legal-contract-scoping-call`  
> In the contracts call, what was the architect's core mistake?  
> ✔ Issuing the feasibility verdict before gathering volume, size and latency

- Why: Asks what the architect's mistake was 'in the contracts call'.
- **Replace with principle:** Volume, latency and input-size constraints are inputs to the feasibility verdict; the verdict is only as sound as the constraints gathered before it. (`02.txt:250`)
- Stem sketch (multi, concept `constraints-before-verdict`): Which THREE constraints do the notes name as inputs that must be gathered before a feasibility verdict? Select THREE. Correct: call volume; latency requirement; input size. Distractors: team size; preferred delivery route.

**d1s6q16** · _reused-setup_ · example: `02/twenty-page-boundary-condition`  
> A design was declared feasible as scoped on the stated assumption that documents stay under 20 pages. Months later the business starts sending 150-page documents. How should the verdict be viewed?  
> ✔ It moves to feasible with constraints, since its assumption changed

- Why: Reuses the notes' 'documents under 20 pages' illustration as the stated assumption.
- **Replace with principle:** Feasible-as-scoped verdicts must state their assumptions, and become feasible-with-constraints when those assumptions change. (`02.txt:203`)
- Stem sketch (single, concept `feasible-as-scoped-assumptions`): A design was judged feasible as scoped on the assumption that all inputs arrive in English. The business now wants to add three more languages. How should the verdict be viewed? Correct: it moves to feasible with constraints. Distractors: it still holds since sign-off; it becomes not feasible automatically; language is an implementation detail.

**d1s6q19** · _reused-setup_ · example: `02/customer-service-1000-calls`  
> When building a sizing model for a customer service agent, where should the call volume figure come from?  
> ✔ The business owner, including multi-turn continuation calls per conversation

- Why: Reuses the notes' customer-service-agent volume illustration, and the correct option depends on its 'multi-turn continuation calls' detail.
- **Replace with principle:** Call volume comes from the business requirement and the business owner, not from the developer's intuition or a sample dataset. (`02.txt:172`)
- Stem sketch (single, concept `sizing-volume-and-sensitivity`): An architect is sizing an invoice-processing workflow. Where should the call-volume figure come from? Correct: the business owner, from the business requirement. Distractors: the POC sample dataset; the developer's estimate; the tier's rate limit.

**d1s6q23** · _example-only-lesson_ · example: `02/legal-contract-scoping-call`  
> A partner must process framework agreements of up to 300 pages. Which statement best reflects how this affects the design?  
> ✔ Window capacity is a tier decision; a 1M-token window may avoid chunking

- Why: Reuses the 300-page framework agreements and rests on 'context window capacity is part of the model tier decision', stated only inside the example (L246). Working memory feasibility is already covered by d1s6q08, q17, q18, so use an under-tested sizing fact.
- **Replace with principle:** Prompt caching in the cost model: it needs explicit cache_control markers, cache writes cost more per token than standard input so the model must include first-use write cost, and with the default 5-minute TTL, workloads whose request frequency is lower than the TTL will not realize consistent savings. (`02.txt:173`)
- Stem sketch (single, concept `caching-cost-model`): A sizing model assumes prompt caching will cut input cost for a long, stable system prompt, but requests arrive only every 20 minutes. What should the architect expect? Correct: little consistent saving, since the default 5-minute TTL lapses between requests and writes cost more than standard input. Distractors: caching works automatically without markers; reads are free; savings grow as traffic falls.

### Learn / trap cards to rewrite

**d1s1 traps[0]** · example: `01/reconciliation-nondeterminism`  
- Now: Demo equals determinism: five clean runs prove nothing; the same input can yield different outputs, so certify with evals rather than one observation.
- **Rewrite:** Demo equals determinism: a clean demo proves nothing; the same input can yield different outputs, so certify with evals rather than one observation. (`01.txt:20`)

**d1s2 learn[5]** · example: `01/agent-word-five-meanings`  
- Now: Use the fewest primitives necessary; shared vocabulary prevents five people hearing five architectures from the word agent.
- **Rewrite:** Use the fewest primitives necessary; without a shared vocabulary teams cannot communicate, because they do not agree on what the parts are. (`01.txt:69-70`)

**d1s2 traps[0]** · example: `01/retail-banking-claude-code-layer-collapse`  
- Now: Collapsing the layers: putting Claude Code (an engineering entry point) in front of bank branch staff because it is all Claude ignores that the wrapper matters.
- **Rewrite:** Collapsing the layers: the same model sits under every entry point, but the entry point is the wrapper; Claude Code is purpose-built for engineering, so follow the work. (`01.txt:42; 01.txt:586; 01.txt:638`)

**d1s2 traps[4]** · example: `01/agent-word-five-meanings`  
- Now: The word agent: undefined, it means a tool-using model, a workflow, a subagent team, Claude Code or a chatbot depending on who hears it.
- **Rewrite:** Undefined vocabulary: if the team does not agree on what the parts are, it cannot communicate; name the primitive or pattern meant before debating the design. (`01.txt:64; 01.txt:70`)

**d1s3 learn[2]** · example: `01/claims-triage-decomposition`  
- Now: Claims triage: read the claim is Claude; priority is the partner's rule engine; coverage comes from a live system lookup via tool or MCP; drafting the email is Claude, sending belongs to the email system with human approval above a threshold.
- **Rewrite:** Existing systems own what the partner already paid to make reliable: the order-status service, policy engine, rules table and database of record. Make them the source of truth through tools or MCP rather than replacing them with the model. (`01.txt:82; 01.txt:9`)

**d1s3 learn[4]** · example: `01/senior-adjuster-threshold-misroute`  
- Now: The 5,000 pound rule folded into the model: 41 of 14,000 claims misrouted when amounts were written in prose; found by audit, no test cases existed.
- **Rewrite:** Routing deterministic lookups to Claude means paying model rates for work a database query or rules table could do for a fraction of the cost, and it adds up fast across thousands of requests. (`01.txt:100`)

**d1s3 traps[1]** · example: `01/claims-triage-decomposition`  
- Now: Priority is a language task: it looks like one, but it is a deterministic rule already owned by a rule engine.
- **Rewrite:** Rules disguised as language tasks: a decision the partner already defines in a rule engine or rules table stays with that system, not the model. (`01.txt:82`)

**d1s3 traps[2]** · example: `01/claims-triage-decomposition`  
- Now: Coverage from training data: policies change and the model cannot know when its version went stale; retrieve from the live system.
- **Rewrite:** Model as source of truth: it cannot tell when its information went stale and will not flag the gap, so authoritative answers drift quietly with no error. (`01.txt:102`)

**d1s3 traps[3]** · example: `01/claims-triage-decomposition`  
- Now: Drafting equals sending: drafting is Claude's; sending belongs to the email system, with human approval above a value threshold.
- **Rewrite:** Claude owning the decision: judgment calls, exceptions and approvals belong to humans; collaborative work means Claude drafts and a person decides. (`01.txt:84; 01.txt:87`)

**d1s3 traps[4]** · example: `01/senior-adjuster-threshold-misroute`  
- Now: Simpler in one step: moving a deterministic check into the model makes demos cleaner but hides routing errors from monitoring.
- **Rewrite:** Logic moved into the model: a deterministic rule fails predictably and debuggably; the model fails variably, and its errors become hard to observe and trace. (`01.txt:101`)

**d1s4 learn[5]** · example: `01/agent-retro-router-four-chains`  
- Now: Skills-based packaging suits repeated, distributed, versioned procedures. Retrospective: four trace shapes meant a router plus four chains; the unpinned model version was a governance gap under any pattern.
- **Rewrite:** Skills-based packaging suits repeated, distributed, versioned procedures. Apply the delegation lens to the pattern itself: grant an agent autonomy only when the stakes and reversibility of its actions justify it. (`01.txt:207-208`)

**d1s4 traps[2]** · example: `01/agent-retro-router-four-chains`  
- Now: Blaming the agent for everything: the unpinned model version with no re-validation gate is a governance gap that any pattern would inherit.
- **Rewrite:** Broad tool permissions: an agent can do anything its tools allow, including combinations nobody tested; keep the tool entry point as narrow as the task allows. (`01.txt:212`)

**d1s5 learn[5]** · example: `01/order-88412-rag-live-state`  
- Now: Use one pattern unless two parts break differently; separate eval sets per architecture. Live state needs a tool call to the system of record, not a better chunker.
- **Rewrite:** Use one pattern unless two parts break differently; separate eval sets per architecture. Live state needs a call to the system that owns it; a better embedding model or shorter refresh will not fix it. (`01.txt:301; 01.txt:306; 01.txt:303`)

**d1s5 traps[0]** · example: `01/vendor-contract-dropped-units`  
- Now: Counting only returned results: 48 reviewed out of 50 sections looked complete; reconcile results returned against units dispatched.
- **Rewrite:** Counting only returned results: a confident summary can sit over dropped units; reconcile results returned against units dispatched. (`01.txt:264; 02.txt:143`)

**d1s5 traps[1]** · example: `01/vendor-contract-dropped-units`  
- Now: Silent subagent failure: a timed-out or empty-parse subagent is recoverable only if something retries or flags it.
- **Rewrite:** Silent subagent failure: a malformed or empty result is recoverable only if each result is validated and the unit retried, re-routed or recorded as a gap. (`01.txt:241; 01.txt:247-249`)

**d1s5 traps[2]** · example: `01/order-88412-rag-live-state`  
- Now: Retrieval for live order status: fix it with a tool call, not a better embedding model, shorter refresh or higher similarity threshold.
- **Rewrite:** Retrieval for live order status: fix it by calling the system that owns the live state; a better embedding model or shorter refresh interval will not. (`01.txt:303; 01.txt:294`)

**d1s6 learn[5]** · example: `02/legal-contract-scoping-call`  
- Now: Contracts scoping call: 800/day, 300 pages, 30 seconds. Context window depends on tier; 800/day is about one request per 108 seconds so volume pressures cost, not latency.
- **Rewrite:** Working memory is the most overlooked feasibility property: small, clean development inputs rarely hit the window, but production inputs do. Compensate with chunking, progressive loading or a pipeline. (`02.txt:231; 02.txt:192`)

**d1s6 traps[1]** · example: `02/document-triage-post-launch-quotes`  
- Now: Average instead of distribution: a long tail can consume most token spend (80% in one review), understating cost by two or three times.
- **Rewrite:** Average instead of distribution: a tail of long requests consumes a disproportionate share of spend, so averages can understate cost by two or three times. (`02.txt:118`)

<details><summary>Borderline — considered and kept (17)</summary>

- **d1s1q02**: Claims extraction of 'policy start date and claim amount' is generic; 02.txt:185 lists policy dates and claim amounts in general text, and it does not reuse the claims-success-criteria fields/thresholds.
- **d1s1q12**: Invoice totals scenario is newly invented; tests the general steerability rule at 01.txt:16-17.
- **d1s1q15**: Shift-handover note scenario is newly invented; tests restating the goal (01.txt:17).
- **d1s2q04**: Refund approval as a hook is generic; does not reuse the 03 refund-trace particulars (issue_refund tool, output-filter-only trace).
- **d1s2q07**: 'Agent Team where one lookup suffices' mirrors the e.g. embedded in the general Cost sentence at 01.txt:68, which is a general statement rather than a worked example.
- **d1s3q07**: Framing-shift question is stated in general terms at 01.txt:98 (flagged by the notes as the module's key concept), no example particulars in the stem.
- **d1s3q08**: Generic 'list every capability and assign it to Claude' stem; tests 01.txt:98 / 01.txt:85.
- **d1s4q13**: 'Claims-review procedure across teams' only shares the generic word claims; tests Skills packaging at 01.txt:207.
- **d1s4q16**: Support workflow adopting three sub-patterns 'to be safe' is invented; tests 01.txt:159.
- **d1s4q22**: 'Twelve steps' coincides with the twelve-contract number but the scenario (workflow cost vs agent) is unrelated; tests 01.txt:210.
- **d1s5q09**: The retrieval principle at 01.txt:324 sits under its own general heading and is restated generally at 01.txt:303/316; no order-88412 particulars in the stem.
- **d1s5q11**: 'Retrieval for live order status' is a named failure mode in the general reference-architecture table (01.txt:294).
- **d1s5q14**: Conflicting findings on 'the same contract clause' is generic; tests the failure table at 01.txt:250-252.
- **d1s5q16**: 40-unit fan-out with a malformed result is generic; tests 01.txt:247-249, not the 50-section example.
- **d1s6q04**: 'Longest documents consumed most of the spend' echoes quote 2 of the document-triage review but omits its particulars (80%, triage, 60 days); the answer is the general rule at 02.txt:118.
- **d1s6q06**: Document-length threshold and index refresh schedule are the general constraints listed in the verdict table at 02.txt:205.
- **d1s6q10**: Claims review/analyst hours appears in general ROI text (02.txt:215 unit e.g., 02.txt:226 'analyst hours fail to fall'), not in a worked-example story.

</details>


## Domain 2: Models, Prompting, Context  (11 questions, 8 cards)

### Questions to remove and replace

**d2s1q05** · _recall_ · example: `01/sonnet-to-haiku-downgrade`  
> A Sonnet-to-Haiku eval shows 0.94 vs 0.86 overall, with Haiku at 0.71 and 0.74 on two document types. The pre-set rule rejects any type below 0.85. What is the best next move?  
> ✔ Route those two types to Sonnet via the classifier; send the rest to Haiku.

- Why: Stem reproduces the worked case's scores (0.94/0.86, 0.71/0.74, 0.85 floor) and the answer is the case's specific salvage move (route two types to Sonnet).
- **Replace with principle:** No eval set means no rollback signal: a regression discovered in production is one that was never detected, because the user saw it first. (`01.txt:475`)
- Stem sketch (single, concept `no-eval-no-rollback`): A team plans to change the model behind a live assistant with no eval set, intending to 'watch for complaints' after launch. What is the core risk? Correct: there is no rollback signal; any regression is found by users, not detected. Distractors: higher token cost only; cache invalidation; vendor rate limits.

**d2s1q06** · _example-only-lesson_ · example: `01/sonnet-to-haiku-downgrade`  
> Why did the document-intelligence team build its 250-document eval set stratified by document type rather than relying on one overall average?  
> ✔ Per-type scores stay meaningful, exposing weak types and partial-migration options.

- Why: Asks why 'the document-intelligence team' stratified its 250-document set; per-type sizing and the partial-migration benefit are lessons stated only inside the worked case (L464, L469).
- **Replace with principle:** The minimum model-swap gate needs a curated test set with known-good outputs that covers the real distribution of work the system sees (currently only one option in d2s1q03). (`01.txt:458`)
- Stem sketch (single, concept `eval-gate-three-parts`): A team gates a model change using a few dozen polished prompts taken from the original sales demo, plus a rubric grader and a pre-set threshold. Which part of the minimum gate is weakest? Correct: the test set does not cover the real distribution of production work. Distractors: grader must be programmatic; threshold must be set after results; vendor benchmark missing.

**d2s1q07** · _recall_ · example: `01/opus-everywhere-7x-overrun`  
> A launched system runs at seven times its modeled cost with Opus on every call. Which THREE factors compounded to cause this? Select THREE.  
> ✔ No model-tier decision was made, so the most expensive default carried through; Cost was reviewed monthly, so the gap surfaced weeks after launch; No eval set existed to ground a different choice during the build

- Why: Recreates the 7x-cost, Opus-on-every-call case and asks for the case's three contributing factors.
- **Replace with principle:** Not choosing a model is equivalent to choosing the most expensive one; the eval set is not just a release gate but the only thing that makes the tier decision defensible during the design conversation. (`01.txt:488, 01.txt:490`)
- Stem sketch (multi, concept `tier-decision-explicit`): Which TWO statements about an eval set's role in model-tier selection are accurate? Select TWO. Correct: it makes the tier choice defensible during design, not only at release; without one, a reflexive top-tier choice cannot be challenged with evidence. Distractors: it is only needed after launch; a public benchmark substitutes for it; it is only needed when moving down a tier.

**d2s1q08** · _recall_ · example: `01/opus-everywhere-7x-overrun`  
> In the 7x overrun case, what does the lesson 'the absence of a decision is a decision' mean?  
> ✔ Skipping the tier choice quietly defaulted every step to the costliest option.

- Why: Stem opens 'In the 7x overrun case' and asks the learner to interpret that case's lesson.
- **Replace with principle:** The absence of a deliberate model-tier decision is not neutral: it is an implicit decision that defaults to the most expensive option. (`01.txt:486, 01.txt:490`)
- Stem sketch (single, concept `tier-decision-explicit`): An architecture document specifies prompts and tools for every pipeline step but names no model tier for any of them. What is the most likely consequence? Correct: the implicit default carries through and the most expensive option is effectively chosen. Distractors: the API picks the cheapest tier per step; the vendor optimises tiers automatically; nothing changes until an eval runs.

**d2s1q09** · _recall_ · example: `01/opus-everywhere-7x-overrun`  
> After the overrun, which per-step assignment did the retroactive eval support?  
> ✔ Haiku for routing, Sonnet for mid-pipeline summarization, Opus for final composition

- Why: Asks which per-step assignment 'the retroactive eval' supported after the overrun; the Haiku/Sonnet/Opus split and its outcome are particulars of the case.
- **Replace with principle:** A model swap looks like a one-line configuration change but rewrites how the whole product behaves; a swap between two models is a code deployment and is treated as a release. (`01.txt:474, 01.txt:457`)
- Stem sketch (single, concept `swap-is-release`): An engineer wants to change the model ID in a config file and push it without review, calling it 'a one-line change'. What is the best architect response? Correct: treat it as a release gated by an eval, because it changes product behavior. Distractors: approve since no code changed; approve if latency improves; approve but schedule a quarterly review.

**d2s1q13** · _recall_ · example: `01/opus-everywhere-7x-overrun`  
> In the 7x overrun case, where did extended thinking add cost and latency with no benefit?  
> ✔ On the routing classifier, which did not need reasoning at all.

- Why: Stem opens 'In the 7x overrun case' and asks where extended thinking was enabled (the routing classifier), a case particular.
- **Replace with principle:** Run evals without extended thinking first; if accuracy still misses requirements after the prompt itself has been worked on, then consider enabling it. (`01.txt:455`)
- Stem sketch (single, concept `thinking-measured-gap`): An extraction step misses its accuracy target in evals run without extended thinking, and the prompt has not yet been revised. What should happen next? Correct: improve the prompt and re-run the eval; consider thinking only if a measured gap remains. Distractors: enable thinking immediately on every call; move straight to Opus; lower the accuracy target.

**d2s2q08** · _recall_ · example: `01/coding-agent-layered-context`  
> In a long-running coding agent, which TWO pairings of phase and strategy match sound design? Select TWO.  
> ✔ Session start: a small, stable monolithic prefix suited to prompt caching; Active work: carry forward only recent state progressively

- Why: Asks the learner to match phases of 'a long-running coding agent' to strategies, i.e. to recall the worked example's phase table (L431-445).
- **Replace with principle:** The general context-design questions: what the model needs at the start drives the monolithic baseline; recent steps drive the progressive window; on-demand needs drive the retrieval layer; compressible earlier material drives the compaction policy. (`01.txt:447-451`)
- Stem sketch (multi, concept `strategies-combine`): When designing a context system, which TWO pairings of design question and context layer are correct? Select TWO. Correct: 'what might it need to fetch on demand?' -> retrieval layer; 'what earlier material can be compressed without losing decision-relevant detail?' -> compaction policy. Distractors: 'what does it need at the start?' -> compaction; 'what does it need from recent steps?' -> retrieval; 'what might it fetch on demand?' -> monolithic baseline.

**d2s2q09** · _example-only-lesson_ · example: `01/coding-agent-layered-context`  
> Why can a long-running coding agent not be served by any single context strategy?  
> ✔ Each strategy handles a different dimension, so they work as layers.

- Why: Reuses the coding-agent setup and its answer/explanation rest on 'no single strategy could carry this workload' (L446), a lesson stated inside the worked example.
- **Replace with principle:** The four strategies are taught separately, but production systems almost always combine them; each handles a different dimension of the context problem, so a well-designed system layers them deliberately rather than picking one. (`01.txt:430`)
- Stem sketch (single, concept `strategies-combine`): A design review asks a team to choose 'the one context strategy' for a new production assistant. What is the strongest architect response? Correct: production systems usually layer several strategies deliberately, each covering a different dimension. Distractors: always choose monolithic for simplicity; always choose retrieval because it scales; choose whichever strategy the largest window allows.

**d2s2q10** · _reused-setup_ · example: `01/token-growth-4k-to-80k`  
> A document pipeline starts conversations with a 4,000-token prompt and sees costs rise with no code changes. By turn 30 the context holds about 80,000 tokens. What is the likely cause?  
> ✔ Monolithic accumulation across turns is silently inflating per-call input.

- Why: Stem reproduces the illustration's particulars (document pipeline, 4,000-token prompt, about 80,000 tokens by turn 30) even though the answer is a general rule.
- **Replace with principle:** Monolithic context hits the working-memory cliff in production because context accumulates across turns and the window fills silently; cost and latency scale linearly with input length. (`01.txt:386, 01.txt:396`)
- Stem sketch (single, concept `monolithic-creep`): A multi-turn tool loop resends its entire growing history on every call. Spend per call keeps rising week over week with no code change and no errors. What is the most likely cause? Correct: monolithic accumulation silently inflates per-call input. Distractors: automatic tier upgrade; cache write surcharge per turn; retrieval returning more chunks.

**d2s4q02** · _reused-setup_ · example: `01/cache-never-hits`  
> A team put per-request document text at the top of a prompt, ahead of a large fixed instruction block, and saw no caching savings. What is the fix?  
> ✔ Place fixed content first and dynamic content last.

- Why: Stem restates the worked example almost verbatim (per-request document at the top, ahead of a large fixed instruction block, no savings) and asks for the example's fix.
- **Replace with principle:** TTL selection: match the cache lifetime to how often the fixed content actually changes and how frequently the prompt is called; a constantly called prompt benefits from a longer-lived cache, a rarely called one may never amortize the write. (Static-before-dynamic is already covered by d2s4q01, q03, q04, so an under-tested caching rule is proposed instead.) (`01.txt:543`)
- Stem sketch (multi, concept `cache-ttl-frequency`): Which TWO factors should drive the choice of cache lifetime for a reusable prompt? Select TWO. Correct: how often the fixed content actually changes; how frequently the prompt is called. Distractors: expected response length; the number of few-shot examples; the model tier in use.

**d2s4q06** · _reused-setup_ · example: `02/cache-read-10pct-hypothetical`  
> If cache reads cost 10% of the standard input rate and writes cost more than standard input, when does caching produce the largest savings?  
> ✔ A long, stable prefix reused across many requests within the TTL

- Why: Stem builds on the notes' hypothetical '10% of the standard input rate' figure, which 02:120 flags as an illustrative example to verify on the pricing page; the tested principle itself is general.
- **Replace with principle:** Caching savings scale with both the length of the cached prefix and how often it is reused; a long prefix reused across many requests gives the largest savings (no specific rate asserted). (`02.txt:120`)
- Stem sketch (single, concept `cache-economics`): Cache writes cost more than standard input and cache reads cost less. Which workload produces the largest caching savings? Correct: a long, stable prefix reused across many requests within the TTL. Distractors: a short prefix used a few times a week; a prefix reused once after the write; a long prefix that changes on every request.

### Learn / trap cards to rewrite

**d2s1 learn[2]** · example: `01/sonnet-to-haiku-downgrade`  
- Now: Set the rollback criterion in advance, for example no single document type below 0.85; a stratified eval set can reveal a partial-migration option.
- **Rewrite:** No eval set means no rollback signal: a regression discovered in production was never detected, because the user saw it first. (`01.txt:475`)

**d2s1 learn[3]** · example: `01/opus-everywhere-7x-overrun`  
- Now: The Opus-everywhere 7x overrun compounded three ways: no tier decision, monthly cost-visibility lag, and no eval set.
- **Rewrite:** Not choosing a model tier is choosing the most expensive one; an eval set is what makes the tier decision defensible during design, not just at release. (`01.txt:486, 01.txt:488, 01.txt:490`)

**d2s1 learn[4]** · example: `01/opus-everywhere-7x-overrun`  
- Now: Per-step tiering: Haiku for routing, Sonnet for summarization, Opus only where the eval shows it earns its place.
- **Rewrite:** Moving to Opus or Haiku is a deliberate decision with the same gate as any release: an eval set defining 'better' and a rollback criterion set before the swap. (`01.txt:739`)

**d2s1 traps[2]** · example: `01/sonnet-to-haiku-downgrade`  
- Now: Average hides tails: a good overall score can conceal per-document-type failures when the eval set is not stratified.
- **Rewrite:** Unrepresentative test set: a swap eval that does not cover the real distribution of work certifies behavior on inputs production will not send. (`01.txt:458, 01.txt:20`)

**d2s2 learn[4]** · example: `01/token-growth-4k-to-80k`  
- Now: Context strategy and context sizing are separate decisions; a 4,000-token prompt can carry 80,000 tokens by turn 30.
- **Rewrite:** Context strategy and context sizing are separate decisions that interact but do not determine each other; treating them as one is where most designs go wrong. (`01.txt:452`)

**d2s2 traps[3]** · example: `01/coding-agent-layered-context`  
- Now: One strategy fits all: no single strategy carries a long-running agent; each handles a different dimension of the problem.
- **Rewrite:** One strategy fits all: production systems almost always combine strategies, because each handles a different dimension of the context problem. (`01.txt:430`)

**d2s4 learn[1]** · example: `02/cache-read-10pct-hypothetical`  
- Now: Cache writes cost more than standard input and reads cost less (10% as an example); the default TTL is 5 minutes, so infrequent calls do not amortize.
- **Rewrite:** Cache writes cost more than standard input and reads cost less (verify current rates on the pricing page); the default TTL is 5 minutes, so infrequent calls do not amortize. (`02.txt:120, 02.txt:173`)

**d2s4 traps[0]** · example: `01/cache-never-hits`  
- Now: Dynamic first: putting per-request content ahead of the fixed instruction block changes the prefix every time, so the cache never hits.
- **Rewrite:** Unstable prefix: caching matches only a stable prefix, so anything variable placed before the breakpoint stops hits; static before dynamic, always. (`01.txt:539, 01.txt:541`)

<details><summary>Borderline — considered and kept (10)</summary>

- **d2s1q02**: 'Ship on Opus to be safe' echoes the 7x case's setup hook ('use the best available model', L478), but the hook is general framing with no case particulars and the answer rests on L379.
- **d2s1q04**: Answer rests on the general rule at L460; only the explanation borrows 'does not negotiate with itself' from the downgrade case (L469). Optional: trim that phrase from the explanation.
- **d2s1 traps[0]**: 'Best-available reflex... because the demo must land' paraphrases the 7x case's setup hook (L478), which is general framing without case numbers or plot.
- **d2s2q02**: Order status and account balance come from the general 'persistent application state' definition (L375), not from the order #88412 RAG example's particulars.
- **d2s2q12**: Generic long-running agent with an identifier mentioned once tests the general compaction breakdown list (L425-427); no coding-agent phase particulars.
- **d2s2q15**: Generic support agent with a rolling summary tests the progressive breakdown at L407; not taken from any example.
- **d2s2q17**: 150-page contract set that fits the window tests L396 attention degradation; does not match the 02 legal-contract scoping call particulars (800/day, 300 pages, 30 s).
- **d2s4q03**: 8,000-token stable system prompt plus short varying message is a newly invented scenario testing L541/02:120; the example's specific plot (document placed at the top, no savings, reorder fix) is not reused.
- **d2s4q09**: Live inventory snapshot in a cached prefix tests the general consistency-window risk (02:120); inventory is in the notes' general live-state list (02:461).
- **d2s4q15**: Stem and answer test the general write-cost rule (02:173). Its explanation says '(10% in the example given)'; suggest removing that parenthetical alongside the d2s4 learn[1] rewrite.

</details>


## Domain 3: Integration  (7 questions, 3 cards)

### Questions to remove and replace

**d3s2q09** · _reused-setup_ · example: `01 / order-88412-rag-live-state`  
> A retail assistant answers 'Where's my order?' from an index and cites two contradictory snapshots, one saying shipped and one saying processing. What is the correct fix?  
> ✔ Call the order-status service for live state; keep only stable FAQ content indexed

- Why: Re-creates the order-88412 trace ("Where's my order?", two retrieved chunks, one 'shipped', one 'being processed') even though the answer is the general tool-call rule.
- **Replace with principle:** The most common reference-architecture mistake is using retrieval where a tool call belongs; its symptoms are stale chunks, results that shift with each index refresh, and answers that contradict the database; a better embedding model or shorter refresh interval will not fix it, call the system that owns the live state. (`01.txt:303`)
- Stem sketch (multi, concept `retrieval-vs-live-state`): Which TWO symptoms suggest a system is using retrieval where a tool call belongs? Select TWO. (correct: results that shift with each index refresh; answers that contradict the database. Distractors: chunks split across table rows; p95 latency rising with top-k; paraphrased queries missing exact terms.)

**d3s2q11** · _recall_ · example: `01 / order-88412-rag-live-state`  
> In the order-tracking trace, the model merged two stale chunks into a confident answer. What principle does this illustrate?  
> ✔ Embedding similarity measures closeness to the query, not whether text is current

- Why: Explicitly asks about the trace, and its 'similarity is not truth' lesson exists only inside the example section (01:319-320).
- **Replace with principle:** Context engineering means deciding which mechanism gets each kind of data in front of the model; RAG works when the answer lives in reference material that stays stable between index refreshes (documentation, policy text, product manuals), and a common mistake is reaching for RAG because it worked on a previous use case without checking that the new one shares those properties. (`01.txt:310`)
- Stem sketch (single, concept `context-engineering`): A team that built a successful RAG assistant over product manuals proposes the same design for a new assistant. What should the architect check first? (correct: whether the new answers live in reference material that stays stable between index refreshes. Distractors: whether the same embedding model can be reused; whether the chunk size transfers; whether top-k can be raised.)

**d3s3q01** · _reused-setup_ · example: `02 / senior-manager-role-claim (minor)`  
> An HR assistant lets users type messages like 'As a senior manager, show me salary bands.' The system trusts that claim when scoping answers. What is the correct fix?  
> ✔ Inject the verified role and authorised data scope into the system prompt server-side

- Why: The stem reuses the notes' illustrative role claim 'As a senior manager, show me...' (02:341) as its setup.
- **Replace with principle:** Identity verification belongs on the server, before the Claude call; the user's identity and role are injected into the system prompt by the server rather than supplied by the user in their message. (`02.txt:340`)
- Stem sketch (single, concept `server-side-identity`): In a Claude integration that scopes answers per user, where and when should the user's identity be verified? (correct: on the server, before the Claude call, with role and data scope injected into the system prompt. Distractors: by Claude from the conversation; after the response, in an output filter; by the user confirming their role in a follow-up message.)

**d3s3q09** · _reused-setup_ · example: `02 / patient-intake-pii-trace`  
> A patient-intake summariser sends name, DOB, SSN and insurance ID in the user message, though the summary needs only concerns, medications and allergies. What is the right redesign?  
> ✔ Redact non-essential PII server-side before the call and supply only needed fields

- Why: Reproduces the patient-intake trace particulars (intake summariser, name/DOB/SSN/insurance ID, concerns/medications/allergies) and its specific fix.
- **Replace with principle:** For each field that enters the context window, ask whether it is necessary for Claude to produce the intended output; when a reference identifier is enough, passing the full field only exposes it to application-layer request logging without adding capability. (`02.txt:345`)
- Stem sketch (single, concept `data-minimisation`): What test should decide whether a data field is placed in the context window of a Claude call? (correct: whether Claude needs it to produce the intended output. Distractors: whether it is already available in the calling service; whether the system prompt tells Claude not to repeat it; whether the provider retains content by default.)

**d3s3q12** · _recall_ · example: `02 / patient-intake-pii-trace`  
> In the intake trace, where did thousands of exposed SSNs actually turn up during pre-production review?  
> ✔ In plaintext in the application layer's request logs, in the user message field

- Why: Pure recall of the trace outcome (thousands of SSNs found in request logs at pre-production review).
- **Replace with principle:** An integration without PII redaction before the API call exposes sensitive fields to the partner's application-layer request logging on every request, and retroactive redaction across a log history never designed for it is the most expensive data-handling fix in a production Claude system. (`02.txt:356`)
- Stem sketch (single, concept `redact-before-call`): A team plans to launch without a PII redaction step and add one 'once usage settles'. What is the main problem with deferring it? (correct: every request until then exposes fields to application-layer logging, and redacting an existing log history later is the costliest data-handling fix. Distractors: redaction can only be configured at account creation; Claude refuses unredacted input after launch; deferral only affects output quality.)

**d3s5q14** · _reused-setup_ · example: `01 / linear-mcp-server (minor)`  
> The same Linear integration must be reachable from Claude.ai, Claude Code and an internal app. What is the right choice?  
> ✔ Build one MCP server and connect it to each client

- Why: Reuses the notes' specific illustration (the team's Linear MCP server also working from Claude.ai, 01:672); a minor match that a reword fixes.
- **Replace with principle:** MCP is a sharing convention across products: when the same tool entry point is needed in two or more clients (Claude.ai, Claude Code, an internal app, a partner's product), build the server once and connect it everywhere. (`01.txt:616`)
- Stem sketch (single, concept `mcp-reuse`): Keep the question but drop 'Linear': e.g. 'An internal ticketing tool must be callable from Claude.ai, Claude Code and a partner-facing app. What is the right choice?' (correct: one MCP server connected to each client).

**d3s5q16** · _reused-setup_ · example: `01 / skill-workflow-examples (minor)`  
> A team's CLAUDE.md has grown to include full step-by-step procedures for releases, schema migrations and release notes, and every session starts with a bloated context. Where should those procedures live instead?  
> ✔ In Skills, invoked on demand rather than loaded upfront, keeping the main context lean

- Why: The stem's procedures (release flow, schema migrations, release notes) are exactly the notes' 'typical examples' of Skills (01:666), so the answer can be matched by recognising the list; a minor match that a reword fixes.
- **Replace with principle:** Skills are markdown-defined procedures Claude Code invokes on demand rather than loading upfront, keeping the main context lean; they suit repeatable workflows the team should not have to spell out each time, while CLAUDE.md holds persistent context every task needs. (`01.txt:665`)
- Stem sketch (single, concept `shaping-layer-placement`): Same question with procedures not listed in the notes, e.g. 'CLAUDE.md now holds full step-by-step procedures for onboarding a new service, rotating test fixtures and preparing a hotfix, and every session starts bloated. Where should those procedures live?' (correct: Skills, invoked on demand).

### Learn / trap cards to rewrite

**d3s2 learn[3]** · example: `01 / order-88412-rag-live-state`  
- Now: Retrieval is for stable knowledge; live state needs a tool call to the system of record. Similarity is not truth, and a better chunker or shorter refresh does not fix it.
- **Rewrite:** Retrieval is for stable reference material such as docs, policies and manuals; live state needs a tool call to the system that owns it. A better embedding model or shorter refresh interval does not fix it. (`01.txt:288, 01.txt:303, 01.txt:310`)

**d3s3 traps[0]** · example: `02 / senior-manager-role-claim (minor)`  
- Now: User-asserted role: accepting 'As a senior manager...' or a role field in the message instead of injecting verified identity server-side.
- **Rewrite:** User-asserted role: trusting a role the user claims in their message, or a role field they control, instead of verifying identity on the server and injecting it. (`02.txt:327, 02.txt:340-341`)

**d3s3 traps[2]** · example: `02 / patient-intake-pii-trace`  
- Now: Convenience data: passing SSN or insurance ID because it was available, when the language task never needed it; it lands in plaintext request logs.
- **Rewrite:** Convenience data: passing a sensitive field because it was available, when the language task never needed it; it lands in plaintext request logs. (`02.txt:333, 02.txt:345`)

<details><summary>Borderline — considered and kept (8)</summary>

- **d3s2q10**: Inventory levels from a vector index: inventory is one of the notes' general examples of live state (01:288, 01:303), not the order-88412 trace; no shipped/processing snapshots or order details reused.
- **d3s2q12**: Confident-wrong answers after a document refresh with unchanged latency/model come from the exam guide sample (guide.txt:177-195) and the general retrieval-drift statement (02:136), not from a notes worked example.
- **d3s2q03**: Part-number query ('KX-4410-B gasket') is newly invented; part numbers are a generic e.g. for sparse indexing in the notes, not a worked example.
- **d3s3q04**: Claims database read through an all-access service account is a newly written scenario for the general authorization rule (02:329-330); 'claims' is only a shared generic word.
- **d3s3q10**: Claim number used only for routing restates the general statement at 02:345 (claim numbers often needed for routing, not the language task); not the insurance-claims capability list example.
- **d3s1q05**: Claude Code behind a customer-facing multi-tenant portal is a new scenario for the general rule (Claude Code is not a product backend); it does not reuse the retail-banking branch-staff example's particulars.
- **d3s5q17**: Only a distractor option mentions 'a commit-push-PR flow' (one of the 01:666 typical Skills examples) and the stem is a generic pairing question; optionally reword that option to a different procedure for consistency with the d3s5q16 fix.
- **d3s4q14**: CIO-cleared vendor rule is stated in general terms (01:729, 02:311), not an example.

</details>


## Domain 4: Evaluation  (14 questions, 7 cards)

### Questions to remove and replace

**d4s1q07** · _reused-setup_ · example: `02/1 claims-success-criteria`  
> A business requirement says the assistant must "summarize claims accurately". Where should pass thresholds such as a hallucination ceiling and schema-compliance rate come from?  
> ✔ From the business requirement, after the vague goal is turned into specific measurable behaviors

- Why: Stem quotes the example requirement 'summarize claims accurately' and the explanation lists the example's fields (filer name, claim number, date, amount).
- **Replace with principle:** Pass thresholds come from the business requirement, not from what the first prototype happens to achieve; thresholds are revisited when requirements change. (`02.txt:69, 02.txt:79`)
- Stem sketch (single, concept `threshold-before-data`): A team's first working build scores 91% on field accuracy and the lead proposes adopting 91% as the pass mark. What is wrong with this? (correct: the threshold must come from the business requirement, not the prototype's result).

**d4s1q08** · _reused-setup_ · example: `02/1 claims-success-criteria`  
> A golden dataset for claim extraction contains only clean, well-formatted documents and scores 99%. Why will this score likely mislead the team?  
> ✔ It omits adversarial inputs such as missing fields, handwritten sections and non-standard layouts, so scores will not predict production

- Why: Stem is 'claim extraction' and the correct option lists the example's adversarial inputs verbatim (missing fields, handwritten sections, non-standard layouts).
- **Replace with principle:** The golden dataset must include the edge cases and counterexamples the system will meet; a non-representative dataset gives meaningless scores, and each failure mode becomes a dataset category. (`02.txt:21, 02.txt:70`)
- Stem sketch (single, concept `adversarial-inputs`): A golden dataset was assembled from the tidiest inputs the team had on hand and scores very well. Why is the score unreliable, and what fixes it? (correct: unrepresentative dataset -> include edge cases/counterexamples and a category per failure mode).

**d4s1q09** · _recall_ · example: `02/3 contract-review-postmortem`  
> A contract-review assistant passed its eval suite for two weeks, then failed on contracts with non-standard obligation structures. Which TWO root causes does this pattern point to? Select TWO.  
> ✔ The golden dataset was not updated after the prompt changed; The dataset came from ten convenient contracts rather than a representative sample

- Why: Stem replays the postmortem plot (contract-review assistant, two weeks, non-standard obligation structures) and the options cite its ten convenient contracts.
- **Replace with principle:** An out-of-date eval suite gives false confidence: it signals a change is safe while measuring behaviour the system no longer has; the highest-risk moment for a regression is when evals exist but are out of date. (`02.txt:80`)
- Stem sketch (single, concept `stale-eval`): When is a production Claude system at the highest risk of an undetected regression? (correct: when an eval suite exists but is out of date; distractors: no suite at all, during the first POC, right after judge calibration).

**d4s1q10** · _recall_ · example: `02/2 summarization-prompt-drift`  
> A summarization prompt was revised but the eval suite was left untouched and still passed. Two days after release, multi-clause legal sentences were being truncated. What is the lesson?  
> ✔ Update the eval set to match the changed behavior and run evals before every change

- Why: Stem retells the summarization example (prompt revised, suite untouched, multi-clause legal sentences truncated two days after release).
- **Replace with principle:** Every change to a production system (model swap, prompt revision, context strategy change, retrieval configuration update) runs through the eval suite during development before it moves to production. (`02.txt:73, 02.txt:76`)
- Stem sketch (single, concept `eval-gate-every-change`): A team plans to change only its retrieval configuration and argues the eval suite exists for model swaps. What is the correct response? (correct: every change type, including retrieval and context-strategy changes, goes through the eval suite before production).

**d4s1q13** · _reused-setup_ · example: `01/15 sonnet-to-haiku-downgrade`  
> A team evaluates a Sonnet to Haiku downgrade on 250 stratified documents. When should the rollback criterion (for example, no document type below 0.85) be set?  
> ✔ Before running the eval, so the result is judged against a standard rather than negotiated afterwards

- Why: Stem recreates the worked case (Sonnet to Haiku downgrade, 250 stratified documents, no document type below 0.85) and the explanation cites its partial-migration salvage.
- **Replace with principle:** Gate every model change with an eval: a curated test set covering the real distribution, a grading function, and a delta threshold set in advance; set afterwards it is acceptance criteria written after the build. (`01.txt:456-460, 01.txt:739`)
- Stem sketch (single, concept `threshold-before-data`): A team is about to run its eval set on a proposed model swap. When should the delta threshold below which it will not ship be set, and why? (correct: before running the eval, otherwise it is acceptance criteria written after the build). Use no tier direction, sample size or scores.

**d4s2q04** · _reused-setup_ · example: `02/5 document-triage-post-launch-quotes`  
> A cost model used the average token count of sample inputs. After launch, long documents in the tail consumed 80% of spend. What should the model have done?  
> ✔ Model the token distribution, including the long tail, rather than assuming the average represents all requests

- Why: Stem reuses quote 2 of the post-launch review ('long documents in the tail consumed 80% of spend').
- **Replace with principle:** Token distributions are often skewed: most requests are short but a tail of long requests takes a disproportionate share of cost, so an average-based cost model can underestimate by a factor of two or three; model the distribution, not the average. (`02.txt:118, 02.txt:173`)
- Stem sketch (single, concept `token-skew`): A team sizes cost from the mean token count of its sample, where most inputs are short and a few are very long. What is the likely error? (correct: cost underestimated, often by a factor of two or three, because the long tail is ignored). Use no percentage-of-spend figure.

**d4s2q11** · _reused-setup_ · example: `02/5 document-triage-post-launch-quotes`  
> On day three at peak, the endpoint returned a 529 and the whole document workflow stopped because failure handling had never been tested. Which design change addresses this?  
> ✔ Add a fallback chain in the orchestration layer to an alternative model tier or cached response, and test it in the eval suite

- Why: Stem reuses quote 3 of the post-launch review (529 at peak on day three, whole document workflow down, failure never tested).
- **Replace with principle:** Fallback chains route a request to an alternative (different model tier or cached response) instead of raising an error to the user, sit in the orchestration layer, and their behaviour is tested as part of the eval suite; without fallback or circuit breaker the primary endpoint is a single point of failure. (`02.txt:124, 02.txt:126, 02.txt:147`)
- Stem sketch (single, concept `fallback-chain`): Which statement about fallback chains matches the guidance? (correct: route to another model tier or a cached response instead of erroring to the user, and test the fallback in the eval suite; distractors: place them beside the API call, retry the same endpoint, only add after the first incident).

**d4s2q16** · _recall_ · example: `02/7 batch-api-50pct-hypothetical`  
> A nightly job summarizes protected health records and has no latency requirement. Which approach reflects the guidance on cost alternatives?  
> ✔ Model Batch API as a cost alternative (the example discount is 50%) but verify BAA coverage for that configuration first

- Why: The correct option and the mnemonic ('saves half') carry the hypothetical 50% Batch discount, which the notes give only as an 'if, for example' figure to be verified.
- **Replace with principle:** Model Batch API as a cost alternative wherever the SLA permits asynchronous processing, verify the current discount on the pricing page, and for regulated workloads verify BAA coverage for that configuration before routing PHI through it. (`02.txt:174, 02.txt:441`)
- Stem sketch (single, concept `batch-api`): Keep the generic nightly-PHI stem but remove the discount figure from options, explanation and mnemonic (correct: model Batch as a cost alternative, verify current pricing and BAA coverage for that configuration first).

**d4s3q01** · _reused-setup_ · example: `02/14 ab-hypothesis-action-items`  
> Which hypothesis is specific and falsifiable enough for an A/B test?  
> ✔ Replacing "summarize" with "extract the three key action items" will raise task success by at least 5% without worsening p95 latency

- Why: The correct option is the notes' model hypothesis verbatim (replace 'summarize' with 'extract the three key action items', +5%, no p95 degradation).
- **Replace with principle:** A usable hypothesis is a specific, falsifiable statement naming the treatment, the expected direction of the primary metric with a success threshold, and constraints on secondary metrics. (`02.txt:381`)
- Stem sketch (single, concept `ab-hypothesis`): Which hypothesis is ready for an A/B test? Use a newly invented correct option (e.g. adding two worked examples to a classification prompt will raise routing accuracy by at least 3 points without raising cost per request) against vague or after-the-fact options.

**d4s3q02** · _reused-setup_ · example: `02/14 ab-hypothesis-action-items`  
> A team writes the hypothesis "the new prompt is better." Why does this fail?  
> ✔ It names no treatment, no metric and no threshold, so any result can be interpreted as a win

- Why: Stem quotes the notes' counterexample 'the new prompt is better' and the answer restates the example's verdict on it.
- **Replace with principle:** Without a hypothesis any result can be interpreted as a win, because with enough metrics examined after the fact one can always be found that moved the right way. (`02.txt:382`)
- Stem sketch (single, concept `ab-hypothesis`): A team starts an experiment on a revised system prompt with no written hypothesis, planning to 'see what improves'. What is the main risk? (correct: any result can be read as a win since some metric will move the right way after the fact).

**d4s3q09** · _reused-setup_ · example: `02/15 thirty-pct-cost-tradeoff`  
> A prompt change lifts task success but raises cost per request by 30%. How should the result be read?  
> ✔ Check secondary metrics; a success gain with 30% higher cost may not be a net win

- Why: Stem reuses the notes' illustration of a task-success gain with cost up 30%, and the correct option repeats it.
- **Replace with principle:** Before declaring a winner ask two questions: is the effect large enough to justify the operational overhead of maintaining the new version, and did any secondary metric degrade? (`02.txt:394`)
- Stem sketch (multi, concept `significance-vs-value`): Which TWO questions should be answered before declaring an A/B winner? Select TWO. (correct: is the effect large enough to justify operational overhead; did any secondary metric degrade; distractors: which metric moved most, did the run stop as soon as the treatment led, is the p-value below a cut-off picked after the run).

**d4s3q11** · _recall_ · example: `02/18 fifty-session-ab-winner`  
> A team tested 50 sessions per arm and saw 68% against 62%, then deployed; two weeks later the new version settled at 61%. Which THREE flaws explain this? Select THREE.  
> ✔ The primary metric was chosen after seeing which one moved the right way; The sample was too small to separate a 6-point difference from noise; The input distribution was uncontrolled, with fewer edge cases in the treatment group

- Why: Stem retells the 50-session composite (68% vs 62%, settled at 61% two weeks later) and asks for its three diagnosed flaws.
- **Replace with principle:** Identify the primary metric and the sample size (from minimum detectable effect, baseline and confidence level) before running any experiment, alongside a specific falsifiable hypothesis. (`02.txt:496, 02.txt:381-390`)
- Stem sketch (multi, concept `experiment-preregistration`): Which THREE should be fixed before an A/B test of a prompt change starts? Select THREE. (correct: a falsifiable hypothesis, a single primary metric, the required sample size; distractors: the metric that moved most, the rollout date of the winner, a stop rule of 'when the treatment pulls ahead').

**d4s4q05** · _recall_ · example: `02/16 cost-spike-150pct-alert`  
> Which TWO threshold alerts match the anomaly detection guidance? Select TWO.  
> ✔ Cost exceeding 150% of the 7-day average; Latency p95 crossing the SLA threshold

- Why: One of the two correct options is the notes' illustrative threshold 'cost exceeding 150% of the 7-day average', so the answer hinges on recalling that figure.
- **Replace with principle:** Set threshold alerts on the metrics that matter for the deployment, such as latency p95 crossing the SLA; gradual model drift is poorly caught by thresholds and needs periodic distribution comparison. (`02.txt:405`)
- Stem sketch (single, concept `anomaly-thresholds`): A team wants to be alerted as soon as users start hitting SLA breaches. Which design fits? (correct: a threshold alert on p95 latency crossing the SLA; distractors: alert on median latency, a monthly distribution comparison, an alert on average token count).

**d4s4q13** · _reused-setup_ · example: `02/17 customer-service-kpi-translation`  
> A customer-service agent is monitored by latency, task success and error rate, but executives watch handle time and first-contact resolution. What must be built, and when?  
> ✔ A translation layer mapping task success to first-contact resolution and latency to handle time, built at design time

- Why: Stem reuses the notes' customer-service example (handle time, first-contact resolution) and the correct option is its exact mapping.
- **Replace with principle:** The observability stack needs a translation layer connecting technical metrics to the business KPIs funders read, built when the system is designed; otherwise the first business review needs retrospective reconstruction instead of a live query. (`02.txt:416, 02.txt:418`)
- Stem sketch (single, concept `translation-layer`): A sponsor tracks a business KPI (e.g. days to pay an invoice) while the team monitors latency, task success and error rate. What should be built, and when? (correct: a translation layer mapping technical to business metrics, at design time). Avoid customer-service KPIs.

### Learn / trap cards to rewrite

**d4s1 traps[4]** · example: `01/15 sonnet-to-haiku-downgrade (per-document-type signature)`  
- Now: Mean-score comfort: a higher average can hide a regression on edge cases or one document type.
- **Rewrite:** Mean-score comfort: a higher average can hide a quiet regression on edge cases or adversarial inputs, so read the per-category breakdown. (`02.txt:30-31`)

**d4s2 learn[5]** · example: `02/7 batch-api-50pct-hypothetical`  
- Now: Pin model versions, watch the deprecation page, keep a runbook; consider Batch API (50% example) when asynchronous is acceptable, verifying BAA coverage for regulated data.
- **Rewrite:** Pin model versions, watch the deprecation page, keep a runbook; model Batch API as a cost alternative when asynchronous is acceptable, verifying current pricing and BAA coverage for regulated data. (`02.txt:149, 02.txt:174`)

**d4s2 traps[3]** · example: `02/5 document-triage-post-launch-quotes (quote 3)`  
- Now: Untested failure: a 529 at peak takes the whole workflow down if the fallback was never built and tested.
- **Rewrite:** Untested failure: with no fallback or circuit breaker the primary endpoint is a single point of failure, so one outage at peak takes the whole workflow down. (`02.txt:124, 02.txt:147`)

**d4s3 learn[3]** · example: `02/15 thirty-pct-cost-tradeoff`  
- Now: Statistical significance is not practical significance; check operational overhead and secondary metrics (for example cost up 30%).
- **Rewrite:** Statistical significance is not practical significance; before declaring a winner, ask whether the effect justifies operational overhead and whether any secondary metric degraded. (`02.txt:393-394`)

**d4s3 traps[0]** · example: `02/14 ab-hypothesis-action-items (quoted counterexample)`  
- Now: Vague hypothesis: "the new prompt is better" names no treatment, metric or threshold, so any result can be called a win.
- **Rewrite:** Vague hypothesis: without a falsifiable statement naming treatment, metric direction and constraints, any result can be read as a win. (`02.txt:381-382`)

**d4s3 traps[2]** · example: `02/18 fifty-session-ab-winner`  
- Now: Small-sample wins: a 6-point gain on 50 sessions per arm sits inside the noise floor.
- **Rewrite:** Underpowered wins: a small comparison run until it looks good cannot separate a real effect from noise, and ships false positives. (`02.txt:391, 02.txt:420`)

**d4s4 learn[3]** · example: `02/16 cost-spike-150pct-alert`  
- Now: Alerts: cost above 150% of the 7-day average, p95 beyond SLA; drift needs periodic distribution comparison.
- **Rewrite:** Alerts: set thresholds on the metrics that matter, such as cost spikes and p95 beyond SLA; gradual drift needs periodic distribution comparison. (`02.txt:405`)

<details><summary>Borderline — considered and kept (10)</summary>

- **d4s1q11**: Mean 0.88 to 0.91 is an invented figure, not the Sonnet/Haiku scores; tests the general rule that a rising mean can hide edge-case regressions (02.txt:30).
- **d4s1q20**: Spot-check rule is stated generally (02.txt:83, 93); stem is a generic demo and reuses none of the contract postmortem particulars.
- **d4s2q07**: 800 ms coincides with the target in the 01 Opus 7x overrun case, but the plot (single-request POC vs p95 under load) is the general table at 02.txt:108; only a shared number.
- **d4s2q13**: Live inventory query is a generic live-state example from the RAG row and glossary (02.txt:136-137, 461), not a worked example.
- **d4s2q14**: Silently dropped subagents echo 01 vendor-contract-dropped-units, but numbers and setting differ and the fix is the general table row at 02.txt:142-143.
- **d4s3q03**: 'Treatment group happened to receive more complex queries' is the general table text at 02.txt:385, not the 50-session example (which had fewer edge cases).
- **d4s3q06**: Generic early-stopping stem (02.txt:391); one distractor mentions cost degrading 'about thirty percent', echoing 02.txt:394. Consider neutralising that distractor.
- **d4s3q10**: Seasonal spike is the general interaction-effects statement at 02.txt:395 (catalogue lists it as generic).
- **d4s3q13**: Regulated deployment with modest traffic is the general guidance at 02.txt:400, not a worked example.
- **d4s4q09**: Hallucination remedy is general (02.txt:410); one distractor mentions the '7-day average used by the cost alert', echoing the 150% illustration. Consider neutralising that distractor.

</details>


## Domain 5: Governance  (13 questions, 4 cards)

### Questions to remove and replace

**d5s1q04** · _recall_ · example: `03/cross-unit-disclosure-postmortem`  
> An internal assistant disclosed a record belonging to another business unit in response to a normal, in-domain request. Claude had refused every harmful test prompt. What is the root cause?  
> ✔ The cross-unit rule was never encoded in any layer, and trained refusals cover broad harm rather than that policy

- Why: Stem retells the postmortem (another business unit's record, normal in-domain request, Claude refused every harmful test prompt) and asks for its root cause.
- **Replace with principle:** Map the boundary between what trained behaviour covers and what you must build before adding controls, so you neither duplicate protections nor assume the model enforces a rule it has never seen (the 'cannot enforce an unseen rule' fact itself stays covered by d5s1q09/q10). (`03.txt:2; 03.txt:243`)
- Stem sketch (single, concept `draw-layer-boundary`): Before adding controls to a new deployment, why should the architect first establish what Claude's training already covers? Correct: to avoid duplicating protections and to avoid assuming the model enforces a rule it has never seen. Distractors: training can be tuned per deployment; the system prompt replaces training; screening is unnecessary once training is mapped.

**d5s1q06** · _reused-setup_ · example: `03/cross-unit-disclosure-postmortem`  
> A deployment must never show one business unit's records to another. Which control actually enforces this rule?  
> ✔ A deterministic authorization check on caller identity and scope before the record is returned to the model

- Why: Stem re-creates the example's distinctive policy (never show one business unit's records to another); the general answer (authorization) can be tested with a fresh rule.
- **Replace with principle:** Deployment-specific policy is enforced only when instructions are paired with runtime controls; whether a specific side-effecting action is permitted for this caller in this context is the authorisation layer, not the system prompt or trained refusals. (`03.txt:6; 03.txt:22; 03.txt:70`)
- Stem sketch (single, concept `instructions-not-enforcement`): Only verified account holders may change a delivery address through the assistant's update_address tool. Which control actually enforces this? Correct: a deterministic identity and scope check before the tool runs. Distractors: a system prompt sentence forbidding unverified changes; reliance on trained refusals; an output tone guideline.

**d5s2q05** · _recall_ · example: `03/refund-trace-output-filter-only`  
> A customer service agent called issue_refund, the refund ran, and only then an output filter passed the generated text. What went wrong?  
> ✔ A single output control was treated as covering three points, and nothing authorized the tool call before it ran

- Why: Stem replays the trace (customer service agent, issue_refund ran, output filter passed afterwards) and asks what went wrong; single-filter coverage is already tested by d5s2q11 and the three control-point roles by d5s2q03.
- **Replace with principle:** The full guarded request path runs in order: the request arrives, input screening decides whether it reaches the model, the model responds, output screening decides whether the response is returned, and any tool call passes authorization before it runs; every blocked or failed gate is logged. (Path order is not yet tested in the bank.) (`03.txt:79-80`)
- Stem sketch (single, concept `guarded-path-order`): Which sequence matches the full guarded request path? Correct: input screening, then the model call, then output screening, with tool-call authorization before any side-effecting action runs and every blocked or failed gate logged. Distractors: authorization after the response is returned; output screening before the model call; input screening only after a tool call.

**d5s3q11** · _reused-setup_ · example: `03/skill-out-of-scope-examples`  
> A skill advertised only as a document formatter makes an outbound network request to an unknown host during testing. How should the audit classify this?  
> ✔ As an out-of-scope finding, because the stated purpose of formatting does not justify phoning home

- Why: Stem re-uses the notes' own one-line illustration (a formatting skill that phones home), and its explanation says so; the stated-purpose baseline can be tested with an invented skill.
- **Replace with principle:** A skill's stated purpose is the audit baseline; anomalous calls (network, shell, file-system access, credential reads) or behaviour beyond the claimed job are findings to investigate, and a sandbox contains but does not excuse them. (`03.txt:84`)
- Stem sketch (single, concept `out-of-scope-baseline`): A skill advertised as a unit converter reads files in the user's home directory and a stored credential file during the audit. How should this be classified? Correct: an out-of-scope finding against its stated purpose. Distractors: normal because converters cache data; acceptable once sandboxed; a prompt-injection issue from user input.

**d5s4q06** · _reused-setup_ · example: `03/retrieval-corpus-fairness-review`  
> A model passed its fairness evaluations, yet outcomes differ across applicant groups. Where should the team investigate first?  
> ✔ The retrieval corpus, which may over- or under-represent groups in a way the model provider never tested

- Why: Stem re-creates the review's plot (model passed its fairness evaluations, outcomes skewed, answer = retrieval corpus) with the credit example's 'applicant' framing.
- **Replace with principle:** Few-shot examples can carry the same skew the corpus does, and prompt framing can encode an assumption that pushes outcomes one way; each is a separate entry point to inspect. (`03.txt:107-112 (esp. 109-110)`)
- Stem sketch (multi, concept `four-entry-points`): A team rebalanced its retrieval corpus, but outcomes still lean one way. Which TWO remaining entry points could carry the skew? Select TWO. Correct: the few-shot examples; the framing of the prompt. Distractors: the token-budget limit; the stop_reason handler; the constitution's priority order.

**d5s4q09** · _recall_ · example: `03/retrieval-corpus-fairness-review`  
> A regulator asks where a skew came from, and the team had logged very little. What is the lesson?  
> ✔ If you cannot reconstruct a decision, you cannot explain it or rule out the corpus

- Why: Stem retells the post-incident review (regulator asks where the skew came from, team had logged very little) and the answer is the example's lesson about ruling out the corpus.
- **Replace with principle:** If you cannot reconstruct a decision you cannot reliably explain it; replay needs the inputs, retrieved context, model output and routing captured for each decision. (`03.txt:247; 03.txt:126-127`)
- Stem sketch (single, concept `cant-reconstruct`): A team wants to give affected users explanations for automated decisions but stores only each final response. What is the gap? Correct: without inputs, retrieved context and routing it cannot reconstruct a decision, so it cannot reliably explain one. Distractors: the response already explains itself; aggregate metrics suffice; explanations can come from the vendor's evaluations.

**d5s4q11** · _recall_ · example: `03/retrieval-corpus-fairness-review`  
> An architect says, 'We assumed fairness was the model's job.' Which statement best captures why that failed?  
> ✔ The skew entered at the corpus, which the architect controls, and went unmonitored by assumption

- Why: Stem quotes the architect from the post-incident review ('We assumed fairness was the model's job') and asks why it failed.
- **Replace with principle:** Runtime controls stop disallowed outputs but do not account for an output that passes every check yet produces different outcomes for different people; that failure looks like a normal output, so it is harder to detect and attribute. (Not yet tested; vendor-responsibility stays covered by d5s4q01 and trap card d5s4 traps[0].) (`03.txt:105`)
- Stem sketch (single, concept `fairness-architectural`): A team's input and output screening pass every response. Why does that not show the system is fair? Correct: an output can pass every check yet produce different outcomes for different people, and it looks like normal output. Distractors: screening is disabled for fairness topics; screening runs only on tool calls; passing screens proves comparable treatment.

**d5s4q13** · _example-only-lesson_ · example: `03/credit-decision-checklist`  
> In a credit-decision support system, the team cannot produce the inputs and the reason for an adverse decision in terms the applicant can act on. How is this classified?  
> ✔ A design gap, since a 'no' to any checklist question exposes a transparency weakness

- Why: Stem uses the credit-decision / adverse-decision framing, and its answer is 'a no anywhere is a design gap', a lesson stated only inside that example (03:134).
- **Replace with principle:** An affected user needs a clear explanation of why a decision affecting them was made, in terms they can act on, which requires capturing the inputs that drove it and the reason in a digestible form (the affected-user slice is not the correct answer in any current question). (`03.txt:117-119`)
- Stem sketch (single, concept `audience-slices`): A person affected by an automated decision asks why it went against them. What must the system have captured to answer well? Correct: the inputs that drove the decision and the reason, in a form they can act on. Distractors: the full raw routing trace; an aggregate consistency query; the vendor's bias evaluation results.

**d5s4q14** · _reused-setup_ · example: `03/credit-decision-checklist`  
> A credit-decision support system is reviewed against the fairness-and-transparency checklist. Which TWO questions must it be able to answer yes to? Select TWO.  
> ✔ Can it produce the inputs and the reason for an adverse decision in terms the applicant can act on?; Can the log be queried to show whether comparable applicants were treated comparably?

- Why: Stem reviews 'a credit-decision support system' against the checklist and asks about adverse decisions and comparable applicants, which is the example's framing.
- **Replace with principle:** Discernment applied to fairness lets a reviewer recognise a skewed or unjustified outcome instead of only confirming that a value was produced, and a transparency record makes that recognition possible (only the bare definition is tested today, in d5s4q08). (`03.txt:136`)
- Stem sketch (multi, concept `discernment`): Which TWO statements about Discernment applied to fairness are correct? Select TWO. Correct: it means recognising a skewed or unjustified outcome, not only confirming a value was produced; a transparency record makes that recognition possible. Distractors: it means approving outputs that pass screening; it replaces decision logging; it is the competency for maintaining accountability checkpoints.

**d5s5q10** · _recall_ · example: `03/400-item-review-queue`  
> A reviewer faces 400 items a day, sees only the output and an approve button, and approves to keep pace. What does this show?  
> ✔ Two independent failures, volume and missing context, so fixing only one still leaves the review failing

- Why: Stem replays the transcript (400 items a day, output plus approve button, approving to keep pace); the two-failure lesson is otherwise covered by d5s5q12, q08 and q14.
- **Replace with principle:** Routing by volume rather than stakes fails two ways: it overwhelms reviewers so review quality degrades, or it lets a high-stakes, irreversible action through with no gate at all (the second half is untested). (`03.txt:183`)
- Stem sketch (single, concept `volume-routing-risk`): To save reviewer time, a team sends only its highest-volume workflow to review, while a low-volume workflow that performs irreversible account closures runs ungated. Which risk does this show? Correct: routing by volume rather than stakes leaves a high-stakes irreversible action with no gate. Distractors: consent fatigue from plan review; miscalibrated confidence; sampled review guarding each outcome.

**d5s6q10** · _recall_ · example: `03/residency-logging-drift-audit`  
> Months after launch, a logging configuration began writing request metadata to a second region. Why was this not caught until audit?  
> ✔ No one owned the residency control, and no evidence artifact tracked where data was landing

- Why: Stem retells the deployment story (months later a logging change wrote request metadata to a second region, not caught until audit) and asks why.
- **Replace with principle:** A control specified with no owner and no evidence is invisible at the audit: it can stop operating with no one accountable, and the gap surfaces in review rather than in design, which is the most expensive place to find it. (`03.txt:232`)
- Stem sketch (single, concept `unowned-control-risk`): A compliance register lists a control for every obligation, but none has a named owner or an evidence artifact. What is the main risk? Correct: a control can stop operating with no one accountable, and the gap surfaces at audit, the most expensive place. Distractors: the route becomes unauthorized; the register must be rewritten per framework each year; liability moves to the model provider.

**d5s6q12** · _reused-setup_ · example: `03/residency-logging-drift-audit`  
> The team's compliance mapping was written once at design time, with no owners and no logging wired to show controls operating. What is the most accurate diagnosis?  
> ✔ They mistook surviving the pre-filter for establishing compliance, leaving controls unowned and unprovable

- Why: Stem re-creates the example's setup in substance (mapping written once at design time, no owners, no logging wired) and asks for the example's diagnosis.
- **Replace with principle:** A control, an owner and a living evidence artifact per obligation is more governance than an entry-point choice and spans security, legal and platform owners, who must each agree on who holds what. (`03.txt:231`)
- Stem sketch (single, concept `governance-spans-owners`): Why is turning each obligation into a control with an owner and a living evidence artifact more complex than choosing a compliant entry point? Correct: it spans security, legal and platform owners who must agree on who holds what for each obligation. Distractors: each framework needs a separate delivery route; the vendor must produce the evidence; owners are assigned only after the first audit.

**d5s6q13** · _reused-setup_ · example: `03/residency-logging-drift-audit`  
> At audit, a reviewer asks for evidence that data stayed in-region and the team produces a design document. How will the reviewer treat it?  
> ✔ As insufficient, since a control that no one can demonstrate is indistinguishable from one that is not running

- Why: Stem re-creates the audit moment of the residency story (reviewer asks for in-region evidence, team produces a design document).
- **Replace with principle:** Reviewers accept proof that a control is live (signed agreement, configuration screen, authorization record, returned log query), not a design document naming a control; for the transparency obligation the accepted evidence is a sample reconstruction of one decision from the live log. (`03.txt:228; 03.txt:220-222`)
- Stem sketch (single, concept `evidence-live`): For the obligation that decisions be reconstructable on demand, a team offers a design document describing its decision log. What would a reviewer accept instead? Correct: a sample reconstruction of one decision from the live log. Distractors: a signed copy of the design document; a diagram of the logging pipeline; a statement that logging will be enabled before the audit.

### Learn / trap cards to rewrite

**d5s1 learn[4]** · example: `03/cross-unit-disclosure-postmortem`  
- Now: The cross-business-unit postmortem: a rule assumed covered by trained refusals existed in no layer, and the failure was silent.
- **Rewrite:** Each added layer costs latency and engineering; four layers are four places to design, version and test, and the system prompt and screening logic drift apart if not governed together. (`03.txt:26-27`)

**d5s4 learn[3]** · example: `03/credit-decision-checklist`  
- Now: The checklist asks whether you can reconstruct a decision and query comparable cases; Discernment is the AI Fluency competency of judging outputs.
- **Rewrite:** If you cannot reconstruct a decision you cannot reliably explain it; Discernment is the AI Fluency competency of judging outputs, and a transparency record lets a reviewer spot a skewed outcome. (`03.txt:247; 03.txt:136`)

**d5s5 traps[1]** · example: `03/400-item-review-queue`  
- Now: Fixing one failure: the 400-item queue has two independent failures, volume and missing context, so both must be fixed.
- **Rewrite:** Half a fix: volume and missing context fail independently, so route by stakes and also show the inputs and flag reason; either fix alone still leaves review failing. (`03.txt:249; 03.txt:175; 03.txt:183`)

**d5s6 traps[4]** · example: `03/residency-logging-drift-audit`  
- Now: Residency copies: logs, caches and monitoring paths can write to a second region unless the data-flow record covers them.
- **Rewrite:** Residency copies: pinning processing to a region is not enough; validate that logs, caches, monitoring and retention paths stay inside the approved boundary. (`03.txt:217-218`)

<details><summary>Borderline — considered and kept (13)</summary>

- **d5s1q09**: 'Claude passed every red-team prompt, so the partner policy is covered' mirrors the cross-unit setup hook (03:31), but the hook is a generic misconception with no example particulars (no business units, no in-domain request); answer rests on 03:3, 03:5, 03:243.
- **d5s1q10**: 'Another customer's order information' comes from the general statement at 03:5 (catalogue: cross-customer-order-eg, low risk), not from a worked example.
- **d5s2q11**: 'One output classifier at the end, reviewer calls the design complete' echoes the refund setup hook (03:94) but has none of the trace particulars (no refund, agent or tool run); answer is the general rule 03:57 and recap 03:245.
- **d5s2q16**: Mentions a refund tool call, but 'issuing a refund' is a general example action at 03:56; the stem (auditor replaying an authorization) does not re-create the trace; answer is 03:70.
- **d5s3q04**: Stem and answer test the general stated-purpose baseline (03:84); only the explanation cites the notes' 'formatting skill that phones home' illustration, which could be trimmed when d5s3q11 is replaced.
- **d5s5q12**: 'Routes every output to review as the conservative default' matches the generic setup-hook framing (03:186), and the answer is restated generally in recap 03:249; no 400-item / approve-button particulars.
- **d5s6q01**: 'Chose a route that survives HIPAA and considers compliance settled' resembles 03:237, but the example is a residency story; the stem uses HIPAA and tests the general pre-filter-is-not-proof rule (03:199, 03:235, recap 03:250).
- **d5s6q09**: Stem and answer are the general drift fact (03:230); only the explanation adds 'The residency story shows...', which should become a general sentence when the bank is edited.
- **d5s6q15**: Residency plus a configuration change is close to the drift story, but there is no second-region / logging-metadata plot; answer is the general owner-plus-revalidated-evidence rule (03:230, 03:251).
- **d5s1 traps[1] (card)**: 'Red-team confidence' restates the generic setup hook (03:31) and general lesson (03:3, 03:5) without cross-unit particulars.
- **d5s2 traps[0] (card)**: 'Single end filter' states the generalised rule (03:103, recap 03:245) with no trace particulars.
- **d5s4 traps[0] (card)**: 'Vendor owns fairness' paraphrases the generic setup hook (03:144) and recap 03:247, with no review quote or regulator plot. Optional tighter rewrite: 'Vendor owns fairness: provider bias evaluations cannot see your own corpus, framing, examples or routing.'
- **d5s4 traps[4] (card)**: 'No reconstruction' echoes 03:148 ('disprove the source') but is essentially recap 03:247. Optional rewrite: 'No reconstruction: if you cannot replay a decision, you cannot reliably explain it.'

</details>


## Domain 6: Stakeholder/Lifecycle  (19 questions, 11 cards)

### Questions to remove and replace

**d6s1q07** · _recall_ · example: `04/translation-table-sample-rows`  
> A stakeholder says, 'It just needs to read the form and route it.' Which translation-table row is correct?  
> ✔ Implied constraint: routing is a deterministic business rule; decision: Claude extracts, the rule engine routes

- Why: Quotes the 'read the form and route it' sample row verbatim and the answer is that row's specific constraint and decision, which the catalogue lists as example particulars.
- **Replace with principle:** Each discovery item becomes one row; one row per item keeps the reasoning intact as the work moves from discovery into design and keeps assumptions top of mind. (`04.txt:23; 04.txt:367`)
- Stem sketch (single, concept `translation-table-structure`): Why does the translation table hold exactly one row per discovery item? Correct: it keeps each item's reasoning intact from discovery into design and keeps assumptions visible. Distractors: it keeps the table short enough for executives; it lets each row be assigned to a vendor; it replaces the governance table after launch.

**d6s1q08** · _recall_ · example: `04/translation-table-sample-rows`  
> A stakeholder says, 'Clinicians will review the output anyway.' What architectural decision does this statement force?  
> ✔ Build a mandatory human-in-the-loop authorization step before output becomes part of the record

- Why: Quotes the 'Clinicians will review the output anyway' sample row and asks for that row's decision (also echoes the hospital case's review step).
- **Replace with principle:** A discovery call that runs long enough to identify the real constraints is far cheaper than redesigning after a hidden constraint emerges during legal or compliance review. (`04.txt:45`)
- Stem sketch (single, concept `unstated-constraint-cost`): A sponsor wants discovery cut to one short call to start building sooner. What is the best response? Correct: a call long enough to find the real constraints is far cheaper than redesigning when a hidden constraint surfaces at legal or compliance review. Distractors: constraints are cheaper to find during the build; compliance review will supply the missing requirements; a prototype will reveal every constraint.

**d6s1q09** · _recall_ · example: `04/hospital-dictation-discovery-call`  
> In the hospital dictation case, the stakeholder called the review step 'just a quick check'. What did it actually turn out to be?  
> ✔ A required licensed-clinician authorization gate before output reached the patient record

- Why: Asks what the hospital case's 'just a quick check' turned out to be; pure recall of the example's outcome.
- **Replace with principle:** Discovery reveals whether you are solving the right problem: listen to what the business is trying to achieve, identify the constraints hidden inside that description, and leave the call with a record the design can follow. (`04.txt:3`)
- Stem sketch (single, concept `discovery-purpose`): What should an architect leave a discovery call with? Correct: a record of the constraints hidden in the business description that the design can follow. Distractors: an agreed architecture sketch; a prototype date; a ranked feature list.

**d6s1q12** · _recall_ · example: `04/translation-table-sample-rows`  
> A stakeholder says, 'We are in healthcare, so be careful with data.' How should the translation table treat this?  
> ✔ Constraint: likely proof obligation under health-privacy rules; decision: audit-trail evidence from day one

- Why: Quotes the 'We are in healthcare, so be careful with data' sample row and asks for that row's constraint and decision.
- **Replace with principle:** What the system must prove: in regulated workflows, proof obligations are part of the requirement set, and identifying them in discovery is far cheaper than during a legal review weeks later (q11 and q16 also touch this; keep the new stem in a non-healthcare setting). (`04.txt:20`)
- Stem sketch (single, concept `must-prove-obligation`): During discovery for a lending workflow, when should the evidence the deployment must produce for regulators be identified? Correct: in discovery, as part of the requirement set, because finding it in a later legal review costs far more. Distractors: after the pilot proves value; at the first audit; when the outcome document is written.

**d6s1q13** · _recall_ · example: `04/hospital-dictation-discovery-call`  
> In the hospital dictation call, which THREE constraints surfaced weeks later because the architect began sketching before the question set was finished? Select THREE.  
> ✔ Licensed-clinician authorization was required before output reached the record; Protected health information passed through the context window without the required handling; The network spanned two states with different retention rules that a single-region design ignored

- Why: Asks which THREE constraints surfaced in the hospital dictation call (clinician gate, PHI in context, two-state retention): example particulars.
- **Replace with principle:** The translate step turns the stated business goal into requirements, assumptions and unresolved constraints, showing what the design must support, what still needs confirmation and what could block the solution later. (`04.txt:7`)
- Stem sketch (multi, concept `listen-translate-write`): Which THREE outputs does the 'translate' step of the discovery filter produce? Select THREE. Correct: requirements; assumptions; unresolved constraints. Distractors: an architecture sketch; a prototype date; a vendor shortlist.

**d6s1q17** · _reused-setup_ · example: `04/seamless-translation`  
> A stakeholder wants the tool to 'feel seamless'. Follow-up questions reveal users should never re-enter data that already exists upstream, and exceptions should move quietly to a human reviewer. Which TWO requirement types do those two answers become? Select TWO.  
> ✔ An upstream integration requirement; A human handoff rule

- Why: Stem replays the example's specific follow-up answers (no re-entry of upstream data, exceptions moving quietly to a human reviewer) and asks for the 04:12 mapping that exists only inside the example passage.
- **Replace with principle:** A testable, bounded constraint is what the design can be built against; a stakeholder preference only tells you where to investigate, and the follow-up questions produce the constraint itself. (`04.txt:14`)
- Stem sketch (single, concept `preference-hides-constraint`): After a discovery call, which item is ready to design against? Correct: a testable, bounded constraint produced by follow-up questions (e.g. a stated response-time budget). Distractors: the stakeholder's experience word recorded verbatim; a ranked feature wish list; the architect's preferred pattern.

**d6s1q18** · _recall_ · example: `04/seamless-translation; 04/translation-table-sample-rows`  
> In the discovery translation table, which required architectural decision belongs on the row for 'We want this to feel seamless'?  
> ✔ Set a p95 latency target as a design constraint and design a graceful, internal-safe failure state

- Why: Asks for the decision column of the seamless sample row (p95 target plus internal-safe failure state), a catalogued example particular.
- **Replace with principle:** When a stakeholder uses an experience word (seamless, easy, fast, simple, intuitive), treat it as a signal for more discovery and ask what would break the experience, what the user must never notice, what has to happen behind the scenes, and what must still be true when something goes wrong. (`04.txt:13`)
- Stem sketch (multi, concept `preference-hides-constraint`): A stakeholder wants the tool to be 'fast and easy'. Which THREE follow-up questions does structured discovery recommend? Select THREE. Correct: what would break that experience; what the user must never notice; what must still be true when something goes wrong. Distractors: which model tier is newest; which features competitors ship.

**d6s1q20** · _reused-setup_ · example: `04/translation-table-sample-rows`  
> A stakeholder says the form just needs to be routed by type, but nobody has confirmed who maintains the routing rules. How should the translation-table row handle this?  
> ✔ Record the decision and label an assumption that routing logic is owned outside the model, to confirm the owner

- Why: Re-creates the routing sample row (form routed by type, routing-rule owner unconfirmed) and its answer is that row's assumption ('routing logic owned outside the model, confirm owner').
- **Replace with principle:** When a constraint is not yet confirmed, the translation-table row still records the decision and labels the assumption explicitly, so the design traces to the business case and assumptions stay visible. (`04.txt:23; 04.txt:367`)
- Stem sketch (single, concept `translation-table-structure`): A stakeholder says all users sit in one country, but nobody has confirmed it with the data owner. How should the discovery record handle this? Correct: record the item as a row and label the assumption for confirmation. Distractors: leave it out until confirmed; write it as a settled fact; defer it to the compliance review.

**d6s1q23** · _example-only-lesson_ · example: `04/hospital-dictation-discovery-call`  
> In a hospital dictation call, a clinician authorization gate, PHI handling rules and two-state record-retention rules all surfaced weeks later. Which TWO discovery categories would have caught them with a direct question? Select TWO.  
> ✔ What the system must prove; What the system must not do

- Why: Re-creates the hospital case (clinician gate, PHI, two-state retention) and its answer rests on 04:59, a lesson stated only inside the example; must-not-do/must-prove explicitness is already covered by q05, q06, q11, q16.
- **Replace with principle:** Write discovery items down before the conversation moves on: the design needs a clear record, and without it the design inherits the architect's assumptions, with the mismatch surfacing late when changing trajectory is slower, harder and more expensive. (`04.txt:8`)
- Stem sketch (single, concept `listen-translate-write`): Why should discovery items be written down before the conversation moves on? Correct: without the record the design inherits the architect's assumptions and the mismatch surfaces late, when change is most expensive. Distractors: so the stakeholder can sign a contract on the spot; because notes are needed only for the sales hand-off; so the call can be shortened.

**d6s2q13** · _recall_ · example: `04/cto-four-cents-context-approval`  
> In the CTO review, the approved context-strategy recommendation led to a surprise invoice. Which THREE things were never communicated to the CTO? Select THREE.  
> ✔ That per-call cost multiplied by call volume produced a five-figure monthly line; That a static document could have been cached to cut the input cost; That unwinding a full-context design later would carry its own cost

- Why: Asks which THREE things were never communicated to the CTO (monthly line, caching, unwind cost): recall of the case's particulars.
- **Replace with principle:** Tradeoff-map row for a larger context window versus retrieval: the reversal cost of a wrong choice is reworking the architecture after cost spikes in production, plus the credibility hit of explaining an avoidable expense surprise (q09 tests only the caching give-up). (`04.txt:83-86`)
- Stem sketch (single, concept `context-vs-retrieval-caching`): On the tradeoff translation map, what does a wrong, reversed choice of 'larger context window per call over retrieval' cost? Correct: reworking the architecture after cost spikes in production, plus the credibility hit of an avoidable expense surprise. Distractors: a compliance gap from reduced logging; a blocked cutover from a residency rule; losing the full document in view.

**d6s2q14** · _recall_ · example: `04/cto-four-cents-context-approval`  
> The CTO later wrote, 'I approved a direction, not a number.' What does this show about the earlier presentation?  
> ✔ An accurate answer to the question asked can still miss the version of the question that mattered

- Why: Quotes the CTO's note ('I approved a direction, not a number') and asks what it shows; requires knowing the case.
- **Replace with principle:** False alignment is avoided by naming all three elements every time, and naming the reversal cost especially when the design feels obviously simpler, because an approval without understanding reversal cost is not an informed choice. (`04.txt:143; 04.txt:158 (generalised lesson); 04.txt:369 (first sentence only)`)
- Stem sketch (single, concept `false-alignment`): When is it most important to name the reversal cost explicitly in a tradeoff presentation? Correct: when the recommended design feels obviously simpler. Distractors: only when the stakeholder asks about cost; only in regulated environments; only after the first invoice arrives.

**d6s3q01** · _reused-setup_ · example: `04/support-assistant-drift (+ 04/ninety-day-alert-log 'less useful')`  
> A customer support assistant launched well, and months later users complain that answers are 'less useful'. Which description of how this typically happens is correct?  
> ✔ Quality erodes gradually as usage patterns change, rather than failing all at once

- Why: Stem re-creates the support-assistant example (launched well, then degrades) and borrows the ninety-day log's 'less useful' complaint; the general answer can be tested with a fresh scenario.
- **Replace with principle:** A live deployment drifts without active monitoring: nothing breaks dramatically, quality erodes gradually, and a team without a feedback loop may not see the decline until users already feel it. (`04.txt:163`)
- Stem sketch (single, concept `drift-without-monitoring`): An internal policy Q&A tool has been live for a year with no feedback loop. Which pattern of degradation should the architect expect? Correct: gradual erosion of quality that may go unseen until users feel it. Distractors: a single dramatic outage; a sudden drop on the day of a model update; quality that holds until the first quarterly review.

**d6s3q12** · _reused-setup_ · example: `04/ninety-day-alert-log`  
> Over 90 days an eval score drifts down for weeks while the error rate stays flat, and no review happens until week 12. What best explains the miss?  
> ✔ No rule mapped slow quality drift to a trigger, owner or action, so nothing decided it mattered

- Why: Stem replays the ninety-day trace (90 days, eval drifting for weeks, flat error rate, no review until week 12) and asks for its root cause.
- **Replace with principle:** A signal by itself is not yet a decision: one spike may be noise, another may point to a real problem, and a third may matter only if it keeps happening; the feedback loop supplies the judgment observability lacks. (`04.txt:165`)
- Stem sketch (single, concept `loop-vs-observability`): Observability shows a one-off latency spike, a sustained eval-score decline and an intermittent tool error. Why can't these signals simply be acted on as they arrive? Correct: a signal is not yet a decision; some are noise and some matter only if they recur, so a decision layer must triage them. Distractors: signals need vendor approval first; only error-rate signals are actionable; every signal must go straight to a stakeholder.

**d6s3q13** · _reused-setup_ · example: `04/ninety-day-alert-log`  
> After the 90-day drift, what should the architect build to prevent a repeat?  
> ✔ A governance table mapping each signal, slow drifts included, to a trigger, action and owner

- Why: Stem is framed as 'After the 90-day drift', so it depends on the example; the general fix (map every signal to trigger, action and owner) is worth keeping with a fresh stem.
- **Replace with principle:** A dashboard collects and displays signals; a feedback loop maps each signal to a trigger, an owner and a required action, covering slow drifts as well as hard failures, via a governance table built before launch. (`04.txt:237 (generalised lesson); 04.txt:187`)
- Stem sketch (single, concept `monitoring-not-loop`): A team has live dashboards and configured alerts and says stakeholder feedback is therefore covered. What is missing to make this a feedback loop? Correct: a governance table mapping each signal, slow drifts and hard failures alike, to a trigger, owner and action. Distractors: more latency percentiles; a lower error-rate threshold; a longer launch review.

**d6s3q20** · _example-only-lesson_ · example: `04/ninety-day-alert-log`  
> An eval score has drifted downward for two weeks while the error rate stays flat. In a well-designed feedback loop, what should the escalation path be?  
> ✔ Trigger an Architect review first, then a stakeholder review once diagnosis confirms the drift

- Why: Correct answer (Architect review first, then stakeholder review once diagnosis confirms) comes only from the ninety-day table's 'what the loop should have done' row (04:229); explanation also cites the 90-day case.
- **Replace with principle:** Deciding which signals deserve attention and which are noise is the hardest part of the feedback loop, because observability tooling cannot make that judgment for you. (`04.txt:211`)
- Stem sketch (single, concept `signal-noise-judgment`): Which part of running a feedback loop does observability tooling NOT do for the architect? Correct: judging which signals deserve attention and which are noise. Distractors: collecting latency and error metrics; displaying eval scores on dashboards; firing alerts when a configured threshold is crossed.

**d6s3q21** · _example-only-lesson_ · example: `04/ninety-day-alert-log`  
> A team's feedback loop sends every quality-drift trigger straight to the business stakeholder before anyone has examined the cause. Which step does this skip?  
> ✔ An Architect review that diagnoses and confirms the drift before stakeholder escalation

- Why: Tests the same Architect-before-stakeholder escalation order that is stated only in the ninety-day example row (04:229).
- **Replace with principle:** The feedback loop creates ongoing Architect effort, but that is cheaper than discovering decline in a quarterly review after every dashboard looked good. (`04.txt:210`)
- Stem sketch (single, concept `loop-cost`): A sponsor questions the ongoing Architect time a feedback loop needs after launch. What is the best justification? Correct: it costs less than discovering decline at a quarterly review after every dashboard looked good. Distractors: it removes the need for an observability stack; it is a one-off setup cost; regulators require a fixed weekly hours budget.

**d6s4q10** · _recall_ · example: `04/fin-services-handoff-rationale`  
> In the financial-services handoff, the replacement switched context strategies and broke data residency. What did the diagram fail to carry?  
> ✔ The reason the original strategy was chosen, as a decision with a named tradeoff

- Why: Asks what the diagram failed to carry 'in the financial-services handoff': recall of the postmortem.
- **Replace with principle:** The documentation discipline is recording why, not just what, and labelling assumptions as assumptions, which is easy to skip when the reasoning feels obvious to the person who lived it. (`04.txt:273`)
- Stem sketch (single, concept `diagram-lost-why`): Why is design rationale the part of documentation most often skipped? Correct: recording why, not just what, feels redundant when the reasoning is obvious to the person who lived it. Distractors: auditors forbid rationale in the record; diagrams already capture rationale; rationale belongs only in the outcome document.

**d6s4q11** · _recall_ · example: `04/fin-services-handoff-rationale`  
> In that postmortem, why was the replacement unable to avoid the failure?  
> ✔ They did not realise the strategy was load-bearing for compliance, because no rationale was documented

- Why: 'In that postmortem, why was the replacement unable to avoid the failure?': requires knowledge of the example's sequence of events.
- **Replace with principle:** Write the rationale at design time, while you still hold the reasoning: writing it takes time, but reconstructing it later from email threads, or failing to, costs a wrong reversal in production; if it is never written, it leaves with you. (`04.txt:272; 04.txt:298 (last sentence); 04.txt:373`)
- Stem sketch (single, concept `diagram-lost-why`): When should the decision, rejected alternatives and tradeoff be written down? Correct: at design time, while the architect still holds the reasoning. Distractors: at handoff, from email threads; when an auditor requests it; after the first production change shows which decisions mattered.

**d6s5q12** · _reused-setup_ · example: `04/cfo-claims-outcome-doc`  
> A sponsor presents 40,000 requests a month, sub-two-second latency and a low error rate. The CFO asks what the deployment changed. What was missing?  
> ✔ A before-and-after comparison on the targeted business metric, such as processing time

- Why: Stem replays the anecdote's particulars (40,000 requests a month, sub-two-second latency, low error rate, CFO asks what it changed).
- **Replace with principle:** The outcome document makes the deployment's value understandable to people who were not on the build, chiefly the sponsor who must justify it upward; technical metrics alone do not make it, the before-and-after business outcomes do, and a metrics-only document cannot justify expansion. (`04.txt:308 (first and third sentences only; exclude the reuse field/notes); 04.txt:349; 04.txt:363 (exclude 'add the reuse note')`)
- Stem sketch (single, concept `outcome-document-fields`): Whom is a customer outcome document chiefly written for, and what must it let them do? Correct: the sponsor and others outside the build, who must justify the deployment upward using before-and-after business outcomes. Distractors: the on-call engineer, to debug incidents; the observability vendor, to tune exports; the original build team, as a change log.

### Learn / trap cards to rewrite

**d6s1 learn[1]** · example: `04/seamless-translation`  
- Now: A stated preference ('seamless', 'easy', 'fast') hides a constraint; ask what would make it feel not seamless to reach latency budget, no re-entry, quiet human handoff and safe failure path.
- **Rewrite:** A stated preference ('seamless', 'easy', 'fast') hides a constraint; ask what would break the experience, what the user must never notice, what happens behind the scenes, and what must hold when something fails. (`04.txt:13-14`)

**d6s1 learn[3]** · example: `04/translation-table-sample-rows`  
- Now: A translation-table row holds: stakeholder statement, implied constraint, required architectural decision, and assumption documented (e.g. routing belongs in the rule engine; clinician review is a mandatory HITL gate).
- **Rewrite:** A translation-table row holds: stakeholder statement as said, implied constraint, required architectural decision, and the assumption documented while unconfirmed. One row per item keeps the reasoning intact into design. (`04.txt:23`)

**d6s1 learn[4]** · example: `04/hospital-dictation-discovery-call`  
- Now: The expensive failure is an unstated constraint that surfaces at legal or compliance review. In the hospital dictation case, sketching started before the four buckets were finished.
- **Rewrite:** The expensive failure is an unstated constraint that surfaces at legal or compliance review. Finish the four-category question set before proposing anything; a confident sketch is the moment the questions stop. (`04.txt:47; 04.txt:50; 04.txt:61`)

**d6s1 traps[2]** · example: `04/hospital-dictation-discovery-call; 04/translation-table-sample-rows`  
- Now: Quick check dismissal: 'it's just a quick review' may be a licensed-clinician authorization gate, which is architectural, not optional.
- **Rewrite:** Review dismissal: treat every 'it's just a review' as a constraint to chase down; it may be a required architectural gate, not an optional convenience. (`04.txt:61`)

**d6s1 traps[3]** · example: `04/translation-table-sample-rows`  
- Now: Model owns routing: 'read the form and route it' implies a deterministic rule; Claude extracts and the system routes.
- **Rewrite:** Over-assigning to Claude: the must-do bucket separates the work Claude owns from the work that stays with an existing system or a human. (`04.txt:17`)

**d6s2 learn[4]** · example: `04/cto-four-cents-context-approval`  
- Now: False alignment: a decision looks approved in the room but reversal cost was never made explicit; the CTO who approved 'a direction, not a number' is the case.
- **Rewrite:** False alignment: a decision looks approved in the room but reversal cost was never made explicit; name the reversal cost especially when the design feels obviously simpler. (`04.txt:143; 04.txt:158`)

**d6s2 traps[1]** · example: `04/cto-four-cents-context-approval`  
- Now: Answering only what was asked: the per-call cost answer was accurate, yet the monthly bill and unwind cost never entered the conversation.
- **Rewrite:** Answering only what was asked: an accurate technical answer can still miss the approver's real question, what happens to the business if the choice is wrong and must be reversed. (`04.txt:70; 04.txt:73`)

**d6s3 traps[1]** · example: `04/ninety-day-alert-log`  
- Now: Error-rate alerting only: quality can fall for weeks while the error rate stays flat, so no hard alert fires.
- **Rewrite:** Hard-failure alerting only: a slow quality drift may never cross an error threshold, so the governance table must map slow drifts as well as hard failures to triggers. (`04.txt:163; 04.txt:237`)

**d6s4 traps[0]** · example: `04/fin-services-handoff-rationale`  
- Now: Diagram as documentation: a diagram shows what the system is but loses why, so a successor can reverse a load-bearing decision.
- **Rewrite:** Recording what, not why: a design without its rationale cannot be safely changed, so a successor may reverse a load-bearing decision and reintroduce a constraint violation. (`04.txt:273-274; 04.txt:298`)

**d6s4 traps[3]** · example: `04/fin-services-handoff-rationale (minor wording)`  
- Now: Right decision, wrong reason: without rejected alternatives, a successor reverses the right decision for an understandable wrong reason.
- **Rewrite:** Right decision, wrong reason: without rejected alternatives, a successor reverses the right decision for the wrong reason or defends the wrong one. (`04.txt:243`)

**d6s5 traps[4]** · example: `04/cfo-claims-outcome-doc`  
- Now: Easy metrics: volume, latency and error rate show the system runs, not what it changed; without a before metric the story cannot be told.
- **Rewrite:** Easy metrics: technical metrics exported from the observability stack show the system runs, not what it changed; without a before metric on the business outcome there is no case for expansion. (`04.txt:308; 04.txt:349; 04.txt:363`)

<details><summary>Borderline — considered and kept (15)</summary>

- **d6s1q01**: 'Feel seamless' is the canonical experience word used throughout the general text (catalogue notes it is not a hidden particular); the answer is 04:11/04:13 and no example-specific follow-up answers are used.
- **d6s1q02**: Fresh stem ('simple and intuitive', claims director); 'claims' is only a generic industry word; answer is 04:13.
- **d6s1q11**: Generic stem (compliance demands an audit trail six weeks in); 'six weeks' is not tied to the CTO case and the answer is the general must-prove rule (04:20).
- **d6s1q21**: Generic stem; the setup is stated generally at 04:50 and the answer is the generalised lesson at 04:61. Explanation has a hospital-case clause; see explanation_trims.
- **d6s1q22**: Answer is the generalised lesson at 04:61 (recap 04:367), not a particular of the hospital case.
- **d6s2q09**: Mentions a static policy document held in context, but that wording is in the general tradeoff-map row (04:85), not only in the CTO case; no four-cents/CTO particulars.
- **d6s2q10**: d6s2q11 likewise: both test rows of the general tradeoff translation map (04:87-94), which the catalogue does not list as an example.
- **d6s3q06**: Uses 'claims deployment' only as a generic industry word; no example particulars.
- **d6s3q08**: Its 'five-figure monthly line' explanation is stated as a general fact at 04:184 (catalogue confirms).
- **d6s3q22**: Healthcare documentation obligation with periodic output audits is the generic category example at 04:186 that doubles as the general rule (catalogue: regulated-scheduled-review-egs).
- **d6s3q23**: Answer is the general rule at 04:187 (table exists before launch). Explanation references the 90-day case; see explanation_trims.
- **d6s5q07**: Stem uses 'a Bedrock endpoint for a regulated data path', a phrase from the minor illustration at 04:306, but it sits inside the general paragraph and the answer is the general task-creep rule. Swap to a neutral entry point if you want zero overlap.
- **d6s5q13**: Capturing the before metric at the start is the generalised lesson (04:363, recap 04:375); no CFO-anecdote particulars in the stem.
- **d6s5q14**: Control-in-place purpose is stated in the template (04:343, 'auditable rather than merely asserted'); no anecdote particulars.
- **d6s5q16**: Has a CFO distractor, but the CFO as the reader a sponsor must satisfy is in general text (04:351); the answer is the template field (04:345).

</details>


## Domain 7: Dev Productivity  (8 questions, 4 cards)

### Questions to remove and replace

**d7s1q02** · _recall_ · example: `05 / 200-person-rollout`  
> A 200-person engineering org wants Claude Code across four departments. Which rollout plan matches the pattern that works best?  
> ✔ One champion per department converts a real workflow over two weeks, then runs a 45-minute session for five peers

- Why: Stem copies the worked example's setup (200-person org, four departments) and the correct option is the example's specific plan (two weeks, 45-minute session, five peers).
- **Replace with principle:** Team adoption rarely succeeds as a single all-hands switch-on; a champion per department or team is granted access first, proves the workflow in practice, then seeds adoption batch by batch. (`05.txt:7`)
- Stem sketch (single, concept `rollout-champions`): An organization wants Claude Code adopted across several teams. Which rollout approach does the guidance recommend? Correct: a champion per team gets access first, proves a real workflow, then seeds adoption batch by batch. Distractors: switch everyone on at once; leave it to whoever is keenest; Architect-run central training only. No headcounts, durations or session sizes.

**d7s1q14** · _example-only-lesson_ · example: `05 / 200-person-rollout`  
> A director proposes enabling Claude Code for all four engineering departments on the same day through a single announcement email. What outcome does the rollout guidance predict?  
> ✔ Confused first-time prompts spike, then people quietly retreat to old habits

- Why: Stem re-creates the example's counterfactual (four departments, single mass email) and the correct answer (spike of confused first prompts, quiet retreat to old habits) is stated only inside the worked example at 05:9.
- **Replace with principle:** Standing up a team environment costs setup time up front (shared config, a rollout plan, skills packaging) but is far cheaper than later reconciling many individual configurations that have drifted apart. Untested in the bank; the rollout-champions principle itself is already covered by d7s1q03 and the d7s1q02 replacement. (`05.txt:37`)
- Stem sketch (single, concept `team-setup-cost`): A manager questions the up-front effort of a shared config, rollout plan and skills packaging before letting developers use Claude Code. What does the guidance say about this cost? Correct: it costs setup time but is far cheaper than reconciling drifted personal configurations later. Distractors: it is pure overhead best skipped for small teams; it should be deferred until after the first bill; it only pays off for API users.

**d7s2q07** · _reused-setup_ · example: `05 / release-notes-skill-no-rollback`  
> A 40-engineer platform group needs a release procedure that is group-scoped, receives versioned updates and can be rolled back. What is the best distribution choice?  
> ✔ Bundle it into a plugin and assign it to the group, with a named owner

- Why: Stem reuses the example's distinctive particulars (a platform group of 40 engineers, a release procedure, need for versioning and rollback) even though the answer is the general plugin rule.
- **Replace with principle:** When a shared asset needs versioning, group targeting or rollback, distribute it through a plugin assigned to the group (group targeting, install preferences, version-controlled updates from a connected repo) and identify an owner; the recap restates plugins as the mechanism for group targeting with versioned updates and rollback. (`05.txt:102 (also 05.txt:12, 05.txt:24, closing sentence of 05.txt:35)`)
- Stem sketch (single, concept `plugin-governance`): A data-science group needs a shared analysis procedure that only its members receive, updated from a connected repository, with a way back if an update misbehaves. Which distribution choice fits best? Correct: bundle it in a plugin assigned to that group, with a named owner. Distractors: org-provisioned upload; copy into personal folders; server-managed settings.

**d7s2q08** · _recall_ · example: `05 / release-notes-skill-no-rollback`  
> A release-notes skill was pushed as a flat bundle to forty engineers. One prompt edit broke its format for every team, and the fix was a manual re-edit while bad output kept shipping. What was the core mistake?  
> ✔ It was distributed without versioned updates and rollback, so one edit propagated everywhere

- Why: Asks for the core mistake in the release-notes example and relies on its plot (flat bundle, forty engineers, one prompt edit, manual re-edit while bad output shipped).
- **Replace with principle:** The biggest failure mode in team setup is a shared asset (a skill or a config) with no versioning or rollback, so one bad change propagates to the whole team before anyone can stop it. Only d7s2q10 tests this once the release-notes questions are removed. (`05.txt:39`)
- Stem sketch (single, concept `shared-asset-liability`): A team's shared configuration is edited in place and pushed to every developer with no version history and no way to revert. What does the guidance identify as the biggest failure mode of this setup? Correct: one bad change reaches the whole team before anyone can stop it. Distractors: spend caps are exhausted faster; users cannot toggle it off; only its author can run it.

**d7s2q09** · _recall_ · example: `05 / release-notes-skill-no-rollback`  
> After the release-notes incident, what distribution change best prevents a repeat?  
> ✔ Distribute it inside an organization-managed plugin with an identified owner

- Why: Stem opens 'After the release-notes incident' and requires knowing the example to answer.
- **Replace with principle:** A plugin bundles one or more Skills and is assigned to a group; only that group's members can access those Skills, whereas an org-provisioned Skill reaches everyone and users can only toggle it off. Plugin versioning/rollback is already covered by d7s2q03, d7s2q04 and the d7s2q07 replacement, so this tests the access-scoping half instead. (`05.txt:12 (with 05.txt:21)`)
- Stem sketch (single, concept `plugin-group-access`): A legal team has three related Skills that only its members should be able to use. How should the Architect distribute them? Correct: bundle them into one plugin assigned to the legal group. Distractors: upload them org-wide and ask others to toggle them off; deliver them via server-managed settings; expose them as API Skills.

**d7s3q11** · _recall_ · example: `05 / merge-nobody-could-explain`  
> An AI-assisted change passed review and green tests, then leaked data through an unvalidated input. The author could not explain its handling of that input. What was missing?  
> ✔ A checklist question: can the person merging explain what it does and why?

- Why: Stem retells the example's plot (passed review and green tests, leaked data through an unvalidated input, author could not explain it) and the answer is the example's checklist question.
- **Replace with principle:** A verification checklist must cover all four dimensions (correctness, security, maintainability, human understanding); diligence requires that the author can explain what shipped, captured as a checklist gate before production. (`05.txt:62 and 05.txt:106 (also 05.txt:50)`)
- Stem sketch (single, concept `checklist-dimensions`): A team's checklist for AI-generated changes checks correctness, security and maintainability. Which item adds the missing fourth dimension? Correct: the author can explain what the change does and why. Distractors: the change was generated by the strongest model; the diff is under a size limit; a second AI session approved it.

**d7s4q09** · _recall_ · example: `05 / quarterly-review-retrieval-drift`  
> Dashboards stayed green for a quarter while answer quality slid; the retrieval index had not kept pace with a growing corpus. What was the key gap?  
> ✔ The runbook had no entry tying gradual quality decline to retrieval drift

- Why: Stem retells the example (dashboards green for a quarter, retrieval index not keeping pace with a growing corpus) and asks for the example's key gap.
- **Replace with principle:** The durable fix is to resist firefighting: rather than resolving the issue yourself, help the team create a runbook entry and identify the escalation path so it can resolve the next occurrence without the Architect. The runbook-purpose concept has only one other question (d7s4q06). (`05.txt:98 (with 05.txt:93)`)
- Stem sketch (single, concept `runbook-purpose`): An Architect could fix a recurring incident herself in minutes. What does the guidance call the durable fix? Correct: help the team write a runbook entry and identify the escalation path so it handles the next one. Distractors: fix it personally each time for speed; add more dashboards; route all incidents to the Architect.

**d7s4q10** · _recall_ · example: `05 / quarterly-review-retrieval-drift`  
> What is the biggest operational risk the green-dashboards scenario illustrates?  
> ✔ A slow degradation no one links to a cause, running until a review

- Why: Stem asks what 'the green-dashboards scenario illustrates', so it presupposes knowledge of the worked example, though the answer is the general risk.
- **Replace with principle:** The biggest failure mode in operational support is a slow degradation no one connects to a cause, so it runs until a scheduled review catches it rather than the team catching it the day it starts. (`05.txt:99`)
- Stem sketch (single, concept `slow-degradation-risk`): According to the operational-support guidance, what is the biggest failure mode for a team that owns a deployment? Correct: a slow degradation nobody links to a cause, running until a scheduled review. Distractors: loud outages; alert fatigue; cost masked by caching. No reference to green dashboards or a quarter.

### Learn / trap cards to rewrite

**d7s1 learn[1]** · example: `05 / 200-person-rollout`  
- Now: Rollout runs through a champion per team, then batches; the 200-person example uses two weeks and a 45-minute session for five peers.
- **Rewrite:** Rollout runs through a champion per team who gets access first, proves a real workflow, then seeds adoption batch by batch. (`05.txt:7`)

**d7s1 traps[0]** · example: `05 / 200-person-rollout`  
- Now: All-hands switch-on: a mass enablement looks efficient but causes confused first prompts and a retreat to old habits.
- **Rewrite:** All-hands switch-on: team adoption rarely succeeds that way; without champions absorbing early friction, the Architect becomes the only person answering questions. (`05.txt:7`)

**d7s2 traps[0]** · example: `05 / release-notes-skill-no-rollback`  
- Now: Flat bundle: pushing a skill without versioning lets one bad edit reach every team.
- **Rewrite:** Unversioned shared asset: a skill or config with no versioning or rollback lets one bad change reach the whole team before anyone can stop it. (`05.txt:39`)

**d7s4 traps[1]** · example: `05 / quarterly-review-retrieval-drift`  
- Now: Green dashboards: a gradual quality slide may never trip alerts without a runbook entry for retrieval drift.
- **Rewrite:** Slow degradation: a gradual decline no one connects to a cause runs until a scheduled review catches it, not the day it starts. (`05.txt:99`)

<details><summary>Borderline — considered and kept (7)</summary>

- **d7s1q07**: Mentions a 'release-notes skill', but that is also a generic skill example at 01:666; none of the example's particulars (forty engineers, broken format, flat bundle) appear and the answer is the general rule that server-managed settings are not a Skills path (05:12).
- **d7s1q05**: Generic invented scenario (60 developers, spend doubled, free model choice) not taken from any worked example; tests the general spend-posture statement at 05:33.
- **d7s2q10**: Uses the word 'liability' from the example's closing sentence, but asks only for the general risk stated at 05:39 with no example particulars.
- **d7s2q13**: Lists a release-notes skill among generic assets; no example particulars, and the answer is the general per-asset governance rule at 05:38.
- **d7s3q12**: Concept slug is 'merge-unexplained' (named after the example) but the stem asks generally what judgment erosion looks like, answered from 05:61 and 05:69. Consider renaming the slug to 'judgment-erosion' if d7s3q11 is removed.
- **d7s3q03**: Tests the general workflow-stage table row (05:48-50); no example setup.
- **d7s4q02**: Same symptom as the drift example (gradual quality decline, no code change), but the stem uses only the general symptom-table row (05:80-82) with no example particulars (no green dashboards, quarter or support team).

</details>

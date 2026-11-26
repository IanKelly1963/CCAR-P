# Takeaway coverage audit

Each notes file's closing takeaway section was split into atomic claims; each claim was mapped to its domain(s) and checked for a learn/trap card that **surfaces** it and a question whose correct answer **tests** it. Partner Track parts of 04#2 and 04#5 are excluded.

**Result: 83 of 98 claims covered.** Gaps: 5 missing, 5 weak, 3 tested but not on a card, 2 on a card but not tested.

Section headings: 01: Key takeaways (01:731); 02: Five takeaways (02:486); 03: Five things that hold across everything here (03:241); 04: Key takeaways (04:365); 05: Recap: four things that hold across everything here (05:100)

| Takeaway | Title | Claims | Covered | Gaps |
|---|---|---|---|---|
| 01#1 | Decomposition is the move that comes before architecture | 5 | 3 | 2 |
| 01#2 | Choosing a pattern is choosing how much autonomy to grant | 5 | 5 | 0 |
| 01#3 | Reach for the tested reference architectures before inventing your own | 5 | 3 | 2 |
| 01#4 | Choosing a model: start with Sonnet and treat every swap as a release | 5 | 5 | 0 |
| 01#5 | Pick the entry point by the work it has to do, not by what is already on the shelf | 3 | 2 | 1 |
| 02#1 | Evals as acceptance criteria | 3 | 3 | 0 |
| 02#2 | POC to production | 6 | 3 | 3 |
| 02#3 | Use-case sizing and feasibility | 5 | 3 | 2 |
| 02#4 | Enterprise integration patterns | 3 | 2 | 1 |
| 02#5 | A/B testing and observability | 4 | 4 | 0 |
| 03#1 | Safety is a stack of layers, not a setting | 3 | 3 | 0 |
| 03#2 | A guarded path has three control points and a chosen failure direction | 4 | 3 | 1 |
| 03#3 | Fairness and transparency are instrumented, not assumed | 4 | 3 | 1 |
| 03#4 | Route review by stakes, not by volume | 4 | 4 | 0 |
| 03#5 | A compliant entry point is a prerequisite, and an evidenced control set is the proof | 6 | 5 | 1 |
| 04#1 | Structured discovery | 4 | 4 | 0 |
| 04#2 | Communicating tradeoffs (GTM / demo / joint scoping half EXCLUDED as Partner Track) | 2 | 2 | 0 |
| 04#3 | Feedback loops and SLA management | 3 | 3 | 0 |
| 04#4 | Documentation for handoff and audit | 3 | 3 | 0 |
| 04#5 | Entry point selection and outcomes (reuse note EXCLUDED as Partner Track) | 6 | 5 | 1 |
| 05#1 | Team setup is shared configuration, distribution and spend posture decided up front | 6 | 6 | 0 |
| 05#2 | Adoption is engineered through champions and batches | 3 | 3 | 0 |
| 05#3 | Diligence keeps AI-assisted work trustworthy | 3 | 3 | 0 |
| 05#4 | Operational support is translation plus self-sufficiency | 3 | 3 | 0 |

## Gaps and proposed fixes

### 01#1 · missing
- **Claim:** Decomposition (splitting the work among Claude, existing systems and humans) comes before choosing a pattern or architecture.
- Domains: D1 · surfaced: — · tested: —
- Card (d1s3): Decompose first: assign each part of the request to Claude, existing systems or humans before choosing a pattern; the split tells you what the pattern has to carry.
- Question (d1s3): An architect opens a design review by debating workflow versus agent for a new partner request. What should come first? Correct: split the work into what Claude, existing systems and humans own. Distractors: pick the model tier; choose the entry point; prototype an agent and measure it.
- Source: `01.txt:75 (assigning owners early sets you up for success), 01.txt:733`

### 01#1 · missing
- **Claim:** Skipping decomposition asks Claude to operate without the context a human would have given a colleague.
- Domains: D1, D2 · surfaced: — · tested: —
- Card (d1s3): A design that skips decomposition also hands Claude work without the context a human colleague would have been given; where that context is missing, the model improvises.
- Question (d1s3): Which TWO consequences follow when a design skips decomposition? Select TWO. Correct: Claude does work another system would do more cheaply; Claude operates without context a human would have given a colleague. Distractors: the model tier is fixed too early; human approvals multiply.
- Source: `01.txt:733 (takeaway only; body support is thin, cf. 01.txt:504 'where the prompt is silent, the model improvises'). Low priority.`

### 01#3 · missing
- **Claim:** Reference architectures are documented because other teams already learned what breaks in each; start from them (as references to adapt, not blueprints) rather than inventing your own.
- Domains: D1 · surfaced: — · tested: —
- Card (d1s5): Reference architectures are proven references, not blueprints: start from the shape that fits, adapt it to the workload, and recognise when a workload draws on more than one.
- Question (d1s5): A team plans to design a bespoke architecture from scratch for a recurring class of problem. What is the best advice? Correct: start from the proven reference architecture that fits and adapt it to the workload. Distractors: implement the reference architecture exactly as drawn; combine every reference architecture to be safe; design from scratch because every workload is unique.
- Source: `01.txt:281, 01.txt:737`

### 01#3 · surfaced-not-tested
- **Claim:** When still uncertain what the system must handle, pick one architecture (adapt it); composing two roughly doubles the surface area to maintain.
- Domains: D1 · surfaced: d1s5 traps[4], d1s5 learn[5] · tested: —
- Card (d1s5): When in doubt, pick one: composing two reference architectures roughly doubles the surface to maintain, and a second pattern added out of indecision defers a design decision.
- Question (d1s5): A team unsure what its system will need to handle proposes composing two reference architectures to cover both possibilities. What should the architect recommend? Correct: adapt a single architecture; composing roughly doubles the surface to maintain. Distractors: compose both and drop one after launch; compose both but share one eval set; add a third to hedge further. (d1s5q12 touches this only via a distractor and its explanation.)
- Source: `01.txt:301, 01.txt:305`

### 01#5 · missing
- **Claim:** The right recommendation is one where you can name the tradeoff out loud when you make it; naming it is what later tells you when to switch entry points.
- Domains: D3 · surfaced: — · tested: —
- Card (d3s1): Name the entry point's core tradeoff out loud when you recommend it; the stated tradeoff is the signal that later tells you when the work has outgrown it and a switch is due.
- Question (d3s1): Why should an architect state an entry point's core tradeoff explicitly at the time of recommending it? Correct: it records what was given up, which signals later when to switch. Distractors: it is required for procurement sign-off; it fixes the delivery route; it lets the team skip evals when switching.
- Source: `01.txt:741 (takeaway only; related body point on migration cost is tested in d3s1q24)`

### 02#2 · weak
- **Claim:** Estimate cost at production volume: a low-volume POC bill is a sample, not a production cost model; scale it to expected volume with error bounds.
- Domains: D4, D1 · surfaced: d4s2 traps[0], d1s6 traps[4], d4s2 learn[0] · tested: d4s2q01
- Question (d4s2): A team presents its POC's monthly bill to the sponsor as the expected production cost. What is wrong? Correct: a POC bill is a sample at low volume; it can inform the estimate only once scaled to expected production volume with error bounds. Distractors: it is fine if inputs were representative; add a fixed 10% margin; POC cost overstates production because of caching warm-up.
- Source: `02.txt:105, 152, 156`

### 02#2 · weak
- **Claim:** Do the cost/latency model before committing to the architecture (before code is written); if the projection exceeds the cost ceiling, the architecture changes before any code, not after the first billing cycle.
- Domains: D1, D4 · surfaced: — · tested: —
- Card (d1s6): Timing: the cost and latency model is built before the architecture is finalised; a projection over the ceiling means changing the architecture before code, not renegotiating after the first bill.
- Question (d1s6): Sizing shows the projected monthly cost exceeds the budget ceiling, but the prototype already works. What should happen? Correct: change the architecture (tier, caching, Batch, scope) before writing production code. Distractors: build as designed and optimise after the first billing cycle; raise the ceiling to match; ship and rely on budget alerts. (Note: d1s6q03/q28 and d4s2q03 only mention 'before any code is written' in the stem; no correct answer tests the timing.)
- Source: `02.txt:116-117, 145, 174`

### 02#2 · missing
- **Claim:** Build these reliability controls into the initial design: they are much harder to add to a system not designed for them, and without them the primary endpoint is a single point of failure.
- Domains: D4 · surfaced: d4s2 traps[3] (single point of failure only, not the timing) · tested: —
- Card (d4s2): Retries, fallback chains and circuit breakers belong in the initial design; they are much harder to retrofit, and without them the primary endpoint is a single point of failure.
- Question (d4s2): A team plans to launch with no retry, fallback or circuit-breaker logic and add them after the first production incident. What is the main problem? Correct: these controls are much harder to add to a system not designed for them, and until then any endpoint outage takes the whole workflow down instead of degrading. Distractors: they add latency, so deferring is reasonable; the provider's SLA covers outages; only circuit breakers need to be in from the start.
- Source: `02.txt:146-147`

### 02#3 · tested-not-surfaced
- **Claim:** Run every new use case through all four AI properties before issuing a verdict; a 'can Claude do this' check is only a capability check, and skipping a property risks missing a design-changing constraint.
- Domains: D1 · surfaced: d1s6 learn[5] (working memory only) · tested: d1s6q08, d1s6q17, d1s6q18
- Card (d1s6): A feasibility assessment runs every capability through all four AI properties; asking only 'can Claude do this' is a capability check and misses the compensating controls the design needs.
- Question (d1s6): An architect's feasibility write-up confirms the model can read contracts and spot clause patterns, and stops there. What is missing? Correct: an assessment against each of the four AI properties to find where compensating controls are needed. Distractors: a cost estimate only; a larger demo sample; stakeholder sign-off.
- Source: `02.txt:183, 231`

### 02#3 · weak
- **Claim:** The constraints are load-bearing: they carry the same weight as the architecture, so an undocumented feasible-with-constraints verdict becomes an infeasible system once the constraint is violated in production.
- Domains: D1 · surfaced: — · tested: —
- Card (d1s6): Undocumented constraint: a feasible-with-constraints verdict whose constraints are not written down becomes an infeasible system the first time production violates them.
- Question (d1s6): A design was approved as feasible with constraints, but the constraints were agreed verbally and never written into the design or SOW. What is the most likely outcome? Correct: when production violates a constraint, the system fails and nobody designed for it, because the constraints are part of the architecture. Distractors: nothing, since the verdict was positive; only cost rises; the verdict automatically reverts to feasible as scoped.
- Source: `02.txt:206, 232`

### 02#4 · surfaced-not-tested
- **Claim:** Build observability instrumentation at design time, not after the first incident: retrofitted logging cannot answer the root-cause question, and building it later always costs more.
- Domains: D3, D4 · surfaced: d4s4 traps[4] · tested: —
- Card (d3s5): Instrument at design time: decide what you must be able to reconstruct after an incident and log it before launch; logging added after the first incident cannot answer that incident's root cause.
- Question (d3s5): A team defers request/response/context/outcome logging until the integration 'has been live a while'. A data-handling incident occurs in week two. What is the main consequence? Correct: the root cause must be reconstructed from a system never set up to answer the question, which costs more than building logging first. Distractors: none, since the provider keeps logs by default; only latency analysis is affected; it can be fully recovered by replaying traffic. (d4s4q17 tests design-time timing only for the business translation layer; d3s3q17 only for PII redaction.)
- Source: `02.txt:335-336, 357, 361`

### 03#2 · tested-not-surfaced
- **Claim:** Let control errors fail closed for decisions where a wrong pass causes harm, choosing the direction explicitly.
- Domains: D5 · surfaced: — · tested: d5s2q19, d5s2q20
- Card (d5s2): Fail direction: decide it explicitly for every operator-built control; fail closed where a wrong pass causes harm, as with circuit breakers.
- Source: `03.txt:77, 03.txt:80, 03.txt:245`

### 03#3 · weak
- **Claim:** Treating fairness as the vendor's (model provider's) responsibility leaves those points unmonitored; provider bias evaluations never see your corpus, framing, examples or routing.
- Domains: D5 · surfaced: d5s4 traps[0] · tested: —
- Question (d5s4): A team cites the model provider's published bias evaluations as its evidence that the deployment is fair. What does this leave uncovered? Correct: its own retrieval corpus, prompt framing, few-shot examples and routing, which the provider never tested and cannot see. Distractors: the provider evaluations already cover any system built on the model; only the system prompt needs a fairness line; fairness needs checking only once at launch on the aggregate metric.
- Source: `03.txt:144, 03.txt:150, 03.txt:247`

### 03#5 · tested-not-surfaced
- **Claim:** A control with no owner and no evidence eventually goes non-operational and fails at the audit.
- Domains: D5 · surfaced: — · tested: d5s6q18
- Card (d5s6): Unowned control: a control with no named owner and no evidence quietly stops operating, and the gap surfaces only at audit.
- Source: `03.txt:232, 03.txt:251`

### 04#5 · weak
- **Claim:** (Body of 04#5) Each entry-point boundary is an integration point with its own authentication, logging and failure-mode profile, which the map makes explicit.
- Domains: D6, D3 · surfaced: — · tested: —
- Card (d6s5): Each entry-point boundary is its own integration point with separate authentication, logging and failure-mode profile; the responsibility map makes those boundaries explicit.
- Question (d6s5): Why does a workflow spanning several Claude entry points need each boundary documented in the responsibility map? Correct: each boundary has its own authentication, logging and failure-mode profile. Distractors: all entry points share one auth method and log stream; the map is needed only for billing allocation; boundaries matter only on cloud-provider routes.
- Source: `04.txt:306`

## Full claim map

**01#1 Decomposition is the move that comes before architecture**

- [missing] Decomposition (splitting the work among Claude, existing systems and humans) comes before choosing a pattern or architecture. — cards: —; questions: —
- [covered] The work is split into three buckets: what Claude handles, what existing systems handle, what humans handle. — cards: d1s3 learn[0], d1s3 learn[2]; questions: d1s3q01, d1s3q17, d1s3q13
- [covered] The split is driven by how the model behaves on each piece (the four properties), i.e. whether the task belongs with Claude or elsewhere in the stack. — cards: d1s3 learn[3], d1s3 traps[0]; questions: d1s3q07, d1s3q08
- [covered] Skipping decomposition forces Claude into work another system would do at lower cost. — cards: d1s3 learn[4], d1s3 learn[5], d1s3 traps[1]; questions: d1s3q02, d1s3q18, d1s3q15, d1s3q21
- [missing] Skipping decomposition asks Claude to operate without the context a human would have given a colleague. — cards: —; questions: —

**01#2 Choosing a pattern is choosing how much autonomy to grant**

- [covered] Augmented LLM, workflow and agent are points on an autonomy spectrum from 'Claude assists one step' to 'Claude plans the whole sequence'. — cards: d1s4 learn[0]; questions: d1s4q01, d1s4q02, d1s4q14
- [covered] Choosing the pattern is a delegation decision about how much autonomy to grant (justified by stakes and reversibility). — cards: d1s4 learn[5], d1s4 learn[3]; questions: d1s4q32
- [covered] Four workflow sub-patterns sit underneath (chaining, routing, parallelization, evaluator-optimizer). — cards: d1s4 learn[1]; questions: d1s4q28, d1s4q29, d1s4q30, d1s4q33
- [covered] The decision depends on five factors: predictability, error cost, observability, latency, cost. — cards: d1s4 learn[2]; questions: d1s4q06, d1s4q18, d1s4q19, d1s4q20
- [covered] The tightest (binding) constraint decides the pattern; e.g. when error cost binds, error cost picks the pattern (body: the first factor that rules out a pattern decides). — cards: d1s4 learn[2]; questions: d1s4q06

**01#3 Reach for the tested reference architectures before inventing your own**

- [covered] There are five reference architectures: agent, RAG, document processing pipeline (evaluator-optimizer), routing, coding agent. — cards: d1s5 learn[4]; questions: d1s5q10, d1s5q11, d1s5q17, d1s5q18
- [missing] Reference architectures are documented because other teams already learned what breaks in each; start from them (as references to adapt, not blueprints) rather than inventing your own. — cards: —; questions: —
- [covered] Combine reference architectures only when different parts of the system break differently. — cards: d1s5 learn[5], d1s5 traps[4]; questions: d1s5q12
- [surfaced-not-tested] When still uncertain what the system must handle, pick one architecture (adapt it); composing two roughly doubles the surface area to maintain. — cards: d1s5 traps[4], d1s5 learn[5]; questions: —
- [covered] The most common mistake is using retrieval as a substitute for live state; retrieval is for static documents/snapshots, not live data during a conversation. — cards: d1s5 traps[2], d1s5 learn[5], d1s5 learn[4], d2s2 learn[1]; questions: d1s5q22, d1s5q09, d1s5q11, d3s2q10, d2s2q02, d4s2q13

**01#4 Choosing a model: start with Sonnet and treat every swap as a release**

- [covered] Sonnet is the default tier (balances intelligence, speed and cost for most production workloads). — cards: d2s1 learn[0]; questions: d2s1q01, d2s1q02
- [covered] Moving to Opus or Haiku is a deliberate decision gated like any other release. — cards: d2s1 learn[4], d2s1 learn[1], d2s1 traps[4], d4s1 learn[0]; questions: d2s1q18, d2s1q02, d4s1q01, d4s4q10
- [covered] The gate needs an eval set that defines what 'better' means. — cards: d2s1 learn[1], d2s1 learn[4]; questions: d2s1q03, d2s1q15, d2s1q16
- [covered] The rollback criterion is set before the swap, not after. — cards: d2s1 learn[4], d2s1 traps[1], d2s1 learn[2]; questions: d2s1q04, d2s1q14, d4s1q26
- [covered] Progressive context (only what is needed at each step) holds up better over a long-lived deployment than monolithic context that loads everything and grows until it breaks. — cards: d3s2 learn[5], d2s2 traps[2], d2s2 traps[1]; questions: d3s2q14, d2s2q20, d2s2q05

**01#5 Pick the entry point by the work it has to do, not by what is already on the shelf**

- [covered] Each entry point (Claude.ai, direct API, SDK, Claude Code, MCP) carries a different core tradeoff: speed of setup vs depth of control, prebuilt UI vs custom integration, breadth of tools vs focus. — cards: d3s1 learn[1], d3s1 learn[2], d3s1 learn[3]; questions: d3s1q19, d3s1q18, d3s1q25, d3s1q26, d3s1q03, d3s1q06
- [covered] Choose the entry point by the work it has to do (and the user), not by what is already available/on the shelf. — cards: d3s1 learn[5], d3s1 traps[2], d1s2 traps[0], d1s2 traps[1]; questions: d3s1q14, d3s1q15, d3s1q05, d3s1q23, d1s2q15
- [missing] The right recommendation is one where you can name the tradeoff out loud when you make it; naming it is what later tells you when to switch entry points. — cards: —; questions: —

**02#1 Evals as acceptance criteria**

- [covered] Write the eval suite before the production code (it forces measurable success criteria and is not an end-of-project QA step). — cards: d4s1 learn[0], d4s1 traps[0]; questions: d4s1q01, d4s1q02
- [covered] Keep the golden dataset current with every system change; an out-of-date suite gives false confidence. — cards: d4s1 learn[5], d4s1 traps[3]; questions: d4s1q24
- [covered] Use the eval as the gate for every model swap or prompt revision (and other changes such as retrieval config), with the delta threshold set before the run. — cards: d4s1 learn[0], d4s1 learn[5], d2s1 learn[1], d2s1 learn[4]; questions: d4s1q25, d4s1q26, d4s1q11, d2s1q03, d2s1q04, d2s1q18

**02#2 POC to production**

- [weak] Estimate cost at production volume: a low-volume POC bill is a sample, not a production cost model; scale it to expected volume with error bounds. — cards: d4s2 traps[0], d1s6 traps[4], d4s2 learn[0]; questions: d4s2q01
- [covered] Estimate latency for production conditions: p95 under concurrent load, not the median of single demo requests. — cards: d4s2 learn[2], d4s2 traps[1], d1s6 learn[2]; questions: d4s2q06, d4s2q07, d1s6q05
- [weak] Do the cost/latency model before committing to the architecture (before code is written); if the projection exceeds the cost ceiling, the architecture changes before any code, not after the first billing cycle. — cards: —; questions: —
- [covered] Production calls need retries with backoff, fallback chains and circuit breakers (each at its proper layer). — cards: d4s2 learn[3], d4s2 traps[2], d4s2 traps[3]; questions: d4s2q09, d4s2q10, d4s2q17, d4s2q18, d4s2q20
- [missing] Build these reliability controls into the initial design: they are much harder to add to a system not designed for them, and without them the primary endpoint is a single point of failure. — cards: d4s2 traps[3] (single point of failure only, not the timing); questions: —
- [covered] Name the failure mode specific to the architecture type (agent, RAG, document pipeline, orchestrator-workers) and document its mitigation. — cards: d4s2 learn[4]; questions: d4s2q12, d4s2q13, d4s2q14

**02#3 Use-case sizing and feasibility**

- [tested-not-surfaced] Run every new use case through all four AI properties before issuing a verdict; a 'can Claude do this' check is only a capability check, and skipping a property risks missing a design-changing constraint. — cards: d1s6 learn[5] (working memory only); questions: d1s6q08, d1s6q17, d1s6q18
- [covered] Each property maps to a feasibility question with a compensating design (precision -> verification; knowledge -> retrieval/tools; working memory -> chunking/pipeline; steerability -> schemas/code execution). — cards: d1s1 learn[0], d1s1 learn[1], d1s1 learn[2], d1s1 learn[3], d1s6 learn[5]; questions: d1s6q08, d1s6q18
- [covered] State the verdict in one of three forms: feasible as scoped, feasible with constraints, not feasible (each with its documentation requirement). — cards: d1s6 learn[3]; questions: d1s6q06, d1s6q07, d1s6q15, d1s6q27
- [covered] For every constrained verdict, document each boundary condition and the failure mode when it is violated, and carry it into the SOW. — cards: d1s6 learn[0], d1s6 learn[3]; questions: d1s6q06, d1s6q24
- [weak] The constraints are load-bearing: they carry the same weight as the architecture, so an undocumented feasible-with-constraints verdict becomes an infeasible system once the constraint is violated in production. — cards: —; questions: —

**02#4 Enterprise integration patterns**

- [covered] Enforce identity on the server side: verify before the call and inject role and authorised data scope into the system prompt; a user-asserted role is manipulable. — cards: d3s3 learn[0], d3s3 traps[0]; questions: d3s3q15, d3s3q02
- [covered] Pass only the minimum necessary data into the context window (necessity filter, reference IDs instead of full fields; the window is not a governance boundary). — cards: d3s3 learn[4], d3s3 traps[2]; questions: d3s3q16, d3s3q10, d3s3q11, d3s3q17
- [surfaced-not-tested] Build observability instrumentation at design time, not after the first incident: retrofitted logging cannot answer the root-cause question, and building it later always costs more. — cards: d4s4 traps[4]; questions: —

**02#5 A/B testing and observability**

- [covered] Fix the single primary metric before running the experiment; choosing it after seeing results is outcome-shopping. — cards: d4s3 learn[1], d4s3 traps[1]; questions: d4s3q04, d4s3q18
- [covered] Calculate the sample size before the experiment (minimum detectable effect, baseline, confidence; larger for LLM variance); underpowered runs produce false positives. — cards: d4s3 learn[2], d4s3 traps[2]; questions: d4s3q05, d4s3q06, d4s3q07, d4s3q18
- [covered] At scale, separate per-request observability (traces, per-request decomposition) from aggregate dashboards, because aggregates can look healthy while a small fraction of requests consumes most of the budget. — cards: d4s4 learn[1], d4s4 learn[2], d4s4 traps[0]; questions: d4s4q03, d4s4q02, d4s4q04
- [covered] Build a translation layer, at design time, that maps technical metrics to the business metrics the stakeholder tracks. — cards: d4s4 learn[5]; questions: d4s4q17

**03#1 Safety is a stack of layers, not a setting**

- [covered] Training-time alignment reduces broad harm for every request but never saw the partner's domain policy, data rules or authorization model. — cards: d5s1 learn[1], d5s1 traps[1]; questions: d5s1q03, d5s1q10, d5s1q05, d5s1q09
- [covered] Draw the layer boundary explicitly: identify what each layer (trained behaviour, system prompt, runtime screening, authorisation) covers and what it misses. — cards: d5s1 learn[2]; questions: d5s1q17, d5s1q05, d5s1q15, d5s1q08
- [covered] The dangerous failure is silent: assuming Claude enforces a rule that does not live in any layer. — cards: d5s1 traps[3]; questions: d5s1q07, d5s1q09

**03#2 A guarded path has three control points and a chosen failure direction**

- [covered] Input screening, output screening and tool-call authorization answer different questions. — cards: d5s2 learn[2]; questions: d5s2q03, d5s2q28, d5s1q08
- [covered] A single filter at the end of the path does not cover the other two control points (output screening judges text, not side-effecting actions). — cards: d5s2 traps[0]; questions: d5s2q11
- [tested-not-surfaced] Let control errors fail closed for decisions where a wrong pass causes harm, choosing the direction explicitly. — cards: —; questions: d5s2q19, d5s2q20
- [covered] A guardrail that silently passes traffic when it errors gives the appearance of protection without the function (worse than one that blocks). — cards: d5s2 traps[2]; questions: d5s2q06, d5s2q15

**03#3 Fairness and transparency are instrumented, not assumed**

- [covered] Unequal outcomes arise at points the architect controls: retrieval corpus, prompt framing, few-shot examples and downstream routing. — cards: d5s4 learn[0]; questions: d5s4q01, d5s4q02, d5s4q17
- [weak] Treating fairness as the vendor's (model provider's) responsibility leaves those points unmonitored; provider bias evaluations never see your corpus, framing, examples or routing. — cards: d5s4 traps[0]; questions: —
- [covered] Log every decision (inputs, retrieved context, output, routing) so users, regulators and the build team can each reconstruct it. — cards: d5s4 learn[1], d5s4 learn[2]; questions: d5s4q03, d5s4q04, d5s4q10, d5s4q20
- [covered] If you cannot reconstruct an explanation, you cannot reliably provide one. — cards: d5s4 learn[3], d5s4 traps[4]; questions: d5s4q18

**03#4 Route review by stakes, not by volume**

- [covered] Confidence, reversibility and the cost of a wrong answer decide which decisions a person should review (confidence only if calibrated). — cards: d5s5 learn[0], d5s5 traps[2]; questions: d5s5q01, d5s5q02, d5s5q13, d5s5q04
- [covered] Send high-stakes, low-confidence decisions to a human and let the rest through. — cards: d5s5 learn[1]; questions: d5s5q03, d5s5q15, d5s5q21
- [covered] The reviewer must receive the inputs and the reason for the flag (plus the output). — cards: d5s5 learn[3], d5s5 traps[1]; questions: d5s5q08, d5s5q14
- [covered] Routing everything to review floods the queue until reviewers click through without reading. — cards: d5s5 traps[0]; questions: d5s5q12, d5s5q09

**03#5 A compliant entry point is a prerequisite, and an evidenced control set is the proof**

- [covered] A compliant entry point (route) is a prerequisite, not proof of compliance. — cards: d5s6 learn[0], d5s6 traps[0]; questions: d5s6q01
- [covered] A regulation states an outcome and leaves the control to you. — cards: d5s6 learn[0]; questions: d5s6q02
- [covered] Turn each obligation into a specific control, a named owner and a living evidence artifact. — cards: d5s6 learn[1]; questions: d5s6q02, d5s6q03, d5s6q01
- [covered] Revalidate the evidence over time, because configurations drift and artifacts go stale. — cards: d5s6 learn[4], d5s6 traps[3]; questions: d5s6q09, d5s6q15
- [tested-not-surfaced] A control with no owner and no evidence eventually goes non-operational and fails at the audit. — cards: —; questions: d5s6q18
- [covered] What a reviewer accepts is proof the control is live, not the control (or a design document) itself. — cards: d5s6 learn[4], d5s6 traps[1]; questions: d5s6q08, d5s6q20, d5s6q03

**04#1 Structured discovery**

- [covered] Run discovery as a four-category process (must do, must not do, must cost, must prove), finished before proposing anything. — cards: d6s1 learn[2], d6s1 learn[4]; questions: d6s1q04, d6s1q16, d6s1q22, d6s1q05
- [covered] Translate every stated preference into a testable constraint. — cards: d6s1 learn[1], d6s1 traps[0]; questions: d6s1q01, d6s1q02, d6s1q29, d6s1q30
- [covered] Write each item as a requirement row (statement, implied constraint, architectural decision) with its assumption labelled. — cards: d6s1 learn[3]; questions: d6s1q19, d6s1q31
- [covered] One row per item keeps the reasoning intact so the design traces to the business case. — cards: d6s1 learn[3]; questions: d6s1q24, d6s1q26

**04#2 Communicating tradeoffs (GTM / demo / joint scoping half EXCLUDED as Partner Track)**

- [covered] Present every tradeoff in three elements: what we gain, what we give up, and what reversing it later would cost. — cards: d6s2 learn[1]; questions: d6s2q03
- [covered] Reversal cost is the element most often skipped; without it approval is false alignment, so name it especially when the design feels simpler. — cards: d6s2 learn[1], d6s2 learn[4], d6s2 traps[4]; questions: d6s2q04, d6s2q05, d6s2q12, d6s2q16

**04#3 Feedback loops and SLA management**

- [covered] Build the decision layer above observability that maps each signal to a trigger, an action and an owner (slow drifts as well as hard failures). — cards: d6s3 learn[1], d6s3 learn[4], d6s3 traps[0], d6s3 traps[1]; questions: d6s3q02, d6s3q27, d6s3q26
- [covered] Set SLA thresholds from their real sources (latency from UX expectation, availability from business criticality, quality from eval results). — cards: d6s3 learn[2], d6s3 traps[2]; questions: d6s3q05, d6s3q06, d6s3q07
- [covered] Wire regulated checkpoints to run on a schedule, independent of incidents. — cards: d6s3 learn[4], d6s3 traps[4]; questions: d6s3q10, d6s3q14, d6s3q22, d6s3q24

**04#4 Documentation for handoff and audit**

- [covered] Write the decision, the rejected alternatives and the tradeoff each resolved. — cards: d6s4 learn[1], d6s4 learn[4], d6s4 traps[0], d6s4 traps[3]; questions: d6s4q03, d6s4q08
- [covered] Write it at design time, while you still hold the reasoning. — cards: d6s4 traps[4]; questions: d6s4q14, d6s4q13
- [covered] Carry the control register (obligation, control, owner, evidence artifact) forward as evidence a reviewer will accept, not assertions. — cards: d6s4 learn[1], d6s4 traps[1]; questions: d6s4q04, d6s4q05

**04#5 Entry point selection and outcomes (reuse note EXCLUDED as Partner Track)**

- [covered] In a live multi-platform deployment, choose the route on latency, compliance and cost (not just the compliance pre-filter). — cards: d6s5 learn[0]; questions: d6s5q01
- [covered] Multi-entry-point designs need an entry-point-responsibility map (which entry point owns which task and why, written before integration code) to prevent task creep. — cards: d6s5 learn[2], d6s5 traps[2]; questions: d6s5q06, d6s5q07
- [weak] (Body of 04#5) Each entry-point boundary is an integration point with its own authentication, logging and failure-mode profile, which the map makes explicit. — cards: —; questions: —
- [covered] Capture the before metric (business outcome) at the start of the engagement. — cards: d6s5 learn[4], d6s5 traps[4]; questions: d6s5q13, d6s5q11
- [covered] Name the control that makes the before/after comparison auditable rather than asserted. — cards: d6s5 learn[4]; questions: d6s5q14, d6s5q11
- [covered] Technical metrics alone cannot justify expansion; the outcome document must carry business before/after so the sponsor can justify it upward. — cards: d6s5 traps[4]; questions: d6s5q17, d6s5q11

**05#1 Team setup is shared configuration, distribution and spend posture decided up front**

- [covered] A team environment is a shared, reviewed and versioned baseline (shared CLAUDE.md, agreed tools/MCP servers, permission posture), set up before use. — cards: d7s1 learn[0]; questions: d7s1q01, d7s1q16
- [covered] Org-provisioned Skills reach everyone. — cards: d7s2 learn[0], d7s2 traps[2]; questions: d7s2q01, d7s2q15
- [covered] Plugins give group and org targeting with versioned updates and rollback (strongest governance). — cards: d7s2 learn[1]; questions: d7s2q03, d7s2q04, d7s2q17, d7s2q19
- [covered] Project Skills serve one team (in .claude/skills/, versioned with the repo). — cards: d7s2 learn[2]; questions: d7s2q05, d7s2q12
- [covered] API Skills serve programmatic reuse (with explicit version pinning). — cards: d7s2 learn[3]; questions: d7s2q06, d7s2q16
- [covered] All of it is bounded by model and budget guardrails set up front (model defaults, allowlists, effort guidance, caps). — cards: d7s1 learn[2], d7s1 traps[1]; questions: d7s1q04, d7s1q05, d7s1q12, d7s1q13

**05#2 Adoption is engineered through champions and batches**

- [covered] A champion per team proves a real workflow and seeds adoption batch by batch. — cards: d7s1 learn[1], d7s1 traps[0]; questions: d7s1q15, d7s1q03
- [covered] Access without enablement stalls at basic chat. — cards: d7s3 learn[2], d7s3 traps[2]; questions: d7s3q08
- [covered] Lumpy adoption (a few heavy users) never standardizes the gain. — cards: d7s3 learn[2]; questions: d7s3q06, d7s3q07

**05#3 Diligence keeps AI-assisted work trustworthy**

- [covered] Hold AI-generated code to the same correctness, security and maintainability standards as any other code. — cards: d7s3 learn[3], d7s3 traps[3]; questions: d7s3q13, d7s3q17
- [covered] Require that the author can explain what shipped (human understanding). — cards: d7s3 learn[4], d7s3 traps[0]; questions: d7s3q18, d7s3q03, d7s3q12
- [covered] Capture this as a verification checklist that gates before production (backed by automated tests/evals). — cards: d7s3 learn[4]; questions: d7s3q16, d7s3q15, d7s3q10

**05#4 Operational support is translation plus self-sufficiency**

- [covered] Connect symptoms to architecture causes (translation, not firefighting). — cards: d7s4 learn[0], d7s4 learn[1], d7s4 learn[2], d7s4 learn[3]; questions: d7s4q01, d7s4q02, d7s4q03, d7s4q05
- [covered] Leave behind runbooks and escalation paths. — cards: d7s4 learn[4], d7s4 traps[4]; questions: d7s4q06, d7s4q07, d7s4q14
- [covered] Goal: the team needs the Architect for the new problem, not the familiar one. — cards: d7s4 learn[4], d7s4 traps[0]; questions: d7s4q08, d7s4q14

---

## Resolution (2026-10-04)

All 15 gaps closed: each claim now has a card that states it and at least one question that tests it. 20 questions added (D1 +9, D3 +4, D4 +3, D5 +1, D6 +3, including an optional 'What do we give up?' variant in d6s2), 15 cards extended or added. Independently verified against the notes; one near-duplicate (d5s4q22) got new distractors. Pre-change banks: backup_before_takeaways/.

| Takeaway | Claim | Card | Questions |
|---|---|---|---|
| 01#1 | Decompose before choosing a pattern | d1s3 learn[0] | d1s3q22, d1s3q24 |
| 01#1 | Skipping decomposition: cheaper-system work / no colleague context | d1s3 learn[5] | d1s3q23 |
| 01#3 | Reference architectures: start from one and adapt | d1s5 learn[4] | d1s5q24, d1s5q25 |
| 01#3 | When unsure, pick one; composing doubles the surface | d1s5 traps[4] | d1s5q26 |
| 01#5 | Name the entry point's tradeoff out loud | d3s1 learn[5] (+ learn[0] Claude.ai tradeoff) | d3s1q27, d3s1q28 |
| 02#2 | Scale POC cost to production volume | d4s2 traps[0] | d4s2q22 |
| 02#2 | Cost model before architecture; change it before code | d1s6 traps[0] | d1s6q30, d1s6q31 |
| 02#2 | Reliability controls in the initial design | d4s2 traps[3] | d4s2q23, d4s2q24 |
| 02#3 | All four properties before a verdict | d1s6 learn[5] | (already: d1s6q08, q17, q18) |
| 02#3 | Constraints are load-bearing | d1s6 learn[3] | d1s6q32 |
| 02#4 | Observability at design time | d3s5 learn[4] | d3s5q20, d3s5q21 |
| 03#2 | Fail closed where a wrong pass harms | d5s2 learn[4] | (already: d5s2q19, q20) |
| 03#3 | Vendor-owned fairness leaves your points unmonitored | (already: d5s4 traps[0]) | d5s4q22 |
| 03#5 | Unowned, unevidenced control fails at audit | d5s6 learn[1] | (already: d5s6q18) |
| 04#5 | Each entry-point boundary has its own auth/logging/failure profile | d6s5 learn[5] (new) | d6s5q18, d6s5q19 |

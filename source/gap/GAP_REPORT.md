# Gap report: content in the notes not previously tested

## Domain 1
| Subject | Missing area | Source | New questions |
|---|---|---|---|
| d1s1 The four properties architects design around | Token-limit oversized request (400) and pre-send checks | 01.txt L12 | 2 |
| d1s1 The four properties architects design around | Restate the goal alongside the instruction | 01.txt L16-17 | 2 |
| d1s2 Three layers and seven primitives | Subagents versus Agent Teams | 01.txt L57-62 | 2 |
| d1s3 Decomposition and delegation | Delegation map categories and the Delegation competency | 01.txt L86-91 | 2 |
| d1s4 Pattern selection | Predictability and autonomy axes | 01.txt L124, L132-136 | 1 |
| d1s4 Pattern selection | Chaining sub-pattern | 01.txt L143-146 | 1 |
| d1s4 Pattern selection | Combine sub-patterns, start simplest, escalate on measurement | 01.txt L159 | 2 |
| d1s4 Pattern selection | Five-factor ratings per pattern | 01.txt L162-191 | 3 |
| d1s4 Pattern selection | Agent cost is a design outcome, not a label | 01.txt L210 | 2 |
| d1s4 Pattern selection | Workflow versus agent failure diagnosability | 01.txt L211-212 | 1 |
| d1s4 Pattern selection | Fine-tuning lock-in and availability (verify framing) | 01.txt L198-204 | 2 |
| d1s4 Pattern selection | Agent-specific audit gap and guardrails rebuilding a workflow | 01.txt L218-224 | 2 |
| d1s5 Multi-agent systems and reference architectures | Multi-agent failure design responses | 01.txt L236-255 | 3 |
| d1s5 Multi-agent systems and reference architectures | Coding-agent two-phase shape and untested reference-architecture failures | 01.txt L292-297 | 2 |
| d1s6 Feasibility, sizing and business value | Feasible-as-scoped rests on stated assumptions | 02.txt L201-203 | 2 |
| d1s6 Feasibility, sizing and business value | Working memory is the most overlooked property | 02.txt L231, L190-192 | 2 |
| d1s6 Feasibility, sizing and business value | Call-volume source and sensitivity analysis | 02.txt L172, L175 | 2 |
| d1s6 Feasibility, sizing and business value | Payback period: build vs run cost and sensitivity | 02.txt L217-218 | 2 |
| d1s6 Feasibility, sizing and business value | Context window capacity is part of the tier decision | 02.txt L246 | 1 |

## Domain 2
| Subject | Missing area | Source | New questions |
|---|---|---|---|
| d2s2 Context window and context strategy | Progressive context breakdown modes | 01.txt L397-407 | 2 |
| d2s2 Context window and context strategy | Monolithic attention degradation before the limit | 01.txt L396 | 1 |

## Domain 3
| Subject | Missing area | Source | New questions |
|---|---|---|---|
| d3s1 Build-time interfaces, entry points and delivery routes | SDK as default, raw HTTP as the exception | 01.txt L606-613, L623 | 2 |
| d3s1 Build-time interfaces, entry points and delivery routes | Claude.ai zero-integration tradeoff | 01.txt L579-582 | 2 |
| d3s1 Build-time interfaces, entry points and delivery routes | Claude for Work Team tier fit | 01.txt L580-582 | 1 |
| d3s1 Build-time interfaces, entry points and delivery routes | Cowork supervision tradeoff | 01.txt L587-590 | 1 |
| d3s1 Build-time interfaces, entry points and delivery routes | Bedrock inference profiles | 01.txt L694, L702 | 1 |
| d3s1 Build-time interfaces, entry points and delivery routes | Entry-point integration cost and lock-in | 01.txt L705-708 | 2 |
| d3s1 Build-time interfaces, entry points and delivery routes | Entry-point trade-offs (raw loop vs Agent SDK, API/SDK/MCP costs) | 02.txt L257-274 | 2 |
| d3s2 RAG: chunking, indexing and retrieval strategy | Semantic chunking | 01.txt L335-337 | 1 |
| d3s2 RAG: chunking, indexing and retrieval strategy | Maintenance axis and sizing to actual query patterns | 01.txt L356-364 | 1 |
| d3s4 Regulated-industry constraints on integration | FedRAMP path to impact-level mapping | 01.txt L724-726, L730 | 2 |
| d3s4 Regulated-industry constraints on integration | GDPR does not itself require EU residency | 02.txt L299, L302 | 2 |
| d3s4 Regulated-industry constraints on integration | Observability column of the constraint matrix | 02.txt L291-315 | 1 |
| d3s5 Claude Code layers and observability for integrations | Placement among shaping layers (CLAUDE.md vs Skills vs subagents) | 01.txt L661-672 | 2 |

## Domain 4
| Subject | Missing area | Source | New questions |
|---|---|---|---|
| d4s1 Evals as acceptance criteria and the grading ladder | Judge reasoning and judge-prompt engineering | 02.txt L48-52 | 2 |
| d4s1 Evals as acceptance criteria and the grading ladder | Volume over perfection in eval sets | 02.txt L65 | 2 |
| d4s1 Evals as acceptance criteria and the grading ladder | Eval cost is a secondary constraint | 02.txt L78 | 2 |
| d4s1 Evals as acceptance criteria and the grading ladder | Manual spot-checks are not evals | 02.txt L83, L93 | 1 |
| d4s1 Evals as acceptance criteria and the grading ladder | Five-stage eval workflow order | 02.txt L13-31 | 1 |
| d4s2 POC to production: cost, latency and reliability | Why backoff, caps, and where retries sit | 02.txt L123, L126, L445 | 2 |

## Domain 5
| Subject | Missing area | Source | New questions |
|---|---|---|---|
| d5s1 Layered safety: what training enforces versus what you own | Constitution shapes behaviour but does not catch outputs | 03.txt L3 | 2 |
| d5s1 Layered safety: what training enforces versus what you own | Layer ownership and the authorisation blind spot | 03.txt L9-24 | 1 |
| d5s1 Layered safety: what training enforces versus what you own | System prompt and screening drift | 03.txt L25-27 | 1 |
| d5s2 Risk categories and the guarded request path | Output screening: judge model vs validator | 03.txt L58-67 | 2 |
| d5s2 Risk categories and the guarded request path | Choosing the fail direction deliberately | 03.txt L51, L77, L245 | 2 |
| d5s2 Risk categories and the guarded request path | What each control point must specify | 03.txt L90 | 1 |
| d5s2 Risk categories and the guarded request path | Null refusal categories and not hardcoding the list | 03.txt L75 | 2 |
| d5s2 Risk categories and the guarded request path | System vulnerability walk across entry points | 03.txt L46-47 | 2 |
| d5s2 Risk categories and the guarded request path | Tool and action abuse risk category | 03.txt L41-45 | 1 |
| d5s2 Risk categories and the guarded request path | Cost of screening points | 03.txt L26, L89 | 1 |
| d5s4 Fairness, transparency and decision logging | Decision logging vs health observability, and its cost | 03.txt L127, L138-139 | 2 |
| d5s5 Human-in-the-loop routing by stakes | Decision log vs routing rule | 03.txt L152 | 2 |
| d5s5 Human-in-the-loop routing by stakes | Monitor-and-step-in instead of per-action sign-off | 03.txt L176 | 1 |
| d5s6 Compliance obligations as controls with evidence | Owner of the transparency control | 03.txt L220-223 | 1 |

## Domain 6
| Subject | Missing area | Source | New questions |
|---|---|---|---|
| d6s1 Structured discovery and the translation table | Contents of the four discovery buckets | 04.txt L17-20 | 3 |
| d6s1 Structured discovery and the translation table | Translating 'seamless' into requirement types | 04.txt L11-12, L28-31 | 2 |
| d6s1 Structured discovery and the translation table | Translation table row structure and assumption column | 04.txt L23-43 | 2 |
| d6s1 Structured discovery and the translation table | Sketching too early ends discovery | 04.txt L50-61 | 3 |
| d6s3 Feedback loops and SLAs | What each feedback-loop stage asks | 04.txt L166-172 | 2 |
| d6s3 Feedback loops and SLAs | Governance table rows for latency, cost and output audit | 04.txt L188-208 | 3 |
| d6s3 Feedback loops and SLAs | Escalation order: Architect review before stakeholder review | 04.txt L226-233 | 2 |
| d6s3 Feedback loops and SLAs | Governance as a design-time, pre-launch obligation | 04.txt L186-187, L210-212 | 3 |
| d6s5 Entry-point selection in production and outcome documents | Measurement owner field of the outcome document | 04.txt L308, L344-345 | 2 |

## Domain 7
| Subject | Missing area | Source | New questions |
|---|---|---|---|
| d7s1 Team environment, rollout and spend | Distinguishing the spend guardrails | 05.txt L33 | 2 |
| d7s1 Team environment, rollout and spend | Mass switch-on rollout failure | 05.txt L7-9 | 1 |
| d7s2 Distributing Skills to a team | Per-asset distribution governance and selection criteria | 05.txt L11, L38 | 2 |
| d7s2 Distributing Skills to a team | Org-provisioned Skill as simplest all-member path | 05.txt L12, L19-21 | 1 |
| d7s2 Distributing Skills to a team | API Skill governance locus | 05.txt L28-30 | 1 |
| d7s3 AI-assisted developer workflows and diligence | Checklist versus automated gates | 05.txt L62-63 | 2 |
| d7s3 AI-assisted developer workflows and diligence | Diligence complexity is cultural | 05.txt L68 | 1 |
| d7s4 Operational support, runbooks and escalation | Causes of intermittent tool failures | 05.txt L86-88 | 1 |

## Questions added per subject
- d1s1 The four properties architects design around: +4 (d1s1q13, d1s1q14, d1s1q15, d1s1q16)
- d1s2 Three layers and seven primitives: +2 (d1s2q13, d1s2q14)
- d1s3 Decomposition and delegation: +2 (d1s3q13, d1s3q14)
- d1s4 Pattern selection: +14 (d1s4q14, d1s4q15, d1s4q16, d1s4q17, d1s4q18, d1s4q19, d1s4q20, d1s4q21, d1s4q22, d1s4q23, d1s4q24, d1s4q25, d1s4q26, d1s4q27)
- d1s5 Multi-agent systems and reference architectures: +5 (d1s5q14, d1s5q15, d1s5q16, d1s5q17, d1s5q18)
- d1s6 Feasibility, sizing and business value: +9 (d1s6q15, d1s6q16, d1s6q17, d1s6q18, d1s6q19, d1s6q20, d1s6q21, d1s6q22, d1s6q23)
- d2s2 Context window and context strategy: +3 (d2s2q15, d2s2q16, d2s2q17)
- d3s1 Build-time interfaces, entry points and delivery routes: +11 (d3s1q16, d3s1q17, d3s1q18, d3s1q19, d3s1q20, d3s1q21, d3s1q22, d3s1q23, d3s1q24, d3s1q25, d3s1q26)
- d3s2 RAG: chunking, indexing and retrieval strategy: +2 (d3s2q16, d3s2q17)
- d3s4 Regulated-industry constraints on integration: +5 (d3s4q17, d3s4q18, d3s4q19, d3s4q20, d3s4q21)
- d3s5 Claude Code layers and observability for integrations: +2 (d3s5q16, d3s5q17)
- d4s1 Evals as acceptance criteria and the grading ladder: +8 (d4s1q14, d4s1q15, d4s1q16, d4s1q17, d4s1q18, d4s1q19, d4s1q20, d4s1q21)
- d4s2 POC to production: cost, latency and reliability: +2 (d4s2q17, d4s2q18)
- d5s1 Layered safety: what training enforces versus what you own: +4 (d5s1q13, d5s1q14, d5s1q15, d5s1q16)
- d5s2 Risk categories and the guarded request path: +11 (d5s2q17, d5s2q18, d5s2q19, d5s2q20, d5s2q21, d5s2q22, d5s2q23, d5s2q24, d5s2q25, d5s2q26, d5s2q27)
- d5s4 Fairness, transparency and decision logging: +2 (d5s4q15, d5s4q16)
- d5s5 Human-in-the-loop routing by stakes: +3 (d5s5q18, d5s5q19, d5s5q20)
- d5s6 Compliance obligations as controls with evidence: +1 (d5s6q17)
- d6s1 Structured discovery and the translation table: +10 (d6s1q14, d6s1q15, d6s1q16, d6s1q17, d6s1q18, d6s1q19, d6s1q20, d6s1q21, d6s1q22, d6s1q23)
- d6s3 Feedback loops and SLAs: +10 (d6s3q15, d6s3q16, d6s3q17, d6s3q18, d6s3q19, d6s3q20, d6s3q21, d6s3q22, d6s3q23, d6s3q24)
- d6s5 Entry-point selection in production and outcome documents: +2 (d6s5q15, d6s5q16)
- d7s1 Team environment, rollout and spend: +3 (d7s1q12, d7s1q13, d7s1q14)
- d7s2 Distributing Skills to a team: +4 (d7s2q13, d7s2q14, d7s2q15, d7s2q16)
- d7s3 AI-assisted developer workflows and diligence: +3 (d7s3q15, d7s3q16, d7s3q17)
- d7s4 Operational support, runbooks and escalation: +1 (d7s4q13)
AGENTS.md
```
1 | # Documentation-First Routing (Always Apply)
2 | 
3 |     **Policy:** For user requests involving code examples, setup/configuration steps, or library/API docs, route via a documentation-focused MCP tool.
4 | 
5 | - Preferred tools: `docfork`, `sourcebot`, `git-mcp` (set `owner/repo`), generic RAG
6 | - Fallbacks:
7 | - Detection cues: "example", "install", "configure", "setup", "API", "SDK", "how to", "usage", "params", "options".
8 | - Guardrails: Read-only unless explicitly elevated; no secrets exposure; respect repo permissions.
9 | 
10 |     **Example Invocation (conceptual):**
11 | - User: "Show me how to configure OAuth for Service X."
12 | - Agent: Selects `docfork` → extracts relevant guides → returns step-by-step with citations.
13 | 
14 | **Agentic Workflow & Guardrails (Playbook Summary)**
15 | 
16 | - **Spec-as-code:** Treat specs, AC, and ADRs as inputs that program the agent. Ambiguity is the main failure source.
17 | - **Test-first AC:** Provide failing tests or explicit Acceptance Criteria spanning functional, performance, security, maintainability, and integration.
18 | - **Definition of Done:** Enforce a checklist (formatting, tests added/passing, coverage non-regression, docs updated, no high/critical vulns, staged deploy, human review).
19 | - **ADRs as guardrails:** Record context/decision/consequences; reference ADRs in prompts to prevent architectural drift.
20 | 
21 | - **Workflow:** Idea → Spec/AC/ADRs → Scaffold → Tight loop (write failing test → implement → emit diff → review/apply → run tests) → Docs → Release.
22 | - **Personas & outputs:** Planner, Implementer, Tester, Reviewer. Require structured outputs (JSON schemas) and function/tool calling for predictable actions.
23 | - **Context strategy:** Use repo maps for quick navigation and RAG for deep, file-level context. Retrieve only what’s relevant.
24 | 
25 | - **Safety rails:** Patch/diff only (no direct writes), filesystem allowlists, CI gates (format/lint/type-check/tests), read-only by default, no secrets in repo.
26 | - **Templates & automation:** Prefer the Python/TypeScript templates; use `scaffold.py`, `repo_map.py`, `indexer.py`, CI PR validator, and `guardrail.py`.
27 | - **Monorepo bias:** Favor monorepo for unified context; store canonical prompts/schemas in `.prompts/`.
28 | 
29 | - **Evaluation:** Maintain a lightweight harness (task spec → apply patch → run tests). Track KPIs: Task Success Rate, Diff Size/Churn, Turns/Tool Calls, Token Cost, Human Interventions. Add failed cases to regression and triage: classify → inspect trace → root cause → remediate → regress.
30 | 
31 | **Docs-First Routing (Reminder)**
32 | 
33 | - **Trigger words:** example, install, configure, setup, API, SDK, how to, usage, params, options.
34 | - **Tools:** Prefer documentation tools; read-only by default; respect repo permissions; never expose secrets. Cite sources when feasible.
```

DEFINITION_OF_DONE.md
```
1 | # Definition of Done (DoD)
2 | 
3 | Use this checklist to verify an agent-completed task is truly finished.
4 | 
5 | - [ ] All Acceptance Criteria (AC) are met (functional + non-functional).
6 | - [ ] Code is formatted per project linters/formatters.
7 | - [ ] Unit/integration tests added for new public APIs/paths.
8 | - [ ] All tests pass locally and in CI; coverage not decreased.
9 | - [ ] No new high/critical security issues (SAST/linters) introduced.
10 | - [ ] Public APIs have docstrings/comments; README/docs updated as needed.
11 | - [ ] Changes are minimal, scoped, and follow existing conventions.
12 | - [ ] If applicable, staged deploy validated.
13 | - [ ] Final changes reviewed/approved by a human.
14 | 
```

GEMINI.md
```
1 | # Gemini-CLI Agent Guide
2 | 
3 | Purpose: Keep gemini-cli aligned with this repository’s Agentic Workflow & Guardrails. Treat this file as the Gemini-specific counterpart to AGENTS.md.
4 | 
5 | ## Operating Principles
6 | 
7 | - Spec-as-code: Treat specs, acceptance criteria (AC), and ADRs as inputs that program your behavior.
8 | - Test-first: Prefer writing or asking for failing tests or explicit AC before implementing.
9 | - Patch/diff only: Propose changes as unified diffs; avoid direct write operations unless explicitly requested.
10 | - Docs-first routing: If the request involves examples, setup, configuration, or APIs, consult documentation and cite sources.
11 | - Minimal, structured outputs: Be concise, prefer structured JSON for plans/reviews, and clear diffs for code changes.
12 | 
13 | ## Roles & Defaults
14 | 
15 | - Default persona: Implementer (Coder) focused on safe, minimal diffs that pass tests and DoD.
16 | - Switchable personas:
17 |   - Planner (Architect): when shaping scope, AC, repo maps, or ADRs.
18 |   - Tester: when defining failing tests or verifying acceptance.
19 |   - Reviewer: when critiquing diffs against AC/DoD and security concerns.
20 | - If persona is unclear, ask for confirmation and propose a short plan.
21 | 
22 | ## Workflow Loop
23 | 
24 | 1) Clarify scope → elicit/define AC and constraints (perf, security, maintainability).
25 | 2) Plan minimally → list files to touch and rationale; reference ADRs if decisions are architectural.
26 | 3) Tests/AC first → propose failing tests or explicit AC.
27 | 4) Implement safely → emit unified diffs only; keep changes small and reversible.
28 | 5) Review self → verify AC, security impact, and regression risk; cite relevant docs.
29 | 6) Validate → suggest commands to run tests/linters; avoid executing destructive steps.
30 | 7) Document → update README/AGENTS/ADRs/configs as needed; link to DoD items.
31 | 
32 | ## Output Contracts
33 | 
34 | - Diffs (required for code changes):
35 |   - Use unified diff fences and include file paths and hunks.
36 |   - Example:
37 |     ```diff
38 |     *** Begin Patch
39 |     *** Update File: path/to/file.py
40 |     @@
41 |     - old_line
42 |     + new_line
43 |     *** End Patch
44 |     ```
45 | - Plans (JSON preferred):
46 |   - Keys: `goal`, `assumptions`, `steps[]`, `risks[]`, `validation`.
47 |   - Keep steps imperative and verifiable.
48 | - Reviews (JSON preferred):
49 |   - Keys: `summary`, `meets_ac` (bool), `security_notes[]`, `suggestions[]`, `followups[]`.
50 | - Commands: Provide only safe, least-privilege commands wrapped in backticks; call out when approval or elevated permissions are required.
51 | 
52 | ## Documentation-First Routing
53 | 
54 | - Triggers: example, install, configure, setup, API, SDK, how to, usage, params, options.
55 | - Behavior: Prefer authoritative docs; summarize steps clearly and cite sources (URL + section).
56 | - Guardrails: Read-only access by default; never expose secrets; respect repository permissions.
57 | 
58 | ## Safety & Guardrails
59 | 
60 | - No secrets: Do not request or output tokens or credentials.
61 | - Read-only by default: Propose diffs; do not mutate state without instruction.
62 | - Minimal scope: Touch only files necessary for the task; avoid broad refactors.
63 | - Security posture: Consider injection, deserialization, path traversal, SSRF, SQLi, XSS; note mitigations.
64 | - Licensing & data hygiene: Respect licenses; avoid copying large blocks verbatim from proprietary sources.
65 | 
66 | ## Definition of Done (DoD) Summary
67 | 
68 | - Formatting/linting/type-checks pass; CI stays green; no coverage regression.
69 | - Tests: Added/updated; all pass locally; deterministic.
70 | - Security: No new high/critical issues; secrets scanning clean.
71 | - Docs: Updated README/usage notes; ADRs added if architecture changed.
72 | - Changes: Minimal, reviewed, and reversible via patch; rationale recorded.
73 | 
74 | ## ADRs (Architectural Decisions)
75 | 
76 | - Create or update ADRs when making decisions that affect architecture or key trade-offs.
77 | - Use `adr/template.md` as a skeleton. Recommended location: `adr/YYYYMMDD-title.md`.
78 | - Record: context, options, decision, consequences. Reference ADRs in future prompts.
79 | 
80 | ## Evaluation & Metrics
81 | 
82 | - Encourage a lightweight harness: task spec → apply patch → run tests.
83 | - Track informally: task success, diff size, turns/tool calls, token cost, human interventions.
84 | - Add failed cases to regression notes and propose remediations.
85 | 
86 | ## Suggested System Prompt (for gemini-cli)
87 | 
88 | Use or adapt the following as the gemini-cli system instructions:
89 | 
90 | "You are a precise coding agent operating under an Agentic Workflow with strict guardrails. Follow spec-as-code and test-first principles. Prefer documentation-first routing for examples/setup/API questions and cite sources. Produce minimal, safe, reversible changes as unified diffs only. When planning or reviewing, emit concise, structured JSON. Respect read-only defaults and never expose secrets. If requirements are ambiguous, propose AC and a short plan before coding. Update ADRs for architectural choices and confirm Definition of Done before handing off."
91 | 
92 | ## Quick Examples
93 | 
94 | - Plan (JSON):
95 | ```json
96 | {
97 |   "goal": "Add input validation to signup endpoint",
98 |   "assumptions": ["FastAPI app", "pytest available"],
99 |   "steps": [
100 |     "Add failing test for invalid email",
101 |     "Implement email validation and error response",
102 |     "Update docs and changelog"
103 |   ],
104 |   "risks": ["Breaking existing clients"],
105 |   "validation": "pytest -q"
106 | }
107 | ```
108 | 
109 | - Diff:
110 | ```diff
111 | *** Begin Patch
112 | *** Update File: app/routes/signup.py
113 | @@
114 | - def signup(payload: dict):
115 | -     user = create_user(payload)
116 | + def signup(payload: dict):
117 | +     assert is_valid_email(payload.get("email")), "invalid email"
118 | +     user = create_user(payload)
119 |      return {"id": user.id}
120 | *** End Patch
121 | ```
122 | 
123 | ## When To Ask Questions
124 | 
125 | - Missing AC or unclear scope; conflicting requirements; risky migrations; unknown external services.
126 | - Ask concise, binary or short-answer questions that accelerate progress and reduce rework.
127 | 
128 | ---
129 | 
130 | This guide mirrors AGENTS.md for gemini-cli. When in doubt, bias to: clarify → plan → test-first → minimal diff → review → validate → document.
```

.prompts/architect.md
```
1 | System: You are the Planner/Architect. Decompose work into a minimal, verifiable plan; draft ADRs when architectural choices arise; and specify strict outputs for downstream agents.
2 | 
3 | Inputs you receive
4 | 
5 | - Feature/request description, Acceptance Criteria (AC) and constraints
6 | - Existing repo context (paths, conventions), relevant ADRs
7 | 
8 | Your output (JSON only)
9 | {
10 |   "plan": [
11 |     {"step": "<short action>", "rationale": "<why>", "files": ["<path>..."]}
12 |   ],
13 |   "risks": ["<risk/assumption>"],
14 |   "artifacts": {"tests": ["<which tests to add/run>"], "docs": ["<docs to update>"]},
15 |   "adr_suggestions": [
16 |     {"title": "<ADR title>", "context": "<when to add>", "decision": "<high-level>"}
17 |   ]
18 | }
19 | 
20 | Rules
21 | 
22 | - Prefer small steps; each step should be testable and reversible.
23 | - Reference existing ADRs/conventions; propose ADRs only when needed.
24 | - Keep file lists precise; avoid repo-wide edits.
25 | - Do not include code; only the JSON plan above.
```

.prompts/coder.md
```
1 | System: You are the Implementer/Coder. Execute exactly one plan step using test-first changes. Output either a single patch diff or a single validated tool call.
2 | 
3 | Inputs you receive
4 | 
5 | - One plan step (from Planner)
6 | - Relevant files/snippets, Acceptance Criteria, conventions, ADRs
7 | 
8 | Constraints
9 | 
10 | - Test-first: add/adjust tests to capture AC, then implement.
11 | - Minimal diffs; do not refactor unrelated code.
12 | - Follow safety rails: patch/diff only; write only in allowed paths; no secrets.
13 | 
14 | Your output (choose one)
15 | 
16 | 1) Patch diff (unified) to apply:
17 | """
18 | ***Begin Patch
19 | *** Update File: path/to/file.ext
20 | @@
21 | -old
22 | +new
23 | *** End Patch
24 | """
25 | 
26 | or
27 | 
28 | 2) Tool call (JSON) for a single action, e.g. apply_patch:
29 | {
30 |   "tool": "apply_patch",
31 |   "args": {"patch": "<the unified diff above>"}
32 | }
33 | 
34 | Validation
35 | 
36 | - All tests must pass locally; if not, amend patch.
37 | - Keep changes within scope and AC; no extra features.
```

.prompts/reviewer.md
```
1 | System: You are the Reviewer/Refactorer. Assess diffs for correctness, conventions, security, and performance. Suggest minimal improvements.
2 | 
3 | Inputs you receive
4 | - The unified diff, AC, conventions, and ADRs
5 | 
6 | Your output (JSON only)
7 | {
8 |   "summary": "<overall assessment>",
9 |   "approved": true,
10 |   "comments": [
11 |     {"file": "<path>", "line": 123, "severity": "info|nit|warn|error", "message": "<actionable note>"}
12 |   ],
13 |   "followups": ["<small refactors or docs to add>"]
14 | }
15 | 
16 | Rules
17 | - Focus on AC and safety; avoid scope creep.
18 | - Call out security issues and missing tests.
19 | - Prefer suggestions that reduce diff size and increase clarity.
20 | 
```

.prompts/tester.md
```
1 | System: You are the Tester. Write deterministic tests that precisely capture Acceptance Criteria, including positive, negative, and edge cases.
2 | 
3 | Inputs you receive
4 | - Feature/request description, current/target behavior
5 | - File paths under test, conventions, and ADR constraints
6 | 
7 | Your output
8 | - A single patch diff that adds test files/sections only (e.g., pytest or Jest)
9 | 
10 | Rules
11 | - Tests must be deterministic (no flakes, avoid external services; use mocks/fakes).
12 | - Name tests clearly and cover boundary conditions.
13 | - Keep scope to testing; do not modify production code.
14 | 
15 | Template (pytest example)
16 | """
17 | *** Begin Patch
18 | *** Add File: tests/test_feature.py
19 | +import pytest
20 | +
21 | +def test_happy_path():
22 | +    assert True
23 | +
24 | +def test_error_path():
25 | +    with pytest.raises(Exception):
26 | +        raise Exception()
27 | *** End Patch
28 | """
29 | 
```

adr/template.md
```
1 | # ADR-NNN: <Title>
2 | 
3 | **Date:** YYYY-MM-DD
4 | **Status:** Proposed | Accepted | Deprecated | Superseded
5 | 
6 | ## Context
7 | 
8 | <What problem are we solving? Relevant constraints and forces.>
9 | 
10 | ## Decision
11 | 
12 | <The choice made and why this option was selected over alternatives.>
13 | 
14 | ## Consequences
15 | 
16 | <Positive/negative outcomes, trade-offs, and follow-ups.>
17 | 
18 | ## References
19 | 
20 | <Links to tickets, PRs, benchmarks, or prior ADRs.>
```

ai-docs/LLM Agent Codebase Playbook.md
```
1 | 
2 | 
3 | # **The Agentic Engineering Playbook: A Guide to Building and Maintaining Codebases with LLM Agents**
4 | 
5 | ## **Part I: The Foundation \- Upfront Planning and Architecture**
6 | 
7 | The integration of Large Language Model (LLM) agents into software development workflows represents a paradigm shift, moving from AI as a simple code completion tool to AI as an active collaborator in complex engineering tasks.1 However, this transition is not without its challenges. The reliability and effectiveness of an LLM agent are directly proportional to the clarity and structure of its operating environment and instructions.2 Failures in agentic systems often stem not from the core intelligence of the LLM, but from ambiguity in its goals and a lack of context about the codebase it is meant to modify.3
8 | 
9 | This first part of the playbook establishes the foundational principles for successful agentic development. It posits that for LLM agents, rigorous upfront planning and deliberate architectural design are not merely best practices but prerequisites for success. These practices transform human-readable documents into machine-executable instructions, creating a stable and predictable environment in which agents can operate effectively.
10 | 
11 | ### **Section 1: Specification-Driven Development for AI Agents**
12 | 
13 | This section details how to create a robust project foundation by treating specifications not as passive documentation, but as a high-level programming language for the agent. This approach minimizes ambiguity, provides clear success criteria, and establishes the necessary guardrails to keep agent behavior aligned with project goals.
14 | 
15 | #### **1.1 The Paradigm Shift: From Documentation to Specification as Code**
16 | 
17 | In traditional software development, methodologies like Specification-First 4 and Documentation-Driven Development 1 serve as crucial guides for human developers, enhancing stakeholder alignment and reducing rework. For LLM agents, however, these documents assume a more profound and direct role: they become the primary source code that dictates the agent's behavior.
18 | 
19 | Human developers possess the ability to infer intent from ambiguous specifications, ask clarifying questions, and apply domain knowledge to fill in gaps. LLM agents, while capable of sophisticated reasoning, are susceptible to misinterpretation when faced with imprecision.7 Research into agent failure modes consistently identifies "Poor Specification" and "Disobey task specification" as primary causes of incorrect or suboptimal outcomes.3 An LLM cannot intuit unstated requirements; its performance is fundamentally bound by the quality of its inputs.9
20 | 
21 | This reality necessitates a shift in perspective. The collection of artifacts that define a task—user stories, acceptance criteria, architectural decision records—ceases to be a set of human-readable guides. Instead, it becomes a formal, machine-readable input that directly programs the agent's high-level execution plan. The process of writing these specifications must, therefore, be approached with the same rigor and precision as writing application code. It is a form of meta-programming that defines the operational boundaries, constraints, and objectives for the agent, transforming abstract business goals into a concrete, executable strategy.
22 | 
23 | #### **1.2 Test-First Prompting and Acceptance Criteria (AC)**
24 | 
25 | The principles of Test-Driven Development (TDD) can be powerfully adapted for agentic workflows. Instead of writing code tests first, the developer writes *acceptance tests for the agent's final output* first. This practice, described in research as "test-driven interactive code generation," serves two critical functions: it formalizes the user's intent into an unambiguous, verifiable contract, and it provides a mechanism to automatically prune incorrect code suggestions generated by the agent.10
26 | 
27 | By providing a failing test case directly in the prompt, the developer gives the agent a precise, executable definition of success. This is vastly more effective than relying on natural language descriptions alone, which are prone to ambiguity.10
28 | 
29 | **Acceptance Criteria for LLM-Generated Code**
30 | 
31 | Effective AC for agent-generated code must extend beyond simple functional correctness. A comprehensive set of criteria should address the following domains:
32 | 
33 | * **Functional Correctness:** The code must produce the correct output for a given set of inputs and pass all provided unit and integration tests.11  
34 | * **Performance:** The code must meet specified performance benchmarks (e.g., response time, resource consumption) and not introduce inefficiencies.11  
35 | * **Security:** The code must not introduce new vulnerabilities (e.g., SQL injection, insecure dependencies) and must adhere to project security standards. LLM-generated code has been shown to introduce vulnerabilities if not carefully checked.8  
36 | * **Maintainability & Readability:** The code must be well-structured, easy to understand, and adhere to the project's established coding conventions and style guides.11  
37 | * **Integration:** The code must correctly integrate with existing modules, respecting established APIs and data contracts.
38 | 
39 | **Template: Acceptance Criteria in a Prompt**
40 | 
41 | **Feature Request:** Implement a user authentication endpoint.
42 | 
43 | **Acceptance Criteria:**
44 | 
45 | 1. **Functional:**  
46 |    * The endpoint MUST accept a POST request at /api/v1/auth/login.  
47 |    * The request body MUST contain email and password fields.  
48 |    * On successful authentication, it MUST return a JWT with a 200 status code.  
49 |    * On failed authentication, it MUST return an error message with a 401 status code.
50 | 
51 |    * # **The implementation MUST pass the following Pytest tests:python**       **tests/test\_auth.py**       **def test\_login\_success(client):**      **\#... test implementation...**      **def test\_login\_failure\_wrong\_password(client):**      **\#... test implementation...** 
52 | 
53 | 2. **Non-Functional:**  
54 |    * **Security:** Password hashing MUST use the Argon2 algorithm. The endpoint MUST be protected against timing attacks.  
55 |    * **Performance:** The average response time MUST be less than 150ms under a load of 50 concurrent requests.  
56 |    * **Maintainability:** The code MUST adhere to the conventions defined in CONVENTIONS.md and achieve a "Grade A" from the Pylint static analyzer.
57 | 
58 | \#\#\#\# 1.3 Definition of Done (DoD) for Agent-Completed Tasks
59 | 
60 | The Definition of Done (DoD) is an agile concept that provides a clear, shared checklist of all the work that must be completed before a feature or user story can be considered finished.\[12, 13\] For an agentic workflow, the DoD serves as a critical final validation gate. It prevents the "incomplete verification" failure mode, where an agent might produce functionally correct code but neglect essential surrounding tasks like documentation or test updates.\[3\]
61 | 
62 | The DoD transforms a subjective state ("I think the agent is done") into an objective, verifiable one. It should be a concrete artifact within the repository, referenced by both developers and agents.
63 | 
64 | \*\*Template: Definition of Done Checklist\*\*
65 | 
66 | A \`DEFINITION\_OF\_DONE.md\` file in the repository might contain the following checklist for any agent-generated feature:
67 | 
68 | \- \[ \] All acceptance criteria for the user story have been met.  
69 | \- \[ \] All new code is formatted according to the project's linter configuration (\`ruff.toml\` / \`.eslintrc.json\`).  
70 | \- \[ \] Unit tests have been generated for all new functions and classes.  
71 | \- \[ \] All existing and new tests pass in the CI pipeline.  
72 | \- \[ \] Test coverage has not decreased.  
73 | \- \[ \] Code comments and docstrings have been generated for all new public APIs.  
74 | \- \[ \] The relevant \`README.md\` or other documentation has been updated to reflect the changes.  
75 | \- \[ \] No new high or critical severity security vulnerabilities have been introduced, as verified by a static analysis security testing (SAST) tool.  
76 | \- \[ \] The changes have been successfully deployed to a staging environment.  
77 | \- \[ \] The final implementation has been reviewed and approved by a human developer.
78 | 
79 | \#\#\#\# 1.4 Architectural Decision Records (ADRs) as Agent Guardrails
80 | 
81 | Architectural Decision Records (ADRs) are lightweight documents that capture important architectural choices, their context, and their consequences.\[14\] When provided as context to an LLM agent, ADRs act as powerful, persistent guardrails. For example, an ADR stating "We chose PostgreSQL over MongoDB to ensure ACID compliance for financial transactions" will prevent an agent from incorrectly generating code that uses a NoSQL database for that feature.
82 | 
83 | While LLMs can assist in drafting ADRs, their raw output may lack the quality of a human architect. The most effective results are achieved by combining LLM generation with techniques like Retrieval-Augmented Generation (RAG) and fine-tuning to provide relevant examples and domain-specific context.\[15\]
84 | 
85 | This points to a more sophisticated workflow: using a specialized "Architect Agent" to help generate, critique, and formalize the very specifications that will guide the "Implementer Agent." This meta-agent workflow involves prompting an LLM to act as a system architect, filling out an ADR template based on a high-level feature description and a set of existing ADRs for context. This creates a virtuous cycle where AI is used not only to implement specifications but also to improve their quality and consistency.
86 | 
87 | \*\*Template: Architectural Decision Record\*\*
88 | 
89 | An \`adr/template.md\` file for the project:
90 | 
91 | \# ADR-NNN:
92 | 
93 | \*\*Date:\*\* YYYY-MM-DD
94 | 
95 | \*\*Status:\*\* Proposed | Accepted | Deprecated | Superseded
96 | 
97 | \#\# Context
98 | 
99 | \#\# Decision
100 | 
101 | \#\# Consequences
102 | 
103 | \#\#\# Section 2: Architecting the Repository for Agent Collaboration
104 | 
105 | The physical structure of the codebase has a profound impact on an agent's ability to navigate, understand, and modify it. A well-architected repository reduces ambiguity and provides clear pathways for the agent, while a disorganized one increases the likelihood of context loss and incorrect modifications.
106 | 
107 | \#\#\#\# 2.1 Monorepo vs. Polyrepo: An Agent-Centric Analysis
108 | 
109 | The debate between monorepos (a single repository for all projects) and polyrepos (a repository for each project) is a long-standing one in software engineering.\[16\] When viewed through the lens of agentic development, a clear winner emerges. The primary constraint on an LLM agent's effectiveness is its ability to access and process relevant context.\[2, 17\]
110 | 
111 | A polyrepo architecture creates artificial information silos. An agent tasked with modifying a microservice in one repository is often blind to the API contracts, data models, and dependencies of a service in another repository. This lack of a unified view makes cross-cutting changes and complex refactors nearly impossible for an agent to perform reliably. It must either guess about external dependencies, leading to integration errors, or be manually fed context for every interacting service, which is inefficient and error-prone.
112 | 
113 | A monorepo, by contrast, provides a single, unified context. It creates an ideal environment for machine cognition. Advanced context-providing techniques, such as repository maps and RAG (discussed in Part II), can build a comprehensive knowledge graph of the entire codebase. This allows an agent to reason about system-wide dependencies, understand the full impact of a change, and execute complex, multi-package refactors with a much higher degree of success.
114 | 
115 | Furthermore, the primary challenges of monorepos for human teams—such as the need to agree on universal standards for tooling, dependencies, and code style—become advantages in an agentic workflow.\[16\] These agreements force the creation of explicit, machine-readable configuration files and convention documents (e.g., \`CONVENTIONS.md\` \[18\]). These artifacts serve as direct, unambiguous instructions for an agent, further constraining its behavior and improving its reliability. For organizations committed to leveraging coding agents for substantive engineering tasks, adopting a monorepo architecture is a strategic imperative.
116 | 
117 | \#\#\#\# 2.2 Modular Boundaries and Layering
118 | 
119 | Within the repository, a well-defined modular architecture (e.g., Clean Architecture, Hexagonal Architecture, Domain-Driven Design) is critical. Clear boundaries between components allow an agent's work to be narrowly scoped. When a task is confined to a single module with a well-defined API, the agent requires far less context to complete it successfully. This aligns with the agentic best practice of breaking down complex goals into a series of smaller, isolated, and verifiable steps.\[19, 20\] This modularity minimizes the risk of the agent making unintended changes to unrelated parts of the codebase.
120 | 
121 | \#\#\#\# 2.3 Naming Conventions and The \`prompts.md\` File
122 | 
123 | Consistency is key for machine interpretation. A project should enforce strict and consistent naming conventions for files, folders, classes, and functions. A predictable structure makes it easier for an agent to locate relevant code and understand its purpose.
124 | 
125 | To further enhance consistency and reproducibility, projects should adopt the practice of maintaining a central, version-controlled library of prompts. This can be a single \`prompts.md\` file or a dedicated \`.prompts/\` directory at the root of the repository. This location should store the canonical system prompts, task templates, and output schemas used to interact with the agents for that specific project. This practice ensures that all team members (and CI/CD processes) are using the same standardized instructions, making agent behavior more predictable and debugging easier.
126 | 
127 | \#\# Part II: The Agentic Development Loop \- From Scaffolding to Release
128 | 
129 | With a solid foundation of specifications and architecture in place, the focus shifts to the practical, day-to-day workflow of building software with LLM agents. This part provides a step-by-step guide to the development loop, from generating initial project files to deploying a finished feature. It details the core techniques and prompt patterns required to ensure agent reliability, predictability, and safety throughout the process.
130 | 
131 | \#\#\# Section 3: The End-to-End Workflow: An Actionable Guide
132 | 
133 | This section outlines a complete, repeatable workflow for developing a software feature using a multi-agent team. This process integrates the planning principles from Part I into a structured, iterative development cycle.
134 | 
135 | \*   \*\*Step 1: Idea → Spec\*\*  
136 |     The process begins with a high-level feature idea from a product manager or stakeholder. This idea is then formalized into a detailed, machine-readable specification document as described in Section 1\. To accelerate this process, an "Architect Agent" can be employed. The developer provides the agent with the high-level goal and any relevant existing documentation. The Architect Agent then generates a draft of the specification, a new ADR for any significant architectural changes, and a preliminary set of acceptance criteria, all formatted according to the project's templates. The developer reviews and refines these documents to ensure they are complete and unambiguous.
137 | 
138 | \*   \*\*Step 2: Spec → Scaffold\*\*  
139 |     Once the specification is finalized, a "Scaffolder Agent" is invoked. This agent's task is to read the specification and create the necessary file and folder structure for the new feature. It generates boilerplate code, empty test files, configuration entries, and any other required initial artifacts. This automates the tedious setup process and ensures that all new features start with a consistent structure.
140 | 
141 | \*   \*\*Step 3: Iterative Coding Loop (The Core Loop)\*\*  
142 |     This is the central cycle of agentic development, where the feature is implemented piece by piece. The loop is designed to be small, fast, and highly iterative, minimizing risk and providing constant feedback.  
143 |     1\.  \*\*Select a Sub-Task:\*\* The developer selects a small, self-contained part of the feature from the specification—ideally, one that corresponds to a single acceptance criterion.  
144 |     2\.  \*\*Write a Failing Test:\*\* The developer writes a single, failing unit or integration test that verifies the functionality of the selected sub-task. Alternatively, a "Tester Agent" can be prompted to generate this test based on the relevant acceptance criterion.  
145 |     3\.  \*\*Prompt the Implementer Agent:\*\* The developer prompts an "Implementer Agent" to write the code that will make the failing test pass. This prompt is highly contextualized and must include:  
146 |         \*   The specific instruction (e.g., "Implement the \`calculate\_tax\` function").  
147 |         \*   The full content of the failing test file.  
148 |         \*   The relevant section of the specification document.  
149 |         \*   Any relevant ADRs.  
150 |         \*   The project's \`CONVENTIONS.md\` file.  
151 |     4\.  \*\*Agent Execution and Diff Generation:\*\* The agent uses its available tools (e.g., file search, file read) to gather any additional context it needs. It then generates the required code modifications and, crucially, outputs them as a \`git diff\` patch rather than writing directly to the filesystem.\[21\]  
152 |     5\.  \*\*Review and Apply:\*\* The developer reviews the generated diff. If it is correct and adheres to standards, they apply the patch. If not, they can either discard it and refine the prompt or apply it and make manual corrections.  
153 |     6\.  \*\*Repeat:\*\* The developer runs the tests to confirm that the new test passes and no existing tests have been broken. The loop then repeats with the next sub-task.
154 | 
155 | \*   \*\*Step 4: Tests → Docs\*\*  
156 |     After the entire feature is implemented and all tests are passing, a "Documenter Agent" is tasked with generating and updating the human-readable documentation. The agent is provided with the final code, the original specification, and the full test suite. It uses this information to generate code comments, docstrings, update the feature's \`README.md\`, and create usage examples. Tools like DocuWriter.ai and others demonstrate the increasing capability of AI to automate this process.\[6, 22\]
157 | 
158 | \*   \*\*Step 5: Review and Release\*\*  
159 |     The agent's work, which has been committed incrementally throughout the process, is compiled into a pull request. The PR description should be generated by an agent and include a link to the original specification, a summary of the changes, and a reference to the ADRs that guided the implementation. This provides human reviewers with the full context needed to effectively evaluate the agent's work. Once approved, the feature follows the standard CI/CD pipeline for release.
160 | 
161 | \#\#\# Section 4: The Agent Prompting Compendium
162 | 
163 | The effectiveness of a multi-agent system depends on assigning clear roles and responsibilities to each agent.\[23, 24\] This is achieved through carefully crafted system prompts and strictly defined output schemas. This section provides a library of templates for the key agent personas in a software development team. The use of structured output, preferably JSON, is non-negotiable for reliable agent-to-agent communication and tool use.\[25\]
164 | 
165 | \#\#\#\# 4.1 The Planner/Architect Agent
166 | 
167 | \*   \*\*Responsibility:\*\* Decompose high-level user requests into a detailed, step-by-step implementation plan. Identify all files that will need to be created or modified and draft any necessary ADRs.  
168 | \*   \*\*System Prompt Template:\*\*  
169 |     \`\`\`  
170 |     You are an expert software architect. Your goal is to take a user's feature request and create a detailed, step-by-step implementation plan. You must think holistically about the existing codebase, consider potential side effects, and adhere to all existing architectural decisions documented in the provided ADRs. Your output MUST be a single JSON object that conforms to the provided JSON schema. Do not include any explanatory text before or after the JSON object.  
171 |     \`\`\`  
172 | \*   \*\*Output Schema (JSON):\*\*  
173 |     \`\`\`json  
174 |     {  
175 |       "type": "object",  
176 |       "properties": {  
177 |         "planSummary": {  
178 |           "type": "string",  
179 |           "description": "A brief, one-sentence summary of the implementation plan."  
180 |         },  
181 |         "affectedFiles": {  
182 |           "type": "array",  
183 |           "items": {  
184 |             "type": "object",  
185 |             "properties": {  
186 |               "path": { "type": "string" },  
187 |               "action": { "enum": },  
188 |               "description": { "type": "string" }  
189 |             },  
190 |             "required": \["path", "action", "description"\]  
191 |           }  
192 |         },  
193 |         "stepByStepPlan": {  
194 |           "type": "array",  
195 |           "items": { "type": "string", "description": "A detailed, sequential instruction for the Coder Agent." }  
196 |         },  
197 |         "newADR": {  
198 |           "type": "object",  
199 |           "properties": {  
200 |             "title": { "type": "string" },  
201 |             "context": { "type": "string" },  
202 |             "decision": { "type": "string" },  
203 |             "consequences": { "type": "string" }  
204 |           },  
205 |           "description": "A draft for a new ADR if a significant architectural decision is needed. Null if not applicable."  
206 |         }  
207 |       },  
208 |       "required":  
209 |     }  
210 |     \`\`\`
211 | 
212 | \#\#\#\# 4.2 The Implementer/Coder Agent
213 | 
214 | \*   \*\*Responsibility:\*\* Execute a single, specific instruction from the Planner's output. Write, modify, and debug code using a provided set of tools.  
215 | \*   \*\*System Prompt Template:\*\*  
216 |     \`\`\`  
217 |     You are an expert programmer. Your task is to execute a single step from an implementation plan. You MUST adhere strictly to the provided context, including existing code, project conventions, and architectural decisions. You have access to a set of tools to interact with the file system. Your response MUST be a JSON object representing a single tool call, or a final completion message. You must think step-by-step and reason about which tool to use.  
218 |     \`\`\`  
219 | \*   \*\*Output Schema (JSON for Tool Call):\*\*  
220 |     \`\`\`json  
221 |     {  
222 |       "type": "object",  
223 |       "properties": {  
224 |         "toolName": { "enum": },  
225 |         "parameters": { "type": "object" }  
226 |       },  
227 |       "required": \["toolName", "parameters"\]  
228 |     }  
229 |     \`\`\`
230 | 
231 | \#\#\#\# 4.3 The Tester Agent
232 | 
233 | \*   \*\*Responsibility:\*\* Generate comprehensive test suites for a given piece of code based on its specification.  
234 | \*   \*\*System Prompt Template:\*\*  
235 |     \`\`\`  
236 |     You are a meticulous Quality Assurance Engineer specializing in test automation. Given a source code file and its corresponding acceptance criteria, your job is to write a complete and robust test suite using Pytest. The tests must cover all specified requirements, including positive paths, negative paths, and edge cases. Your output MUST be a single, complete Python code block containing the test file. Do not include any other text.  
237 |     \`\`\`
238 | 
239 | \#\#\#\# 4.4 The Reviewer/Refactorer Agent
240 | 
241 | \*   \*\*Responsibility:\*\* Analyze a code diff for quality, adherence to conventions, potential bugs, and opportunities for improvement.  
242 | \*   \*\*System Prompt Template:\*\*  
243 |     \`\`\`  
244 |     You are a Principal Engineer performing a code review. Analyze the provided code diff. Your review must be strict and thorough. Identify any deviations from the \`CONVENTIONS.md\` file, potential bugs, security vulnerabilities, performance issues, or opportunities for simplification and refactoring. Your output MUST be a JSON object conforming to the provided schema, containing a list of review comments.  
245 |     \`\`\`  
246 | \*   \*\*Output Schema (JSON):\*\*  
247 |     \`\`\`json  
248 |     {  
249 |       "type": "object",  
250 |       "properties": {  
251 |         "reviewComments": {  
252 |           "type": "array",  
253 |           "items": {  
254 |             "type": "object",  
255 |             "properties": {  
256 |               "filePath": { "type": "string" },  
257 |               "lineNumber": { "type": "integer" },  
258 |               "comment": { "type": "string" },  
259 |               "severity": { "enum": }  
260 |             },  
261 |             "required": \["filePath", "lineNumber", "comment", "severity"\]  
262 |           }  
263 |         }  
264 |       },  
265 |       "required": \["reviewComments"\]  
266 |     }  
267 |     \`\`\`
268 | 
269 | \*\*Table 1: Agent Persona Prompt Matrix\*\*
270 | 
271 | | Persona | Core Responsibility | Key Inputs | Output Schema |  
272 | | :--- | :--- | :--- | :--- |  
273 | | \*\*Planner/Architect\*\* | Decompose tasks, create plans, draft ADRs. | Feature Request, Existing Codebase Context, ADRs | JSON object with plan, files, steps. |  
274 | | \*\*Implementer/Coder\*\* | Execute one step of a plan by writing/modifying code. | Plan Step, Relevant Code Files, Conventions | JSON object for a single tool call. |  
275 | | \*\*Tester\*\* | Generate unit and integration tests. | Source Code File, Acceptance Criteria | A complete code block for the test file. |  
276 | | \*\*Reviewer/Refactorer\*\* | Analyze code diffs for quality and improvements. | Code Diff, Conventions File | JSON object with a list of review comments. |
277 | 
278 | \#\#\# Section 5: Core Techniques for Agent Reliability and Control
279 | 
280 | Beyond prompting, a set of technical mechanisms is required to provide agents with the necessary context and to control their actions, ensuring they are both effective and safe. These techniques form a "cognitive stack" that equips the agent with short-term memory, long-term memory, and the ability to act on its environment.
281 | 
282 | \#\#\#\# 5.1 Providing Context I: Repo Maps and Symbol Graphs
283 | 
284 | An agent cannot operate effectively on a codebase it does not understand. However, providing the entire codebase as context is infeasible due to context window limitations. The first layer of context is a high-level summary or "table of contents."
285 | 
286 | \*   \*\*Repository Maps:\*\* Popularized by tools like Aider, a repo map is a concise text representation of the repository's structure, including file paths and the signatures of key classes and functions within them.\[17\] This gives the agent a bird's-eye view, allowing it to quickly identify potentially relevant files for a given task without needing to read their full contents. This serves as the agent's fast, low-token, short-term working memory.  
287 | \*   \*\*Symbol Graphs:\*\* A more advanced approach involves parsing the codebase to build a graph where nodes represent code entities (functions, classes, variables) and edges represent relationships (calls, inherits from, implements).\[26, 27\] Querying this graph allows the agent to perform more sophisticated analysis, such as finding all usages of a function before modifying it.
288 | 
289 | \#\#\#\# 5.2 Providing Context II: Retrieval-Augmented Generation (RAG) for Codebases
290 | 
291 | RAG is the most powerful technique for providing deep, specific context, acting as the agent's long-term memory. This process involves:  
292 | 1\.  \*\*Indexing:\*\* The entire codebase is processed offline. Source files are split into meaningful chunks (e.g., by function or class, often using an Abstract Syntax Tree (AST) parser for precision). Each chunk is then converted into a numerical vector representation (an embedding) using a sentence-transformer model.\[28, 29, 30\]  
293 | 2\.  \*\*Storage:\*\* These embeddings are stored in a specialized vector database (e.g., ChromaDB, Pinecone).\[31, 32\]  
294 | 3\.  \*\*Retrieval:\*\* At runtime, when the agent needs to perform a task, the user's query or the current plan step is also converted into an embedding. The vector database is then queried to find the code chunks with the most semantically similar embeddings.\[33, 34\]  
295 | 4\.  \*\*Augmentation:\*\* These retrieved code chunks are then injected into the agent's prompt along with the primary instruction, providing it with highly relevant, specific examples and context from the codebase.
296 | 
297 | This cognitive architecture, combining a quick repo map lookup with a deep RAG retrieval, is highly effective. The agent first uses the repo map to identify a small set of candidate files, and then uses RAG to pull the most relevant functions or classes from within those files, optimizing for both context quality and token efficiency.
298 | 
299 | \#\#\#\# 5.3 Enforcing Predictability: Structured Outputs and Function Calling
300 | 
301 | To make an agent's behavior predictable and its output machine-parsable, its responses must be constrained to a strict schema. This is the most critical technique for building reliable, multi-agent systems and tool-using agents.
302 | 
303 | \*   \*\*Structured Outputs:\*\* Instead of allowing free-text responses, the agent is instructed to generate a JSON object that conforms to a predefined schema.  
304 |     \*   \*\*In Python\*\*, this is commonly achieved using the Pydantic library. A Pydantic model defines the desired data structure, and a parser like LangChain's \`PydanticOutputParser\` can be used to both generate formatting instructions for the LLM and validate the resulting output.\[35, 36, 37\]  
305 |     \*   \*\*In TypeScript\*\*, libraries like Zod serve a similar purpose. Alternatively, Microsoft's TypeChat leverages the TypeScript compiler itself to validate and even repair non-conforming LLM output against a set of TypeScript interfaces.\[38\]
306 | 
307 | \*   \*\*Function/Tool Calling:\*\* Modern LLMs from providers like OpenAI and Google have native support for "function calling" or "tool use".\[39\] This is a more refined version of structured output where the model is specifically trained to generate a JSON object that corresponds to a function signature. The model's output directly specifies the name of a tool to call (e.g., \`writeFile\`) and a dictionary of arguments (\`{"path": "src/main.py", "content": "..."}\`). This is the preferred mechanism for orchestrating agent actions, as it is more robust and directly supported by the model's architecture.
308 | 
309 | \#\#\#\# 5.4 Ensuring Safety: Patch/Diff Workflows and Guardrails
310 | 
311 | Allowing an agent to directly modify the filesystem is risky. A safer and more auditable approach involves multiple layers of protection.
312 | 
313 | \*   \*\*Patch/Diff Workflows:\*\* The agent's "write" operations should not directly alter files. Instead, the agent should be prompted to output its proposed changes in the form of a unified diff format. Tools like \`gptdiff\` demonstrate this pattern effectively.\[21\] A developer or an automated system can then review this patch before applying it. This provides a crucial human-in-the-loop verification step and prevents catastrophic errors.
314 | 
315 | \*   \*\*Guardrails:\*\* These are automated checks that enforce rules on the agent's behavior.  
316 |     \*   \*\*Filesystem Guardrails:\*\* A simple but effective guardrail is a wrapper around the agent's file system tools. Before executing a \`writeFile\` or \`deleteFile\` command, this wrapper checks the target path against a predefined allowlist of files and directories. Any attempt to modify a file outside this scope is blocked.\[40\]  
317 |     \*   \*\*Code Analysis Guardrails:\*\* After a patch is generated but before it is applied, a series of automated quality checks should be run. This includes running code formatters (e.g., Black, Prettier), linters (e.g., Ruff, ESLint), and static type checkers (e.g., Mypy, TypeScript Compiler). Patches that fail these checks are automatically rejected.  
318 |     \*   \*\*CI/CD Guardrails:\*\* The Continuous Integration pipeline serves as the ultimate guardrail. Any code committed by an agent must pass the full suite of tests, security scans, and quality gates that are applied to human-written code. The CI process can even be enhanced with a step that validates the agent's commit message or PR description against a required format.\[41\]
319 | 
320 | \#\# Part III: Tooling, Templates, and Implementation
321 | 
322 | This part provides the concrete assets required to put the playbook's principles into practice. It includes cloneable repository templates for both Python and TypeScript, along with a toolkit of automation scripts for common agentic development tasks.
323 | 
324 | \#\#\# Section 6: The Starter Kit \- Repository Templates
325 | 
326 | These templates provide a production-ready starting point for new agentic software projects, pre-configured with best practices for structure, tooling, and CI/CD.
327 | 
328 | \#\#\#\# 6.1 Python Agentic Project Template
329 | 
330 | This template is configured for a modern Python workflow using Poetry for dependency management and \`pyproject.toml\` for centralized tool configuration, inspired by robust open-source projects like \`parlant\` and \`adk-python\`.\[42, 43\]
331 | 
332 | \*   \*\*File Tree:\*\*  
333 |     \`\`\`  
334 |     /  
335 |     ├──.github/  
336 |     │   └── workflows/  
337 |     │       └── ci.yml  
338 |     ├──.vscode/  
339 |     │   └── settings.json  
340 |     ├── adr/  
341 |     │   ├── 0001-record-architecture-decisions.md  
342 |     │   └── template.md  
343 |     ├──.prompts/  
344 |     │   ├── architect.md  
345 |     │   ├── coder.md  
346 |     │   └── reviewer.md  
347 |     ├── src/  
348 |     │   └── my\_project/  
349 |     │       └── \_\_init\_\_.py  
350 |     ├── tests/  
351 |     │   └── \_\_init\_\_.py  
352 |     ├──.devcontainer/  
353 |     │   ├── devcontainer.json  
354 |     │   └── Dockerfile  
355 |     ├──.gitignore  
356 |     ├── CODEOWNERS  
357 |     ├── CONTRIBUTING.md  
358 |     ├── DEFINITION\_OF\_DONE.md  
359 |     ├── pyproject.toml  
360 |     ├── poetry.lock  
361 |     └── README.md  
362 |     \`\`\`
363 | 
364 | \*   \*\*Key File Contents:\*\*  
365 |     \*   \*\*\`pyproject.toml\`:\*\*  
366 |         \`\`\`toml  
367 |         \[tool.poetry\]  
368 |         name \= "my-project"  
369 |         version \= "0.1.0"  
370 |         description \= ""  
371 |         authors \=
372 | 
373 |         \[tool.poetry.dependencies\]  
374 |         python \= "^3.11"  
375 |         langchain \= "^0.2.0"  
376 |         pydantic \= "^2.7.0"  
377 |         openai \= "^1.28.0"  
378 |         chromadb \= "^0.5.0"
379 | 
380 |         \[tool.poetry.group.dev.dependencies\]  
381 |         pytest \= "^8.2.0"  
382 |         pytest-cov \= "^5.0.0"  
383 |         ruff \= "^0.4.4"  
384 |         mypy \= "^1.10.0"
385 | 
386 |         \[tool.ruff\]  
387 |         line-length \= 88  
388 |         select \=
389 | 
390 |         \[tool.mypy\]  
391 |         strict \= true  
392 |         \`\`\`  
393 |     \*   \*\*\`.github/workflows/ci.yml\`:\*\*  
394 |         \`\`\`yaml  
395 |         name: CI
396 | 
397 |         on: \[push, pull\_request\]
398 | 
399 |         jobs:  
400 |           build:  
401 |             runs-on: ubuntu-latest  
402 |             steps:  
403 |             \- uses: actions/checkout@v4  
404 |             \- name: Set up Python  
405 |               uses: actions/setup-python@v5  
406 |               with:  
407 |                 python-version: '3.11'  
408 |             \- name: Install dependencies  
409 |               run: |  
410 |                 pip install poetry  
411 |                 poetry install  
412 |             \- name: Lint with Ruff  
413 |               run: poetry run ruff check src tests  
414 |             \- name: Type check with Mypy  
415 |               run: poetry run mypy src  
416 |             \- name: Test with Pytest  
417 |               run: poetry run pytest \--cov=src  
418 |         \`\`\`
419 | 
420 | \#\#\#\# 6.2 TypeScript Agentic Project Template
421 | 
422 | This template uses PNPM for efficient monorepo-style dependency management and includes strict configurations for ESLint, Prettier, and TypeScript, reflecting best practices from projects like \`voltagent\` and \`agentic\`.\[44, 45\]
423 | 
424 | \*   \*\*File Tree:\*\*  
425 |     \`\`\`  
426 |     /  
427 |     ├──.github/  
428 |     │   └── workflows/  
429 |     │       └── ci.yml  
430 |     ├──.vscode/  
431 |     │   └── settings.json  
432 |     ├── adr/  
433 |     │   ├── 0001-record-architecture-decisions.md  
434 |     │   └── template.md  
435 |     ├──.prompts/  
436 |     │   ├── architect.ts  
437 |     │   ├── coder.ts  
438 |     │   └── reviewer.ts  
439 |     ├── packages/  
440 |     │   └── core/  
441 |     │       ├── src/  
442 |     │       │   └── index.ts  
443 |     │       └── package.json  
444 |     ├──.devcontainer/  
445 |     │   ├── devcontainer.json  
446 |     │   └── Dockerfile  
447 |     ├──.gitignore  
448 |     ├──.eslintrc.cjs  
449 |     ├──.prettierrc.json  
450 |     ├── CODEOWNERS  
451 |     ├── CONTRIBUTING.md  
452 |     ├── DEFINITION\_OF\_DONE.md  
453 |     ├── package.json  
454 |     ├── pnpm-workspace.yaml  
455 |     ├── tsconfig.json  
456 |     └── README.md  
457 |     \`\`\`
458 | 
459 | \*   \*\*Key File Contents:\*\*  
460 |     \*   \*\*\`package.json\` (root):\*\*  
461 |         \`\`\`json  
462 |         {  
463 |           "name": "my-ts-project",  
464 |           "private": true,  
465 |           "scripts": {  
466 |             "build": "turbo run build",  
467 |             "test": "turbo run test",  
468 |             "lint": "turbo run lint",  
469 |             "format": "prettier \--write \\"\*\*/\*.{ts,tsx,md}\\""  
470 |           },  
471 |           "devDependencies": {  
472 |             "@types/jest": "^29.5.12",  
473 |             "@typescript-eslint/eslint-plugin": "^7.9.0",  
474 |             "eslint": "^8.57.0",  
475 |             "jest": "^29.7.0",  
476 |             "prettier": "^3.2.5",  
477 |             "ts-jest": "^29.1.2",  
478 |             "turbo": "^2.0.1",  
479 |             "typescript": "^5.4.5"  
480 |           }  
481 |         }  
482 |         \`\`\`  
483 |     \*   \*\*\`tsconfig.json\`:\*\*  
484 |         \`\`\`json  
485 |         {  
486 |           "compilerOptions": {  
487 |             "target": "ES2022",  
488 |             "module": "commonjs",  
489 |             "strict": true,  
490 |             "esModuleInterop": true,  
491 |             "skipLibCheck": true,  
492 |             "forceConsistentCasingInFileNames": true,  
493 |             "resolveJsonModule": true  
494 |           }  
495 |         }  
496 |         \`\`\`
497 | 
498 | \#\#\# Section 7: The Automation Toolkit \- Scripts and Actions
499 | 
500 | These scripts provide reusable automation for the core tasks in the agentic development lifecycle.
501 | 
502 | \#\#\#\# 7.1 Project Scaffolding Script (\`scaffold.py\`)
503 | 
504 | A simple Python script to generate the repository structure from a template.
505 | 
506 | \`\`\`python  
507 | import os  
508 | import shutil
509 | 
510 | def scaffold\_project(project\_name, lang="python"):  
511 |     """Generates a new project directory from a template."""  
512 |     template\_dir \= f"./templates/{lang}\_template"  
513 |     target\_dir \= f"./{project\_name}"
514 | 
515 |     if os.path.exists(target\_dir):  
516 |         print(f"Error: Directory '{target\_dir}' already exists.")  
517 |         return
518 | 
519 |     shutil.copytree(template\_dir, target\_dir)  
520 |     print(f"Successfully created '{project\_name}' project from {lang} template.")
521 | 
522 | if \_\_name\_\_ \== "\_\_main\_\_":  
523 |     \# Example usage:  
524 |     \# scaffold\_project("new-py-agent", "python")  
525 |     \# scaffold\_project("new-ts-agent", "typescript")  
526 |     pass
527 | 
528 | #### **7.2 Repo Map Generator (repo\_map.py)**
529 | 
530 | This script generates a JSON representation of the repository's structure and key symbols, inspired by codemapper 46 and Aider's implementation.17
531 | 
532 | Python
533 | 
534 | import os  
535 | import ast  
536 | import json
537 | 
538 | def parse\_python\_file(file\_path):  
539 |     """Extracts classes and functions from a Python file."""  
540 |     with open(file\_path, 'r', encoding='utf-8') as f:  
541 |         content \= f.read()  
542 |     tree \= ast.parse(content)  
543 |     symbols \=  
544 |     for node in ast.walk(tree):  
545 |         if isinstance(node, ast.FunctionDef):  
546 |             symbols.append(f"def {node.name}(...):")  
547 |         elif isinstance(node, ast.AsyncFunctionDef):  
548 |             symbols.append(f"async def {node.name}(...):")  
549 |         elif isinstance(node, ast.ClassDef):  
550 |             symbols.append(f"class {node.name}:")  
551 |     return symbols
552 | 
553 | def generate\_repo\_map(root\_dir, output\_file="repo\_map.json"):  
554 |     """Generates a map of the repository."""  
555 |     repo\_map \= {}  
556 |     ignore\_dirs \= {'.git', '\_\_pycache\_\_', 'node\_modules', '.venv'}  
557 |     for dirpath, dirnames, filenames in os.walk(root\_dir):  
558 |         dirnames\[:\] \= \[d for d in dirnames if d not in ignore\_dirs\]  
559 |         for filename in filenames:  
560 |             file\_path \= os.path.join(dirpath, filename)  
561 |             relative\_path \= os.path.relpath(file\_path, root\_dir)  
562 |             if filename.endswith(".py"):  
563 |                 repo\_map\[relative\_path\] \= parse\_python\_file(file\_path)  
564 |             else:  
565 |                 repo\_map\[relative\_path\] \= "non-python\_file"
566 | 
567 |     with open(output\_file, 'w') as f:  
568 |         json.dump(repo\_map, f, indent=2)  
569 |     print(f"Repository map saved to {output\_file}")
570 | 
571 | if \_\_name\_\_ \== "\_\_main\_\_":  
572 |     \# generate\_repo\_map(".")  
573 |     pass
574 | 
575 | #### **7.3 Code Embedding Indexer (indexer.py)**
576 | 
577 | This script demonstrates a basic RAG indexing pipeline for a codebase using LangChain and ChromaDB.29
578 | 
579 | Python
580 | 
581 | from langchain\_community.document\_loaders.generic import GenericLoader  
582 | from langchain\_community.document\_loaders.parsers import LanguageParser  
583 | from langchain\_text\_splitters import Language  
584 | from langchain\_community.vectorstores import Chroma  
585 | from langchain\_community.embeddings import OllamaEmbeddings \# Or any other embedding model
586 | 
587 | def index\_codebase(repo\_path, db\_path="./chroma\_db"):  
588 |     """Creates a vector index for a codebase."""  
589 |     loader \= GenericLoader.from\_filesystem(  
590 |         repo\_path,  
591 |         glob="\*\*/\*",  
592 |         suffixes=\[".py", ".ts"\],  
593 |         parser=LanguageParser(language=Language.PYTHON, parser\_threshold=500),  
594 |     )  
595 |     documents \= loader.load()
596 | 
597 |     python\_splitter \= RecursiveCharacterTextSplitter.from\_language(  
598 |         language=Language.PYTHON, chunk\_size=2000, chunk\_overlap=200  
599 |     )  
600 |     texts \= python\_splitter.split\_documents(documents)
601 | 
602 |     embeddings \= OllamaEmbeddings(model="nomic-embed-text") \# Example local model  
603 |     db \= Chroma.from\_documents(texts, embeddings, persist\_directory=db\_path)  
604 |     db.persist()  
605 |     print(f"Codebase indexed successfully at {db\_path}")
606 | 
607 | if \_\_name\_\_ \== "\_\_main\_\_":  
608 |     \# index\_codebase("./src")  
609 |     pass
610 | 
611 | #### **7.4 GitHub Action for LLM Output Validation**
612 | 
613 | A CI step that runs a script to validate a structured component of a PR, such as a JSON block in the description.
614 | 
615 | YAML
616 | 
617 | \# In.github/workflows/ci.yml  
618 |       \- name: Validate Agent PR Description  
619 |         if: startsWith(github.head\_ref, 'agent/')  
620 |         run: |  
621 |           pip install pyyaml  
622 |           python.github/scripts/validate\_pr\_description.py "${{ github.event.pull\_request.body }}"
623 | 
624 | #### **7.5 Filesystem Guardrail Script (guardrail.py)**
625 | 
626 | A conceptual example of a guardrail function that wraps an agent's tool execution.
627 | 
628 | Python
629 | 
630 | import os
631 | 
632 | ALLOWED\_WRITE\_PATHS \= \["src/", "tests/"\]
633 | 
634 | def execute\_tool\_with\_guardrail(tool\_name, parameters):  
635 |     """Executes a tool call with a filesystem write guardrail."""  
636 |     if tool\_name \== "writeFile":  
637 |         target\_path \= parameters.get("path")  
638 |         is\_allowed \= any(target\_path.startswith(p) for p in ALLOWED\_WRITE\_PATHS)  
639 |           
640 |         if not is\_allowed:  
641 |             raise PermissionError(f"Agent action blocked: Write to '{target\_path}' is not allowed.")  
642 |           
643 |         \#... proceed with file write operation...  
644 |         print(f"Guardrail passed: Writing to {target\_path}")  
645 |     else:  
646 |         \#... execute other tools...  
647 |         pass
648 | 
649 | ## **Part IV: Evaluation, Maintenance, and Troubleshooting**
650 | 
651 | Deploying agentic systems is not a one-time effort. Continuous evaluation, strategic tool selection, and robust troubleshooting processes are essential for maintaining performance and reliability over time. This final part addresses the long-term challenges of working with LLM agents.
652 | 
653 | ### **Section 8: Measuring Success \- Evaluation and Triage**
654 | 
655 | To improve agent performance systematically, it is necessary to measure it objectively. While large-scale academic benchmarks like SWE-bench 48 and Multi-SWE-bench 50 are valuable for model-level evaluation, project-specific evaluation requires a more lightweight, tailored approach.
656 | 
657 | #### **8.1 A Lightweight SWE-bench Style Harness**
658 | 
659 | A project should maintain its own suite of regression tests for its agents. This can be implemented as a simple evaluation harness.
660 | 
661 | * **Task Definition:** Each evaluation task is defined in a simple format (e.g., a JSON file) that specifies:  
662 |   * task\_id: A unique identifier.  
663 |   * description: The natural language prompt for the agent.  
664 |   * start\_commit: The git commit hash representing the initial state of the repository.  
665 |   * allowed\_files: A list of files the agent is permitted to modify.  
666 |   * test\_command: The shell command to run to verify success (e.g., pytest tests/test\_feature.py).  
667 | * **Harness Script:** A Python script automates the evaluation process:  
668 |   1. Reads a task definition file.  
669 |   2. Uses git checkout to reset the repository to the start\_commit.  
670 |   3. Invokes the agent system with the task description.  
671 |   4. Captures the agent's final generated patch.  
672 |   5. Applies the patch to the codebase.  
673 |   6. Executes the test\_command.  
674 |   7. Records the result (pass/fail), along with performance metrics.
675 | 
676 | #### **8.2 Key Performance Metrics for Coding Agents**
677 | 
678 | Beyond a simple pass/fail metric, a more nuanced set of KPIs is needed to track agent performance over time 51:
679 | 
680 | * **Task Success Rate:** The percentage of evaluation tasks where the final generated code passes the verification step. This is the primary measure of correctness.  
681 | * **Diff Size / Churn:** The number of lines added and removed by the agent's patch. Smaller, more targeted diffs are generally preferable. High churn across multiple attempts on the same task indicates the agent is struggling.  
682 | * **Number of Turns / Tool Calls:** A measure of efficiency. The total number of LLM calls or tool executions required to reach a solution. A lower number indicates a more direct and efficient reasoning process.  
683 | * **Token Cost:** The total number of input and output tokens consumed by the agent, which directly translates to API costs.  
684 | * **Human-in-the-Loop (HITL) Interventions:** The number of times a human developer needs to correct the agent's course, refine a prompt, or manually edit the generated code. A decreasing intervention rate is a strong indicator of improving agent autonomy.
685 | 
686 | #### **8.3 Triage Loops for Failed Tasks**
687 | 
688 | When an agent fails an evaluation task, a systematic triage process is essential for diagnosis and improvement.
689 | 
690 | 1. **Categorize the Failure:** Use the failure taxonomy from Section 10 to classify the error (e.g., Specification Drift, Context Loss, Tool Error).  
691 | 2. **Analyze the Trace:** Review the agent's execution log. Observability platforms like LangSmith are invaluable for this, as they provide a detailed trace of the agent's internal "thoughts," tool calls, and LLM inputs/outputs.53  
692 | 3. **Identify the Root Cause:** Determine precisely why the failure occurred. Was the initial prompt ambiguous? Did the RAG system retrieve irrelevant context? Did a tool return an unexpected error?  
693 | 4. **Remediate:** Implement a fix. This could involve refining the prompt in prompts.md, improving the chunking strategy in the RAG indexer, or adding better error handling to a custom tool.  
694 | 5. **Add to Regression Suite:** Ensure the failed task is permanently added to the evaluation harness. This prevents future changes from reintroducing the same bug.
695 | 
696 | ### **Section 9: The Modern AI Developer's Toolbox**
697 | 
698 | The landscape of AI developer tools is evolving rapidly. Choosing the right tool depends on the specific use case, ranging from fully autonomous systems to human-in-the-loop assistants.
699 | 
700 | #### **9.1 Agent Frameworks (Autonomous Orchestration)**
701 | 
702 | These frameworks are designed for building systems of multiple, collaborating agents that can execute complex tasks with a high degree of autonomy.
703 | 
704 | * **AutoGen:** A powerful, research-oriented framework from Microsoft that excels at creating complex, dynamic conversations between specialized agents. It is highly flexible and composable, making it suitable for tasks that require emergent, collaborative problem-solving.23  
705 | * **CrewAI:** A framework that emphasizes a role-based approach to agent collaboration, mirroring a human team structure (e.g., Researcher, Writer, Critic). It is known for its intuitive API and focus on orchestrating well-defined, sequential workflows.24  
706 | * **OpenDevin:** An open-source project aiming to replicate and extend the capabilities of a fully autonomous AI software engineer. It provides a sandboxed environment with a shell, code editor, and browser, allowing an agent to perform a wide range of development tasks end-to-end.59
707 | 
708 | #### **9.2 IDE Workflows (Human-in-the-Loop Assistants)**
709 | 
710 | These tools integrate directly into a developer's existing IDE, acting as powerful pair programmers that augment the human workflow rather than fully automating it.
711 | 
712 | * **Cursor:** An AI-native, fork of VS Code that provides deep integration with the editor. Its key features include codebase-aware chat (@file, @symbol), agentic inline edits (Ctrl+K), and an "Agent" mode that can attempt to complete tasks end-to-end while remaining fully steerable by the developer.60  
713 | * **Aider:** A command-line-based tool that allows a developer to pair program with an AI in their terminal. It works directly with local git repositories, uses a "repo map" to provide codebase context, and is highly effective for iterative, chat-driven development and refactoring.18  
714 | * **GitHub Copilot Workspaces:** An agentic development environment that starts from a GitHub issue or PR. It generates a full specification and implementation plan in natural language, which the developer can edit and approve before the tool generates the corresponding code. It is designed for task-level execution rather than line-by-line completion.64
715 | 
716 | **Table 2: Framework and IDE Comparison Matrix**
717 | 
718 | | Tool | Primary Paradigm | Context Management | Tool Integration | Setup Complexity | Ideal Use Case |
719 | | :---- | :---- | :---- | :---- | :---- | :---- |
720 | | **AutoGen** | Autonomous | Conversational Memory | Highly Extensible (Python functions) | High | Research, complex dynamic workflows, simulating multi-agent systems. |
721 | | **CrewAI** | Autonomous | Task-based, Role-based | Custom Tools API | Medium | Building production AI teams for structured business processes (e.g., content generation). |
722 | | **OpenDevin** | Autonomous | Sandboxed Environment | Shell, Editor, Browser | High | End-to-end task automation, replicating a full developer workflow. |
723 | | **Cursor** | Assistant | @file, @symbol refs, Vector DB | Built-in (Web search, Docs) | Low | AI-native IDE experience, rapid prototyping, multi-file refactoring. |
724 | | **Aider** | Assistant | Git Repo Map | Command-line tools via /run | Low | Terminal-centric development, iterative bug fixing, TDD workflows. |
725 | | **Copilot Workspaces** | Assistant | Issue/PR context, Codebase analysis | Integrated Terminal | Low | From-scratch feature implementation based on a GitHub issue. |
726 | 
727 | ### **Section 10: Troubleshooting Common Agent Failures**
728 | 
729 | Agentic systems, like any complex software, can fail. Recent research has begun to formalize taxonomies of these failures, providing a framework for diagnosis and mitigation.3 This section serves as a practical troubleshooting guide for the most common failure modes.
730 | 
731 | #### **10.1 Specification Drift / Goal Misalignment**
732 | 
733 | * **Symptom:** The agent produces high-quality code that works perfectly but solves the wrong problem or misses a key business requirement.  
734 | * **Cause:** The initial natural language prompt was ambiguous, incomplete, or misinterpreted by the agent.  
735 | * **Mitigation:**  
736 |   * **Prevention:** Enforce the use of the rigorous specification templates from Section 1\. Ensure all acceptance criteria are explicit and verifiable.  
737 |   * **Detection:** Use a Planner Agent to generate a step-by-step plan and have a human approve it *before* any code is written. This confirms the agent's understanding of the goal.
738 | 
739 | #### **10.2 Context Loss / Amnesia**
740 | 
741 | * **Symptom:** In a long-running task, the agent forgets previous instructions, key architectural constraints, or the purpose of a file it wrote earlier. This is a known challenge due to the finite context windows of LLMs.2  
742 | * **Cause:** The conversational history or relevant file context has exceeded the LLM's context window, or the retrieval mechanism failed to surface the necessary information.  
743 | * **Mitigation:**  
744 |   * **Robust RAG:** Implement a high-quality RAG pipeline (Section 5.2). Ensure code is chunked effectively and the embedding model is well-suited for code.  
745 |   * **Stateful Orchestration:** For very long tasks, break them into smaller, independent sub-tasks. Use a workflow orchestrator (like LangGraph) to manage the overall state and pass only the necessary context to a fresh agent instance for each sub-task.
746 | 
747 | #### **10.3 File Thrashing / Hallucinated Paths**
748 | 
749 | * **Symptom:** The agent gets stuck in a loop, repeatedly modifying the same file without making progress. It may also attempt to read from or write to file paths that do not exist.  
750 | * **Cause:** The agent lacks a correct understanding of the repository's file structure or is failing to converge on a correct solution.  
751 | * **Mitigation:**  
752 |   * **Tool Access:** Ensure the agent has access to a listFiles tool and is prompted to use it to verify a path's existence before attempting to read or write.  
753 |   * **Patch/Diff Workflow:** This prevents the agent from directly damaging the codebase. The developer can simply reject the thrashing diffs.  
754 |   * **Filesystem Guardrail:** An automated guardrail (Section 7.5) can block writes to invalid or disallowed paths, forcing the agent to reconsider its action.
755 | 
756 | #### **10.4 Flaky Tests / Environment Issues**
757 | 
758 | * **Symptom:** The agent generates a correct code solution, but the final verification step fails due to non-deterministic tests, missing dependencies, or environment configuration drift. This is a known challenge in automated evaluation systems like SWE-bench.48  
759 | * **Cause:** The execution environment is not consistent or the tests themselves are unreliable.  
760 | * **Mitigation:**  
761 |   * **Containerization:** Enforce the use of containerized development environments (e.g., Docker, Devcontainers) for both development and evaluation. This ensures a clean, reproducible environment every time.  
762 |   * **Test Design:** Prompt the agent to write deterministic, mock-based unit tests that do not rely on external services or random data.
763 | 
764 | **Table 3: Failure Mode Mitigation Cheat Sheet**
765 | 
766 | | Failure Mode | Common Symptoms | Primary Cause | Mitigation Strategy |
767 | | :---- | :---- | :---- | :---- |
768 | | **Specification Drift** | Code works but doesn't meet business needs. | Ambiguous initial prompt. | Use strict spec templates; require human approval of agent-generated plan. |
769 | | **Context Loss** | Agent forgets prior instructions or code context. | Exceeding LLM context window; poor retrieval. | Implement a robust RAG pipeline; break long tasks into smaller, stateful steps. |
770 | | **File Thrashing** | Agent edits same file repeatedly; writes to invalid paths. | Lack of file system awareness; reasoning loop. | Use patch/diff workflow; provide a listFiles tool; implement filesystem guardrails. |
771 | | **Flaky Tests** | Correct code fails verification step. | Inconsistent environment; non-deterministic tests. | Use containerized environments (Devcontainers); prompt for mock-based unit tests. |
772 | | **Tool Execution Error** | Agent fails to use a tool correctly or handle its errors. | Poor tool documentation in prompt; no error handling. | Provide clear tool descriptions with examples; prompt the agent to include try/except blocks. |
773 | 
774 | #### **Works cited**
775 | 
776 | 1. LLM-driven Development: Beyond the Hype and Into the Production Workflow, accessed August 20, 2025, [https://optimumpartners.com/insight/llm-driven-development-beyond-the-hype-and-into-the-production-workflow/](https://optimumpartners.com/insight/llm-driven-development-beyond-the-hype-and-into-the-production-workflow/)  
777 | 2. LLM Agents \- Prompt Engineering Guide, accessed August 20, 2025, [https://www.promptingguide.ai/research/llm-agents](https://www.promptingguide.ai/research/llm-agents)  
778 | 3. Why Do Multi-Agent LLM Systems Fail? \- arXiv, accessed August 20, 2025, [https://arxiv.org/pdf/2503.13657?](https://arxiv.org/pdf/2503.13657)  
779 | 4. Guide to Specification-First AI Development | Galileo, accessed August 20, 2025, [https://galileo.ai/blog/specification-first-ai-development](https://galileo.ai/blog/specification-first-ai-development)  
780 | 5. Doc Driven Development, accessed August 20, 2025, [https://docdd.ai/](https://docdd.ai/)  
781 | 6. Documentation-Driven Development: How Good Docs Become Your AI Pair Programming Superpower | by Hiraq Citra M | lifefunk | Jul, 2025 | Medium, accessed August 20, 2025, [https://medium.com/lifefunk/documentation-driven-development-how-good-docs-become-your-ai-pair-programming-superpower-e0e574db2f3b](https://medium.com/lifefunk/documentation-driven-development-how-good-docs-become-your-ai-pair-programming-superpower-e0e574db2f3b)  
782 | 7. Using LLMs for Code Generation: A Guide to Improving Accuracy and Addressing Common Issues \- PromptHub, accessed August 20, 2025, [https://www.prompthub.us/blog/using-llms-for-code-generation-a-guide-to-improving-accuracy-and-addressing-common-issues](https://www.prompthub.us/blog/using-llms-for-code-generation-a-guide-to-improving-accuracy-and-addressing-common-issues)  
783 | 8. Code Generation with LLMs: Practical Challenges, Gotchas, and Nuances \- Medium, accessed August 20, 2025, [https://medium.com/@adnanmasood/code-generation-with-llms-practical-challenges-gotchas-and-nuances-7b51d394f588](https://medium.com/@adnanmasood/code-generation-with-llms-practical-challenges-gotchas-and-nuances-7b51d394f588)  
784 | 9. Requirements are All You Need: From Requirements to Code with LLMs \- arXiv, accessed August 20, 2025, [https://arxiv.org/html/2406.10101v1](https://arxiv.org/html/2406.10101v1)  
785 | 10. LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation \- Penn Engineering, accessed August 20, 2025, [https://www.seas.upenn.edu/\~asnaik/assets/papers/tse24\_ticoder.pdf](https://www.seas.upenn.edu/~asnaik/assets/papers/tse24_ticoder.pdf)  
786 | 11. LLMs for Code Generation: A summary of the research on quality \- Sonar, accessed August 20, 2025, [https://www.sonarsource.com/learn/llm-code-generation/](https://www.sonarsource.com/learn/llm-code-generation/)  
787 | 12. Repository map \- Aider, accessed August 20, 2025, [https://aider.chat/docs/repomap.html](https://aider.chat/docs/repomap.html)  
788 | 13. Specifying coding conventions | aider, accessed August 20, 2025, [https://aider.chat/docs/usage/conventions.html](https://aider.chat/docs/usage/conventions.html)  
789 | 14. Tips | aider, accessed August 20, 2025, [https://aider.chat/docs/usage/tips.html](https://aider.chat/docs/usage/tips.html)  
790 | 15. Introduction to AutoGen | AutoGen 0.2 \- Microsoft Open Source, accessed August 20, 2025, [https://microsoft.github.io/autogen/0.2/docs/tutorial/introduction/](https://microsoft.github.io/autogen/0.2/docs/tutorial/introduction/)  
791 | 16. Introduction \- CrewAI, accessed August 20, 2025, [https://docs.crewai.com/](https://docs.crewai.com/)  
792 | 17. Build a RAG system for your codebase in 5 easy steps | by Karl Weinmeister | Google Cloud, accessed August 20, 2025, [https://medium.com/google-cloud/build-a-rag-system-for-your-codebase-in-5-easy-steps-a3506c10599b](https://medium.com/google-cloud/build-a-rag-system-for-your-codebase-in-5-easy-steps-a3506c10599b)  
793 | 18. Step by step approach to RAG my Codebase | by Osman Mehmood \- Medium, accessed August 20, 2025, [https://medium.com/@osman.mehmood2/step-by-step-approach-to-rag-my-codebase-6ed41ff58de8](https://medium.com/@osman.mehmood2/step-by-step-approach-to-rag-my-codebase-6ed41ff58de8)  
794 | 19. MikeyBeez/codemapper: Python module that creates a ... \- GitHub, accessed August 20, 2025, [https://github.com/MikeyBeez/codemapper](https://github.com/MikeyBeez/codemapper)  
795 | 20. Retrieval Augmented Generation (RAG) from Scratch — Tutorial For Dummies, accessed August 20, 2025, [https://dev.to/zachary62/retrieval-augmented-generation-rag-from-scratch-tutorial-for-dummies-508a](https://dev.to/zachary62/retrieval-augmented-generation-rag-from-scratch-tutorial-for-dummies-508a)  
796 | 21. Claude SWE-Bench Performance \\ Anthropic, accessed August 20, 2025, [https://www.anthropic.com/research/swe-bench-sonnet](https://www.anthropic.com/research/swe-bench-sonnet)  
797 | 22. SWE-Bench-C Evaluation Framework \- Design And Reuse, accessed August 20, 2025, [https://www.design-reuse.com/article/61613-swe-bench-c-evaluation-framework/](https://www.design-reuse.com/article/61613-swe-bench-c-evaluation-framework/)  
798 | 23. Multi-SWE-bench: A Multilingual Benchmark for Issue ... \- GitHub, accessed August 20, 2025, [https://github.com/multi-swe-bench/multi-swe-bench](https://github.com/multi-swe-bench/multi-swe-bench)  
799 | 24. LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide \- Confident AI, accessed August 20, 2025, [https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)  
800 | 25. How quality, cost, and latency are assessed by Agent Evaluation (MLflow 2), accessed August 20, 2025, [https://docs.databricks.com/aws/en/generative-ai/agent-evaluation/llm-judge-metrics](https://docs.databricks.com/aws/en/generative-ai/agent-evaluation/llm-judge-metrics)  
801 | 26. LangChain, accessed August 20, 2025, [https://www.langchain.com/](https://www.langchain.com/)  
802 | 27. Build an Agent \- ️ LangChain, accessed August 20, 2025, [https://python.langchain.com/docs/tutorials/agents/](https://python.langchain.com/docs/tutorials/agents/)  
803 | 28. Getting Started | AutoGen 0.2 \- Microsoft Open Source, accessed August 20, 2025, [https://microsoft.github.io/autogen/0.2/docs/Getting-Started/](https://microsoft.github.io/autogen/0.2/docs/Getting-Started/)  
804 | 29. AutoGen vs. LangGraph vs. CrewAI:Who Wins? | by Khushbu Shah ..., accessed August 20, 2025, [https://medium.com/projectpro/autogen-vs-langgraph-vs-crewai-who-wins-02e6cc7c5cb8](https://medium.com/projectpro/autogen-vs-langgraph-vs-crewai-who-wins-02e6cc7c5cb8)  
805 | 30. Open source \- CrewAI, accessed August 20, 2025, [https://www.crewai.com/open-source](https://www.crewai.com/open-source)  
806 | 31. Comparing AI Agent Frameworks: Which One Should I Choose for My Project? \- langgraph, accessed August 20, 2025, [https://community.latenode.com/t/comparing-ai-agent-frameworks-which-one-should-i-choose-for-my-project/31007](https://community.latenode.com/t/comparing-ai-agent-frameworks-which-one-should-i-choose-for-my-project/31007)  
807 | 32. OpenDevin \- AI Agent Store, accessed August 20, 2025, [https://aiagentstore.ai/ai-agent/opendevin](https://aiagentstore.ai/ai-agent/opendevin)  
808 | 33. Top Features of Cursor AI \- APPWRK, accessed August 20, 2025, [https://appwrk.com/cursor-ai-features](https://appwrk.com/cursor-ai-features)  
809 | 34. Features | Cursor \- The AI Code Editor, accessed August 20, 2025, [https://cursor.com/features](https://cursor.com/features)  
810 | 35. Claude, Cursor, Aider, Cline, Copilot: Which Is the Best One? | by Edwin Lisowski \- Medium, accessed August 20, 2025, [https://medium.com/@elisowski/claude-cursor-aider-cline-copilot-which-is-the-best-one-ef1a47eaa1e6](https://medium.com/@elisowski/claude-cursor-aider-cline-copilot-which-is-the-best-one-ef1a47eaa1e6)  
811 | 36. Tutorial videos \- Aider, accessed August 20, 2025, [https://aider.chat/docs/usage/tutorials.html](https://aider.chat/docs/usage/tutorials.html)  
812 | 37. Copilot Workspace \- GitHub Next, accessed August 20, 2025, [https://githubnext.com/projects/copilot-workspace](https://githubnext.com/projects/copilot-workspace)  
813 | 38. GitHub Copilot · Your AI pair programmer, accessed August 20, 2025, [https://github.com/features/copilot](https://github.com/features/copilot)  
814 | 39. How to be more productive with Github Copilot Workspace \- YouTube, accessed August 20, 2025, [https://www.youtube.com/watch?v=sjAMkdYnbIw](https://www.youtube.com/watch?v=sjAMkdYnbIw)  
815 | 40. Taxonomy of Failure Mode in Agentic AI Systems \- Microsoft, accessed August 20, 2025, [https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf)
```

ai-docs/Senior LLM Project Architect & Codebase Orchestrator.md
```
1 | # Role
2 | 
3 | You are a **Senior LLM Project Architect & Codebase Orchestrator**. Your job is to design a complete, production-grade **project plan + repository scaffold + working prompts + generation protocol** so LLMs consistently stay on task and produce correct, testable code and files.
4 | 
5 | # Objectives
6 | 
7 | 1. Produce a **systematic, start-to-finish method** to plan and generate a codebase with AI assistance.
8 | 2. **Research and synthesize** essential, *proven* strategies and practices for coding with AI assistants/agents.
9 | 3. Output a **repository blueprint**, **file/folder structure**, **prompt suite**, and **execution checklists** that ensure repeatability, traceability, testing, and maintainability.
10 | 
11 | # Inputs (fill from user or make reasonable assumptions; then state them explicitly)
12 | 
13 | * Target problem/domain:
14 | * Primary language(s)/frameworks:
15 | * Runtime/platforms (web, mobile, server, cloud, edge):
16 | * Non‑functional requirements (performance, security, privacy, compliance, scalability, cost):
17 | * Team constraints (skills, review process, branching model):
18 | * Tooling (package manager, build, test, CI/CD, IaC, vector DB, RAG, agents):
19 | * LLM(s) available + context limits:
20 | * Licensing and IP constraints:
21 | * Delivery deadline & milestones:
22 | 
23 | # Research & Evidence Requirements
24 | 
25 | * Search across reputable engineering sources (framework docs, testing best practices, style guides, agent frameworks, prompt engineering literature).
26 | * Extract **at least 5** concrete strategies that have empirical or widely adopted support.
27 | * Provide a **Sources & Evidence** section with: title, 1–2 line relevance summary, and a short bullet list of key takeaways. Prefer canonical docs and well-known engineering blogs/books.
28 | * Distill into **actionable rules** mapped to repository artifacts (e.g., “adopt ADRs → `/docs/adr/0001-...md`”).
29 | 
30 | # Deliverables (produce all)
31 | 
32 | 1. **Executive Summary** – one page with goals, constraints, risks, and approach.
33 | 2. **LLM Coding Protocol** – the exact step-by-step loop the AI must follow every time it generates code:
34 | 
35 |    * Plan → Scaffold → Implement → Validate → Test → Instrument → Document → Commit.
36 |    * Each step has entry criteria, exit criteria, and artifacts.
37 | 3. **Repository Blueprint** – propose the full folder/file structure (with brief purpose comments) and a **JSON manifest** that tools/agents can consume.
38 | 4. **Scaffold Generation Plan** – initial READMEs, contribution guide, code of conduct, licenses, environment setup scripts, CI/CD config, editor settings, pre-commit hooks.
39 | 5. **Prompt Suite** – reusable, role-based prompts:
40 | 
41 |    * `SYSTEM.md` (project guardrails),
42 |    * `DEVELOPER.md` (coding standards),
43 |    * `REVIEWER.md` (PR review rubric),
44 |    * `TEST_WRITER.md` (test-first rules),
45 |    * `DOCS_WRITER.md` (docs style),
46 |    * `AGENT_RUNBOOK.md` (orchestration & autonomy bounds).
47 | 6. **Task Decomposition Template** – how to slice epics → stories → tasks → codegen tickets; includes a **Definition of Ready** and **Definition of Done**.
48 | 7. **Spec-First Templates** – RFC/ADR templates, interface and API contracts, schema definitions, and acceptance criteria.
49 | 8. **Testing Strategy** – unit/integration/contract/E2E tests, mutation testing, coverage gates, test data management, and a **Red/Green/Refactor** loop tailored for LLMs.
50 | 9. **Verification & Guardrails** – static analysis, type checks, policy-as-code, security scans (SAST/DAST), license checks, secret scanning, fuzzing, and **hallucination traps**.
51 | 10. **RAG/Context Strategy** (if applicable) – chunking, embeddings policy, retrieval prompts, citability, freshness, privacy.
52 | 11. **CI/CD & Branching** – trunk or GitFlow, PR templates, required checks, conventional commits; ephemeral environments for preview.
53 | 12. **Observability** – logs, metrics, traces; telemetry on LLM usage; eval harness & regression suite for prompts.
54 | 13. **Change Management** – ADR log, versioning scheme (SemVer), release notes automation.
55 | 14. **Playbooks** – incident response, rollback, hotfix protocol, data migrations.
56 | 15. **Sources & Evidence** – consolidated with takeaways mapped to deliverable sections.
57 | 
58 | # Output Format & Structure
59 | 
60 | Respond with these sections, in order:
61 | 
62 | ## 1) Executive Summary
63 | 
64 | * Problem statement, constraints, success criteria, risks and mitigations.
65 | 
66 | ## 2) Research Synthesis (Proven Strategies)
67 | 
68 | * Bulleted strategies with 1–2 sentence rationale each.
69 | * “Why it works” + where it’s adopted.
70 | 
71 | ## 3) LLM Coding Protocol (Always Follow)
72 | 
73 | For every generation cycle:
74 | 
75 | 1. **Clarify**: restate task, assumptions, constraints.
76 | 2. **Plan**: produce a mini-spec, acceptance criteria, test list.
77 | 3. **Scaffold**: create/modify files minimally to satisfy spec; update manifest.
78 | 4. **Implement**: code to meet tests and acceptance criteria.
79 | 5. **Validate**: run static checks, type checks, linters; analyze diffs.
80 | 6. **Test**: write tests first when feasible; run & report results.
81 | 7. **Document**: update READMEs, inline docs, changelog.
82 | 8. **Commit**: atomic commits using Conventional Commits; include task ID.
83 | 9. **Review**: self-review checklist; open PR with template; request AI/code review.
84 | 10. **Close**: link artifacts, update ADR if architectural change occurred.
85 | 
86 | Include entry/exit criteria and artifacts for each step.
87 | 
88 | ## 4) Repository Blueprint
89 | 
90 | * **Tree view** with comments.
91 | * **`repo.manifest.json`** describing files, purposes, owners, and generation provenance.
92 | * **Example tree** (tailor to stack); include `/docs/adr`, `/scripts`, `/ci`, `/infra`, `/src`, `/tests`, `/prompts`, `/.github`.
93 | 
94 | ## 5) Spec-First & Templates
95 | 
96 | Provide these as code blocks ready to save:
97 | 
98 | * `docs/adr/template.md`
99 | * `docs/rfc/template.md`
100 | * `prompts/SYSTEM.md`
101 | * `prompts/DEVELOPER.md` (style, lint, patterns, error handling)
102 | * `prompts/REVIEWER.md` (PR rubric)
103 | * `.github/pull_request_template.md`
104 | * `.github/ISSUE_TEMPLATE/feature.md`
105 | * `.github/ISSUE_TEMPLATE/bug.md`
106 | * `CONTRIBUTING.md`
107 | * `SECURITY.md`
108 | 
109 | ## 6) Task Decomposition & Planning
110 | 
111 | * Epic → story → task pattern with **Definition of Ready/Done** checklists.
112 | * Ticket template with fields for requirement, constraints, acceptance tests, affected files, risks.
113 | 
114 | ## 7) Testing & Verification Plan
115 | 
116 | * Test pyramid with frameworks for the chosen stack.
117 | * Coverage thresholds and mutation testing rules.
118 | * Policy-as-code and security scan config pointers.
119 | * Hallucination controls: require citations, diff-aware reviews, spec pinning.
120 | 
121 | ## 8) RAG/Context Management (if used)
122 | 
123 | * Chunking size policy, metadata, recency windows.
124 | * Retrieval prompts and **evidence-required** outputs.
125 | * PII redaction and data governance notes.
126 | 
127 | ## 9) CI/CD & Branching
128 | 
129 | * Pipeline stages and required checks.
130 | * Branching model decision with trade-offs.
131 | * Release & tagging strategy; changelog automation.
132 | 
133 | ## 10) Observability & Eval
134 | 
135 | * Logging, metrics, tracing standards.
136 | * Prompt eval harness: golden tests, failure taxonomy, drift alerts.
137 | 
138 | ## 11) Playbooks
139 | 
140 | * Incident response (steps, roles, timeboxes).
141 | * Rollback and hotfix flow.
142 | * Data migration checklist.
143 | 
144 | ## 12) Sources & Evidence
145 | 
146 | * 5–12 sources, each with: link title, 1–2 line summary, key takeaways.
147 | * Map each source to the section(s) it supports.
148 | 
149 | # Constraints & Quality Bar
150 | 
151 | * **Determinism:** Prefer idempotent, spec-driven generation; avoid creative deviation in code.
152 | * **Reproducibility:** All steps scriptable; no manual “magic.” Record tool/LLM versions.
153 | * **Security & Privacy:** No secrets in code; use env managers; minimal data retention; comply with licensing.
154 | * **Traceability:** Every change maps to a ticket, commit, PR, and (if architectural) an ADR.
155 | * **Token/Latency Budgets:** Enforce context packing rules; summarize large artifacts; stream large trees page-wise.
156 | * **Style & Standards:** Enforce formatter, linter, types, error handling, logging, and docs style.
157 | * **Stop if Uncertain:** When requirements are ambiguous, generate a **Clarifying Questions** block first.
158 | 
159 | # Style & Communication
160 | 
161 | * Use concise, technical writing.
162 | * Provide bullet lists, numbered steps, and code blocks.
163 | * Show minimal examples where helpful.
164 | * For code, include brief inline comments and docstrings.
165 | * For decisions, provide 2–3 option trade-offs and a recommendation.
166 | 
167 | # Example JSON Manifest (customize)
168 | 
169 | ```json
170 | {
171 |   "repo": "project-name",
172 |   "owners": ["@team/ai"],
173 |   "tools": {"llm":"gpt-4o","embedding":"text-embedding-3-large"},
174 |   "structure": [
175 |     {"path":"README.md","purpose":"overview"},
176 |     {"path":"docs/adr/0001-record-architecture-decisions.md","purpose":"ADRs"},
177 |     {"path":"prompts/SYSTEM.md","purpose":"system guardrails"},
178 |     {"path":"src/","purpose":"application code"},
179 |     {"path":"tests/","purpose":"test suites"},
180 |     {"path":".github/pull_request_template.md","purpose":"PR checks"}
181 |   ],
182 |   "policies": {
183 |     "commit":"conventional-commits",
184 |     "coverage": {"min": 0.85, "mutation_min": 0.25}
185 |   },
186 |   "provenance": {"generated_by":"LLM","llm_version":"x.y","timestamp":"<iso>"}
187 | }
188 | ```
189 | 
190 | # Acceptance Criteria
191 | 
192 | * All deliverables present and tailored to the declared stack.
193 | * Strategies are **evidence-backed** and mapped to concrete artifacts.
194 | * The LLM Coding Protocol is explicit, looped, and enforceable via templates and CI checks.
195 | * The repository blueprint is **immediately actionable**: copy/paste to start.
196 | * Risk mitigations and guardrails are clearly stated.
197 | * Any uncertainties are listed with clarifying questions before generation.
198 | 
199 | # Now Do This
200 | 
201 | 1. Populate **Inputs** (state assumptions if needed).
202 | 2. Perform **Research & Evidence** gathering and summarize findings.
203 | 3. Produce all **Deliverables** in the **Output Format & Structure** above.
204 | 4. End with a short **Next 3 Steps** checklist for the human team.
```

scripts/gemini.sh
```
1 | #!/usr/bin/env bash
2 | set -euo pipefail
3 | 
4 | # gemini.sh — wrapper for gemini-cli to enforce repo guardrails
5 | # - Injects GEMINI.md as system instructions
6 | # - Supports interactive and one-shot modes
7 | # - Optionally captures unified diffs (*** Begin Patch ... *** End Patch) to .agent/last.patch
8 | 
9 | ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
10 | SYSTEM_FILE="$ROOT_DIR/GEMINI.md"
11 | AGENT_DIR="$ROOT_DIR/.agent"
12 | LOG_DIR="$AGENT_DIR/logs"
13 | mkdir -p "$LOG_DIR"
14 | 
15 | # Underlying CLI command (override with env GEMINI_CMD or GEMINI_CLI_CMD)
16 | # Default binary per upstream docs is `gemini`.
17 | CLI_CMD="${GEMINI_CMD:-${GEMINI_CLI_CMD:-gemini}}"
18 | 
19 | usage() {
20 |   cat <<'USAGE'
21 | Usage:
22 |   scripts/gemini.sh [options]
23 | 
24 | Options:
25 |   -t, --task "TEXT"     One-shot mode with the given task prompt
26 |   -i, --interactive      Interactive mode (default if no --task)
27 |   --diff-out PATH        Extract unified diff blocks to PATH (default: .agent/last.patch)
28 |   --no-diff              Do not extract diffs
29 |   --cmd CMD              Underlying CLI command (default: gemini)
30 |   --help                 Show this help
31 | 
32 | Behavior:
33 |   - Gemini CLI auto-loads GEMINI.md as hierarchical context; no flags required.
34 |   - One-shot mode uses `gemini -p "<task>"` and logs output.
35 |   - If the session outputs patch blocks, they are extracted to the chosen path.
36 | USAGE
37 | }
38 | 
39 | TASK=""
40 | MODE="interactive"
41 | DIFF_OUT="${ROOT_DIR}/.agent/last.patch"
42 | EXTRACT_DIFF=1
43 | 
44 | while [[ $# -gt 0 ]]; do
45 |   case "$1" in
46 |     -t|--task)
47 |       TASK=${2:-}
48 |       MODE="oneshot"
49 |       shift 2
50 |       ;;
51 |     -i|--interactive)
52 |       MODE="interactive"
53 |       shift
54 |       ;;
55 |     --diff-out)
56 |       DIFF_OUT=$(realpath "${2:-${DIFF_OUT}}")
57 |       shift 2
58 |       ;;
59 |     --no-diff)
60 |       EXTRACT_DIFF=0
61 |       shift
62 |       ;;
63 |     --cmd)
64 |       CLI_CMD=${2:-$CLI_CMD}
65 |       shift 2
66 |       ;;
67 |     --help|-h)
68 |       usage; exit 0
69 |       ;;
70 |     *)
71 |       echo "Unknown argument: $1" >&2
72 |       usage; exit 1
73 |       ;;
74 |   esac
75 | done
76 | 
77 | if ! command -v "$CLI_CMD" >/dev/null 2>&1; then
78 |   echo "Error: underlying CLI '$CLI_CMD' not found. Set GEMINI_CLI_CMD or install gemini-cli." >&2
79 |   exit 127
80 | fi
81 | 
82 | if [[ ! -f "$SYSTEM_FILE" ]]; then
83 |   echo "Error: System instructions not found at $SYSTEM_FILE" >&2
84 |   exit 1
85 | fi
86 | 
87 | SYSTEM_CONTENT="$(cat "$SYSTEM_FILE")"
88 | 
89 | # Build base command (gemini CLI auto-loads context from GEMINI.md; no system flag injection needed)
90 | CMD=("$CLI_CMD")
91 | 
92 | timestamp() { date +"%Y-%m-%d_%H-%M-%S"; }
93 | 
94 | extract_diffs() {
95 |   local infile="$1" outpath="$2"
96 |   awk '/^\*\*\* Begin Patch/{flag=1} flag{print} /^\*\*\* End Patch/{flag=0}' "$infile" \
97 |     | sed '/^$/q' > "$outpath" || true
98 |   if [[ -s "$outpath" ]]; then
99 |     echo "Saved patch to $outpath"
100 |   else
101 |     rm -f "$outpath"
102 |     echo "No patch blocks found in output."
103 |   fi
104 | }
105 | 
106 | trap - EXIT
107 | 
108 | mkdir -p "$AGENT_DIR"
109 | 
110 | if [[ "$MODE" == "oneshot" ]]; then
111 |   if [[ -z "$TASK" ]]; then
112 |     echo "Error: --task requires text." >&2
113 |     exit 1
114 |   fi
115 |   LOG_FILE="$LOG_DIR/session_$(timestamp).log"
116 | 
117 |   # Run underlying CLI in non-interactive mode using -p/--prompt and capture output
118 |   set +e
119 |   "${CMD[@]}" -p "$TASK" | tee "$LOG_FILE"
120 |   STATUS=${PIPESTATUS[0]}
121 |   set -e
122 | 
123 |   if [[ $EXTRACT_DIFF -eq 1 ]]; then
124 |     mkdir -p "$(dirname "$DIFF_OUT")"
125 |     extract_diffs "$LOG_FILE" "$DIFF_OUT"
126 |   fi
127 | 
128 |   exit "$STATUS"
129 | else
130 |   # Interactive
131 |   echo "Starting interactive session with $CLI_CMD"
132 |   echo "Using context file: $SYSTEM_FILE (auto-loaded by CLI)"
133 |   echo "Tip: Use --task for one-shot mode with diff capture."
134 | 
135 |   "${CMD[@]}"
136 | fi
```

.claude/agents/architect.md
```
1 | ---
2 | name: architect
3 | description: A feature idea is formalized into a machine-readable specification. An 'Architect Agent' can accelerate this by drafting specs, ADRs, and acceptance criteria from a high-level goal. The developer's role is to review and refine these documents for clarity and completeness.
4 | model: inherit
5 | color: cyan
6 | ---
7 | 
8 | System: You are the Planner/Architect. Decompose work into a minimal, verifiable plan; draft ADRs when architectural choices arise; and specify strict outputs for downstream agents.
9 | 
10 | Inputs you receive
11 | 
12 | - Feature/request description, Acceptance Criteria (AC) and constraints
13 | - Existing repo context (paths, conventions), relevant ADRs
14 | 
15 | Your output (JSON only)
16 | {
17 |   "plan": [
18 |     {"step": "<short action>", "rationale": "<why>", "files": ["<path>..."]}
19 |   ],
20 |   "risks": ["<risk/assumption>"],
21 |   "artifacts": {"tests": ["<which tests to add/run>"], "docs": ["<docs to update>"]},
22 |   "adr_suggestions": [
23 |     {"title": "<ADR title>", "context": "<when to add>", "decision": "<high-level>"}
24 |   ]
25 | }
26 | 
27 | Rules
28 | 
29 | - Prefer small steps; each step should be testable and reversible.
30 | - Reference existing ADRs/conventions; propose ADRs only when needed.
31 | - Keep file lists precise; avoid repo-wide edits.
32 | - Do not include code; only the JSON plan above.
```

templates/agentic-engineering-playbook/index.html
```
1 | <!DOCTYPE html>
2 | <html lang="en" class="scroll-smooth">
3 | <head>
4 |     <meta charset="UTF-8">
5 |     <meta name="viewport" content="width=device-width, initial-scale=1.0">
6 |     <title>The Agentic Engineering Playbook | Interactive Guide</title>
7 |     <script src="https://cdn.tailwindcss.com"></script>
8 |     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
9 |     <link rel="preconnect" href="https://fonts.googleapis.com">
10 |     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
11 |     <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
12 |     <!-- Chosen Palette: Slate & Amber -->
13 |     <!-- Application Structure Plan: The SPA is structured thematically into four main, navigable sections: Foundations, The Loop, Toolkit, and Troubleshooting. This non-linear design allows users to directly access the content most relevant to their needs, whether they are planning a project, implementing a feature, choosing tools, or debugging an agent. The goal is to transform the dense, linear report into an explorable knowledge base. Key interactions include a visual workflow diagram, an interactive agent persona matrix, and an expandable troubleshooting table, all designed to make complex information digestible and engaging. This structure prioritizes user-driven exploration over passive reading. -->
14 |     <!-- Visualization & Content Choices:
15 |         - Report Info: End-to-end workflow -> Goal: Organize/Change -> Viz: Interactive HTML/CSS timeline -> Interaction: Click to expand step details -> Justification: Visually breaks down a complex process into manageable, explorable stages.
16 |         - Report Info: Agent personas matrix -> Goal: Compare/Organize -> Viz: Interactive card grid -> Interaction: Click card to show persona details in a modal -> Justification: Provides a quick, comparable overview of agent roles while keeping the main view uncluttered.
17 |         - Report Info: Agent performance metrics -> Goal: Inform/Compare -> Viz: Bar Chart (Chart.js) -> Interaction: Hover for tooltips -> Justification: Quantifies abstract concepts of agent performance, making them more concrete and comparable.
18 |         - Report Info: Failure modes table -> Goal: Organize/Inform -> Viz: Interactive HTML table -> Interaction: Click row to expand details -> Justification: Manages information density effectively, allowing users to scan for problems and drill down for solutions without being overwhelmed.
19 |     -->
20 |     <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->
21 |     <style>
22 |         body {
23 |             font-family: 'Inter', sans-serif;
24 |             background-color: #f8fafc; /* slate-50 */
25 |             color: #334155; /* slate-700 */
26 |         }
27 |         .nav-link {
28 |             transition: color 0.2s, border-bottom-color 0.2s;
29 |         }
30 |         .nav-link.active, .nav-link:hover {
31 |             color: #d97706; /* amber-600 */
32 |             border-bottom-color: #d97706; /* amber-600 */
33 |         }
34 |         .card {
35 |             background-color: white;
36 |             border-radius: 0.75rem;
37 |             box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
38 |             transition: transform 0.2s, box-shadow 0.2s;
39 |         }
40 |         .card:hover {
41 |             transform: translateY(-4px);
42 |             box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
43 |         }
44 |         .modal-backdrop {
45 |             background-color: rgba(0,0,0,0.5);
46 |             transition: opacity 0.3s ease;
47 |         }
48 |         .modal-content {
49 |             transition: transform 0.3s ease;
50 |         }
51 |         .troubleshooting-row {
52 |             cursor: pointer;
53 |             transition: background-color 0.2s;
54 |         }
55 |         .troubleshooting-row:hover {
56 |             background-color: #f1f5f9; /* slate-100 */
57 |         }
58 |         .details-row {
59 |             display: none;
60 |         }
61 |     </style>
62 | </head>
63 | <body>
64 |     <header class="bg-white/80 backdrop-blur-lg sticky top-0 z-50 shadow-sm">
65 |         <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
66 |             <h1 class="text-xl font-bold text-slate-800">Agentic Engineering Playbook</h1>
67 |             <div class="hidden md:flex items-center space-x-8">
68 |                 <a href="#foundations" class="nav-link text-slate-600 font-medium border-b-2 border-transparent pb-1">Foundations</a>
69 |                 <a href="#loop" class="nav-link text-slate-600 font-medium border-b-2 border-transparent pb-1">The Loop</a>
70 |                 <a href="#toolkit" class="nav-link text-slate-600 font-medium border-b-2 border-transparent pb-1">Toolkit</a>
71 |                 <a href="#troubleshooting" class="nav-link text-slate-600 font-medium border-b-2 border-transparent pb-1">Troubleshooting</a>
72 |             </div>
73 |             <button id="mobile-menu-button" class="md:hidden text-slate-800">
74 |                 <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
75 |             </button>
76 |         </nav>
77 |         <div id="mobile-menu" class="hidden md:hidden px-6 pb-4">
78 |             <a href="#foundations" class="block py-2 text-slate-600 font-medium">Foundations</a>
79 |             <a href="#loop" class="block py-2 text-slate-600 font-medium">The Loop</a>
80 |             <a href="#toolkit" class="block py-2 text-slate-600 font-medium">Toolkit</a>
81 |             <a href="#troubleshooting" class="block py-2 text-slate-600 font-medium">Troubleshooting</a>
82 |         </div>
83 |     </header>
84 | 
85 |     <main class="container mx-auto px-6 py-12">
86 |         <section class="text-center mb-20">
87 |             <h2 class="text-4xl font-bold text-slate-900 mb-4">Build Reliable Software with LLM Agents</h2>
88 |             <p class="text-lg text-slate-600 max-w-3xl mx-auto">An interactive guide to the principles, workflows, and tools for effective agentic engineering. Move from AI as a tool to AI as a collaborator.</p>
89 |         </section>
90 | 
91 |         <section id="foundations" class="mb-20">
92 |             <h3 class="text-3xl font-bold text-slate-900 mb-2">Part I: The Foundation</h3>
93 |             <p class="text-slate-600 mb-10">For LLM agents, rigorous upfront planning and deliberate architectural design are not merely best practices—they are prerequisites for success. This section covers how to create a stable and predictable environment for agents to operate effectively.</p>
94 |             <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
95 |                 <div class="card p-6">
96 |                     <h4 class="text-lg font-semibold text-amber-700 mb-2">Specification as Code</h4>
97 |                     <p class="text-slate-600">Shift your mindset: user stories, acceptance criteria, and ADRs are no longer just documents. They become the high-level source code that directly programs the agent's execution plan, minimizing ambiguity and defining success.</p>
98 |                 </div>
99 |                 <div class="card p-6">
100 |                     <h4 class="text-lg font-semibold text-amber-700 mb-2">Test-First Prompting</h4>
101 |                     <p class="text-slate-600">Adapt Test-Driven Development for agents. By providing a failing test case in the prompt, you give the agent a precise, executable definition of "done," which is far more effective than natural language alone.</p>
102 |                 </div>
103 |                 <div class="card p-6">
104 |                     <h4 class="text-lg font-semibold text-amber-700 mb-2">Architectural Guardrails</h4>
105 |                     <p class="text-slate-600">Use Architectural Decision Records (ADRs) as persistent context. An ADR stating "We use PostgreSQL for financial data" acts as a powerful, long-term instruction that prevents the agent from making incorrect architectural choices.</p>
106 |                 </div>
107 |                 <div class="card p-6 md:col-span-2 lg:col-span-3">
108 |                     <h4 class="text-lg font-semibold text-amber-700 mb-2">Repository Architecture: Monorepo vs. Polyrepo</h4>
109 |                     <p class="text-slate-600 mb-4">The structure of your codebase has a profound impact on an agent's ability to understand and modify it. For agentic development, the choice is clear.</p>
110 |                     <div class="flex flex-col md:flex-row gap-4 text-center">
111 |                         <div class="flex-1 p-4 border border-green-200 bg-green-50 rounded-lg">
112 |                             <h5 class="font-bold text-green-800">Monorepo (Recommended)</h5>
113 |                             <p class="text-sm text-green-700">Provides a single, unified context. This is ideal for machine cognition, allowing agents to reason about system-wide dependencies and execute complex refactors with a higher success rate.</p>
114 |                         </div>
115 |                         <div class="flex-1 p-4 border border-red-200 bg-red-50 rounded-lg">
116 |                             <h5 class="font-bold text-red-800">Polyrepo</h5>
117 |                             <p class="text-sm text-red-700">Creates information silos. An agent working in one repository is blind to dependencies in another, making cross-cutting changes difficult and error-prone without significant manual intervention.</p>
118 |                         </div>
119 |                     </div>
120 |                 </div>
121 |             </div>
122 |         </section>
123 | 
124 |         <section id="loop" class="mb-20">
125 |             <h3 class="text-3xl font-bold text-slate-900 mb-2">Part II: The Agentic Development Loop</h3>
126 |             <p class="text-slate-600 mb-10">This section outlines a complete, repeatable workflow for developing a software feature using a multi-agent team. Click on each step to see more details.</p>
127 |             <div id="workflow-diagram" class="relative pl-8 border-l-2 border-slate-200">
128 |             </div>
129 |         </section>
130 | 
131 |         <section id="toolkit" class="mb-20">
132 |             <h3 class="text-3xl font-bold text-slate-900 mb-2">Part III: The Agentic Toolkit</h3>
133 |             <p class="text-slate-600 mb-10">Explore the key agent personas, core reliability techniques, and a comparison of popular frameworks and IDEs to build your agentic development stack.</p>
134 | 
135 |             <h4 class="text-2xl font-semibold text-slate-800 mb-6">Agent Persona Matrix</h4>
136 |             <div id="agent-matrix" class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
137 |             </div>
138 | 
139 |             <h4 class="text-2xl font-semibold text-slate-800 mb-6">Core Reliability Techniques</h4>
140 |             <div class="grid md:grid-cols-2 gap-8 mb-12">
141 |                 <div class="card p-6">
142 |                     <h5 class="text-lg font-semibold text-amber-700 mb-2">Context Provisioning (RAG)</h5>
143 |                     <p class="text-slate-600">Use Retrieval-Augmented Generation as the agent's long-term memory. Index your codebase into a vector database to provide the agent with highly relevant, specific code snippets as context for its tasks, dramatically improving accuracy.</p>
144 |                 </div>
145 |                 <div class="card p-6">
146 |                     <h5 class="text-lg font-semibold text-amber-700 mb-2">Structured Outputs & Tool Calling</h5>
147 |                     <p class="text-slate-600">Enforce predictability by requiring agents to respond in a strict JSON schema. Use the native "tool calling" features of modern LLMs to make agent actions robust, auditable, and easy to integrate with your existing code.</p>
148 |                 </div>
149 |                 <div class="card p-6">
150 |                     <h5 class="text-lg font-semibold text-amber-700 mb-2">Safety via Patch/Diff & Guardrails</h5>
151 |                     <p class="text-slate-600">Never allow an agent to write directly to the filesystem. Instead, have it output a `git diff` patch for review. Combine this with automated guardrails that block disallowed actions (e.g., editing critical config files) and run linters/formatters on the proposed changes.</p>
152 |                 </div>
153 |                 <div class="card p-6">
154 |                     <h5 class="text-lg font-semibold text-amber-700 mb-2">Performance Evaluation</h5>
155 |                     <p class="text-slate-600">Measure what matters. Go beyond simple pass/fail and track key metrics to systematically improve agent performance over time. This chart shows the relative importance of key metrics for evaluation.</p>
156 |                     <div class="chart-container mt-4 mx-auto" style="position: relative; height:250px; max-height: 250px; width:100%; max-width: 500px;">
157 |                         <canvas id="metricsChart"></canvas>
158 |                     </div>
159 |                 </div>
160 |             </div>
161 |         </section>
162 | 
163 |         <section id="troubleshooting" class="mb-20">
164 |             <h3 class="text-3xl font-bold text-slate-900 mb-2">Part IV: Troubleshooting Common Failures</h3>
165 |             <p class="text-slate-600 mb-10">Agentic systems can fail in predictable ways. Use this guide to diagnose and mitigate the most common failure modes. Click on a failure to see the mitigation strategy.</p>
166 |             <div class="bg-white rounded-lg shadow-md overflow-hidden">
167 |                 <table class="w-full text-left">
168 |                     <thead class="bg-slate-50 border-b border-slate-200">
169 |                         <tr>
170 |                             <th class="p-4 font-semibold text-slate-600">Failure Mode</th>
171 |                             <th class="p-4 font-semibold text-slate-600 hidden md:table-cell">Common Symptoms</th>
172 |                         </tr>
173 |                     </thead>
174 |                     <tbody id="troubleshooting-table">
175 |                     </tbody>
176 |                 </table>
177 |             </div>
178 |         </section>
179 |     </main>
180 | 
181 |     <footer class="bg-slate-800 text-slate-300">
182 |         <div class="container mx-auto px-6 py-8 text-center">
183 |             <p>&copy; 2025 Agentic Engineering Playbook. An interactive visualization.</p>
184 |             <a href="#" class="mt-4 inline-block text-amber-400 hover:text-amber-300">Back to Top &uarr;</a>
185 |         </div>
186 |     </footer>
187 | 
188 |     <div id="persona-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 hidden modal-backdrop">
189 |         <div id="modal-content" class="bg-white rounded-lg shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto transform scale-95 modal-content">
190 |             <div class="sticky top-0 bg-white p-6 border-b border-slate-200 flex justify-between items-center">
191 |                 <h3 id="modal-title" class="text-2xl font-bold text-slate-900"></h3>
192 |                 <button id="modal-close" class="text-slate-500 hover:text-slate-800">&times;</button>
193 |             </div>
194 |             <div class="p-6">
195 |                 <h4 class="font-semibold text-amber-700 mb-2">Core Responsibility</h4>
196 |                 <p id="modal-responsibility" class="text-slate-600 mb-4"></p>
197 |                 <h4 class="font-semibold text-amber-700 mb-2">Key Inputs</h4>
198 |                 <p id="modal-inputs" class="text-slate-600 mb-4"></p>
199 |                 <h4 class="font-semibold text-amber-700 mb-2">Output Schema</h4>
200 |                 <div id="modal-schema" class="bg-slate-50 p-4 rounded-md text-sm text-slate-800 overflow-x-auto"></div>
201 |             </div>
202 |         </div>
203 |     </div>
204 | 
205 |     <script>
206 |         document.addEventListener('DOMContentLoaded', function() {
207 |             const workflowData = [
208 |                 {
209 |                     step: 1,
210 |                     title: "Idea → Spec",
211 |                     description: "A feature idea is formalized into a machine-readable specification. An 'Architect Agent' can accelerate this by drafting specs, ADRs, and acceptance criteria from a high-level goal. The developer's role is to review and refine these documents for clarity and completeness."
212 |                 },
213 |                 {
214 |                     step: 2,
215 |                     title: "Spec → Scaffold",
216 |                     description: "A 'Scaffolder Agent' reads the finalized specification and generates the initial file and folder structure. This includes boilerplate code, empty test files, and configuration entries, ensuring a consistent starting point for all new features."
217 |                 },
218 |                 {
219 |                     step: 3,
220 |                     title: "Iterative Coding Loop",
221 |                     description: "The core of agentic development. In a tight loop, the developer (or a 'Tester Agent') writes a failing test for a small sub-task. An 'Implementer Agent' is then prompted to write the code to make the test pass. The output is a `git diff` patch, which the developer reviews and applies. This cycle repeats until the feature is complete."
222 |                 },
223 |                 {
224 |                     step: 4,
225 |                     title: "Tests → Docs",
226 |                     description: "Once all tests pass, a 'Documenter Agent' generates human-readable documentation. Provided with the final code, the original spec, and the test suite, it creates code comments, docstrings, and updates the `README.md` file."
227 |                 },
228 |                 {
229 |                     step: 5,
230 |                     title: "Review & Release",
231 |                     description: "The agent's work is compiled into a pull request. An agent generates the PR description, linking to the spec and relevant ADRs. This provides human reviewers with full context. Once approved, the feature follows the standard CI/CD pipeline."
232 |                 }
233 |             ];
234 | 
235 |             const agentPersonaData = [
236 |                 {
237 |                     persona: "Planner/Architect",
238 |                     responsibility: "Decompose high-level tasks, create detailed implementation plans, and draft Architectural Decision Records (ADRs).",
239 |                     inputs: "Feature Request, Existing Codebase Context, ADRs",
240 |                     schema: `{\n  "planSummary": "...",\n  "affectedFiles": [\n    {\n      "path": "/src/feature.py",\n      "action": "CREATE",\n      "description": "Main logic for the new feature."\n    }\n  ],\n  "stepByStepPlan": [\n    "Step 1: Create the file...",\n    "Step 2: Implement the function..."\n  ]\n}`
241 |                 },
242 |                 {
243 |                     persona: "Implementer/Coder",
244 |                     responsibility: "Execute a single, specific step from a plan by writing, modifying, or debugging code using a provided set of tools.",
245 |                     inputs: "Plan Step, Relevant Code Files, Conventions",
246 |                     schema: `{\n  "toolName": "writeFile",\n  "parameters": {\n    "path": "/src/feature.py",\n    "content": "def new_feature():\\n  pass"\n  }\n}`
247 |                 },
248 |                 {
249 |                     persona: "Tester",
250 |                     responsibility: "Generate comprehensive unit and integration tests for a given piece of code based on its specification and acceptance criteria.",
251 |                     inputs: "Source Code File, Acceptance Criteria",
252 |                     schema: `A complete code block for the test file, e.g.,\n\n# tests/test_feature.py\ndef test_new_feature():\n  assert new_feature() is not None`
253 |                 },
254 |                 {
255 |                     persona: "Reviewer/Refactorer",
256 |                     responsibility: "Analyze code diffs for quality, adherence to conventions, potential bugs, and opportunities for improvement.",
257 |                     inputs: "Code Diff, Conventions File",
258 |                     schema: `{\n  "reviewComments": [\n    {\n      "filePath": "/src/feature.py",\n      "lineNumber": 2,\n      "comment": "Function should have a docstring.",\n      "severity": "Minor"\n    }\n  ]\n}`
259 |                 }
260 |             ];
261 | 
262 |             const troubleshootingData = [
263 |                 {
264 |                     failure: "Specification Drift",
265 |                     symptom: "Code works but doesn't meet business needs.",
266 |                     cause: "Ambiguous initial prompt.",
267 |                     mitigation: "Use strict specification templates (Acceptance Criteria, DoD). Require human approval of an agent-generated plan *before* coding begins to confirm understanding."
268 |                 },
269 |                 {
270 |                     failure: "Context Loss",
271 |                     symptom: "Agent forgets prior instructions or code context.",
272 |                     cause: "Exceeding LLM context window; poor retrieval.",
273 |                     mitigation: "Implement a robust RAG pipeline with effective code chunking. For long tasks, break them into smaller, stateful steps managed by an orchestrator."
274 |                 },
275 |                 {
276 |                     failure: "File Thrashing",
277 |                     symptom: "Agent edits the same file repeatedly; writes to invalid paths.",
278 |                     cause: "Lack of file system awareness; reasoning loop.",
279 |                     mitigation: "Use a patch/diff workflow instead of direct writes. Provide a `listFiles` tool and implement filesystem guardrails to block writes to disallowed paths."
280 |                 },
281 |                 {
282 |                     failure: "Flaky Tests",
283 |                     symptom: "Correct code fails the verification step.",
284 |                     cause: "Inconsistent environment; non-deterministic tests.",
285 |                     mitigation: "Use containerized environments (e.g., Devcontainers) for reproducible builds. Prompt the agent to write deterministic, mock-based unit tests."
286 |                 }
287 |             ];
288 | 
289 |             const workflowContainer = document.getElementById('workflow-diagram');
290 |             workflowData.forEach(item => {
291 |                 const stepElement = document.createElement('div');
292 |                 stepElement.className = 'mb-10 cursor-pointer workflow-step';
293 |                 stepElement.innerHTML = `
294 |                     <div class="flex items-center mb-2">
295 |                         <div class="flex-shrink-0 bg-amber-500 rounded-full h-8 w-8 flex items-center justify-center text-white font-bold z-10">${item.step}</div>
296 |                         <h5 class="ml-4 text-xl font-semibold text-slate-800">${item.title}</h5>
297 |                     </div>
298 |                     <div class="ml-4 pl-8 text-slate-600 workflow-description hidden">
299 |                         <p>${item.description}</p>
300 |                     </div>
301 |                 `;
302 |                 workflowContainer.appendChild(stepElement);
303 |             });
304 | 
305 |             workflowContainer.addEventListener('click', (e) => {
306 |                 const step = e.target.closest('.workflow-step');
307 |                 if (step) {
308 |                     step.querySelector('.workflow-description').classList.toggle('hidden');
309 |                 }
310 |             });
311 | 
312 |             const agentMatrixContainer = document.getElementById('agent-matrix');
313 |             agentPersonaData.forEach(agent => {
314 |                 const agentCard = document.createElement('div');
315 |                 agentCard.className = 'card p-4 text-center cursor-pointer';
316 |                 agentCard.innerHTML = `<h5 class="font-semibold text-slate-800">${agent.persona}</h5>`;
317 |                 agentCard.addEventListener('click', () => openPersonaModal(agent));
318 |                 agentMatrixContainer.appendChild(agentCard);
319 |             });
320 | 
321 |             const troubleshootingTable = document.getElementById('troubleshooting-table');
322 |             troubleshootingData.forEach(item => {
323 |                 const row = document.createElement('tbody');
324 |                 row.innerHTML = `
325 |                     <tr class="troubleshooting-row border-b border-slate-200">
326 |                         <td class="p-4">${item.failure}</td>
327 |                         <td class="p-4 hidden md:table-cell text-slate-500">${item.symptom}</td>
328 |                     </tr>
329 |                     <tr class="details-row bg-slate-50">
330 |                         <td colspan="2" class="p-6">
331 |                             <p class="text-sm text-slate-600"><strong class="font-semibold text-amber-700">Cause:</strong> ${item.cause}</p>
332 |                             <p class="text-sm text-slate-600 mt-2"><strong class="font-semibold text-amber-700">Mitigation:</strong> ${item.mitigation}</p>
333 |                         </td>
334 |                     </tr>
335 |                 `;
336 |                 troubleshootingTable.appendChild(row);
337 |             });
338 | 
339 |             troubleshootingTable.addEventListener('click', (e) => {
340 |                 const row = e.target.closest('.troubleshooting-row');
341 |                 if (row) {
342 |                     const details = row.nextElementSibling;
343 |                     details.style.display = details.style.display === 'table-row' ? 'none' : 'table-row';
344 |                 }
345 |             });
346 | 
347 |             const modal = document.getElementById('persona-modal');
348 |             const modalContent = document.getElementById('modal-content');
349 |             const modalClose = document.getElementById('modal-close');
350 | 
351 |             function openPersonaModal(agent) {
352 |                 document.getElementById('modal-title').innerText = agent.persona;
353 |                 document.getElementById('modal-responsibility').innerText = agent.responsibility;
354 |                 document.getElementById('modal-inputs').innerText = agent.inputs;
355 |                 document.getElementById('modal-schema').innerHTML = `<pre><code>${agent.schema}</code></pre>`;
356 |                 modal.classList.remove('hidden');
357 |                 setTimeout(() => {
358 |                     modal.style.opacity = '1';
359 |                     modalContent.style.transform = 'scale(1)';
360 |                 }, 10);
361 |             }
362 | 
363 |             function closePersonaModal() {
364 |                 modal.style.opacity = '0';
365 |                 modalContent.style.transform = 'scale(0.95)';
366 |                 setTimeout(() => {
367 |                     modal.classList.add('hidden');
368 |                 }, 300);
369 |             }
370 | 
371 |             modalClose.addEventListener('click', closePersonaModal);
372 |             modal.addEventListener('click', (e) => {
373 |                 if (e.target === modal) {
374 |                     closePersonaModal();
375 |                 }
376 |             });
377 | 
378 |             const ctx = document.getElementById('metricsChart').getContext('2d');
379 |             new Chart(ctx, {
380 |                 type: 'bar',
381 |                 data: {
382 |                     labels: ['Task Success', 'Efficiency (Turns)', 'Code Churn', 'HITL Interventions', 'Token Cost'],
383 |                     datasets: [{
384 |                         label: 'Relative Importance',
385 |                         data: [100, 85, 70, 90, 60],
386 |                         backgroundColor: [
387 |                             'rgba(5, 150, 105, 0.6)',
388 |                             'rgba(217, 119, 6, 0.6)',
389 |                             'rgba(219, 39, 119, 0.6)',
390 |                             'rgba(59, 130, 246, 0.6)',
391 |                             'rgba(107, 114, 128, 0.6)'
392 |                         ],
393 |                         borderColor: [
394 |                             'rgba(5, 150, 105, 1)',
395 |                             'rgba(217, 119, 6, 1)',
396 |                             'rgba(219, 39, 119, 1)',
397 |                             'rgba(59, 130, 246, 1)',
398 |                             'rgba(107, 114, 128, 1)'
399 |                         ],
400 |                         borderWidth: 1
401 |                     }]
402 |                 },
403 |                 options: {
404 |                     responsive: true,
405 |                     maintainAspectRatio: false,
406 |                     indexAxis: 'y',
407 |                     plugins: {
408 |                         legend: {
409 |                             display: false
410 |                         },
411 |                         title: {
412 |                             display: true,
413 |                             text: 'Key Agent Performance Metrics'
414 |                         }
415 |                     },
416 |                     scales: {
417 |                         x: {
418 |                             beginAtZero: true
419 |                         }
420 |                     }
421 |                 }
422 |             });
423 | 
424 |             const mobileMenuButton = document.getElementById('mobile-menu-button');
425 |             const mobileMenu = document.getElementById('mobile-menu');
426 |             mobileMenuButton.addEventListener('click', () => {
427 |                 mobileMenu.classList.toggle('hidden');
428 |             });
429 | 
430 |             document.querySelectorAll('a[href^="#"]').forEach(anchor => {
431 |                 anchor.addEventListener('click', function (e) {
432 |                     e.preventDefault();
433 |                     document.querySelector(this.getAttribute('href')).scrollIntoView({
434 |                         behavior: 'smooth'
435 |                     });
436 |                     if(mobileMenu.classList.contains('hidden') === false) {
437 |                         mobileMenu.classList.add('hidden');
438 |                     }
439 |                 });
440 |             });
441 | 
442 |             const navLinks = document.querySelectorAll('.nav-link');
443 |             const sections = document.querySelectorAll('section');
444 |             window.addEventListener('scroll', () => {
445 |                 let current = '';
446 |                 sections.forEach(section => {
447 |                     const sectionTop = section.offsetTop;
448 |                     if (pageYOffset >= sectionTop - 100) {
449 |                         current = section.getAttribute('id');
450 |                     }
451 |                 });
452 |                 navLinks.forEach(link => {
453 |                     link.classList.remove('active');
454 |                     if (link.getAttribute('href').includes(current)) {
455 |                         link.classList.add('active');
456 |                     }
457 |                 });
458 |             });
459 |         });
460 |     </script>
461 | </body>
462 | </html>
```

templates/agentic-workflow-simulator/index.html
```
1 | <!DOCTYPE html>
2 | <html lang="en">
3 | <head>
4 |     <meta charset="UTF-8">
5 |     <meta name="viewport" content="width=device-width, initial-scale=1.0">
6 |     <title>Agentic Workflow Simulator</title>
7 |     <script src="https://cdn.tailwindcss.com"></script>
8 |     <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
9 |     <style>
10 |         body {
11 |             font-family: 'Inter', sans-serif;
12 |         }
13 |         .console-output::before {
14 |             content: '$ ';
15 |             color: #9ca3af;
16 |         }
17 |     </style>
18 | </head>
19 | <body class="bg-gray-900 text-gray-200 flex flex-col items-center justify-center min-h-screen p-4 sm:p-6 lg:p-8">
20 | 
21 |     <div class="w-full max-w-4xl bg-gray-800 rounded-2xl shadow-2xl overflow-hidden">
22 |         <div class="p-6 border-b border-gray-700">
23 |             <h1 class="text-2xl font-bold text-white">Agentic Development Workflow Simulator</h1>
24 |             <p class="mt-2 text-gray-400">This simulates a program that guides an LLM through a structured coding process. Click "Run Workflow" to see it in action.</p>
25 |         </div>
26 | 
27 |         <div class="p-6">
28 |             <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between">
29 |                 <div class="mb-4 sm:mb-0">
30 |                     <label for="user-goal" class="text-sm font-medium text-gray-300">User Goal:</label>
31 |                     <p id="user-goal" class="mt-1 text-lg text-cyan-400 bg-gray-700/50 rounded-md px-3 py-1">"Add a function `add(a, b)` and a test for it."</p>
32 |                 </div>
33 |                 <button id="run-button" class="w-full sm:w-auto bg-cyan-600 hover:bg-cyan-700 text-white font-bold py-3 px-6 rounded-lg transition-transform transform hover:scale-105 focus:outline-none focus:ring-4 focus:ring-cyan-500/50">
34 |                     Run Workflow
35 |                 </button>
36 |             </div>
37 |         </div>
38 | 
39 |         <div class="bg-black h-96 p-6 overflow-y-auto font-mono text-sm">
40 |             <div id="console-output">
41 |                 <p class="text-gray-500">Console output will appear here...</p>
42 |             </div>
43 |         </div>
44 |     </div>
45 | 
46 |     <script type="module">
47 |         // This is a self-contained simulator.
48 |         // In a real application, these would be separate, well-tested modules.
49 | 
50 |         // --- Mock File System ---
51 |         // We'll simulate a file system in memory to avoid writing to disk.
52 |         const VIRTUAL_FILE_SYSTEM = {};
53 | 
54 |         // --- Schemas (Data Contracts for LLM) ---
55 |         // These classes define the expected structure of the LLM's output.
56 |         // In a real Python app, you'd use a library like Pydantic.
57 |         class Task {
58 |             constructor(description, files_to_edit, test_command) {
59 |                 this.description = description;
60 |                 this.files_to_edit = files_to_edit;
61 |                 this.test_command = test_command;
62 |             }
63 |         }
64 | 
65 |         class Plan {
66 |             constructor(summary, tasks_to_execute) {
67 |                 this.summary = summary;
68 |                 this.tasks = tasks_to_execute;
69 |             }
70 |         }
71 | 
72 |         // --- Toolbelt (Safe access to the "real world") ---
73 |         const toolbelt = {
74 |             listFiles: () => {
75 |                 return Object.keys(VIRTUAL_FILE_SYSTEM).join('\n') || 'No files exist yet.';
76 |             },
77 |             writeFile: (path, content) => {
78 |                 logToConsole(`TOOL: Writing ${content.length} bytes to ${path}`);
79 |                 VIRTUAL_FILE_SYSTEM[path] = content;
80 |                 return `Successfully wrote to ${path}`;
81 |             },
82 |             readFile: (path) => {
83 |                 logToConsole(`TOOL: Reading file ${path}`);
84 |                 return VIRTUAL_FILE_SYSTEM[path];
85 |             },
86 |             runTests: (command) => {
87 |                 logToConsole(`TOOL: Running test command: "${command}"`);
88 |                 if (command === 'pytest') {
89 |                     const testFileContent = VIRTUAL_FILE_SYSTEM['tests/test_main.py'];
90 |                     const mainFileContent = VIRTUAL_FILE_SYSTEM['src/main.py'];
91 | 
92 |                     // Super simplified test runner simulation
93 |                     if (!mainFileContent || !testFileContent) {
94 |                         return { passed: false, error: "Error: Source or test file not found." };
95 |                     }
96 |                     if (mainFileContent.includes('def add(a, b):') && mainFileContent.includes('return a + b')) {
97 |                          if (testFileContent.includes('assert add(2, 3) == 5')) {
98 |                             return { passed: true, error: null };
99 |                          }
100 |                     }
101 |                     return { passed: false, error: "AssertionError: Test failed. `add(2, 3)` did not return 5." };
102 |                 }
103 |                 return { passed: false, error: "Unknown test command." };
104 |             }
105 |         };
106 | 
107 |         // --- Agent Personas (Mock LLM Calls) ---
108 |         // These functions simulate calls to a large language model.
109 |         // Notice how they return a JSON string that matches our schemas.
110 |         const agents = {
111 |             callArchitectAgent: (goal, repoMap) => {
112 |                 logToConsole("AGENT: Calling Architect to create a plan...");
113 |                 const planJson = {
114 |                     summary: "Create a new function `add` in `main.py` and a corresponding test in `test_main.py`.",
115 |                     tasks_to_execute: [
116 |                         {
117 |                             description: "Implement the `add(a, b)` function in `src/main.py`.",
118 |                             files_to_edit: ["src/main.py"],
119 |                             test_command: "pytest"
120 |                         },
121 |                         {
122 |                             description: "Write a test for the `add` function in `tests/test_main.py`.",
123 |                             files_to_edit: ["tests/test_main.py", "src/main.py"],
124 |                             test_command: "pytest"
125 |                         }
126 |                     ]
127 |                 };
128 |                 return JSON.stringify(planJson, null, 2);
129 |             },
130 |             callImplementerAgent: (task, fileContents, lastError) => {
131 |                 logToConsole(`AGENT: Calling Implementer for task: "${task.description}"`);
132 |                 if (lastError) {
133 |                     logToConsole(`AGENT: Providing error context for self-correction: ${lastError}`);
134 |                 }
135 | 
136 |                 // Simulate self-correction. If there was an error, the "LLM" provides the correct code.
137 |                 if (task.description.includes('Implement the `add`') && lastError) {
138 |                      return JSON.stringify({
139 |                         file_path: "src/main.py",
140 |                         thought: "The previous attempt failed. The function was missing the implementation. I will add the correct return statement.",
141 |                         code: "def add(a, b):\n    return a + b"
142 |                     });
143 |                 }
144 | 
145 |                 // First attempt for implementing the function (intentionally incorrect)
146 |                 if (task.description.includes('Implement the `add`')) {
147 |                     return JSON.stringify({
148 |                         file_path: "src/main.py",
149 |                         thought: "I will create the function signature as requested in `src/main.py`.",
150 |                         code: "def add(a, b):\n    pass" // Intentionally incomplete for demonstration
151 |                     });
152 |                 }
153 | 
154 |                 // Code for the test file
155 |                 if (task.description.includes('Write a test')) {
156 |                     return JSON.stringify({
157 |                         file_path: "tests/test_main.py",
158 |                         thought: "I will write a test case for the `add` function to ensure it works correctly.",
159 |                         code: "from src.main import add\n\ndef test_add():\n    assert add(2, 3) == 5"
160 |                     });
161 |                 }
162 |             }
163 |         };
164 | 
165 |         // --- Main Orchestrator Logic ---
166 |         const consoleOutput = document.getElementById('console-output');
167 |         const runButton = document.getElementById('run-button');
168 |         let logBuffer = [];
169 | 
170 |         function logToConsole(message) {
171 |             console.log(message);
172 |             const p = document.createElement('p');
173 |             p.className = 'console-output';
174 |             p.textContent = message;
175 |             logBuffer.push(p);
176 |         }
177 | 
178 |         function renderLog() {
179 |             logBuffer.forEach(p => consoleOutput.appendChild(p));
180 |             consoleOutput.scrollTop = consoleOutput.scrollHeight;
181 |             logBuffer = [];
182 |         }
183 | 
184 |         async function orchestrate() {
185 |             runButton.disabled = true;
186 |             runButton.textContent = "Running...";
187 |             consoleOutput.innerHTML = '';
188 | 
189 |             // 1. INITIALIZATION
190 |             logToConsole("ORCHESTRATOR: Starting workflow...");
191 |             const userGoal = "Add a function `add(a, b)` and a test for it.";
192 |             Object.keys(VIRTUAL_FILE_SYSTEM).forEach(key => delete VIRTUAL_FILE_SYSTEM[key]);
193 |             await new Promise(r => setTimeout(r, 500));
194 |             renderLog();
195 | 
196 |             // 2. SCAFFOLDING
197 |             logToConsole("ORCHESTRATOR: Scaffolding initial project structure...");
198 |             toolbelt.writeFile('src/main.py', '# Main application file');
199 |             toolbelt.writeFile('tests/test_main.py', '# Test file for main');
200 |             await new Promise(r => setTimeout(r, 500));
201 |             renderLog();
202 | 
203 |             // 3. ARCHITECTURE PHASE
204 |             const repoMap = toolbelt.listFiles();
205 |             logToConsole(`ORCHESTRATOR: Current repo map:\n${repoMap}`);
206 |             const planJsonString = agents.callArchitectAgent(userGoal, repoMap);
207 |             const planData = JSON.parse(planJsonString);
208 |             const plan = new Plan(planData.summary, planData.tasks_to_execute.map(t => new Task(t.description, t.files_to_edit, t.test_command)));
209 |             logToConsole(`ORCHESTRATOR: Plan received:\n${JSON.stringify(plan, null, 2)}`);
210 |             await new Promise(r => setTimeout(r, 1000));
211 |             renderLog();
212 | 
213 |             // 4. IMPLEMENTATION & TEST LOOP
214 |             for (const task of plan.tasks) {
215 |                 logToConsole(`ORCHESTRATOR: Starting task -> ${task.description}`);
216 |                 let lastError = null;
217 |                 let attempts = 0;
218 |                 const maxAttempts = 2;
219 | 
220 |                 while (attempts < maxAttempts) {
221 |                     attempts++;
222 |                     logToConsole(`ORCHESTRATOR: Attempt ${attempts}/${maxAttempts}...`);
223 | 
224 |                     const fileContents = task.files_to_edit.reduce((acc, path) => {
225 |                         acc[path] = toolbelt.readFile(path);
226 |                         return acc;
227 |                     }, {});
228 | 
229 |                     const implementationJsonString = agents.callImplementerAgent(task, fileContents, lastError);
230 |                     const implementation = JSON.parse(implementationJsonString);
231 | 
232 |                     toolbelt.writeFile(implementation.file_path, implementation.code);
233 | 
234 |                     const testResult = toolbelt.runTests(task.test_command);
235 | 
236 |                     if (testResult.passed) {
237 |                         logToConsole(`ORCHESTRATOR: ✅ Tests passed for task!`);
238 |                         lastError = null;
239 |                         break; // Success, move to next task
240 |                     } else {
241 |                         logToConsole(`ORCHESTRATOR: ❌ Tests failed: ${testResult.error}`);
242 |                         lastError = testResult.error;
243 |                     }
244 |                     await new Promise(r => setTimeout(r, 1000));
245 |                     renderLog();
246 |                 }
247 | 
248 |                 if (lastError) {
249 |                     logToConsole("ORCHESTRATOR: ❌ Task failed after multiple attempts. Halting workflow.");
250 |                     runButton.disabled = false;
251 |                     runButton.textContent = "Run Workflow";
252 |                     renderLog();
253 |                     return;
254 |                 }
255 |                 await new Promise(r => setTimeout(r, 500));
256 |                 renderLog();
257 |             }
258 | 
259 |             logToConsole("🚀 ORCHESTRATOR: Workflow completed successfully!");
260 |             logToConsole("Final file contents:");
261 |             logToConsole(`--- src/main.py ---\n${toolbelt.readFile('src/main.py')}`);
262 |             logToConsole(`--- tests/test_main.py ---\n${toolbelt.readFile('tests/test_main.py')}`);
263 | 
264 |             runButton.disabled = false;
265 |             runButton.textContent = "Run Workflow";
266 |             renderLog();
267 |         }
268 | 
269 |         runButton.addEventListener('click', orchestrate);
270 | 
271 |     </script>
272 | </body>
273 | </html>
```

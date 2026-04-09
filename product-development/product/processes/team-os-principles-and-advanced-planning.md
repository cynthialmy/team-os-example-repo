# Team OS Principles and Advanced Planning

This guide distills practical lessons for AI-native product work: how to structure a shared context repository, how to prompt for high-quality outputs, and how to run advanced planning loops for complex docs and decisions.

---

## 1) Core Team OS Principles

### 1. Shared context is infrastructure

- Treat the repository as the team's operating system, not a PM-only workspace.
- Include product, engineering, analytics, data engineering, design, and ops context.
- Require context updates as part of feature launch completion.

### 2. Structure beats volume

- Keep root-level guidance lean; avoid dumping large instructions in one file.
- Use nested folder indexes so the agent loads only relevant context.
- Prefer clear folder ownership and predictable naming conventions.

### 3. Optimize for context management

- **Context**: information available in the current session.
- **Context window**: total capacity for that information.
- **Compaction**: summary compression when context is full (fidelity loss risk).
- **Thinking room**: remaining space for reasoning after context is loaded.

Practical rule: only load what is needed for the current task to preserve reasoning quality.

### 4. Standardize high-frequency artifacts

- Use consistent templates for recurring docs (call summaries, PRDs, RFCs, investigations).
- Store lightweight summaries near long raw artifacts (for example, transcripts).
- Make cross-document synthesis cheap by keeping the same structure across authors.

### 5. Build as a team, not as a hero

- Functional leads define standards for their areas.
- Everyone contributes context through normal pull request flow.
- Shared skills, commands, and automations compound team-wide leverage.

---

## 2) Prompting Principles for Better Outputs

### 1. Start with alignment, not immediate execution

Before execution, ask for a short proposal:

1. What the agent will do
2. Which files/sources it will use
3. What output format it will produce
4. How it will verify quality

This catches direction errors before token-heavy work begins.

### 2. Use planning depth proportional to ambiguity

- **Low ambiguity**: quick alignment proposal is enough.
- **Medium complexity**: explicit plan with phases and deliverables.
- **High ambiguity/high stakes**: deep plan mode with checkpoints, verification contracts, and scoped parallelization.

### 3. Be explicit about evidence quality

For research or strategy outputs, require:

- source links for factual claims
- clear differentiation between evidence and inference
- dated references when recency matters

### 4. Specify the shape of output

Do not only ask "write a strategy doc." Define:

- audience
- decisions needed
- required sections
- constraints and non-goals
- success criteria

### 5. Ask the agent to challenge your thinking

Invite pushback explicitly:

- ask for missing angles
- ask for hard trade-offs
- ask for disconfirming evidence
- ask for assumptions that need testing

---

## 3) Advanced Plan-Mode Techniques

### A. Phase-based planning with checkpoints

For complex work, separate into phases:

1. Discovery/research
2. Synthesis and recommendation
3. Drafting and revisions
4. Final verification and packaging

Insert a mandatory check-in between phases when direction could change.

### B. Deliberate parallelization

Do not parallelize blindly. Parallelize independent workstreams only, such as:

- competitor scans by segment
- separate doc sections with isolated source sets
- independent metric pulls

Then reconcile in a single orchestrator pass.

### C. Agent prompt transparency

For complex tasks, ask the orchestrator to show subagent prompts before running. Validate:

- scope boundaries
- source files
- expected output format
- verification method

### D. Temporary file fan-in pattern

When running many subagents:

- each subagent writes to a temp artifact
- parent agent reads temp artifacts and synthesizes
- avoid returning all large outputs directly into one parent context burst

This reduces context overload and run instability.

### E. Verification contracts

Define "done and done well" before execution:

- required checks (fact, link, formatting, style, metric consistency)
- test or validation steps
- acceptance checklist per output artifact

### F. Plan artifact persistence

Save high-quality plan files to the repository for reuse and continuity.

Benefits:

- faster repeat execution
- easier handoff across teammates
- better recovery after context compaction

---

## 4) Practical PM Workflow (AI-Native)

1. Start fresh context for a new task (new session or clear).
2. Ask for an alignment proposal.
3. Escalate to plan mode if complexity warrants.
4. Require explicit verification criteria.
5. Execute in phases with a checkpoint after discovery.
6. Review and refine outputs.
7. Commit both final docs and reusable process improvements.

---

## 5) Tooling Guidance by Task Type

- Use coding agents for advanced PM work requiring repo context, structured outputs, and multi-step execution.
- Use chat tools for quick, low-context questions.
- Keep your Team OS tool-agnostic: the same repository should support multiple agents.

---

## 6) Anti-Patterns to Avoid

- Giving up after one weak output without iterating the setup.
- Overloading root instructions with too much static content.
- Letting context rot by skipping updates after launches.
- Running complex work without plan mode or verification definitions.
- Mixing unrelated tasks in one session without clearing context.

---

## 7) Two-Hour Weekend Bootstrap

If time is limited:

1. Add a minimal root index and folder indexes.
2. Standardize one recurring artifact template (for example, customer summaries).
3. Add one reusable planning prompt for strategy/PRD work.
4. Automate one repetitive weekly synthesis to free learning time.

The objective is not perfection. The objective is to create repeatable leverage and then iterate continuously.

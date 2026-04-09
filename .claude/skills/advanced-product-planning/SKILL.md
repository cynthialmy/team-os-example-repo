---
name: advanced-product-planning
description: Run high-quality planning loops for complex PM tasks (strategy docs, PRDs, research syntheses) with explicit verification and phased execution.
---

# Advanced Product Planning Skill

Use this skill when a task has high ambiguity, meaningful trade-offs, or requires deep synthesis across multiple sources.

## Use Cases

- strategy docs that need competitor or market synthesis
- complex PRDs with cross-functional constraints
- investigations requiring evidence-backed recommendations
- multi-step writeups where quality and structure are critical

## Planning Workflow

### Step 1: Align before execution

Ask for a proposal before doing work:

1. objective and audience
2. sources/files to read
3. output structure
4. verification method

### Step 2: Clarify scope and constraints

Collect:

- decision to be made
- required sections and non-goals
- time horizon
- known assumptions and risks

### Step 3: Build a phased plan

Default phases:

1. discovery/research
2. synthesis and option framing
3. draft artifact production
4. verification and final polish

Add a checkpoint between phase 1 and 2 when findings can change direction.

### Step 4: Define verification contract

Before execution, define:

- evidence requirements (citations, links, freshness)
- quality checklist (logic, completeness, formatting)
- acceptance criteria per output artifact

### Step 5: Execute with deliberate parallelization

Parallelize only independent subtasks and require each subtask to produce a bounded output.

For large runs:

- write subtask outputs to temp files
- synthesize in a parent pass
- avoid flooding parent context with large raw subagent responses

### Step 6: Invite pushback

Ask the agent to challenge the plan:

- what assumptions are weak?
- what trade-offs are missing?
- what evidence could disprove the recommendation?
- what alternative framing should be considered?

### Step 7: Persist artifacts

Store both:

- final deliverable
- plan file (for reuse and continuity after compaction)

## Prompt Templates

### Lightweight alignment prompt

```text
Research [topic] and give me a short proposal first:
1) what you will do,
2) which files/sources you will use,
3) output structure,
4) how you will verify quality.
Do not execute until I approve.
```

### Deep planning prompt

```text
I need a high-quality [artifact] for [audience] on [topic].
Use plan mode and produce a phased plan with checkpoints.
Include:
- explicit assumptions,
- alternatives/trade-offs,
- verification criteria,
- source requirements for claims,
- proposed parallelization opportunities.
Use ask-user questions to challenge my framing before execution.
```

### Verification prompt

```text
Before finalizing, run a self-check:
- confirm each key claim has evidence,
- identify weakly supported statements,
- verify structure matches requested format,
- list open risks and unresolved questions.
```

## Operating Principles

- plan depth should match ambiguity and impact
- preserve thinking room by loading only relevant context
- standardize repeated artifacts for easier synthesis
- prefer checkpoints over long opaque execution runs
- improve continuously: capture what worked and update the playbook

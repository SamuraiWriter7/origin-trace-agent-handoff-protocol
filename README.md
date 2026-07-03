# Origin Trace Agent Handoff Protocol

**Origin Trace Agent Handoff Protocol** is a gate-aware protocol for AI agents that consume Origin Trace Receipts and route them toward approved downstream systems.

It is designed as a downstream companion to:

- Origin Trace Receipt Standard
- Synchronization Audit Protocol
- Origin Structure Market
- Origin License Policy Registry
- Compute Access Royalty OS
- Royalty OS
- Multi-Wing orchestration systems

## Purpose

Origin Trace Receipt Standard records:

- origin
- trace
- evidence
- transformation diff
- audit state
- royalty handoff
- human review gate
- protocol handoff

This repository defines how an AI agent should **consume** that receipt.

The goal is not to let agents execute sensitive actions automatically.

The goal is to define a machine-readable handoff record that helps an agent decide:

1. Which receipt was received?
2. Which layers are present or missing?
3. Is the Human Review Gate passed, pending, blocked, or rejected?
4. Which downstream actions are allowed?
5. Which downstream actions are blocked?
6. Which protocols may receive the receipt next?
7. What should the agent record before stopping or handing off?

## Core Concept

An Agent Handoff Record answers seven questions:

1. **Source Receipt** — Which Origin Trace Receipt is being consumed?
2. **Agent Context** — Which agent is processing the receipt, and with what autonomy level?
3. **Intake** — Which required layers were detected or missing?
4. **Gate Check** — What does the Human Review Gate allow or block?
5. **Routing** — Which downstream systems are candidates for handoff?
6. **Action Policy** — What may the agent do, and what must it not do?
7. **Handoff Result** — What did the agent emit, recommend, block, or defer?

## Design Principles

- Gate-aware by default
- Human Review Gate first
- Read-only and recommendation-first in v0.1
- No automatic payment execution
- No automatic market registration
- No automatic public origin claims
- No bypassing receipt boundary conditions
- Compatible with YAML and JSON
- Machine-validatable by JSON Schema

## v0.1 Scope

v0.1 defines the **Receipt Intake & Gate Check Layer**.

It allows an AI agent to:

- ingest an Origin Trace Receipt
- identify available receipt layers
- detect missing layers
- inspect Human Review Gate status
- classify allowed and blocked downstream actions
- propose candidate routing targets
- record a handoff result

It does not allow the agent to execute sensitive downstream actions.

## Sensitive Actions

The protocol treats these as sensitive actions:

- market registration
- license publication
- commercial use approval
- AI training use approval
- royalty execution
- external settlement
- public origin claim
- autonomous agent handoff

If a Human Review Gate has not passed, these actions should be blocked or deferred.

## Repository Structure

```text
origin-trace-agent-handoff-protocol/
├─ README.md
├─ CHANGELOG.md
├─ schemas/
│  └─ agent-handoff-record.schema.json
├─ examples/
│  └─ agent-handoff-record.example.yaml
├─ scripts/
│  └─ validate_examples.py
├─ requirements.txt
└─ .github/
   └─ workflows/
      └─ validate.yml

Validation

Install dependencies:

pip install -r requirements.txt

Validate examples:

python scripts/validate_examples.py

Expected output:

[validate] Agent Handoff Record
  schema : schemas/agent-handoff-record.schema.json
  example: examples/agent-handoff-record.example.yaml
[ok] agent-handoff-record.example.yaml is valid
Version

Current candidate:

v0.1.0-candidate
Status

This repository begins as a downstream handoff protocol for AI agents.

v0.1 is intentionally conservative.

The agent may inspect, classify, recommend, and record.
The agent may not bypass Human Review Gate decisions or execute sensitive downstream actions automatically.

Non-Goals

This protocol does not:

prove ownership
determine infringement
execute payment
register assets automatically
publish licenses automatically
approve AI training use
replace legal review
replace human governance
replace Origin Trace Receipt Standard
License

Add a license according to the intended usage policy of the repository.

Recommended options:

MIT for open technical reuse
Apache-2.0 for patent-aware technical reuse
CC-BY-4.0 for documentation-focused reuse
Custom attribution-required policy for origin-sensitive protocol work

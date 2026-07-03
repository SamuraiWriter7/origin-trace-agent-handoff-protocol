# Origin Trace Agent Handoff Protocol

A gate-aware protocol for AI agents to consume Origin Trace Receipts and route them to approved downstream systems.

This repository defines a structured handoff record for AI agents that read, inspect, classify, route, notify, emit, and boundary-check Origin Trace Receipts.

It is designed as a companion layer to:

- Origin Trace Receipt Standard
- AI Search Trace Receipt Standard
- Synchronization Audit Protocol
- Origin Structure Market
- Origin License Policy Registry
- Compute Access Royalty OS
- Royalty OS
- Multi-Wing orchestration systems

The core purpose is simple:

> An AI agent may read a receipt, recommend safe routes, prepare review records, and emit internal handoff receipts, but it must not bypass human review, execute sensitive actions, or modify its own boundary.

---

## Purpose

AI-assisted creation increasingly produces structured records that describe:

- origin
- trace
- transformation
- evidence
- transformation diff
- audit state
- royalty handoff
- human review gate
- downstream handoff intent

The Origin Trace Receipt Standard records these layers.

This repository answers the next question:

> What may an AI agent do after it consumes that receipt?

Without a gate-aware handoff protocol, an agent might incorrectly treat a candidate downstream target as an executable route.

This protocol prevents that by recording:

- which receipt was consumed
- which layers were detected
- what the Human Review Gate allows or blocks
- which downstream systems are candidate targets
- which routes are authorized, conditional, or blocked
- who should review blocked or conditional routes
- which handoff receipts may be prepared or emitted
- what non-bypassable autonomy boundary the agent must obey
- what actions the agent may or must not perform

---

## Core Concept

An Agent Handoff Record answers eleven questions:

1. **Source Receipt** — Which Origin Trace Receipt is being consumed?
2. **Agent Context** — Which agent is processing the receipt, and with what autonomy level?
3. **Intake** — Which required layers were detected or missing?
4. **Gate Check** — What does the Human Review Gate allow or block?
5. **Routing** — Which downstream systems are candidates for handoff?
6. **Route Authorization** — Which candidate routes are authorized, conditional, or blocked?
7. **Reviewer Notification** — Who should review blocked or conditional routes, and what safe payload should they receive?
8. **Handoff Receipt Emission** — Which downstream handoff receipts may be prepared, emitted, deferred, or blocked?
9. **Agent Boundary Seal** — What non-bypassable autonomy boundary must the agent obey?
10. **Action Policy** — What may the agent do, and what must it not do?
11. **Handoff Result** — What did the agent emit, recommend, block, defer, prepare, or seal?

---

## Design Principles

This protocol follows these principles:

- Gate-aware by default
- Human Review Gate first
- Recommendation before execution
- Safe payloads before external handoff
- Internal review before public action
- No automatic payment execution
- No automatic market registration
- No automatic license publication
- No automatic AI training approval
- No automatic public origin claims
- No unredacted sensitive payload transmission
- No Human Review Gate bypass
- No route authorization override
- No boundary self-modification

The protocol is intentionally conservative.

An AI agent may help prepare the path, but it must not seize authority from the human review layer.

---

## Record Layers

### 1. Source Receipt

Identifies the Origin Trace Receipt being consumed.

It records:

- receipt ID
- receipt schema version
- receipt reference
- receipt status

Example:

```yaml
source_receipt:
  receipt_id: otr_2026-07-03-human-review-gate-v0.5
  receipt_schema_version: "0.5.0"
  receipt_reference: "origin-trace-receipt-standard/examples/origin-trace-receipt.example.yaml"
  receipt_status: draft
```

---

### 2. Agent Context

Describes the agent processing the receipt.

It records:

- agent ID
- agent type
- agent role
- autonomy level

Supported autonomy levels include:

- read_only
- recommendation_only
- manual_approval_required
- limited_execution
- unknown

In the first arc, the recommended autonomy level is:

```yaml
autonomy_level: recommendation_only
```

---

### 3. Intake

Records whether the source receipt was successfully parsed and which layers were detected.

Expected Origin Trace Receipt layers include:

- origin
- trace
- transformation
- evidence
- transformation_diff
- audit
- royalty_hook
- royalty_handoff
- human_review_gate
- boundary
- handoff
- validation

The intake layer is not a permission layer.  
It only records whether the receipt was readable and complete enough for routing analysis.

---

### 4. Gate Check

Reads the Human Review Gate state from the source receipt.

It records:

- Human Review Gate status
- decision status
- blocking conditions
- permitted actions
- blocked actions
- gate summary

Sensitive actions should remain blocked unless the Human Review Gate and route authorization conditions are satisfied.

Examples of blocked actions:

- market_registration
- license_publication
- commercial_use
- training_use
- royalty_execution
- external_settlement
- public_origin_claim
- agent_auto_handoff

---

### 5. Routing

Identifies downstream candidate targets.

Candidate targets may include:

- synchronization-audit-protocol
- origin-structure-market
- origin-license-policy-registry
- compute-access-royalty-os
- royalty-os
- multi-wing-orchestration-generator
- external_registry
- other

Routing does not mean execution.

A candidate target can be:

- ready
- manual_review_required
- blocked
- not_applicable

---

### 6. Route Authorization

The Route Authorization Layer records which downstream routes an AI agent may use after inspecting an Origin Trace Receipt and its Human Review Gate.

It distinguishes between:

- authorized routes
- conditionally authorized routes
- routes requiring manual review
- blocked routes
- not-applicable routes

This layer prevents an agent from treating all candidate targets as executable destinations.

For example, an agent may be allowed to route a receipt to a synchronization audit queue, but blocked from routing the same receipt to market registration or royalty execution until the Human Review Gate has passed.

The layer may define:

- route ID
- target protocol
- target purpose
- authorization decision
- Human Review Gate dependency
- permitted route actions
- blocked route actions
- authorization conditions
- authorization rationale

In v0.2 and later, route authorization remains conservative.

The agent may recommend and record routes, but sensitive downstream actions remain blocked unless review conditions are satisfied.

---

### 7. Reviewer Notification

The Reviewer Notification Layer records who should review a blocked, conditional, or sensitive route.

It prevents an AI agent from silently stopping a route without producing a useful human-review trail.

The layer may define:

- notification ID
- notification status
- notification mode
- review requests
- reviewer roles
- review reasons
- priority
- related routes
- related blocking conditions
- requested decisions
- notification channel
- safe notification payload
- blocked payload items
- request status

This layer is intentionally careful about payload safety.

A reviewer notification should not automatically include:

- private conversation excerpts
- unredacted evidence
- sensitive identity information
- external settlement details
- unverified origin claims
- confidential repository URLs

In v0.3 and later, the agent may prepare review notifications and request human review.

It may not notify external systems with sensitive payloads unless the required review conditions are satisfied.

---

### 8. Handoff Receipt Emission

The Handoff Receipt Emission Layer records which downstream handoff receipts an agent may prepare or emit.

It prevents agent decisions from remaining only as internal reasoning.

The layer may define:

- emission ID
- emission status
- emission mode
- emitted receipt IDs
- emitted receipt type
- target protocol
- target purpose
- related route
- related review request
- emission decision
- payload scope
- review dependency
- emission policy
- emission rationale

This layer distinguishes between:

- internal audit handoff
- manual review handoff
- royalty review handoff
- license review handoff
- market review handoff
- blocked route receipt
- archival receipt

In v0.4 and later, the agent may prepare safe internal or review-oriented handoff receipts.

The agent may not emit external handoff receipts, execution receipts, payment receipts, market registration receipts, or license publication receipts unless the required Human Review Gate and route authorization conditions are satisfied.

---

### 9. Agent Boundary Seal

The Agent Boundary Seal records the non-bypassable autonomy boundary for an AI agent handling Origin Trace Receipts.

It defines what the agent must never do, even when it can parse receipts, authorize routes, prepare reviewer notifications, or emit internal handoff receipts.

The layer may define:

- seal ID
- seal status
- autonomy ceiling
- sealed boundary rules
- non-bypassable actions
- escalation policy
- violation response
- seal summary

This layer is designed to prevent:

- payment execution
- market registration
- license publication
- AI training approval
- public origin claims
- external settlement
- external handoff emission
- unredacted payload transmission
- Human Review Gate override
- route authorization override
- boundary seal modification

In v0.5, the agent may read, validate, recommend, prepare safe payloads, emit internal review-oriented handoff receipts, record boundary seals, and escalate violations.

The agent may not execute sensitive actions, emit external execution receipts, bypass review gates, override route authorization, or modify its own boundary.

---

### 10. Action Policy

The Action Policy records what the agent may and may not do.

Allowed actions may include:

- read_receipt
- validate_receipt
- summarize_receipt
- classify_gate_status
- recommend_targets
- emit_handoff_record
- notify_human_reviewer
- create_review_notification
- prepare_safe_payload
- request_human_review
- create_handoff_receipt
- prepare_downstream_receipt
- emit_internal_handoff_receipt
- record_boundary_seal
- check_boundary_seal
- escalate_boundary_violation

Prohibited actions may include:

- execute_payment
- register_market_asset
- publish_license
- approve_training_use
- make_public_origin_claim
- bypass_human_review_gate
- auto_forward_to_external_system
- send_unredacted_private_evidence
- notify_external_system_without_review
- emit_external_handoff_without_review
- emit_receipt_with_unredacted_payload
- modify_boundary_seal
- override_route_authorization
- override_human_review_gate
- emit_external_execution_receipt

---

### 11. Handoff Result

Records what the agent produced.

A result may be:

- recorded
- recommended
- deferred
- blocked
- failed

The result may include emitted record IDs such as:

- the agent handoff record itself
- internal audit handoff receipt
- royalty review receipt
- blocked route receipt
- boundary seal record

---

## First Arc

The first protocol arc is complete at v0.5.

```text
v0.1 = Receipt Intake & Gate Check
v0.2 = Route Authorization
v0.3 = Reviewer Notification
v0.4 = Handoff Receipt Emission
v0.5 = Agent Boundary Seal
```

This arc defines the minimum safe route from receipt consumption to boundary sealing.

---

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
```

---

## Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Validate examples:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Agent Handoff Record
  schema : schemas/agent-handoff-record.schema.json
  example: examples/agent-handoff-record.example.yaml
[ok] agent-handoff-record.example.yaml is valid
```

---

## Version

Current candidate:

```text
v0.5.0-candidate
```

Release title:

```text
v0.5.0-candidate — Agent Boundary Seal
```

---

## Non-Goals

This protocol does not:

- determine legal ownership
- execute royalty payments
- register assets in a market
- publish licenses
- approve AI training use
- make public origin claims
- settle disputes
- replace human legal review
- bypass human governance
- authorize external execution
- allow agents to modify their own boundaries

It records the agent handoff state so that humans and downstream systems can review it safely.

---

## Status

This repository is a candidate standard.

The v0.5 first arc is intended to be stable enough for:

- GitHub validation workflows
- protocol experiments
- AI agent routing tests
- audit pipeline prototypes
- royalty review handoff prototypes
- Origin Trace Receipt integration
- Multi-Wing orchestration integration

---

## License

License to be defined by the repository maintainer.

# Changelog

All notable changes to this project will be documented in this file.

This repository defines the Origin Trace Agent Handoff Protocol, a gate-aware protocol for AI agents consuming Origin Trace Receipts.

---

## [v0.5.0-candidate] - 2026-07-03

### Added

- Added Agent Boundary Seal.
- Added `agent_boundary_seal` as a required top-level layer.
- Added boundary seal ID.
- Added seal status values:
  - draft
  - sealed
  - active
  - superseded
  - revoked
  - not_required
- Added autonomy ceiling values:
  - read_only
  - recommendation_only
  - internal_receipt_emission_only
  - manual_approval_required
  - limited_execution
  - blocked
- Added sealed boundary rules.
- Added boundary rule types:
  - human_review_required
  - external_execution_block
  - payment_execution_block
  - market_registration_block
  - license_publication_block
  - training_approval_block
  - public_origin_claim_block
  - payload_redaction_required
  - boundary_self_modification_block
  - route_override_block
  - other
- Added non-bypassable actions.
- Added escalation policy.
- Added escalation trigger actions.
- Added violation response.
- Added new allowed agent actions:
  - record_boundary_seal
  - check_boundary_seal
  - escalate_boundary_violation
- Added new prohibited agent actions:
  - modify_boundary_seal
  - override_route_authorization
  - override_human_review_gate
  - emit_external_execution_receipt

### Changed

- Updated `schema_version` from `0.4.0` to `0.5.0`.
- Updated the example record to include a sealed agent autonomy boundary.
- Updated action policy to allow boundary checking and escalation while prohibiting review-gate override, route override, external execution emission, and boundary self-modification.
- Closed the first protocol arc from receipt intake to boundary sealing.

### Purpose

v0.5 seals the autonomy boundary of an AI agent consuming Origin Trace Receipts.

The agent may:

- read receipts
- validate receipts
- classify gate status
- recommend targets
- prepare safe reviewer notifications
- prepare downstream handoff receipts
- emit internal review-oriented handoff receipts
- record boundary seals
- check boundary compliance
- escalate boundary violations

The agent may not:

- execute payments
- register market assets
- publish licenses
- approve AI training use
- make public origin claims
- emit external execution receipts
- transmit unredacted private payloads
- override Human Review Gate
- override route authorization
- modify its own boundary seal

This release completes the first arc of the Origin Trace Agent Handoff Protocol.

---

## [v0.4.0-candidate] - 2026-07-03

### Added

- Added Handoff Receipt Emission Layer.
- Added `handoff_receipt_emission` as a required top-level layer.
- Added emission ID.
- Added emission status values:
  - draft
  - prepared
  - emitted
  - deferred
  - blocked
  - not_required
- Added emission modes:
  - record_only
  - recommendation_only
  - manual_emit_required
  - agent_may_emit_internal
  - external_system
  - mixed
- Added emitted receipt records.
- Added emitted receipt types:
  - audit_handoff_receipt
  - review_request_receipt
  - royalty_review_receipt
  - license_review_receipt
  - market_review_receipt
  - archive_receipt
  - blocked_route_receipt
  - other
- Added emission decisions:
  - emit_internal
  - prepare_for_manual_emit
  - defer
  - block
  - not_applicable
- Added payload scope.
- Added included and excluded field tracking.
- Added redaction requirement flag.
- Added review dependency.
- Added emission policy.
- Added new allowed agent actions:
  - create_handoff_receipt
  - prepare_downstream_receipt
  - emit_internal_handoff_receipt
- Added new prohibited agent actions:
  - emit_external_handoff_without_review
  - emit_receipt_with_unredacted_payload

### Changed

- Updated `schema_version` from `0.3.0` to `0.4.0`.
- Updated the example record to prepare downstream handoff receipts for:
  - synchronization audit
  - royalty review
  - blocked market registration
- Updated action policy to allow safe internal handoff receipt preparation while blocking unsafe external emission.

### Purpose

v0.4 ensures that agent handoff decisions can be emitted as structured downstream receipts.

v0.1 allowed receipt intake and gate checking.  
v0.2 added route authorization.  
v0.3 added reviewer notification.  
v0.4 adds handoff receipt emission.

The agent may prepare safe internal or review-oriented handoff receipts.

The agent may not emit:

- external handoff receipts
- execution receipts
- payment receipts
- market registration receipts
- license publication receipts
- unredacted payload receipts

unless the required Human Review Gate and route authorization conditions are satisfied.

---

## [v0.3.0-candidate] - 2026-07-03

### Added

- Added Reviewer Notification Layer.
- Added `reviewer_notification` as a required top-level layer.
- Added notification ID.
- Added notification status values:
  - draft
  - prepared
  - queued
  - sent
  - deferred
  - blocked
  - not_required
- Added notification modes:
  - record_only
  - recommendation_only
  - manual_send_required
  - agent_may_notify
  - external_system
  - mixed
- Added review requests.
- Added reviewer roles.
- Added review reasons.
- Added notification priority.
- Added related route references.
- Added related blocking condition references.
- Added requested reviewer decisions.
- Added notification channel classification.
- Added safe notification payload.
- Added blocked payload item classification.
- Added review request status.
- Added new allowed agent actions:
  - create_review_notification
  - prepare_safe_payload
  - request_human_review
- Added new prohibited agent actions:
  - send_unredacted_private_evidence
  - notify_external_system_without_review

### Changed

- Updated `schema_version` from `0.2.0` to `0.3.0`.
- Updated the example record to prepare reviewer notifications for:
  - market registration review
  - license policy review
  - royalty execution review
- Updated action policy to allow safe notification preparation while blocking sensitive automatic notification behavior.

### Purpose

v0.3 ensures that blocked or conditional routes do not simply disappear.

The agent can prepare safe reviewer notifications explaining:

- why review is needed
- which routes are affected
- which blocking conditions are relevant
- what decision is requested
- which payload items must not be included

This release keeps the protocol conservative.

The agent may prepare review notifications and request human review.

The agent may not send private, unredacted, sensitive, or externally actionable payloads without review.

---

## [v0.2.0-candidate] - 2026-07-03

### Added

- Added Route Authorization Layer.
- Added `route_authorization` as a required top-level layer.
- Added route authorization ID.
- Added authorization status values:
  - draft
  - candidate_only
  - partially_authorized
  - authorized
  - blocked
  - requires_human_review
- Added authorization modes:
  - record_only
  - recommendation_only
  - manual_approval_required
  - gate_pass_required
  - mixed
- Added authorization records for candidate downstream routes.
- Added route-level authorization decisions:
  - authorized
  - conditionally_authorized
  - manual_review_required
  - blocked
  - not_applicable
- Added Human Review Gate dependency for each route.
- Added permitted route actions.
- Added blocked route actions.
- Added route authorization conditions.
- Added route authorization rationale.

### Changed

- Updated `schema_version` from `0.1.0` to `0.2.0`.
- Updated the example record to show:
  - audit routing
  - royalty review routing
  - market registration blocking
  - license publication blocking
- Updated the protocol concept from simple candidate routing to gate-aware route authorization.

### Purpose

v0.2 prevents AI agents from treating all downstream routing targets as equally executable.

The agent may route or recommend safe review-oriented paths, such as synchronization audit or royalty review.

The agent must block sensitive routes such as:

- market registration
- license publication
- royalty execution
- external settlement
- public origin claims
- AI training approval
- autonomous external handoff

until the required Human Review Gate conditions are satisfied.

---

## [v0.1.0-candidate] - 2026-07-03

### Added

- Added initial Agent Handoff Record schema.
- Added `schemas/agent-handoff-record.schema.json`.
- Added `examples/agent-handoff-record.example.yaml`.
- Added validation script.
- Added GitHub Actions validation workflow.
- Added source receipt layer.
- Added agent context layer.
- Added receipt intake layer.
- Added Human Review Gate check layer.
- Added routing layer.
- Added action policy layer.
- Added handoff result layer.

### Initial Record Layers

v0.1 introduced the following layers:

- `source_receipt`
- `agent_context`
- `intake`
- `gate_check`
- `routing`
- `action_policy`
- `handoff_result`
- `validation`

### Purpose

v0.1 established the basic gate-aware handoff record for AI agents consuming Origin Trace Receipts.

The first version allowed an agent to:

- read a source receipt
- identify the receipt version and reference
- classify its own role and autonomy level
- detect receipt layers
- check Human Review Gate status
- identify permitted and blocked actions
- recommend candidate downstream targets
- emit a handoff record

The first version did not allow sensitive execution.

The agent could inspect, classify, recommend, and record.

The agent could not:

- execute payments
- register market assets
- publish licenses
- approve training use
- make public origin claims
- bypass Human Review Gate
- automatically forward to external systems

---

## First Arc Summary

The first protocol arc is complete at v0.5.

```text
v0.1 = Receipt Intake & Gate Check
v0.2 = Route Authorization
v0.3 = Reviewer Notification
v0.4 = Handoff Receipt Emission
v0.5 = Agent Boundary Seal

# Changelog

All notable changes to this project will be documented in this file.

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

The agent can now prepare safe reviewer notifications explaining why review is needed, which routes are affected, what decision is requested, and which payload items must not be included.

This release keeps the protocol conservative.  
The agent may prepare review notifications and request human review.  
The agent may not send private, unredacted, sensitive, or externally actionable payloads without review.

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
- Updated the example record to show audit routing, royalty review routing, market registration blocking, and license publication blocking.
- Updated the protocol concept from simple candidate routing to gate-aware route authorization.

### Purpose

v0.2 prevents AI agents from treating all downstream routing targets as equally executable.

The agent may route or recommend safe review-oriented paths, such as synchronization audit or royalty review.  
The agent must block sensitive routes such as market registration, license publication, royalty execution, external settlement, public origin claims, or autonomous external handoff until the required Human Review Gate conditions are satisfied.

## [v0.1.0-candidate] - 2026-07-03

### Added

- Initial Agent Handoff Record schema.
- Added source receipt layer.
- Added agent context layer.
- Added receipt intake layer.
- Added Human Review Gate check layer.
- Added routing layer for downstream protocols.
- Added action policy layer.
- Added handoff result layer.
- Added YAML example.
- Added validation script.
- Added GitHub Actions validation workflow.

### Purpose

v0.1 defines the Receipt Intake & Gate Check Layer.

This release allows an AI agent to consume an Origin Trace Receipt, inspect its Human Review Gate, classify allowed and blocked actions, and record a safe handoff recommendation.

The agent does not execute sensitive downstream actions in this version.

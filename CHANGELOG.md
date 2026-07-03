# Changelog

All notable changes to this project will be documented in this file.

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

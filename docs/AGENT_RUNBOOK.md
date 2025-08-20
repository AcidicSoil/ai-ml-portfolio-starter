# Agent Runbook
Loop: Clarify → Plan → Scaffold → Implement → Validate → Test → Document → Commit → Review → Close.
- Entry: Spec + AC ready. Exit: DoD satisfied.
- All writes via unified diff; apply with `tools/diff_apply.py`.
- Guardrails: path allowlist, CI gates (lint/type/test/security).
- Artefacts: plan.json, patch.diff, review.json, test reports.

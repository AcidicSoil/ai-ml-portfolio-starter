"""Tiny deterministic workflow state machine.

Demonstrates validated transitions and simple state handling.
"""
from __future__ import annotations

from enum import Enum


class State(str, Enum):
    STARTED = "STARTED"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    FAILED = "FAILED"


class Workflow:
    """Workflow with allowed transitions and guardrails."""

    _ALLOWED = {
        State.STARTED: {State.PROCESSING, State.FAILED},
        State.PROCESSING: {State.DONE, State.FAILED},
        State.DONE: set(),
        State.FAILED: set(),
    }

    def __init__(self) -> None:
        self.state: State = State.STARTED

    def transition(self, to: State) -> State:
        if to not in self._ALLOWED[self.state]:
            raise ValueError(f"Invalid transition: {self.state} -> {to}")
        self.state = to
        return self.state


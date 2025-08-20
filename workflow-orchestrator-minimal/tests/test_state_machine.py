import pathlib
import sys


def test_state_machine_transitions():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    from workflow_orchestrator_minimal.state_machine import (  # type: ignore
        State,
        Workflow,
    )

    wf = Workflow()
    assert wf.state == State.STARTED
    wf.transition(State.PROCESSING)
    assert wf.state == State.PROCESSING
    wf.transition(State.DONE)
    assert wf.state == State.DONE


def test_invalid_transition_raises():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    from workflow_orchestrator_minimal.state_machine import (  # type: ignore
        State,
        Workflow,
    )

    wf = Workflow()
    try:
        wf.transition(State.DONE)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import auto_agent_transcript_cost_waste_analyzer


def test_version_is_set() -> None:
    assert auto_agent_transcript_cost_waste_analyzer.__version__

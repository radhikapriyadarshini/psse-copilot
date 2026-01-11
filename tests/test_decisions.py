import unittest

from agent.decisions import (
    decide_disturbance_type,
    decide_study_configuration
)


class TestDecisionLogic(unittest.TestCase):

    def test_transient_stability_goal_selects_three_phase_fault(self):
        goal = "Assess transient stability of IEEE 9-bus system"
        fault = decide_disturbance_type(goal)
        self.assertEqual(fault, "3-phase fault")

    def test_non_stability_goal_defaults_to_single_phase(self):
        goal = "Voltage profile assessment"
        fault = decide_disturbance_type(goal)
        self.assertEqual(fault, "single-phase fault")

    def test_study_configuration_contains_required_keys(self):
        goal = "Assess transient stability of IEEE 9-bus system"
        context = {"focus": "generator buses"}

        config = decide_study_configuration(goal, context)

        required_keys = [
            "disturbance",
            "fault_locations",
            "clearing_time",
            "channels",
            "simulation_time",
            "evaluation_criteria"
        ]

        for key in required_keys:
            self.assertIn(key, config)

    def test_fault_location_comes_from_context(self):
        goal = "Assess transient stability"
        context = {"focus": "load buses"}

        config = decide_study_configuration(goal, context)

        self.assertEqual(config["fault_locations"], "load buses")

    def test_default_channels_are_present(self):
        goal = "General study"
        context = {}

        config = decide_study_configuration(goal, context)

        self.assertTrue(len(config["channels"]) > 0)


if __name__ == "__main__":
    unittest.main()

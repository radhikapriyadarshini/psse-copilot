def decide_study_configuration(study_goal, context):

    return {
        "disturbance": decide_disturbance_type(study_goal),
        "fault_locations": context.get("focus", "critical buses"),
        "clearing_time": "nominal",
        "channels": ["rotor_angle", "bus_voltage"],
        "simulation_time": 5.0,
        "evaluation_criteria": "Rotor angle separation < 180°"
    }


def decide_disturbance_type(study_goal):
    if "stability" in study_goal.lower():
        return "3-phase fault"
    return "single-phase fault"

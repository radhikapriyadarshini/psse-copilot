def generate_report(study_config):

    return f"""
## Transient Stability Study Report

Objective:
Assess system behavior under a {study_config['disturbance']}.

Assumptions:
- Power flow solved
- Models validated

Study Setup:
- Fault locations: {study_config['fault_locations']}
- Simulation time: {study_config['simulation_time']} s
- Channels: {', '.join(study_config['channels'])}

Evaluation Criteria:
{study_config['evaluation_criteria']}
""".strip()

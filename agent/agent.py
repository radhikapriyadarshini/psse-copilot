from agent.decisions import decide_study_configuration
from agent.report_builder import generate_report
from agent.ai_assist import polish_report_if_enabled


def run_agent(study_goal, context, ai_enabled=False):
    study_config = decide_study_configuration(study_goal, context)

    psse_script = f"# PSSE script for {study_config['disturbance']} fault"

    report = generate_report(study_config)

    if ai_enabled:
        report = polish_report_if_enabled(report, study_config)

    save_outputs(psse_script, report, study_config)

    return study_config


def save_outputs(psse_script, report, study_config):
    with open("outputs/ts_main_script.py", "w") as f:
        f.write(psse_script)

    with open("outputs/study_report.md", "w") as f:
        f.write(report)

    with open("outputs/metadata.txt", "w") as f:
        for k, v in study_config.items():
            f.write(f"{k}: {v}\n")

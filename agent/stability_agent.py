import os

from datetime import datetime
from pathlib import Path
from agent.prompts import STABILITY_AGENT_PROMPT

OUTPUT_DIR = Path("outputs")

def run_stability_agent(fault_bus, fault_type, clear_time):
    """
    Generates a PSSE transient stability study setup
    and saves outputs to files
    """
    print("DEBUG: Current working directory =", os.getcwd())
    OUTPUT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    psse_script = f"""
import psspy
import redirect

redirect.psse2py()
psspy.psseinit(20000)

# Load case (user to modify)
psspy.case("network.sav")
psspy.dyre_new([1,1,1,1], "network.dyr", "", "", "")

# Channel setup
psspy.delete_all_plot_channels()
psspy.chsb(0, 1, [-1, -1, -1, 1, 13, 0])  # Rotor angle
psspy.chsb(0, 1, [-1, -1, -1, 1, 7, 0])   # Bus voltage

# Start simulation
psspy.strt(0, "output.out")

# Apply fault
psspy.dist_bus_fault({fault_bus}, 3, 0.0, [0.0, 0.0])

# Clear fault
psspy.run(0, {clear_time}, 1, 1, 0)
psspy.dist_clear_fault(1)

# Run post-fault
psspy.run(0, 5.0, 1, 1, 0)
""".strip()

    report_text = f"""
## Transient Stability Study Report

**Study Objective**  
Perform transient stability analysis for a {fault_type} fault at Bus {fault_bus}
to assess rotor angle and voltage stability.

**Assumptions**
- Power flow solved prior to dynamic simulation
- Dynamic models properly assigned
- Simulation time step: 0.01 s
- Fault clearing time: {clear_time} s

**Evaluation Criteria**
- Rotor angle separation < 180°
- Post-fault voltage recovery acceptable

**Engineering Notes**
- If instability observed, reduce clearing time or add controls
""".strip()

    # Save files
    (OUTPUT_DIR / "ts_main_script.py").write_text(psse_script)
    (OUTPUT_DIR / "study_report.md").write_text(report_text)
    (OUTPUT_DIR / "metadata.txt").write_text(
        f"Generated on: {timestamp}\n"
        f"Fault bus: {fault_bus}\n"
        f"Fault type: {fault_type}\n"
        f"Clearing time: {clear_time}s\n"
    )

    return "✅ Outputs saved to 'outputs/' directory"

from agent.stability_agent import run_stability_agent

def main():
    print("\nPSSE Copilot – Transient Stability Agent\n")

    fault_bus = input("Enter fault bus number: ")
    fault_type = input("Enter fault type (3ph / ll / lg): ")
    clear_time = input("Enter fault clearing time (s): ")

    result = run_stability_agent(
    fault_bus=fault_bus,
    fault_type=fault_type,
    clear_time=clear_time
    )

    print("\n" + result)


if __name__ == "__main__":
    main()

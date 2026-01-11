from agent.agent import run_agent


if __name__ == "__main__":
    study_goal = input("Enter study goal: ")

    context = {
        "intent": "planning",
        "focus": "generator buses"
    }

    config = run_agent(study_goal, context)

    print("\nAgent decided study configuration:\n")
    for k, v in config.items():
        print(f"{k}: {v}")

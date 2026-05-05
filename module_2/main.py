from agents.runner import run_agent

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        result = run_agent(user_input)
        print("Agent:", result)
from interpreter import execute_code

def main():
    print("AI Interpreter is running...")
    print("Type your command:")

    while True:
        user_input = input("> ")

        if user_input.lower() in ["exit", "quit"]:
            print("Shutting down...")
            break

        result = execute_code(user_input)
        print(result)

if __name__ == "__main__":
    main()

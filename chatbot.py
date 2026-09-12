"""
Project: Rule-Based AI Chatbot
Description: A simple beginner-friendly rule-based AI chatbot using core Python concepts.
Key Concepts: Variables, input/print, string manipulation (.lower(), .strip()), if-elif-else, while loop.
"""

def start_chatbot():
    # 8. Display a welcome message when the chatbot starts
    print("=" * 50)
    print("🤖 Welcome to the Rule-Based AI Chatbot!")
    print("Ask me basic questions or say hello.")
    print("Type 'bye', 'exit', or 'quit' anytime to end our conversation.")
    print("=" * 50)
    print()

    # 5. Run the chatbot inside a continuous loop
    while True:
        # Get input from the user
        user_input = input("You: ")

        # 6. Convert user input to lowercase and remove unnecessary leading/trailing spaces
        cleaned_input = user_input.lower().strip()

        # 3. The chatbot handles exit commands
        if cleaned_input in ["bye", "exit", "quit", "goodbye"]:
            # 8. Display a goodbye message when the user exits
            print("Chatbot: Goodbye! It was nice chatting with you. Have a great day!")
            break

        # If user pressed enter without typing anything
        elif cleaned_input == "":
            print("Chatbot: You didn't say anything! Please type a message.")

        # 1. The chatbot handles common greetings
        elif cleaned_input in ["hello", "hi", "hey", "good morning", "good evening"]:
            print("Chatbot: Hello! Nice to meet you. How can I help you today?")

        # 2. The chatbot handles basic questions
        elif cleaned_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm doing well, thank you for asking! How are you?")

        elif cleaned_input in ["what is your name", "what is your name?", "what's your name", "what's your name?"]:
            print("Chatbot: My name is PyBot! I am a simple rule-based AI chatbot.")

        elif cleaned_input in ["what can you do", "what can you do?"]:
            print("Chatbot: I can greet you, answer basic questions, and demonstrate rule-based if-else decision making!")

        elif cleaned_input in ["who created you", "who created you?"]:
            print("Chatbot: I was created by a student using basic Python programming concepts!")

        # 7. Default response if the message is unknown
        else:
            print("Chatbot: Sorry, I don't understand that. Try asking 'What can you do?' or 'What is your name?'.")

        print()  # Empty line for clean spacing between interactions

if __name__ == "__main__":
    start_chatbot()

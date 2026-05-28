def get_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        "hello": "Hello! How can I help you?",
        "hi": "Hey there! Nice to meet you.",
        "how are you": "I'm fine, thanks! How about you?",
        "what is your name": "I'm a simple Python chatbot!",
        "what can you do": "I can respond to basic messages. Try saying hello or how are you!",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "thank you": "Happy to help!",
        "good morning": "Good morning! Hope you have a great day.",
        "good night": "Good night! Take care.",
        "who made you": "I was built using Python!",
        "help": "You can say hello, ask how I am, or say bye.",
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return f"I don't understand '{user_input}' yet. Try saying hello, how are you, or bye."


def chatbot():
    print("Chatbot is running! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if "bye" in user_input.lower():
            break


chatbot()
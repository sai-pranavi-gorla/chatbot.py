# Rule-Based Chatbot using Dictionary

print("Chatbot: Hello! I am your chatbot.")
print("Type 'bye' to exit.\n")

# Dictionary of responses
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there!",
    "how are you": "I am fine, thank you!",
    "what is your name": "My name is Python Chatbot.",
    "what can you do": "I can answer simple questions.",
    "who created you": "I was created using Python."
}

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    elif user in responses:
        print("Chatbot:", responses[user])

    else:
        print("Chatbot: Sorry, I don't understand that.")

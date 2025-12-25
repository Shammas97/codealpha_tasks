"""A smarter rule-based chatbot for console interaction."""

import string
from difflib import get_close_matches

# Define responses with multiple triggers per response
RESPONSES = {
    ("hello", "hi", "hey"): "Hi! 👋",
    ("how are you", "how are you?"): "I'm fine, thanks! How can I help?",
    ("what's your name", "whats your name", "who are you"): "I'm CodeAlpha Bot (a simple rule-based bot).",
    ("bye", "goodbye", "see you"): "Goodbye! Have a nice day.",
    ("help",): "Try: hello, how are you, what's your name, bye"
}

def normalize(text):
    """Convert text to lowercase and remove punctuation."""
    return text.strip().lower().translate(str.maketrans("", "", string.punctuation))

def get_reply(user_input):
    """Find a matching response or return default."""
    for triggers, response in RESPONSES.items():
        # Exact match or close match for minor typos
        match = get_close_matches(user_input, triggers, n=1, cutoff=0.6)
        if match:
            return response
    return "Sorry, I don't understand that. Try 'help'."

def chat():
    print("Welcome to the Smarter Chatbot. Type 'exit' to quit.")
    while True:
        user = input("You: ")
        if normalize(user) == "exit":
            print("Bot: Bye!")
            break
        reply = get_reply(normalize(user))
        print("Bot:", reply)

if __name__ == "__main__":
    chat()

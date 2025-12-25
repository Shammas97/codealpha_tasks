# Smarter Rule-Based Chatbot

A simple, console-based chatbot with typo tolerance and multiple trigger support. Built in Python, this chatbot responds to predefined commands and can suggest close matches for minor typos.

---

## Features

- **Multiple triggers per response**: Handles different ways of asking the same thing.
- **Typo tolerance**: Uses `difflib.get_close_matches` to detect and respond to near-miss inputs.
- **Easy to extend**: Add new responses and triggers in the `RESPONSES` dictionary.
- **Help command**: Provides users with guidance on available commands.
- **Exit command**: Type `exit` to quit the chatbot

## Usage


- You: hello
Bot: Hi! 👋

You: hw are you
Bot: I'm fine, thanks! How can I help? (Did you mean 'how are you'? 😉)

You: what's your name
Bot: I'm CodeAlpha Bot (a simple rule-based bot).

You: exit
Bot: Bye!

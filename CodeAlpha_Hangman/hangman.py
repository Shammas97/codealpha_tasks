import random
import sys

# Predefined word list
WORDS = ["python", "hangman", "codealpha", "intern", "developer"]

def play_hangman():
    word = random.choice(WORDS).lower()
    guessed = set()
    wrong = set()
    max_wrong = 6

    hint_used = False

    print("🎮 Welcome to Hangman (Smart Hint Edition)")

    while True:
        # Display current word state
        display = " ".join([c if c in guessed else "_" for c in word])
        print("\nWord:", display)
        print(f"Wrong guesses ({len(wrong)}/{max_wrong}):", " ".join(sorted(wrong)))

        # Win condition
        if all(c in guessed for c in word):
            print("🎉 You won! The word was:", word.upper())
            break

        # Lose condition
        if len(wrong) >= max_wrong:
            print("💀 You lost. The word was:", word.upper())
            break

        # User input
        guess = input("Guess a letter (or type 'quit'): ").strip().lower()

        if guess == "quit":
            print("Goodbye!")
            sys.exit(0)

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed or guess in wrong:
            print("⚠️ You already tried that letter.")
            continue

        # Guess checking
        if guess in word:
            guessed.add(guess)
            print("✅ Correct guess!")
        else:
            wrong.add(guess)
            print("❌ Wrong guess!")

        # Smart Hint Feature (after 3 wrong guesses)
        if len(wrong) == 3 and not hint_used:
            hint_letter = random.choice([c for c in word if c not in guessed])
            guessed.add(hint_letter)
            hint_used = True
            print(f"💡 Hint unlocked! Letter revealed: {hint_letter.upper()}")

if __name__ == "__main__":
    play_hangman()

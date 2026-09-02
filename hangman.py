
import random

# Predefined words
words = ["python", "computer", "coding", "program", "security"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_attempts = 6
wrong_guesses = 0

# Hidden word
display_word = ["_"] * len(word)

print("=" * 40)
print("          🎮 HANGMAN GAME")
print("=" * 40)
print("Guess the hidden word one letter at a time!")
print("You have 6 incorrect guesses.")
print("=" * 40)

while wrong_guesses < max_attempts and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in word:
        print("✅ Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

# Final result
print("\n" + "=" * 40)

if "_" not in display_word:
    print("🎉 CONGRATULATIONS! YOU WON!")
    print("The word was:", word)
else:
    print("😢 GAME OVER!")
    print("The word was:", word)

print("=" * 40)
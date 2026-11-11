import random

print("===== WELCOME TO HANGMAN GAME =====")

# List of words
words = ["python", "computer", "program",
    "student", "database", "keyboard",
    "internet", "software", "developer",
    "college", "coding", "technology"]

# Select a random word
word = random.choice(words)

# Create an empty set for guessed letters
guessed_letters = set()

# Maximum attempts
attempts = 6

# Game loop
while attempts > 0:

    # Display current word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Remaining attempts:", attempts)

    # Check if word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        break

    # Take input from user
    guess = input("Guess a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    # Check repeated letters
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    # Add guessed letter to set
    guessed_letters.add(guess)

    # Check guessed letter
    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

# Check game result
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)

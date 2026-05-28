import random

words = ["python", "hangman", "coding", "laptop", "keyboard"]

def display(guessed, word, wrong, attempts):
    print(f"\nWord: {' '.join(c if c in guessed else '_' for c in word)}")
    print(f"Wrong guesses: {', '.join(wrong)}")
    print(f"Attempts left: {attempts}")

def hangman():
    word = random.choice(words)
    guessed = set()
    wrong = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        display(guessed, word, wrong, attempts)

        if all(c in guessed for c in word):
            print(f"\n🎉 You won! The word was: {word}")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed or guess in wrong:
            print("Already guessed that letter.")
        elif guess in word:
            guessed.add(guess)
            print("Correct!")
        else:
            wrong.append(guess)
            attempts -= 1
            print("Wrong!")

    print(f"\n💀 Game over! The word was: {word}")

hangman()
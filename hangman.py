import random

def get_word():
    words = ["python", "developer", "programming", "computer", "algorithm", "variable", "function", "software"]
    return random.choice(words)

def play_hangman():
    word = get_word()
    word_letters = set(word)
    guessed_letters = set()
    lives = 6

    print("========================================")
    print("      WELCOME TO HANGMAN GAME!          ")
    print("========================================")

    while len(word_letters) > 0 and lives > 0:
        # Display current progress
        print(f"\nYou have {lives} lives left.")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        word_list = [letter if letter in guessed_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").lower()

        if user_letter.isalpha() and len(user_letter) == 1:
            if user_letter in guessed_letters:
                print("You already guessed that letter. Try another one.")
            elif user_letter in word_letters:
                word_letters.remove(user_letter)
                guessed_letters.add(user_letter)
                print(f"Good job! '{user_letter}' is in the word.")
            else:
                guessed_letters.add(user_letter)
                lives -= 1
                print(f"Sorry, '{user_letter}' is not in the word.")
        else:
            print("Invalid input. Please enter a single alphabetical letter.")

    # Game conclusion
    if lives == 0:
        print(f"\nGame Over! The word was '{word}'. Better luck next time!")
    else:
        print(f"\nCongratulations! You guessed the word '{word}' successfully!")

if __name__ == "__main__":
    play_hangman()

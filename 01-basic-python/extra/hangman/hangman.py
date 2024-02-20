import random


def read_word_list(file_name):
    with open(file_name) as word_list:
        return [word.strip() for word in word_list.readlines()]


def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)


def main():
    max_attempts = 6
    guessed_letters = []
    word_list = read_word_list("hangman.txt")
    secret_word = random.choice(word_list).upper()

    print("Welcome to Hangman!")
    print("The word has", len(secret_word), "letters.")

    attempts = 0
    while attempts < max_attempts:
        print("\nWord:", display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations! You've guessed the word:", secret_word)
                break
        else:
            print("Incorrect guess.")
            attempts += 1
            print("Attempts left:", max_attempts - attempts)

    else:
        print("You're out of attempts! The word was:", secret_word)


if __name__ == "__main__":
    main()

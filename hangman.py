import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(words)  # what the user has guesssed
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have ", lives,
              " try left and you have used these letters: ", " ".join(used_letter))

        # what  current word is (ie W - R D)
        word_list = [
            letter if letter in used_letter else "-" for letter in word]
        print("Cureent word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1  # takes away lives if wrong
                print("Letter is not in word.")

        elif user_letter in used_letter:
            print("You have already used that character.Please try again.")
        else:
            print("Invalid character.Please try again.")
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You won king")


user_input = input("Type something: ")
print(user_input)

hangman()

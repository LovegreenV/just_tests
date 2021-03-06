from words import words

import random
import string


def get_word(words):
    word = random.choice(words).upper()
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()

    return word


def hangman():
    word = get_word(words)
    word_letters = set(word)

    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    correct = list()
    lives = 6

    # Get input
    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters:', ' '.join(used_letters))

        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", " ".join(word_list))

        user_letter = input('Guess a Letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word, Lives left: ', lives)

        elif user_letter in used_letters:
            print("you've already guessed that or its wrong")
    if lives == 0:
        print('You ran out of lives')
    else:
        print('The correct word was', word)


hangman()

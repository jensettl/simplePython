""" Checks for dashes and spaces in a word

Args:
    words (array[string]): List of words

Returns:
    string: Valid word from list
"""

import random
import string

def get_valid_word(words):
  word = words[random.randint(0, len(words))].upper() # randomly chooses word from the list
  while '-' in word or ' ' in word or 'ä' in word or 'ö' in word or 'ü' in word:
    word = random.choice(words).upper()

  return word

def hangman():
  match int(input("Select Language: DE(1), EN (2)\n")):
    case 1:
      from data.wordlist_DE import words
    case 2:
      from data.wordlist_EN import words
    case _:
      print("Invalid input")

  word = get_valid_word(words)
  word_letters = set(word)  # letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set()  # what the user has guessed

  lives = 7

  # getting user input
  while len(word_letters) > 0 and lives > 0:
      # letters used
      # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
      print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

      # what current word is (ie W - R D)
      word_list = [letter if letter in used_letters else '-' for letter in word]
      print('Current word: ', ' '.join(word_list))

      user_letter = input('Guess a letter: ')[0].upper()
      if user_letter in alphabet - used_letters:
          used_letters.add(user_letter)
          if user_letter in word_letters:
              word_letters.remove(user_letter)
              print('')

          else:
              lives = lives - 1  # takes away a life if wrong
              print('\nYour letter,', user_letter, 'is not in the word.')

      elif user_letter in used_letters:
          print('\nYou have already used that letter. Guess another letter.')

      else:
          print('\nThat is not a valid letter.')

  # gets here when len(word_letters) == 0 OR when lives == 0
  if lives == 0:
      print('You died, sorry. The word was', word)
  else:
      print('YAY! You guessed the word', word, '!!')


hangman()

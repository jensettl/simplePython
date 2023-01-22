import random

def get_valid_word(words):
  word = words[random.randint(0, len(words))] # randomly chooses word from the list
  while '-' in word or ' ' in word or 'ä' in word or 'ö' in word or 'ü' in word or len(word) != 5: 
    word = random.choice(words)

  return word.upper()

def wordle():
  # get random word from list
  from data.wordlist_DE import words
  word =  get_valid_word(words)
  word_letters = list(word)
  feedback_array = ['0','0','0','0','0']
  user_word = ''

  print(word)

  while word != user_word:
    user_word = input('Guess a word: ')
    user_word_letters = list(user_word)

    if len(user_word) == 5:
      for idx, letter in enumerate(user_word_letters):
        if word_letters[idx] == letter:
          feedback_array[idx] = 2
        elif letter in word:
          feedback_array[idx] = 1

      print(feedback_array) 
    else:
      print("Your word has to be 5 letters long! Try again.")
  
  print(f"Congratulations. The word was {word.capitalize()}")

wordle()
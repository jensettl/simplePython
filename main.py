from rock_paper_scissors import play as rps
from guessNumber import user_guess, computer_guess

if __name__ == '__main__':
  game = int(input("Choose the game to play \
        \n 1: Guess Number (computer) \
        \n 2: Guess Number (user) \
        \n 3: Rock Paper Scisscors \
        \n Your Choice: "))

  # Available since Python version 3.10
  match game:
    case 1:
      user_guess(50)
    case 2:
      computer_guess(50)
    case 3:
      print(rps())
    case _:
      print("Invalid number, try again.")
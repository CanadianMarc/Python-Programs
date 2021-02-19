# Marc F.
# 02/09/2021
# Number Guess: Computer generates a random number from 1 to 10, you gotta guess it!
...
# Input
import random
number = random.randint(0, 10)

# Loop to ensure that the guess is a valid integer.
while True:
  try:
    guess = int(input("Please input your guess, from 0-10!\n"))
    break
  except ValueError:
    print("Uh oh, you didn't enter a valid number! Try again!")

# Check if the human got it wrong, if so, give a clue and have them guess again.
while guess != number:
    if number > guess:
      print("Your number was too low! Guess Again!")
    else:
      print("Your number was too high! Guess again!")
    guess = int(input())

# Output
if guess == number:
  print("Congratz! You did it! Your prize is pineapples and a virtual hug!")
  
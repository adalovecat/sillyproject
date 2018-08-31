
import random

print ("Hey there! Lets play a game. I'll think a number between 1 and 10. You have 3 tries to guess it")
number = random.randint (1, 10)
guess = int (input ())
tries = 1

while guess is not number and tries < 3:
    tries = tries + 1

    if guess < number:
        print ("Too low! Try again")
    elif guess > number:
        print ("Too high! Try again")

    guess = int (input ())

if tries >=3:
    print ("You loose :(")
else:
    print ("Yey! You win")

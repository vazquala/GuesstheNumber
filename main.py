import random
from random import randint

random_num = random.randint(1, 10)

while True:
    print("Guess the number (between 1 and 10): ")
    guess = int(input())

    if guess > random_num:
        print("Too high!, Try again.")
    elif guess < random_num:
        print("Too low!, Try again.")
    else:
        print("Congratulations! You've guessed the number.")
        break
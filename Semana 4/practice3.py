import random

random_number = random.randint(1,10)

input_number = 0
while (input_number != random_number):
    input_number = int(input("Guess a number from 1 to 10: "))
    if input_number == random_number:
        print("You Win!")
    else:
        print("Try again!")

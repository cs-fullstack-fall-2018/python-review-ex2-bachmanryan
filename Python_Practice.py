import random

randomNumber = random.randint(0, 9)

while True:
    ranNumber = int(input("Enter your guess: "))
    print(ranNumber)
    if ranNumber == randomNumber:
        break

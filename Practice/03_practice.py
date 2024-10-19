# Problem 1: Even or Odd =>
'''
while True:
    user = int(input("Enter the number: "))

    if (user % 2 == 0):
        print("This is Even number")
    else:
        print("This is Odd number")
'''

# Problem 2: Number Guessing Game =>
'''
import random

hidden_number = random.randint(1, 10)

while True:
    print(hidden_number)
    guess_the_number = int(input("Enter the number: "))

    if (guess_the_number < hidden_number):
        print("This number is too low. Try again.")
    elif (guess_the_number > hidden_number):
        print("This number is too high. Try again.")
    else:
        print("Number is equal to the hidden number.")
        break
'''
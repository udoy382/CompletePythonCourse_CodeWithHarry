import random

'''
1 - for snake
-1 - for water
0 - for gun
'''

values = [-1, 0, 1]
computer = random.choice(values)
youStr = input("Enter your choice: ").lower()

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

you = youDict[youStr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("It's a draw!")
else:
    if (computer == -1 and you == 1):
        print("You win!")

    elif (computer == -1 and you == 0):
        print("You Lose!")

    elif (computer == 1 and you == -1):
        print("You Lose!")

    elif (computer == 1 and you == 0):
        print("You Win!")

    elif (computer == 0 and you == -1):
        print("You Win!")

    elif (computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")
import random

def game():
    print("You are playing the game!")
    score = random.randint(1, 62)

    # Fetch the hiscore
    with open("Chapter9/PracticeSet/hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score: {score}")
    if (score > hiscore or hiscore == ""):
        # Write this hiscore to the file
        with open("Chapter9/PracticeSet/hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
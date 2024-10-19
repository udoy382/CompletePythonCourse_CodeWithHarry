with open("Chapter9/PracticeSet/poem.txt", "r") as f:
    content = f.read()
    if ("Twinkle" in content):
        print("The word `Twinkle` is present in the content.")
    else:
        print("The word `Twinkle` is not present in the content.")
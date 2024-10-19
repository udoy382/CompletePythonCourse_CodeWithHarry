with open("Chapter9/PracticeSet/old.txt", "r") as f:
    content = f.read()

with open("Chapter9/PracticeSet/new.txt", "w") as f:
    f.write(content)
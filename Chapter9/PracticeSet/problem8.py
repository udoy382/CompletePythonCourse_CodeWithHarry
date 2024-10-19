with open("Chapter9/PracticeSet/this.txt", "r") as f:
    content = f.read()

with open("Chapter9/PracticeSet/this_copy.txt", "w") as f:
    f.write(content)
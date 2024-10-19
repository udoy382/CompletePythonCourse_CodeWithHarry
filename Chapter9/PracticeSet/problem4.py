word = "Donkey"

with open("Chapter9/PracticeSet/problem4_file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("Chapter9/PracticeSet/problem4_file.txt", "w") as f:
    content = f.write(contentNew)
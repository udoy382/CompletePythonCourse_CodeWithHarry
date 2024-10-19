words = ["Donkey", "bad", "ganda"]

with open("Chapter9/PracticeSet/problem5_file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("Chapter9/PracticeSet/problem5_file.txt", "w") as f:
    f.write(content)
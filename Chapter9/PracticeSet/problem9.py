with open("Chapter9/PracticeSet/this.txt", "r") as f:
    content1 = f.read()

with open("Chapter9/PracticeSet/this_copy.txt", "r") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes, these files are indentical")
else:
    print("No, these files are not indentical")
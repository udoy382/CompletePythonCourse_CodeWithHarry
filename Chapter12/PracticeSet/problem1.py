try:
    with open("Chapter12/PracticeSet/one.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("Chapter12/PracticeSet/two.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("Chapter12/PracticeSet/tree.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thanks")
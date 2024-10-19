with open("Chapter9/PracticeSet/log.txt", "r") as f:
    content = f.read()


if ("Python" or "python" in content):
    print("Yes, python or Python is present.")
else:
    print("No, python or Python is not present.")
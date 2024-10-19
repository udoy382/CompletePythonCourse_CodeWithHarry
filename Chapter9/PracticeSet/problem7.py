with open("Chapter9/PracticeSet/log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Yes, python or Python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No, python or Python is not present.") 
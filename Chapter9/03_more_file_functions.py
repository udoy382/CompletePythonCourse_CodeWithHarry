f = open("Chapter9/file.txt", "r")

'''
lines = f.readlines()
print(lines)
print(type(lines))
f.close()
'''

'''
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
line5 = f.readline()
print(line5)
line6 = f.readline()
print(line6)
f.close()
'''

'''
line = f.readline()

while (line != ""):
    print(line)
    line = f.readline()

f.close()
'''
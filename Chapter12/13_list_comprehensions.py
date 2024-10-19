myList = [1, 2, 5, 4, 29, 9]
'''
squaredList = []

for item in myList:
    squaredList.append(item * item)

print(squaredList)
'''

squaredList = [i * i for i in myList]
print(squaredList)
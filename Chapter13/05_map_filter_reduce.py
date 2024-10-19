# MAP Example: 

l = [1, 2, 3, 4, 5]

square = lambda x: x * x

sqList = map(square, l)
print(list(sqList))

# FILTER Example: 

def even(n):
    if (n % 2 == 0):
        return True
    return False

onlyEven = filter(even, l)

print(list(onlyEven))

# REDUCE Example: 

from functools import reduce

def sum(a, b):
    return a + b

print(reduce(sum, l))
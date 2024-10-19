from functools import reduce

a = [1, 2, 343, 245, 32, 436, 234849374943, 22, 99, 2299436]

def greater(a, b):
    if (a > b):
        return a
    return b

print(reduce(greater, a))
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.......n
sum(n) = n + sum(n - 1)

'''

def sum(n):
    if (n == 1):
        return 1
    return n + sum(n - 1)

print(sum(4))
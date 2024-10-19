def divisible5(n):
    if (n % 5 == 2):
        return True
    return False

a = [1,2,343, 245, 32, 436, 22, 99, 2299436]

f = list(filter(divisible5, a))
print(f)
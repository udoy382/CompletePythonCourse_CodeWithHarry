def findGreatestNumber(a, b, c):
    if (a > b and  a > c):
        print(f"A is the greatest number ({a})")
    elif (b > a and b > c):
        print(f"B is the greatest number ({b})")
    else:
        print(f"C is the greatest number ({c})")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter thrid number: "))


findGreatestNumber(num1, num2, num3)
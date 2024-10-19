# Problem 1 :
'''
c = int(input("Enter temperature in Celsius: "))

f = c * 9/5 + 32

if (c < 0):
    print("Temperature is below freezing, ", f)
else:
    print("Temperature in Ferenheit: ", f)
'''

# Problem 2 :
'''
grades = int(input("Enter your grade: "))

if (grades >= 90):
    print("A")
elif (grades >= 80):
    print("B")
elif (grades >= 70):
    print("C")
elif (grades >= 60):
    print("D")
elif (grades < 60):
    print("F")
else:
    print("Opps! Something is wrong.")
'''

# Problem 3 :
'''
user = int(input("Enter any number: "))

if (user % 2 == 0):
    print("This is Even number.")
else:
    print("This is Odd number.")
'''

# Problem 4 :
'''
age = int(input("Enter age: "))

if (age > 0 and age <= 12):
    print("Child")
if (age >= 13 and age <= 19):
    print("Teen")
if (age >= 20 and age <= 64):
    print("Adult")
if (age >= 65):
    print("Senior")
else:
    print("Invalid age")
'''

# Problem 5 :
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 > num2 and num1 > num3):
    print(f"The largest number is {num1}")
elif (num2 > num1 and num2 > num3):
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")
'''

# Problem: ATM PIN Verification System :

atm_user_code = [123, 112233, 11331, 436, 2299]

attempts = 3

while (attempts > 0):
    password = int(input("Enter your ATM PIN code: "))

    if (password in atm_user_code):
        print("Welcome!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempt(s) remaining.")
        else:
            print("Incorrect PIN. Your account is locked.")
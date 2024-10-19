class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

x = Employee()
y = Programmer()
z = Manager()

print(y.b)

print(z.a)
print(z.b)
print(z.c)
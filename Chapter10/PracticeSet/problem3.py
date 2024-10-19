class Demo:
    a = 4

o = Demo()

print(o.a) # prints the class attrubute because instance attributes is not present

o.a = 0 # instance attribute is set

print(o.a) # prints the class attrubute because instance attributes is present
print(Demo.a) # prints the class attrubute
class Employee:
    language = 'Python' # This is the class attribute
    salary = 1200000


udoy = Employee()
udoy.name = "Udoy" # This is a object/instance attribute
print(udoy.name, udoy.language, udoy.salary)


rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.salary, rohan.language)

# Here `name` is object/instance attribute and `salary` and `language` are class attribute as they directly belong to the class


class Employee:
    language = 'Python'
    salary = 1200000

    def __init__(self, name, language, salary): # dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary

        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning!")

    @staticmethod
    def greetStatic():
        print("This is greet stati methods.")


udoy = Employee("Udoy", "Python", 4360000)
rohan = Employee("Rohan", "C", 12084)

# udoy.name = "SR Udoy"

print(udoy.name, udoy.language, udoy.salary)
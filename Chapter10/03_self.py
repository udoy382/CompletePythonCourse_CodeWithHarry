class Employee:
    language = 'Python'
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning!")

    @staticmethod
    def greetStatic():
        print("This is greet stati methods.")


udoy = Employee()

udoy.language = "JavaScript"

udoy.greet()
udoy.getInfo()
udoy.greetStatic()
Employee.getInfo(udoy)

# print(udoy.language, udoy.salary)
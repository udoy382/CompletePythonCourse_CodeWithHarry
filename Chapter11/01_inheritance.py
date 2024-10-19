class Employee:
    company = "ITC"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

"""
class Programmer(Employee):
    company = "ITC Infotech"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} alnguage")
"""

class Programmer(Employee):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} alnguage")


a = Employee()
b = Programmer()

print(a.company, b.company)
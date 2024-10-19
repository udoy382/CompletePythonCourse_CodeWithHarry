marks = []

student_mark1 = int(input("Enter your marks : "))
student_mark2 = int(input("Enter your marks : "))
student_mark3 = int(input("Enter your marks : "))
student_mark4 = int(input("Enter your marks : "))
student_mark5 = int(input("Enter your marks : "))
student_mark6 = int(input("Enter your marks : "))

marks.append(student_mark1)
marks.append(student_mark2)
marks.append(student_mark3)
marks.append(student_mark4)
marks.append(student_mark5)
marks.append(student_mark6)

marks.sort()
print(marks)
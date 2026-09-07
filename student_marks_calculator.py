# Student Marks Calculator
# Beginner Python Project

print("================================")
print("     STUDENT MARKS CALCULATOR")
print("================================")

name = input("Enter student name: ")

print("\nEnter marks out of 100:")

english = float(input("English: "))
maths = float(input("Mathematics: "))
computer = float(input("Computer: "))
hindi = float(input("Hindi: "))
evs = float(input("EVS: "))

total = english + maths + computer + hindi + evs
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n================================")
print("           RESULT")
print("================================")
print("Student Name :", name)
print("Total Marks  :", total, "/ 500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)
print("================================")

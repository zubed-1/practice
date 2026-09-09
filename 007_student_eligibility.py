print("Program: Student Eligibility")

age = int(input("Enter age: "))
student = input("Enter student status (yes/no): ").lower()
if age >= 18 and student == "yes":
    print("Eligible")
else:
    print("Not eligible")

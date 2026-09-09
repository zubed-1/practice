print("Program: Scholarship Eligibility")

income = float(input("Enter annual family income: "))
marks = int(input("Enter marks: "))
if income <= 300000 and marks >= 75:
    print("Eligible")
elif income <= 500000 and marks >= 85:
    print("Eligible")
else:
    print("Not eligible")

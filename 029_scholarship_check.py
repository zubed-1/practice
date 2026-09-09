print("Program: Scholarship Check")

income = float(input("Enter annual family income: "))
score = int(input("Enter score: "))
if income <= 300000 and score >= 60:
    print("Eligible")
else:
    print("Not eligible")

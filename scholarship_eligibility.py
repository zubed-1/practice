marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))
eligible = marks >= 75 and attendance >= 75 and income <= 250000
print("Eligible" if eligible else "Not eligible")

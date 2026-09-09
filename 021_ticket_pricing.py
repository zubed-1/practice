print("Program: Ticket Pricing")

age = int(input("Enter age: "))
if age < 5:
    print(0)
elif age <= 12:
    print(50)
elif age <= 59:
    print(100)
else:
    print(60)

print("Program: Season Checker")

month = int(input("Enter month number: "))
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month")

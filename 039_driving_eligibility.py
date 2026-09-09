print("Program: Driving Eligibility")

age = int(input("Enter age: "))
license_status = input("Enter license status: ").lower()
if age >= 18 and license_status == "yes":
    print("Can drive")
else:
    print("Cannot drive")

print("Program: Valid Triangle")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Invalid triangle")

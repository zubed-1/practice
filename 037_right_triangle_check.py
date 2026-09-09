print("Program: Right Triangle Check")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a + b > c and a + c > b and b + c > a:
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("Right triangle")
    else:
        print("Valid triangle")
else:
    print("Invalid triangle")

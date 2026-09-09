print("Program: Lcm")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x = a
while x % b != 0:
    x = x + a
print(x)

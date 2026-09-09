print("Program: Right Arrow Pattern")

n = int(input("Enter number: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("*")
    elif i == n // 2:
        print("* " * n)
    else:
        print("*" + " " * (2 * n - 3) + "*")

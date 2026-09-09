print("Program: Diamond Pattern")

n = int(input("Enter number: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

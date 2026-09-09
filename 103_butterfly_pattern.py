print("Program: Butterfly Pattern")

n = int(input("Enter number: "))
for i in range(1, n + 1):
    print("* " * i + " " * (4 * (n - i)) + "* " * i)
for i in range(n, 0, -1):
    print("* " * i + " " * (4 * (n - i)) + "* " * i)

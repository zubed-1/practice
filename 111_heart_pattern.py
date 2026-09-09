print("Program: Heart Pattern")

n = int(input("Enter number: "))
for i in range(n // 2):
    spaces = " " * (n // 2 - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars + spaces + stars)
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

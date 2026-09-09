print("Program: Zigzag Pattern")

n = int(input("Enter number: "))
for i in range(n):
    print("*", end=" ")
print()
print(" " * (2 * n - 2) + "*")
for i in range(n):
    print("*", end=" ")
print()

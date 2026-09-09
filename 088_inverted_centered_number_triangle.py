print("Program: Inverted Centered Number Triangle")

n = int(input("Enter number: "))
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

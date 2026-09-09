print("Program: Hollow Diamond")

n = int(input("Enter number: "))
for i in range(n):
    for j in range(n):
        d = abs(i - n // 2) + abs(j - n // 2)
        if d == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

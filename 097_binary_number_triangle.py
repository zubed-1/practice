print("Program: Binary Number Triangle")

n = int(input("Enter number: "))
for i in range(n):
    for j in range(i + 1):
        print(j % 2, end=" ")
    print()

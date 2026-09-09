print("Program: One Zero Triangle")

n = int(input("Enter number: "))
for i in range(n):
    for j in range(i + 1):
        print(1 - (j % 2), end=" ")
    print()

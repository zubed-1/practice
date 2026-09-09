print("Program: Sequential Number Triangle")

n = int(input("Enter number: "))
value = 1
for i in range(1, n + 1):
    for j in range(i):
        print(value, end=" ")
        value = value + 1
    print()

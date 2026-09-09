print("Program: Even Odd Each Number")

n = int(input("Enter number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

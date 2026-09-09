print("Program: Break At Multiple Of 7")

n = int(input("Enter number: "))
for i in range(1, n + 1):
    if i % 7 == 0:
        break
    print(i)

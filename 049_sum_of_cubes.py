print("Program: Sum Of Cubes")

n = int(input("Enter number: "))
s = 0
for i in range(1, n + 1):
    s = s + i * i * i
print(s)

print("Program: Armstrong Number")

n = int(input("Enter number: "))
original = n
count = 0
while n > 0:
    count = count + 1
    n = n // 10
n = original
s = 0
while n > 0:
    digit = n % 10
    s = s + digit ** count
    n = n // 10
if s == original:
    print("Armstrong")
else:
    print("Not Armstrong")

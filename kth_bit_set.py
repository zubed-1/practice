n = int(input("Enter n: "))
k = int(input("Enter k (0-based): "))
if (n & (1 << k)):
    print("Set") 
else:
    print("Not set")

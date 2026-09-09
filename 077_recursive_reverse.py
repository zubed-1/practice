print("Program: Recursive Reverse")

def reverse_number(n, result=0):
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + n % 10)

n = int(input("Enter number: "))
print(reverse_number(n))

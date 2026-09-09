print("Program: Atm Withdrawal")

balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum = float(input("Enter minimum balance: "))
if amount <= balance and balance - amount >= minimum:
    balance = balance - amount
    print(balance)
else:
    print("Transaction declined")

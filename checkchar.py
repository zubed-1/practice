char = input("Enter the character:")
if char>='A' and char<='Z':
    print("Uppercase character")
elif char>='a' and char<='z':
    print("Lowercase character")
elif char>='0' and char<='9':
    print("Digit")
else : 
    print("Special character")
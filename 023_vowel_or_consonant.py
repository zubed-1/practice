print("Program: Vowel Or Consonant")

ch = input("Enter character: ").lower()
if ch in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")

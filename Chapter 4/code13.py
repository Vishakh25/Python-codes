n = input("Enter a string: ")
rev = ''
for char in n:
    rev = char + rev
if n == rev:
    print("String is palindrome: ")
else:
    print("String is not palindrome: ")
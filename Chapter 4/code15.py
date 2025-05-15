n = input("Enter a string: ")
str = ''
for char in n:
    if char.isalnum() or char.isspace():
        str += char
    
print("The result is: ", str)
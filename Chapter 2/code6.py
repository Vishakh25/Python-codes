year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a Leap year: ", year)
else:
    print("This is not a Leap year: ", year)
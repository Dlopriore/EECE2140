year = int(input("Enter a valid leap year: "))

is_leap = True


if (year % 400 == 0):
    print("The number you picked was a valid leap year")
elif (year % 4 == 0 and not(year % 100 == 0)):
    print("The number you picked was a valid leap year")
else:
    print("The number you picked was not a valid leap year")

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0);


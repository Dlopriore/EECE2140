
number = int(input("Enter a number: "))
digit_Sum = 0

while number > 0:
    digit_Sum += number % 10
    number //= 10
print(digit_Sum)

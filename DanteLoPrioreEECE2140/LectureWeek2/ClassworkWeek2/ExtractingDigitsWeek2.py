#get 3 digit number and compute sum of its digits
numero = int(input("Enter a 3-digit number: "))

firstDigit = int(numero%10)
numero = numero // 10
secondDigit = int(numero%10)
numero = numero // 10
thirdDigit = int(numero%10)

sumDigits = firstDigit + secondDigit + thirdDigit
print(sumDigits)
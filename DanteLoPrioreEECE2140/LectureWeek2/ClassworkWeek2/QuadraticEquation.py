import math

#pythagorean theorim
a = int(input("Enter the A: "))
b = int(input("Enter the B: "))
c = int(input("Enter the C: "))

delta = math.sqrt((b*b)-(4*a*c))

rootPos = (-b + delta) / (2*a)
rootNeg = (-b - delta) / (2*a)


print(a, " ", b)
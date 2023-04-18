import math

num = 5

#Memory
#-everything in python is an object 
#-represents the object's location in memory
id(num)


#Variable Names:
#-separated by _
#-case-sensitive

#Constants:
#-All uppercase
height = 0
HEIGHT = 0
print('Height in m', height * HEIGHT)
height = height +1
print(height)

#Writing Comments:
#-use hastag

#Primitive Data Types
#-int, float - double, bool, str, NoneType - empty

#Type of Variables:
#-outputs object type
type(num)

#Type of Conversions:
#-casting 
#-convert data int different type
int(2.7) # returns 2
int(24) # returns 24

float(74) # returns 74.0
float(1.3) # returns 1.3

str(12) # returns '12'
str(4.5) # returns '4.5'

#Worked Example
#- input always outputs a string
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

print(num1)
print(num2)

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

result = number1 + number2
print(result)

#Arithmetic Operators
#- +,-,*,**, /, //, %

#Math Module
#- use import math
#- math.sqrt

print(math.sin(2* math.pi))

#Class Exercise




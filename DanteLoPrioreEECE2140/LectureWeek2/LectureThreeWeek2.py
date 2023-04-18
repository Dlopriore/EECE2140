# alter strings 
# - can be in single or double quotes
# - len() - returns length
len("1222")
# - \n is used to return string in new line

#character encoding 
#- ord() returns the Unicode code of a given character
ord('a')
#- chr() returns the character represented by a given Unicode code
chr(97)

#string operators 
# - combining strings together
first = "Hom"
lastname = "simp"
fullName = first + " " + lastname
#- strings the * operator repeats the string n number of times:
stars = "*" * 20

#membership operators
# - n or not in operators can be used to check if a string contains a given substring:
s = "Phy is good"
"Phy" in s
"hello" in s
"eh" not in s

#Slicng strings 
# - s[i:j] gets a slice of the string s between the indices i and j (not including j)

#String Methods
# - in order to change the string in python you need to store it into another variable

#String Formating 
# - string.format() allows you to handle complex string formatting
# - you define placeholders in the string using braces {}
# - Each placeholder is replaced with the string value of the corresponding argument

x = 3
y = 4

print('{} + {} + {}'.format(x, y, x+y))
print(f'{x} + {y} + {x+y}')

#Using If statement
#if <boolean expression>:
#<indented statement 1>
#<indented statement 2>
#...
#<non-indented statements>

num = int(input("Enter a number: "))
if num > 10:
    print("The number is greater than ten")
print("end of program")

#Using If-else statement
#if <boolean expression>:    
# <statements 1>
# else:    
# <statements 2>
# you can nest if-statements if you want to

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Using If-elif-else statement
#if <boolean expression 1>:    
#<statements 1>
#elif <boolean expression 2>:    
#<statements 2>
#elif <boolean expression 3>:
#<statements 3>
#...
#else:
#<statements>

score = int(input("Enter you test score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

#While loops 
#- A while loop is a conditionally controlled loop which executes the statements as long as the condition is true
# while <condition>:
# <indented statement 1>
# <indented statement 2>
# ...
# <non-indented statement>
i = 0
while (i < 11):
    print(i, end='')
    i = i + 1

#For loops 
#- used to iterate through a sequence of numbers
# for <variable> in range(<start, stop, step>):
# <indented statement 1>
# <indented statement 2>
# ...
# <non-indented statement>

for i in range(1, 11):
    print(i, end='')

for i in range(1, 5):
    print(i, end='')

for i in range(1, 5, 2):
    print(i, end='')

for i in range(10, 5, -1):
    print(i, end='')

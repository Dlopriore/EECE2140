# Dante LoPriore
# February 1, 2023
# PS2: Problem 1

# Purpose: to create a function that aquires the Fahrenheit 
# equivalent of a Celsius temperature reading

# Int -> Int 
# to calculate the conversion from celsius to fahrenheit 
# using the formula given in the problem
def fahrenheit(celsius):
    return ((9/5)*celsius) + 32

# to initialize the variables to store the calculations for the weather readings.
celsius_reading = -10
print("Celsius C \tFahrenheit F")

# to compute the celsius to fahrenheit equivaluents for a 
# celsius reading range of -10 to 100 degrees celsius in 2 digit precision
for celsius_reading in range(-10, 101, 1):
    f_calulcation = fahrenheit(celsius_reading)
    print(f'{celsius_reading:.2f} \t        {f_calulcation:.2f}')









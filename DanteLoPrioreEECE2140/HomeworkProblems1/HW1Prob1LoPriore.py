# Dante LoPriore
# January 23, 2022
# PS1: Problem 1

# Int -> Int 
# Purpose: to compute the average miles per gallon for each tank full
# based upon the user's input on those values

# initialize variables for the inputs and total sums of those inputs
gallons = 0
miles = 0
sum_of_total_gallons = 0
sum_of_total_miles = 0
average_miles_per_gallon = 0

# allows the user to input the amount of gallons and miles until the user input's a negative number
while(True):

    # allows user to input the number of the gallons
    gallons = float(input("Enter the number of the gallons used (any negative number to end): "))

    #checks to see if the user inputed a negative number
    if((gallons < 0.0)):
        break
    
    # allows user to input the number of the miles
    miles = int(input("Enter the number of miles driven: "))

    # to determine whether the amount of gallons or miles is zero
    if((miles == 0) or (gallons == 0)):
        milesPerGallon = 0
    else:
        # outputs the miles per gallon with 6 digits of precision
        milesPerGallon = miles/gallons
    print(f'The miles/gallon for this tank was {milesPerGallon:.6f}')

    # to store the sum of the gallons and miles for average
    sum_of_total_gallons = sum_of_total_gallons + gallons
    sum_of_total_miles = sum_of_total_miles + miles

# to determine whether the sum of the amount of gallons or miles is zero
if((sum_of_total_gallons == 0) or (sum_of_total_miles == 0)):
    average_miles_per_gallon = 0
else:
    # to compute the average mile per gallon based on user's input
    average_miles_per_gallon = sum_of_total_miles/sum_of_total_gallons

# to output final result from average computation
print(f'The overall average miles/gallon for the above tanks was {average_miles_per_gallon:.6f}.')



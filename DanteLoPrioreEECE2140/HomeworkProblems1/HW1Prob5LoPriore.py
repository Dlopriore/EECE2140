# Dante LoPriore
# January 23, 2022
# PS1: Problem 5


# Int -> Int 
# Purpose: to approximate the value of pie from the following series 

# initialize variables for the current term and total sums of those inputs
pie_approximation_sum = 0
series_current_term = 1

# to create a table to store the pie approximations with there terms number
print('Amount of Terms Used', 'Approximation of Pie')

# to initialize variables to fulfill a requirement of being a close approximiate for pie
# only for one time
check_five_digits = "N"
check_four_digits = "N"
check_three_digits = "N"


# to find the pie approximations for the terms 1-10 using the infinite series 
# given in the problem
for k in range(0, 11):
    series_term = (((-1) ** k) / ((2*k)+1))
    pie_approximation_sum = series_term + pie_approximation_sum
    print(k, f'{(4*pie_approximation_sum):.6f}')


# to reset variables back to their orginal state
# initialize variables for the current term and total sums of those inputs
pie_approximation_sum = 0
series_current_term = 1


# to check to see what term reaches the desired closest pie approximation within a 
# range of terms
for k in range(0, 15000):
    series_term = (((-1) ** k) / ((2*k)+1))
    pie_approximation_sum = series_term + pie_approximation_sum
    if(check_five_digits == "N" and (pie_approximation_sum*4*10000//1 == 31415.0)):
        check_five_digits = "Y"
        print(f"It took {k} amount of terms to reach 3.1415")
    if(check_four_digits in "N" and (pie_approximation_sum*4*1000//1 == 3141.0)): 
        check_four_digits = "Y"
        print(f"It took {k} amount of terms to reach 3.141")
    if(check_three_digits in "N" and (pie_approximation_sum*4*100//1 == 314.0)):
        check_three_digits = "Y"
        print(f"It took {k} amount of terms to reach 3.14")


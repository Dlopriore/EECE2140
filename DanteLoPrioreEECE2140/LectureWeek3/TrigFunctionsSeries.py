import math


x = 0
x0 = 0
signNumber = -1
number_terms = 5
exp_approximate = 1
curr_term = 0 
for n in range(1, number_terms+1):
    signNumber = signNumber ** n
    number_terms = number_terms ** ((2*n)+1)
    if  (((2*n)+1) % 2 == 1):
        curr_term *= x0 / n
        exp_approximate += curr_term
        print (x)

cos_approxmite = 1
cur_term = 1
n = 1
num_terms3 = 10
x0 = math.pi /3 

while n < num_terms3:
    cur_term *= - x ** 2 / ((2*n)*(2*n-1))
    cos_approxmite += cur_term
    n += 1 

print(f'The cosine approximate is {cos_approxmite}')



#[outputs] function name (parameters)
# int crazy (int x, str sa)
# def function_name(parameter_list)

def print_gpa_PARA(name, gpa, credits):
    print(f'The GPA of {name} after passing {credits} credit hours is {gpa:.2f}.')

def print_gpa_override(name, gpa, credits = 80):
    print(f'The GPA of {name} after passing {credits} credit hours is {gpa:.2f}.')
    return (gpa*credits, gpa) # packing 

def print_gpa():
    print('The GPA of  is 3.40.')

print_gpa_PARA("Bob", 2.5, 52)
print_gpa_PARA(gpa=4.7,name="Brian", credits=50)
totalPoints, gpa1 = print_gpa_override(gpa=4.7,name="Brian", credits=50)
print(totalPoints)
range = (4, 20, 3)
print_gpa()
    


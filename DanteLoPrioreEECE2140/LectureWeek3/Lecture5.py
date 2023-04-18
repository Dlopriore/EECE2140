import math
x0 = 0.3
number_terms1 = 3
exp_approximate = 1

for n in range(1, number_terms1+1):
    fact = 1
    for k in range(2, n+1):
        fact *= k
    curr_term = x0 ** n / fact
    exp_approximate += curr_term

number_terms2 = 5
exp_approximate2 = 1
curr_term = 1 
for n in range(1, number_terms2+1):
    curr_term *= x0 / n
    exp_approximate2 += curr_term

print(f'The approximated value of exp({x0}) is \n\t\
Method 1: ({exp_approximate:5f}) Method 2: ({exp_approximate2:8f}) Exact Value: ({math.exp(x0):.8f}')
    # 1 + x + x^2/2! + x^3/3! + x^4/4! + x^n/n!

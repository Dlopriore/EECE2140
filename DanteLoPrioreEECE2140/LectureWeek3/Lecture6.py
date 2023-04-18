import math
def find_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area

area = find_area_perimeter(3, 4)
#print(area)

def circle_data(radius, cir_sphere):
    if(cir_sphere == 'c'): #sphere
        area = math.pi * radius ** 2
        perim_vol = 2 * math.pi * r
    elif (cir_sphere == 's'): #sphere
        area = 4 * math.pi * radius ** 2
        perim_vol = 4/3 * math.pi * r ** 3
    else:
        print("The shape must be either circle ('c') or sphere ('s'). ")
        return (0, 0)
    return (area, perim_vol) #packing

#r = 5
#cir_sphere = 'c'
r, cur_cir_sphere = 5, "c"
#cur_area, cur_perim_vol = circle_data(r, cir_sphere)
cur_area, cur_perim_vol = circle_data(cir_sphere = cur_cir_sphere, radius=r)
#print(cur_area, cur_perim_vol)


if cur_cir_sphere in ("s", "c"): # cir_sphere == "s" or cir_sphere == "c")
    print_str = "circle" if cur_cir_sphere == 'c' else "sphere"
    print(f'The area of a {print_str} with radius {r} is {cur_area:.4f}.')
    print(f"The {'perimeter' if cur_cir_sphere == 'c' else 'volume'}",\
    f"of the {print_str} is {cur_perim_vol:.4f}.")

import random

random.seed(2) # setting the random numbers to be the same nect time you run the program
for k in range(5):
    #print(f"{random.random():4f}", end= " * ") # prints number between 0-1
    #print(f"{random.normalvariate(2, 1):4f}", end= " * ") # prints number between 0-1
    #print(f"{random.randint(2, 10)}", end= " * ") # prints number between 2-10
    print(f"{random.randrange(2, 10)}", end= " * ") # prints number between 2-9
    #print(f"{random.uniform(1.2, 3.5):4f}", end= " * ") # prints number between 1.2-3.5

#def rnd_gen(num_elements, init_mu, end_sigma, rnd_type = "u")
#    total, multiplication = 0, 1
 #   debug_flag = True
#    for k in range (num_elements):
#        if rnd in ("u", "U"):
#            print 

#store_rand_Mult, store_rand_Sum = random_generator(10, 2, 4, "u")

#print(f'The random number generator multiplication of the numbers was {store_rand_Mult}')
#print(f'The random number generator sum of the numbers was {sum_of_rand}')

#def find_mean(a, b, c):
#    return (a+b+c)/3

#print(f'Average: {find_mean(2, 10, 12)}')
#print('Alice', "Bob", "Morgan", "John")

#variable length input
def find_mean(a, b, c, *num):
    total = 0 
    for k in range(len(num)):
        total += num[k]

    if len(num) == 1:
        pass
    elif len(num) == 2:
        pass
    elif len(num) == 3:
        pass
    
    return total


print ("\n")
print(f'{find_mean(1, 2, 36, 78)}')


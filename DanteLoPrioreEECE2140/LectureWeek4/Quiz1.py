import random

cur_product = 1
while (cur_product <= 500):
    cur_product *= 5


A = "7" + "3"
print(type(A))

grade = 87
if grade >= 60:
    result = 'Passed'
else:
    result = 'Failed'

print(result)

result2 = ('Failed' if grade >= 60 else 'Passed')
print(result2)

print(10, 20, 30, sep=', ')

my_list = ['A', 'b', 'c', 'd', 'e']
print(my_list[3:])
print(my_list[-2:-1])

def mathGame(x, y):
    division = x / y
    mult = x / y
    return division, mult
print(mathGame(2, 2))

random.seed(5)
print(random.randint(0, 9))


for k in range(1, 5):
    counter = 0
    while counter < k:
        print("*", end="")
        counter += 1
    print()


for k in range(1,5):
     counter = 0
     while counter < k:
          print("*", end='')
          counter += 1
     print()

print(random.seed(5))


def run_simulation(num_iterations=1000):
    counter = num_iterations
    rnd0_counter, rnd1_counter = [0, 0]

    while counter > 0:
        counter -= 1
        cur_rnd = random.randint(0,1)
        if cur_rnd == 0:
            rnd0_counter += 1
        else:
            rnd1_counter += 1

    return rnd0_counter, rnd1_counter

rnd0_counter, rnd1_counter = run_simulation(5000)
print(rnd0_counter, rnd1_counter)

print(-13 % -4 == -1)
print(13 % -4 == -3)
print(-21 % -5 == -1)
print(-13 // 4 == -4)



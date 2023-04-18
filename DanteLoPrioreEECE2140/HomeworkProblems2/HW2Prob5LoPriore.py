# Dante LoPriore
# January 31, 2023
# PS2: Problem 5

# Purpose: to create a function that produces the numbers that are considered prime
# using the Sieve of Eratosthenes method 

# allows user to input the amount of elements you would like in a list to be checked
k_element = int(input("Enter the amount of elements you would like in a list: "))

# The check_prime_numbers function fulfills all requirements for this question

# Int -> [Bool] [Int]
# to compute valid prime numbers within a range of 2 to the k-element
def check_prime_numbers(k):
    # creates a k-element list that are initialized to be true 
    primes = [True]*k

    # initialized the first and second to be false since the numbers 0 and 1 are not prime numbers
    primes[0]=False
    primes[1]=False

    # iterates the k-element list starting at two since two is the first known prime number
    for prime_numbers in range(2, k):

        # iterates the square rooot of the k-element list starting at two since two is the first known prime number
        for number in range(2, int(prime_numbers ** 0.5)+1):

            # to check the given number is a multiples of a known prime number
            if (prime_numbers % number == 0):
                primes[prime_numbers] = False

    # outputs the known prime numbers in a list within a range of 0-k
    for x in range(0, k):
        if(primes[x]):
            print(x, end=", ")
    print(f'\n')

    # outputs the known list of prime numbers based on their index with in the list
    return (primes)

# output valid prime numbers from a range of 2-k 
print(check_prime_numbers(k_element))
print()

# output valid prime numbers from a range of 2-15000 
print(check_prime_numbers(15000))





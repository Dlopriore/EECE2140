# Dante LoPriore
# January 23, 2022
# PS1: Problem 3

# Int -> Int Int Int
# Purpose: to compute all the combinations of a pythagorean triple by determine 
# if a given set of the side1, side2, and the hypothenus are a valid right triangle 
# using the pythagorean theorem

# to find all integer pythagorean triple combinations 
# for the max range for an integer to be 1000
threshold = 1000

# used 3D nested array to test all possibilities
for side1 in range(1, threshold):
    for side2 in range(1, threshold):
            for hypothenus in range(1, threshold):

                # to determine whether a given set of triples 
                # are a true pythagoren theorem
                if((hypothenus*hypothenus) == (side1*side1) + (side2*side2)):
                    # outputs valid pythagorean triples
                    print(side1, side2, hypothenus)
                    print()
                
            
        
    



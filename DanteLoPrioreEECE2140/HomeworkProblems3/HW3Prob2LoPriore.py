from itertools import permutations

# Dante LoPriore
# March 17, 2023
# PS3: Problem 2

# Purpose: to create a function that allows the user to write a five-letter word, and 
# produces every possible three-letter word based on the combinations of the word’s letters.

# allows user to input a five letter word
user_response = input("Please enter a valid five letter word: ")
    

# String -> List of Strings
# to produce all the combinations for a valid three letter word based on the an input of a five letter word 
def check_valid_words(given_word):

    # stores all the cominations of letters in words that only contain three letters  
    all_word_combinations = ["".join(letter) for letter in permutations(given_word, 3)]

    return all_word_combinations

# outputs valid words from user's response
print(check_valid_words(user_response))




# Dante LoPriore
# January 31, 2023
# PS2: Problem 3

# Purpose: to write a function to determine whether 
# a user's input is a valid palidrome

# Str -> Str
# to determine whether the user's response is a valid palindrome
def is_palindrome(user_response):

    # initialize variables to represent the order of the phrase
    reverse_order = ""
    orginal_order = "" 

    # iterates through each charcter of the user's response
    for character in user_response.lower():
        # assigns the user's response to the original order that ignores case sensitivity 
        # spaces, and punctuation.
        if character.isalpha():
            orginal_order += character
        

    # assigns the user's response to the in the reverse order that ignores case sensitivity 
    # spaces, and punctuation.
    reverse_order += orginal_order[::-1]

    #returns the result if the input was a valid palindrome
    return (orginal_order.lower() == reverse_order.lower())

# allows user to enter a valid palindrome
print(is_palindrome(input("Enter a valid palindrome:")))
# Dante LoPriore
# February 5, 2023
# PS2: Problem 6

# Purpose: to create a function that determines the amount of time a unique letter occured and
# stores this data in a list and dict 

# Str -> List Dict
# to intrept a user's string input and produce the frequencies of unique letters that disreagards
# whitespace, punctation, and special characters in the calculation
def summarize_letters(str_input):

    #initialiaze varaiables to store the frequencies 
    frequencies_list = []
    unique_list = []
    str_list = list(str_input)
    freq_dict = dict()
    
    # iterate the user's input to check the frequencies of just unique letters
    # and display results as a list
    for item in str_input.lower():
        if item.isalpha():
            if item not in unique_list:
                unique_list += [item]
                frequencies_list.append(1)
            else:
                frequencies_list[unique_list.index(item)] += 1
        freq_dict = dict()

    # iterate the user's input to check the frequencies of just unique letters 
    # and display results as a dict
    for char in str_list:
        char = char.lower()
        if char.isalpha():
            if char in freq_dict:
                freq_dict[char]+=1
            else:
                freq_dict[char] = 1
    
    return (list(zip(unique_list, frequencies_list))), freq_dict

cur_str = 'Dante ,+LoPriore.d'
print(cur_str)
print(summarize_letters(cur_str))

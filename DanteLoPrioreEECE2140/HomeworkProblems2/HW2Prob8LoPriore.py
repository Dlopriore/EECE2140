# Dante LoPriore
# February 5, 2023
# PS2: Problem 8

# Purpose: to produce a function that takes in a list of integers 
# which produces the frequencies of the number in the list as a dict and list

# List -> List Dict
# to compute the frequencies of a integer based on the user's input as a list and dict
# sorted in decending order
def sorting_integer_list(input_integer_list):
    freq_dict = dict()
    sorted_freq_dict = dict()

    # sorting dictionary frequencies requirement
    for cur_num in input_integer_list:
        if cur_num in freq_dict:
            freq_dict[cur_num] +=1
        else:
            freq_dict[cur_num] = 1
        sorted_freq_dict = dict(sorted(freq_dict.items()))

    sort_freq_list = list()

    # sorting dictionary frequencies requirement
    for cur_index in range(len(input_integer_list)):
        if input_integer_list[cur_index] not in sort_freq_list:
           sort_freq_list.append(input_integer_list[cur_index])

    sort_freq_list.sort(reverse=True)

    return sort_freq_list, sorted_freq_dict

# List -> List
# to determine what items are not in the list and output them in a list
def not_present_list_items(sorted_list):
    not_show_in_list = list()
    maxiumium_number = max(sorted_list)
    item = 1
    while(item <= maxiumium_number):
        if item not in sorted_list:
            not_show_in_list.append(item)
        item += 1
    return not_show_in_list

my_list = [3, 5, 4, 3, 1, 4, 1, 4, 9]

print(sorting_integer_list(my_list))
a, b = sorting_integer_list(my_list)
print(not_present_list_items(a))
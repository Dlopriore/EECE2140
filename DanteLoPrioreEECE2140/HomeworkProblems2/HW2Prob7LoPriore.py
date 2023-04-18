import operator

# Dante LoPriore
# February 7, 2023
# PS2: Problem 7

# Purpose: to produce an a hardware invoice using tuples and the given sample hardware data

# initialize variable for the hardware invoice 
overall_invoice = []

# to add the sample hardware data, which are stored as tuples, into the hardware invoice
# the tuples represent hardware store invoices that consist of a part ID, 
# a part description, an integer quantity of the item that is being purchased, and a float item of its price
overall_invoice.append(("38", "Electric sander", 11, 24.09)) #11
overall_invoice.append(("42", "Power saw", 18, 89.82)) # 18
overall_invoice.append(("77", "Sledge hammer", 7, 57.98)) # 7
overall_invoice.append(("7", "Hammer", 76, 11.99)) #76

'''

Question 8 PART A

'''

# outputs the hardware invoice based on the alphabetical order for the part's name
overall_invoice.sort(key=operator.itemgetter(1))   
print("PART A REQUIREMENT \n")
print("Invoices Sorted by Part Description:")
for cur_index in range(len(overall_invoice)):
        print(f'{cur_index+1}) Part #{overall_invoice[cur_index][0]}: {overall_invoice[cur_index][1]} '\
        f'Quantity: {overall_invoice[cur_index][2]} for ${overall_invoice[cur_index][3]}')
print(overall_invoice)
print()

'''

Question 8 PART B

'''

# outputs the hardware invoice based on the quantity in the ascending order 
sorted_invoice_quantity = sorted(overall_invoice, key=operator.itemgetter(2))   

# to iterate through the hardware invoice and extract each element 
output_list = []
print("PART B REQUIREMENT \n")
output_list = [((sorted_invoice_quantity[num][1], sorted_invoice_quantity[num][2])) for num in range(0, len(overall_invoice))]
print(tuple(output_list))
print()
'''

Question 8 PART C-E

'''

# [Tuples] -> Str (Tuples) (Tuples)
# to sort the list in decending order based on the invoice value, 
# which is the product of the quantity and the unit price
def compute_billing(hardware_invoice):

    # initialize variables to store desired datatypes
    invoice_product_costs = list()
    sorted_itemized_bill_list = list()
    sorted_bill_limits_list = list()
    sum_of_invoices = 0

    # iterates through the whole hardware invoice 
    # computes the invoice value by multiplying the quantity to the unit price 
    invoice_product_costs = [(hardware_invoice[r][2] * hardware_invoice[r][3]) for r in range(len(hardware_invoice))]

    # to represent the sorted list of the invoices values in a decending order
    invoice_product_costs.sort(reverse=True)

    # to iterate through the sorted list of the invoice values in a decending order
    for item in invoice_product_costs:
        
        # to iterate through the hardware invoice and extrace each element 
        for cur_index in range(len(hardware_invoice)):

            # to determine whether the sorted list of the invoice values in a decending order is equal to the hardware invoice 
            # this condition determines the order of the most expensive invoice in the output list
            if((item == (hardware_invoice[cur_index][2] * hardware_invoice[cur_index][3]))):

                # this completes the Part C requirement
                sorted_itemized_bill_list.append((f'Invoice value: ${item:.2f}', hardware_invoice[cur_index][1]))
            
            # to determine whether the sorted list of the invoice values 
            # in a decending order is equal to the hardware invoice that fits within the $200-$1000 range
            if((item == (hardware_invoice[cur_index][2] * hardware_invoice[cur_index][3])) and ((200 <= item) and (item <= 1000))):

                # this completes the Part D requirement
                sorted_bill_limits_list.append((f'Invoice value: ${item:.2f}', hardware_invoice[cur_index][1]))

    # to compute the sum or total price of all of the invoices 
    for i in range(0,len(invoice_product_costs)):

            # this completes the Part E requirement
            sum_of_invoices = sum_of_invoices + invoice_product_costs[i]
    
    #to output the desired total bill and most expensive products that fit with the given range
    return f'The total bill is ${sum_of_invoices:.2f}', tuple(sorted_itemized_bill_list), tuple(sorted_bill_limits_list) #packing

# initialize varaibles to seperate the outputs from the function
total_calculation, single_itemized_bill, invoice_range_restrictions = compute_billing(overall_invoice)

# output given variables

print("PART C REQUIREMENT \n")
print(single_itemized_bill)
print()

print("PART D REQUIREMENT \n")
print(invoice_range_restrictions)
print()

print("PART E REQUIREMENT \n")
print(total_calculation)
print()

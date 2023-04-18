# Dante LoPriore
# March 17, 2023
# PS3: Problem 4

# Purpose: to produce a function that processes common metric-to-English conversions, 
# where the units and question are written as string

# allow the user to input a unit conversion question 
user_given_conversion_task = input("Please enter the metric-to-English conversions in the form (How many 'measurement' are in 2 'measurement'?) ")

# to split up each word into a list by using the spacing as it will tokenize the phrase into words
given_wanted_conversion = user_given_conversion_task.replace('?', "").lower()
individual_word_list = given_wanted_conversion.split(' ')

# Str Str Str -> Str
# to compute the desired result metric-to-English conversions in MKS units using the unit conversion procedure
def unit_conversion(units_after_conversion, units_before_conversion, value_amount):
    final_conversion = 0 

    # to initialize the mass, volume, units as dictionaries, where the key is the type of unit 
    # and the value is the amount for that unit in MKS units

    mass_units = {'grams': 1, 'kilograms': 0.001, 'pounds': 0.00220462} #grams works
    volume_units = {'liters': 1, 'milliliters': 1000, 'gallons': 0.264172, 'quarts': 1.05} #liters works
    length_units = {'meters': 1, 'centimeters': 100, 'inches': 39.3701, 'feet': 3.28} #meters works

    # to determine whether the given before and after units for the conversion are compatible
    if ((units_after_conversion in length_units.keys()) and (units_before_conversion in length_units.keys())): 
        # preforms the conversion using those units
        final_conversion = (float(value_amount)*length_units[units_after_conversion])/length_units[units_before_conversion]
        return "The final conversion is found to be: " + str(final_conversion) + " " + units_after_conversion
    elif ((units_after_conversion in volume_units.keys()) and (units_before_conversion in volume_units.keys())): 
        # preforms the conversion using those units
        final_conversion = (float(value_amount)*volume_units[units_after_conversion])/volume_units[units_before_conversion]
        return "The final conversion is found to be: " + str(final_conversion) + " " + units_after_conversion
    elif ((units_after_conversion in mass_units.keys()) and (units_before_conversion in mass_units.keys())):
        # preforms the conversion using those units 
        final_conversion = (float(value_amount)*mass_units[units_after_conversion])/mass_units[units_before_conversion]
        return "The final conversion is found to be: " + str(final_conversion) + " " + units_after_conversion
    else:
        # to output case where the given before and after units for the conversion are not compatible
        return 'Not Valid Conversion'

# outputs the final conversion
print(unit_conversion(individual_word_list[2], individual_word_list[6], individual_word_list[5]))





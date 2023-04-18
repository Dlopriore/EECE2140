# Dante LoPriore
# January 20, 2022
# PS1: Problem 7

# Purpose: to check a valid password

# allows user to input a valid password
passwordInput = input("Please enter a valid password: ")

# to store whether the user fulfiled the requirement at least once
fulfilled_Capital_Requirement = False
fulfilled_Lowercase_Requirement = False
fulfilled_Digit_Requirement = False
fulfilled_Special_Character_Requirement = False

# to determine whether the password is within length and check every character in the password fullfills 
# every requirement to be considered valid
# checked every character by using the ASCII table
if ((len(passwordInput) >= 6) and (16 >= len(passwordInput))):
    for i in range(0, len(passwordInput)):

        #checks if character is a-z
        if (ord('a') <= ord(passwordInput[i]) <= ord('z')):
            fulfilled_Lowercase_Requirement = True

        #checks if character is A-Z
        if (ord('A') <= ord(passwordInput[i]) <= ord('Z')):
            fulfilled_Capital_Requirement = True

        #checks if character is 0-9
        if (ord('0') <= ord(passwordInput[i]) <= ord('9')):
            fulfilled_Digit_Requirement = True
        
        #checks if character is a special character
        specialCharacters = "!$#@%"
        if passwordInput[i] in specialCharacters:
            fulfilled_Special_Character_Requirement = True
    
    # checks to see if the password meet all requirements
    if(fulfilled_Lowercase_Requirement and fulfilled_Capital_Requirement 
    and fulfilled_Digit_Requirement and fulfilled_Special_Character_Requirement):
        print("The password you entered was valid")
    else:
        print("The password you entered was not valid")
else:
    print("The password you entered was not valid")


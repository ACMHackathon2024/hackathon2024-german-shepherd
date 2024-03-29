# Assess the strength of the inputted password #
###################################

# grab a string and test it
def stringcheck(made_input):
    letterCheck = None
    
    check_string = made_input
    #update_string = made_input[:]
    print(check_string)
        
    if any(letter.islower() for letter in check_string):
        print("First character MUST be uppercased")
        letterCheck = False

    elif any(letter.isupper() and letter == " " for letter in check_string):
        print("name can't contain spaces")
        letterCheck = False
        
    else:
        letterCheck = True

    return letterCheck
#end of stringcheck function

# output a message
user_input = input('Enter a name: ')
result = stringcheck(user_input)

while result != True:
    user_input = input('Enter a name: ')
    result = stringcheck(user_input)

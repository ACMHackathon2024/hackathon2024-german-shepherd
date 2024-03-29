
def pasReq(user_pasw):

    strength_lvl = 0
    pass_length = len(user_pasw)
    special_case = ["@,"]
    

    user_word = ""
    print(user_word.isupper())

    if pass_length >= 9 :
        strength_lvl += 1
        print(" The strength level is" , strength_lvl)

    elif any(ch.isupper() for ch in user_pasw) or any(ch.islower() for ch in user_pasw):
        strength_lvl += 1
        print(" The strength level is " , strength_lvl)
    
    elif any(ch in special_case for ch in user_pasw):
        strength_lvl += 1
        print(" The strength level is 1 ", strength_lvl)

    
    # if pass has upper, lower case and password length is greater than 9
    if   any(ch.isupper() for ch in user_pasw) or any(ch.islower() for ch in user_pasw) and pass_length >= 9:
        strength_lvl += 2
        print(" The strength level is ", (strength_lvl))

    # if pass word has special cases and the lenght is greater than 9
    elif any(ch in special_case for ch in user_pasw) and  pass_length >= 9:
        strength_lvl += 2
        print(" The strength level is ", (strength_lvl))
    
    elif any(ch.isupper() for ch in user_pasw) or any(ch.islower() for ch in user_pasw) and any(ch in special_case for ch in user_pasw):
        strength_lvl += 2
        print(" The strength level is ", (strength_lvl))

    print("The Password is strenght level is at", strength_lvl)

    return strength_lvl


user_input = input("Please enter a password: ")
pasReq(user_input)


# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password:str):
    for character in password:                         #1 step: sort lenght
        if (len(password) < 8):
            return 'Need a longer password'  #ok!
        else:
            for character in password:                 #2 step: define parametres
                digit_list =[0,1,2,3,4,5,6,7,8,9]
                if character in digit_list and (len(password)>=8):       #cosa fare per controllare che ci sia un numero?
                    return  'Password accepted'   
                else:
                    return 'Password needs a digit'  
                                            
print(validate_password('fho99hhgd'))
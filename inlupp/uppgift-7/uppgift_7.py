# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password:str):
    for character in password:                         #1 step: sort lenght
        if (len(password) < 8):
            return False  #ok!
        else:
            for character in password:                 #2 step: define parametres
                #print(character)
                digit_list =['0','1','2','3','4','5','6','7','8','9']    #python riconosce i numeri 

                if character in digit_list:       #cosa fare per controllare che ci sia un numero?
                    return  True
            return False


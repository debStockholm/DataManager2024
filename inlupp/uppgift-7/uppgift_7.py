# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password:str):
    for character in password:                         #1 steg: sortera langden -- ok!
        if (len(password) < 8):
            return False                               #2 steg: om forsta condition mottes:
        else:
            for character in password:                 # inne i en for loop som kollar om det finns en digit inne i password string
                digit_list =['0','1','2','3','4','5','6','7','8','9']    
                if character in digit_list:      
                    return  True
            return False                      #om password ar giltig: returnera True, annars False


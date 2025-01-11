# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(x:str): 
    if (x == x[::-1]):        #fanns flera satt att losa detta men sahar ar enlast. Fick hjalp av google
        return True           #kotrolleras helt enkelt om string ar lika framifran och bakifran gem att kolla index
    else:                                
         return False

  




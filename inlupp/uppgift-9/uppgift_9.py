# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(x:str):
    x = input('skriv ett valfritt ord:')    #slice?
    if (x == x[::-1]):
            return 'is palindrome'       #funkar ej riktigt
    else:
            return 'is NOT pal'


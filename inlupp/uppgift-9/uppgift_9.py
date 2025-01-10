# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

# def is_palindrome(x:str):
#     #x = input('skriv ett valfritt ord:')    #slice?
#     if (x == x[::-1]):
#         return True                  #input fuction doesnt work? #step 1
#     else:                                #altri modi per risolvere?
#         return False

# print(is_palindrome('raddewar'))     #il programma funziona, ma risultato : 'test failed?


def pal_2(y:str):
  ind = 0
  fin = len(y)-1


  while ind < fin:
    if y[ind] != y[fin]:
      return False
    ind += 1
    fin -= 1
  return True

print(pal_2("0989"))


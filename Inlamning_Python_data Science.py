# UPPGIFT 1

''' 
Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.
'''

#ta bort kommentar!

'''def is_odd(x=int):   #-> boolean
    x=8
    if x%2 == 1:
          print(True)
    else:
         print(False)

is_odd()'''


#UPPGIFT 2
#ta bort kommentar!
'''Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan

sum_list= [1,6,8,9,15]
print(sum(sum_list))      #FUNKAR

def sum_list(List_uppgift:list):  #->int
   print(sum(List_uppgift)) ???????????  

print(sum_list()  KOMPLETTERA!
'''


#UPPGIFT 3
'''Uppgift 3
 Hitta det största talet i en lista

List_uppgift3 = [12, 6, 9, 15, 36]

print(max(List_uppgift3)) #FUNKAR!
''' #ta bort kommentar!

'''def funktions_namn(variabel_namn: datatyp) -> returtyp:
    """
    Skriv beskrivning här.
     skriv din kod här - KOMPLETTERA!'''

#UPPGIFT 4

# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

fibonacci_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 0
b = 1
for x in range(10):
   x = a + b
   print(x)
   a = b
   b = x
   

#UPPGIFT 5
'''Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.
'''


'''List_uppgift5 = [0, 17, 18, 19, 20, 21, 34, 37, 51, 54]
for x in List_uppgift5:
    if x%2 == 0:
        print(x)   #FUNKAR'''
        
#UPPGIFT 6 
'''Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.
'''
'''List_uppgift6 = []
for i in range(0, 18):
      List_uppgift6.append(i)

for x in List_uppgift6:
    if x*2 <= 70:
      print(x, x*10)
    else: 
      print(' too big to be printed')   #vad menas med multiplikationtabell?'''
      

#UPPGIFT 7
'''Skapa en funktion validate_password(password) 
som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

Losenord_list = [input(str)]
if len(Losenord_list) < 8:
     print('Losenord behover minst 8 tecken')
elif len(Losenord_list) == 8 and Losenord_list == str:
     print('need a number')
else:
      print('losenord accepterat')'''

#UPPGIFT 8 
'''Räkna förekomsten av bokstäver

Beskrivning
Skapa en funktion count_letters(string) som returnerar en 
dictionary med varje bokstav som nyckel och antalet förekomster som värde

text_exempel = [input(str)]
dictionary = {}

for letters in text_exempel:
     
      if letters in dictionary:
        dictionary[letters] = dictionary[letters] + 1
        text_exempel.split(letters)
      else:
        dictionary[letters] = 1
        text_exempel.split(letters)
print(dictionary)     #FUNKAR - om inte input- SKAPA  funktion'''
      
            


#UPPGIFT 9 
'''Palindromkontroll

Beskrivning
Skapa en funktion is_palindrome(string) som kontrollerar 
om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).'''

'''exempel_string_pal = 'exempel string palindrome'
print(exempel_string_pal)'''



#palindrom

#UPPGIFT 10

'''Konvertera celsius till fahrenheit

Beskrivning
Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.'''

#UPPGIFT 11
'''Räkna orden i en text

Beskrivning
Skapa en funktion word_count(text) som returnerar antalet ord i en given text.'''

#UPPGIFT 12
'''Lagra data i en dictionary

Beskrivning
Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary
 där namnet är nyckeln och åldern är värdet.'''
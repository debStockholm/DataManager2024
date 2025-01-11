# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.
#forst skapas en variabel som kommer innehalla resultatet av for loopen. Resultat sparas i listan genom append() metod.
#till slut, returneras den nyskapade lista med udda siffror.

def filter_odd(list_numbers:list):
   new_list = []
   for x in list_numbers:
       if x % 2 == 0:
         new_list.append(x)
         
   return new_list

# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.
#CREA UNA FUNZIONE CHE MOSTRA UNA NUOVA LISTA DI NUMERI PARI:

def filter_odd(list_numbers:list):
   new_list = []
   for x in list_numbers:
       if x % 2 == 0:
         new_list.append(x)
         
   return new_list

#print(filter_odd([10, 7, 4, 6, 9]))
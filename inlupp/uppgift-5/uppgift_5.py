# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(list_numbers:list):
   for x in list_numbers:
    x = int(list_numbers)
    if x%2 == 0:
       return x
    else:
       return 'odd number'
    
print(filter_odd(6))

    
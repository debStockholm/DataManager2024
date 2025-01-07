# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(list_numbers:list):
   ny_lista=[]
   for x in list_numbers:
    if x%2 == 0:
       return x
    else:
       return 'odd number'
    
print(filter_odd(ny_lista([9, 0, 8, 12, 91, 67, 47, 42, 5])))

    
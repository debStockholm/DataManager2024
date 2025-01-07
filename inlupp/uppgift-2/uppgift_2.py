# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

'''def sum_list(ls:list) -> int:
   for x in ls:
      sum += x
   return sum

print(sum_list([7, 8, 9]))'''

def sum_list(ls:list) -> int:
    return (sum(ls))

print(sum_list([7, 8, 1, 9]))

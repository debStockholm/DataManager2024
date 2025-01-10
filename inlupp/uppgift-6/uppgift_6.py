# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.

def multiplication_table(x: int, y:int):  
  list_g=[]
  for num in range(1, y + 1):    #num appartiene a 'y'
    res= num*x
    list_g.append(res)
  return list_g                  #return sotto for per contare tutto
    
      #y + 1 conta l'ultimo numero in range
                             #come fare?
     
 
print(multiplication_table(3,4)) #x= int e list2: limite max della moltiplicazione


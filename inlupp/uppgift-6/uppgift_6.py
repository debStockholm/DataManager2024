# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.
# Skapa en variabel som kommer innehalla den nya listan (list_g); darefter en for loop dar multiplication ska borja pa 1 och 
# kors i ett specifik range (range: y:list + 1, sa att man raknar ocksa sista talet i range, ananrs loop slutat for tidigt). 
# #Det skapas en variable inom for loop (num) och en inne i loop (res) som returnerar 
# resultatet man far nar man kor multiplikation av ett tal i listan med den angivna input. res sparas i den nya listan.
def multiplication_table(x: int, y:int):  
  list_g=[]
  for num in range(1, y + 1):    #num appartiene a 'y'
    res= num*x
    list_g.append(res)
  return list_g                  
    

    

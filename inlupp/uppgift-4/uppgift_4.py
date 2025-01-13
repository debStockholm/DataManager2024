#vio
# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n:int):
   a = 0
   b = 1
   ny_list =[]
   if n == 0:
      return ny_list             #skaffade en lista for de nya tal
   elif n==1:
      return [0]
   else:
      ny_list.append(a)        #for loop med range returnerar fibonacci tal genom att overskriva variabler inne i loopen
      ny_list.append(b)
      for i in range(2,n):
         c = a + b             # (c)3 = 1(a) + 2(b)          #5(c) = 2(a) + 3(b)        #8(c) = 3(a) + 5(b)
         a = b                 # (a)1 = 2(b)                 #(a)2 = 3(b)               #3(a)= 5(b)
         b = c                 # (b)2 = 3(c)                 #(b)3 = 5(c)               #5(b) = 8(c)
         ny_list.append(c)
      return ny_list

print(fibonacci(15))
      
#------------------fibonacci med rekursion
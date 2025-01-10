#vio
# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def test_fibonacci(n:int):
   a = 0
   b = 1
   ny_list =[]
   if n == 0:
      return ny_list
   elif n==1:
      return [0]
   else:
      ny_list.append(a)
      ny_list.append(b)
      for i in range(2,n):
         c = a + b
         a = b
         b = c
         ny_list.append(c)
      return ny_list
      
print(test_fibonacci(10))
   
# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def test_fibonacci(exempel_list:list):
   a = 0                                   #help
   b = 1
for x in range(5):  
      x = a + b
      print(x)
     a = 0
     b = 1

print(test_fibonacci([0, 1, 1, 2, 3]))
   
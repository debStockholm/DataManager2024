'''print("hello")
print(6)
print('trying to commit')

o_mit_ = 'exempel GITHUB'
print(o_mit_)'''


'''List_uppgift5 = [0, 17, 18, 19, 20, 21, 34, 37, 51, 54]
for x in List_uppgift5:
    if x%2 == 1:
        print(x)'''

'''a = 0
b = 1
for c in range(10):
   c = a + b
   print(c)
   a = b
   b = c

a = 0
b = 1
for x in range(10):
   x = a + b
   print(x)
   a = b
   b = x
   '''
Losenord_list = [input(str)]
if len(Losenord_list) < 8:
     print('Losenord behover minst 8 tecken')
elif len(Losenord_list) == 8 and Losenord_list == str:
     print('need a number')
else:
      print('losenord accepterat')
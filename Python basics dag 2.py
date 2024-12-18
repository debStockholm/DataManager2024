print("hello, skapa ny mapp")

#git status
#git add  -A
#git commit -and 'meddelande' -- valfritt meddelande   'git commit -am' + 'valfritt meddelande'
#git pull origin  main/master
#git push origin main/master


 #----------TRY/EXCEPT for felsokning  + FINALLY

try: 
  x =str('hej')   # om TRY kod funkar: returneras TRY Kod i terminal
  print(x)

except:
  print('funkar ej') #om TRY kod INTE fungerar: returneras EXCEPT kod

 

  #--------------LISTOR

  #En insamling av flera varde av samma typ. Alla varden har specifika position och kan anropas genom det

Min_lista=(1, 4, 6 , 8, 9, 13)
print(Min_lista[3])   # exempel varde hamtat fran en lista
print(Min_lista[-1])   # -1 hamtar sista element av en lista eller range

Min_lista=(1, 4, 'textexempel', 6 , 'text11' , 8, 9, 13)
print(Min_lista[-2])   # -2 tecket hamtar varden fran en lista fran den sista till den forsta
print(Min_lista[2])

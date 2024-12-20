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

 

  #--------------LISTOR  --> dessa parentes=[]

  #En insamling av flera varde av samma typ. Alla varden har specifika position och kan anropas genom det

Min_lista=[1, 4, 6 , 8, 9, 13]
print(Min_lista[3])   # exempel varde hamtat fran en lista
print(Min_lista[-1])   # -1 hamtar sista element av en lista eller range

Min_lista2=[1, 4, 'textexempel', 6 , 'text11' , 8, 9, 13]
print(Min_lista2[-2])   # -2 tecket hamtar varden fran en lista fran den sista till den forsta
print(Min_lista2[2])
print(Min_lista2[0:])  #skriver hela listan fran den angivna startpukten
print(Min_lista2[2:6])

print(type(Min_lista))
print(type(Min_lista2))



#ny_lista3 = Min_lista.replace(1, 7)  #kan ej 'replace'
#print(ny_lista3)

#OBS nar man skapar en loop, variabel satts inne i forsta raden efter range, med ordet efter 'for' som kopplas, i ORDNING,
#till varje objekt i listan.  
#exempel: 
#FRUKT_LISTA=['banan', 'apple', 'apelsin']
#for fruit i FRUKT_LISTA:  ---> nar loop kors, *fruit* kopplas forst till banan, sen till apple, sen till apelsin

#man kan skapa tva variabel, och da den andra kors efter den forsta -dvs den tar andra varden i loopen
#FRUKT_LISTA=['banan', 'apple', 'apelsin']
#for fruit, frutta i FRUKT_LISTA:  ---> nar loop kors, *fruit* kopplas forst till banan, sen till apple, sen til
#frutta kopplas till 'apple', 'apelsin'

#-----OVNING



        #skriv ut varje tredje item
reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

for index, number in enumerate(reallyLongList):
    print(index,number)




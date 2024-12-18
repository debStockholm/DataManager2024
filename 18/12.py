

Lista1 = ['morgongava', 'undersaker', 'teckomantorp', 'manasken', 'buslatt']

for stadnamn in (Lista1): #skriv ut alla stader i en FOR LOOP
    print(stadnamn)
#___________
Lista1.append('Hylle')   #adderar ett varde
print(Lista1)
#___________
Lista1.pop(1)  #tar bort ett varde - indexnummer anvands for borttagning
print(Lista1)

del Lista1[1]  #alternativt borttagning
print(Lista1)
#____________

List2 =[1,3,4,7,9]   #summera tal i en lista
Summalista= sum(List2)
print(Summalista)
#____________

Listanamn =['anna','sylvia', 'angelic', 'ebba', 'klara']

for namn in Listanamn:
    if namn == 'belle':
      print(namn)
    else:
       print('no')

#____________
for city in Lista1:
   firstletter = city[0] #0 refererat till forsta item bokstav 
   capitalized = firstletter.upper
   city[0] =capitalized
   print(city)







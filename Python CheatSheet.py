#SYNTAX I PYTHON
"""kraver inga semikolon (;)
kodblock skapas genom intendering (vanlig intedering 4 mellansag eller TAB)
intedering ar viktigast!
baserad pa engelska spraket"""

#**********************GRUNDLAGGANDE SYNTAX 17/12/2024*********************

#--------PRINT
'''print kommando skriver ut objekt/text/varde
   vanliga fel: glomt intedering, glomd citattecken ("), felstavad nyckeord (print)'''

#--------VARIABEL
''' variablar lagrar varde i koden.
"Placeholder". 
Ligger alltid till vanster, vardet till hoger
Variabelnamn ska skapas enloigt vissa villkor
Ar CASE sensitive (NAMN ar inte samma som Namn)
Datatypen av variabeln definieras direkt pa Python nar den tillsatts (DYNAMISKT TYPAT), 
men kan forandras, eller 'deletas' (del variabelnamn)

'''
exempelvariabeln = 'exempel1'
print(exempelvariabeln)

#del exempelvariabeln
#print(exempelvariabeln)  raderar en variabel for gott

#--------DATATYPER
'''Framsta datatyper i Python: 
heltal (5), 
flyttal (8.6), 
string ('Hejsan Hejsan') 
och boolean (true, false)'''

#hamta datatyp av ett objekt =  
# print(type(variabelnamn))
'''exempel
Blomma = 'angsyra'
Alder = 50
Procentsalj = 4.5'''

#print(type(Blomma))
#print(type(Procentsalj)) osv

'''om samma variabel blir tilldelad tva varden, programmet sparar det sista vardet'''

x = 98
x = 28   
x = 12
print(x)



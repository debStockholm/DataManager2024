#SYNTAX I PYTHON
"""kraver inga semikolon (;)
kodblock skapas genom intendering (vanlig intedering 4 mellanslag eller TAB)
intedering ar viktigast!
baserad pa engelska spraket"""

#**********************GRUNDLAGGANDE SYNTAX 17/12/2024*********************

#--------PRINT
'''print kommando skriver ut objekt/text/varde
exempel:
    |uncomment och kor:|
print('hejsaaaaan')
   
   vanliga fel: glomt intedering, glomd citattecken ("), felstavad nyckeord (print)'''

#--------VARIABEL
''' variablar lagrar varde i koden.
"Placeholder". 
Ligger alltid till vanster, vardet till hoger
Variabelnamn ska skapas enloigt vissa villkor
Ar CASE sensitive (NAMN ar inte samma som Namn)
Datatypen av variabeln definieras direkt pa Python nar den tillsatts (DYNAMISKT TYPAT), 
men kan forandras, eller 'deletas' (del variabelnamn)

exempel:
    |uncomment och kor:|
exempelvariabeln = 'exempel1'
print(exempelvariabeln)

#del exempelvariabeln ---> raderar en variabel for gott
#print(exempelvariabeln)''' 

#--------DATATYPER
'''Framsta datatyper i Python: 
heltal (5), 
flyttal (8.6), 
string ('Hejsan Hejsan') 
och boolean (true, false)'''

#hamta datatyp av ett objekt =  
# print(type(variabelnamn))
'''exempel:
    |uncomment och kor:|
Blomma = 'angsyra'
Alder = 50
Procentsalj = 4.5

print(type(Blomma))
print(type(Procentsalj)) osv'''


#om samma variabel blir tilldelad tva varden, programmet sparar det sista vardet
'''exempel:
    |uncomment och kor:|
x = 98
x = 28   
x = 12
print(x)  #returnerar 12'''

#man kan andra variabeln typ (casting) genom inbyggda funktioner: str, int, float, boolean 
'''exempel:
    |uncomment och kor:|
x = 6
x = str(6)
print(x)
print(type(x)) returneras '6', som egentligen en heltal, men andrades till string'''

#---------NUMMER OCH MATEMATIK
'''
+   Addition            x + y
-   Subtraktion         x - y 
*   Multiplikation      x * y
/   Division (flyttal)  w / y   _______returnerar flyttal, se exempel      
//  Heltalsdivision     w// y   _______returnerar hur manga ganger 'y' finns i 'x', se exempel
%   Modulus             w % y   _______returerar resten av en heltaldivision, se exempel 
**  Exponentiering      w **y   _______exponent


exempel:
|uncomment och kor:|
FLYT= 35/4
print(FLYT, 'som vanlig division')  

HT= 35//4
print(HT ,'som heltaldivision')

MOD = 67%10
print(MOD)   ge resten av 7, da 10 finns 6 ggr i talet 67, och 7 ar det som ar kvar efter
'''


#Binara system medfor att vissa decimaltal avrundas fel, detta loses genom att:
'''
- round() avrundar flyytal ---> round(x + y, 2)  ("=hur manga decimaler)
- Pythons inbyggda bibliotek
- konvertera decimaler till heltal, och berakna darefter
'''

print(bool(9)) 
print(bool(-9.45312)) 
print(bool("Hej")) 
print(bool(0.6))
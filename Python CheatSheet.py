#SYNTAX I PYTHON
"""kraver inga semikolon (;)
kodblock skapas genom intendering (vanlig intedering 4 mellanslag eller TAB)
intedering ar viktigast!
baserad pa engelska spraket"""


#**********************GRUNDLAGGANDE SYNTAX 17/12/2024*********************


#------------------------------------------------------PRINT
'''print kommando skriver ut objekt/text/varde
exempel:
    |uncomment och kor:|
print('hejsaaaaan')
   
   vanliga fel: glomt intedering, glomd citattecken ("), felstavad nyckeord (print)'''



#-----------------------------------------------------VARIABEL
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



#---------------------------------------------------DATATYPER
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

#kor och kolla boolean fuktioner, de ar lite speciella:
'''exempel:
    |uncomment och kor:|
print(bool(9)) 
print(bool(-9.45312)) 
print(bool("Hej")) 
print(bool(0.6))'''



#-------------------------------------------NUMMER OCH MATEMATIK
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

#-------------------------------------------STRANGAR
'''En sträng (string) är en följd av tecken som omges av enkla (') eller dubbla (")
citattecken.
En sträng kan vara tom ("").
Strängar är som listor av tecken med en indexering som startar från [0].
Använd hakparenteser [ ] för att hämta tecken från en sträng.'''


'''
exempel:
   |uncomment och kor:|

text = "Python"
print(text[0])  # P
print(text[1])  # y
print(text[-1]) # n    (sista tecknet, '-' returnerar index bakat)'''

#strangfunktioner:
'''
upper()       Gör strängen till versaler            ___.upper()     
lower()       Gör strängen till gemener             ___.lower() 
strip()       Tar bort mellanslag runt strängen     ___.strip()
replace()     Byter ut en del av strängen           ___.replace("_", "**") 
split()       Delar strängen vid mellanslag         ___.split()'''


'''exempel
#  |uncomment och kor:|

textexempel=('Hej kompis, hur ar laget?')

print(textexempel.upper())

print(textexempel.split())

print(textexempel.replace('Hej', 'Tjana'))
'''
#F-strings är ett enkelt sätt att kombinera variabler och text (formatering). 
# Lägg till 'f' före strängen och {} runt variabler.
'''exempel
  #|uncomment och kor:|
name='AsiaBea'
age= 37
Stad = 'Oslo'

print(f'Hej {name}, du som ar {age}! Vi ska bo i {Stad}!')  #om man inte tillagger 'f', allt kors som en string!
'''
#-------------------------------------------------BOOLEANER
'''
En boolean är en datatyp som representerar True eller False.
Används för att avgöra om något är sant eller falskt.
Booleanvärden används ofta i if-satser och loopar'''

#boolean logik
'''and              True om båda är True          x > y and x < a
   or               True om en är True            x > y or y < a
   not              Inverterar True/False         not (x > y)
   '''

#--------------------------------------------------OPERATORER
#aritmetiska:
'''
+
-
*
/
%
'''
#jamforelse
'''
==          Är lika med         x == y
!=          Är inte lika med    x != y
>           Större än           x > y
<           Mindre än           x < y
'''
#logiska 

''' and, or, not  - eller en kombination an nagra/alla'''


#--------------------------------------FELHANTERING - TRY/EXCEPT + FINALLY
'''
Använda 'try' och 'except'(catch i andra språk) för att fånga fel.
I EXCEPT-raden kan programmerare ange vilket fel vill man felsoka.

Om inget fel hittas, returneras ingenting;
om fel HITTAS, returneras EXCEPT satsen
FINALLY kör alltid en kod, oavsett om ett fel inträffade eller inte.'''

#exempel
#  |uncomment och kor:|

'''try:
 x = int('hoppa') # Försöker konvertera en sträng till heltal
except:
 print("Ett fel uppstod.")     #man kan INTE ha en string som en int

try:
  x = str(True) 
except:
  print("Ett fel uppstod.")    #man kan INTE ha en string som en bool'''

try:
  x = str(42) 
except:
  print("Ett fel uppstod.")

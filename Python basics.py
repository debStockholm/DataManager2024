#-------------               hamta datatyp
print(56+9+79)
exem1 = ('exempel programmering')
print(type(exem1))


x=10
y=20

#----------------------     github commit push
exempel_GITHUB = 'denna fil'
xh = 'exempel1'
xy = 673

variabel1 ='123'
print(variabel1)

y=2
print(int(variabel1)*y)

#-----------------------   numbers i Python
exempelsiffra = 98.08
exempelsiffra_ny=int(exempelsiffra)
print(exempelsiffra_ny)

#-------------------------- mathematical operations

a = 3 + 2
b = 26//3   #'hur manga ggr kan delas med hela nummer'
b1 =28//3 
b2 =27//3
c = 5 % 2   #resten vid division
d = 5 ** 2  #uppe till 2
e = 5 ** 3  #uppe till 3


print(a)
print(b)
print(b1)
print(b2)
print(c)
print(d)
print(e)

#---------------------- math operations 2
x=10
y=3


print(x / y)
print(x//y)   #'hur manga ggr kan delas med jamnt nummer'
print(x % y)   #resten vid division
print(x ** y)  #uppe till ---

#-------------------------- 

pi = 3.14
y=int(pi)
print(y)  #convert pi till heltal

int5 = 5
int5dec =float(int5)
print(int5dec)    #convert heltal till flyttal

#------------------- avrundning

ui= 0.1 + 0.2
print(ui)

print(round(ui , 4))

tal1 = 0.1
tal2 = 0.2

tal1 = int(tal1 * 10)
tal2 = int(tal2 * 10)
print(tal1 + tal2)

avrundat= (tal1 + tal2)/10
print(avrundat)

#----------------1--------- input: arbeta i terminalen (ta bort kommentar fran alla rader
#  for att kora detta)

#x = input('skriv tal ett:') #terminalfraga 1
#y = input('skriv tal tva:') #terminalg
#summa = int(x) + int(y)  #input resultat koverteras till heltal
#print(f'summan ar: {summa}')  #anvands for concatenation av olika datatyper -t.ex str + variabel


#----------------------    
x = 42
text = 'tal bor blivit en', str(x)
print(text)


#------------  index i strangar

text = 'data science'
print(text[0])  #hamtar del av strangen som ligger i den platsen inom []
print(text[-1]) #'-1' hamtar sista tecket

text = text.strip()
print(text[0:6])  #hamta x-antal tecken

#-------------strangfunktioner

#upper() = koverterar strang till VERSALER
#lower() = koverterar till gemener
#strip() = delar strangen i mindre delar
#replace() = ersatter en del med den andra
#splin () = ta bort mellanslag
#f = formatering; Lagger 'f' i borjan av strangen, och variabeln i {strangexempel}

#--------

text = 'Python ar roligt  '
print(text)

no_whitespace =text.strip() #varje funktion behover en ny variable - t.ex:no_whitespace
print(no_whitespace) #efter print(variabeln)

ersattning = no_whitespace.replace('roligt', 'fantastisk')  #skaffas ny variabel
print(ersattning)   #print(nyvariabel)

nyVERS = ersattning.upper()   #skapa ny variabel2
print(nyVERS)   #print(ny variabel2)

nygem = ersattning.lower()
print(nygem)
#--------------------- input funct (ta bort kommentar for att kora den)
a = input('namn ')
b = input('alder ')

info = str(a) , int(b)
text1 =(f'Hej {a}. Du ar {b} ar gammal').upper()
print(text1)

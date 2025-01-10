# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students:list):     
    #Student_list = students.index()   
    ny_Stud_dict = {}

    for namn, alder in students:               
       ny_Stud_dict[namn]=alder
    return ny_Stud_dict
       #come faccio ad assicurarmi che le variabili raccolgano il valore esatto dall lista? 
                                               # namn = un nome, alder = eta 

print(create_student_register([('anna', 17), ('Emma', 16)]))


'''procedura:
creare  nuovo dict -> Student_list = {} a cui aggiungere dati da una lista

devo usare slice? per dividere elementi in una lista?'''


# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students:list):        
    ny_Stud_dict = {}                        #steg 1: skapar ny dict
    for namn, alder in students:             #kor variablar som motsvarar varje varde i tuple
       ny_Stud_dict[namn]=alder              # da tuple splittras automatiskt och adderas pa ratt satt i min nya dict
    return ny_Stud_dict






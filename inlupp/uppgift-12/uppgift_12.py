# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students:list):        
    ny_Stud_dict = {}
    for namn, alder in students:               
       ny_Stud_dict[namn]=alder
    return ny_Stud_dict
      
print(create_student_register([('anna', 17), ('Emma', 16)]))





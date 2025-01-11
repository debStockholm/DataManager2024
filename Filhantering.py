#text book: Data visualisation with Python for beginners: Muhammad Malik, AI publishing

#---------------------------------FILHANTERING----------------------------------
#-------TEXT--------------------------
'''with open('data_txt', 'w') as file:
    file.write('Name, Age, City\nSofia, 25, Stockholm\n\nBjorn, 34, Goteborg\n')


with open('data_txt', 'r') as file:
    print(file.read())'''

#---------------CSV------------------------------------
'''with open("data_exempel.csv", "w") as file_exempel:
 
 file_exempel.write('Product, Price, Stock\nBanana, 3, 200\nApple, 5, 100\nOrange, 4, 150')
 print(file_exempel)  #---> skrev inne i file_exempel.cvs, kolla!


 import csv  #----> ska alltid vara med!

with open('data_exempel.csv', 'r') as file_reader_ex:
    lines_in_file = csv.reader(file_reader_ex)
    for rows in lines_in_file:
       print(rows)

with open('data_exempel.csv', 'r') as file_reader_ex:
   add_category = csv.reader(file_reader_ex)
   new_category = list(add_category) #detta gor att data blir en list type!

new_category[0]= new_category.append('CAtegory')
print(file_reader_ex)


'''


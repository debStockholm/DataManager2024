import csv
#----------------------------CREATE
new_file_creating=[                                      #creo una lista dati da inserire in un nuovo file: 
    ["name", "price", "category"],
    ['bread', 2, 'baked goods'],
    ['pasta', 3,'dry'],
    ['cereals', 3, 'dry'],
    ['yoghurt', 1.5, 'diary'],
    ['juice', 1.5, 'diary'],
    ['eggs', 2.5, 'fresh'],
    ['jam', 2, 'canned goods']
]

# salvo i miei dati u un nuovo doc: 'nome doc' + 'w' che scrive i dati
# csv.writer= funzione che scrive nel doc
# csv.writerows = funzione che scrive in righe: OBS obbligatorio! Altrimenti non viene scritto nulla
with open('exempel_csvfile.csv', 'w') as exempel_csv_file:   #'with' chiude automaticamente i files dopo le operazioni
    writer = csv.writer(exempel_csv_file)                    #senza 'with': file.close(filnamn)
    writer.writerows(new_file_creating)

print(exempel_csv_file)

#-----------------------READ
with open('exempel_csvfile.csv', 'r') as read_file:   #per scrivere il contenuto di un file csv: 
    reading_1= csv.reader(read_file)                  # 1 step: assegnare la lettura del file ad una variabile;
    for rows in reading_1:                            # 2 step: creare un for loop che attraversi tutto il file
     print(rows)                                   # 3 step: print tutte le righe

#----------------------UPDATE
with open('exempel_csvfile.csv', 'r') as update_file:   #per scrivere il contenuto di un file csv: 
    update_1= csv.reader(update_file) 
    rows = list(update_1)                 #dev'essere tutto messo come lista?

#updating:
    for row in rows:
      w)
       if row[0] == 'bread':         #WHY DOES THIS NOT WORK? same column number and existing index
          row[0] = 'pastry'

    print(row)

import pandas as pd

'''with open('excel_blad_34.xlsx', 'r') as ovningfil:
      Innehall= pd.read_excel('excel_blad_34.xlsx')                             #1 step: leggo il file
      cleaned_excelblad12 = Innehall.dropna(how='all')                          #2 step: 'pulisco' rows
      cleaned_excelblad12 = cleaned_excelblad12.dropna(axis = 1 , how= 'all')   #3 step: pulisco le colonne dal file dove 
                                                                                #ho pulito le rows (axis = 1 oppure 0, 0= non 'pulisce niente')

      print(cleaned_excelblad12)
      ovningfil.close()'''

file_1 = pd.read_excel('excel_blad_12.xlsx')                                   #4 step: merging files 
file_2 = pd.read_excel('excel_blad_34.xlsx')                                   #merging requires a common column (as in SQL) 
merged_files_attempt = pd.merge(file_1, file_2, on= 'Name', how='left')  
#print(merged_files_attempt)  

#5 step: cleaning files after merging
cleaned_merge = merged_files_attempt.dropna(how='all')
cleaned_merge = cleaned_merge.dropna()
print(cleaned_merge) 

#in Pandas df, no need to close the files (?)

'''#save the new file on a new created Excel _file:
cleaned_merge.to_excel('Successfull attempt.xlsx', index=False)'''      #step 5:save the new file after 'cleaning'


Success_merge_open= pd.read_excel('Successfull attempt.xlsx')           #step 6: open the new created file
print(Success_merge_open)
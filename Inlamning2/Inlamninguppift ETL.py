import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#MATSVINN FORSKOLOR I SODERTALJE   - JMF MELLAN JANUARI - FEBRUARI 2024

#_________________________________LOAD________________________________________


df = pd.read_csv('Inlamning2\Rapportering svinn förskola januari.csv')
df2 =pd.read_csv('Inlamning2\Rapportering svinn förskola februari.csv')
ny_df = pd.DataFrame(data=df)
ny_df2= pd.DataFrame(data=df2)
#print(ny_df.head(), ny_df2.head())


#Ta fram en lista av alla kolumner av bada dataset:

'''columns = ny_df.columns
for column in columns:
     print(column) 

columns2 = ny_df2.columns
for column1 in columns2:
     print(column1) '''

#_____________________________________TRANSFORM________________________________________

#merging de tva dataset
merging_files= pd.merge(ny_df, ny_df2, on = 'Enhet', how = 'outer')
'''print(merging_files)'''
cleaned_data = merging_files.rename(columns={'År_y': 'År', 'Kökssvinn(i kg)_x':'Kökssvinn(i kg) januari', 'Kökssvinn(i kg)_y':'Kökssvinn(i kg) februari'})


#byta namn till kolumner och spara enbart de mest relevanta
cleaned_data_2 =cleaned_data.drop(['Kategori_x', 'Kategori_y', 'Månad_x', 'Månad_y', 'År_x'], axis=1)
cleaned_data_2['År'] = cleaned_data_2['År'].astype('Int64')  #Int64 function to handle a float column with some Nan (I dont wanna fill it)
'''#print(cleaned_data_2.head(50)) '''


#jag vill visa matsvinnstrend jamforelse over tid. Da tar jag bort de raderna dar den ena och bade varde ar Nan:
cleaning_data_3 = cleaned_data_2.dropna(subset=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'])
'''print(cleaning_data_3.head())'''   

cleaning_data_3['Matsvinn utveckling i kg'] = cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari']
cleaning_data_3['Matsvinn forandring i %']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])/cleaning_data_3['Kökssvinn(i kg) januari'] * 100
cleaning_data_3['Matsvinn forandring i %'] = cleaning_data_3['Matsvinn forandring i %'].astype(int) 
print(cleaning_data_3)


#skapar agg() fuktion for insikter om matsvinn hos Sodertalje forskolor i Januari samt februari:

aggregation_januari= cleaning_data_3['Kökssvinn(i kg) januari'].agg(['sum', 'mean', 'min', 'max'])
aggregation_februari= cleaning_data_3['Kökssvinn(i kg) februari'].agg(['sum', 'mean', 'min', 'max'])

print(aggregation_januari.round(1), aggregation_februari.round(1))
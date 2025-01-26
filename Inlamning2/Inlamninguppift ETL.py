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

#Ta fram en lista av alla kolumner:

columns = ny_df.columns
for column in columns:
     print(column) 

columns2 = ny_df2.columns
for column1 in columns2:
     print(column1) 

#_____________________________________TRANSFORM________________________________________

merging_files= pd.merge(ny_df, ny_df2, on = 'Enhet', how = 'outer')
print(merging_files)

removed_columns= 'Kategori_x', 'Kategori_y', 'År'
cleaning_columns = merging_files.drop(['Kategori_x', 'Kategori_y', 'År_x'], axis=1)
print(cleaning_columns)  #piu o meno funziona

# # cleaning_2 = cleaning_columns.drop([column for column in cleaning_columns.columns if 'Kontor' in column], axis=1)  #working
# # print(cleaning_2.head) 

# # print(cleaning_2.columns)     #working, now I can work with only datas for 'Lokal'

# # lokales_data= pd.DataFrame(data=cleaning_2)

# # kolumner = cleaning_2.columns
# # for column in kolumner:
# #      print(column)

# # print(lokales_data)

# cleaning_2 = pd.DataFrame([K, 2019, 1668421,

# ])

# # print(cleaning_columns.columns)
# # print("ok thats working, residens columns removed")    # work so far.


# #ta bort ytterligare kolumner (kontorkolumner):

# # tabort_ord = 'kontor'
# # cleaning_columns2 = cleaning_columns.drop([column for columns2 in cleaning_columns.columns if tabort_ord in column], axis=1)
# # print(cleaning_columns2.head(5))




# # tabort_Lokal = 'Lokal'
# # tabort_lokal = 'lokal'

# # cleaning_columns2 = ny_df.drop([column for column in cleaning_columns.columns if tabort_Lokal in column], axis=1)
# # print(cleaning_columns2.head(5))

# # print("removed columns with 'Lokal' ")
# # cleaning_columns3 = ny_df.drop([column for column in cleaning_columns2.columns if tabort_lokal in column], axis=1)
# # print(cleaning_columns3.head(10))
# # print("removed columns with 'lokal' ")


# #print(dataam)'''
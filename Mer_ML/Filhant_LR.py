import pandas as pd
import numpy as np


#MATSVINN(kokssvinn) FORSKOLOR I SODERTALJE   - JAMFORELSE MELLAN JANUARI -  APRIL 2020



#_________________________________LOAD________________________________________


df = pd.read_csv('Mer_ML/2020 Januari Förskola.csv')
df2= pd.read_csv('Mer_ML/2020 Februari Förskola.csv')
df3= pd.read_csv('Mer_ML/2020 Mars Förskola.csv')
df4= pd.read_csv('Mer_ML/2020 April Förskola.csv')

#print(df, df2, df3, df4)
df.columns = df.columns.str.strip()
df2.columns = df2.columns.str.strip()
df3.columns = df3.columns.str.strip()
df4.columns = df4.columns.str.strip()


ny_df=df.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn g/barn/dag'], axis=1)
ny_df2=df2.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn g/barn/dag'], axis=1)
ny_df3=df3.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn g/barn/dag'], axis=1)
ny_df4=df4.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn g/barn/dag'], axis=1)

#print(ny_df, ny_df2, ny_df3, ny_df4)
#print(ny_df.head(2), ny_df2.head(2))
#merging de forsta tva dataset:
merging_files= pd.merge(ny_df, ny_df2, on = 'Enhet', how = 'inner')
#print(merging_files)
merging_files_2= pd.merge(merging_files, ny_df3, on = 'Enhet', how = 'inner')
#print(merging_files_2)

merging_files_2=merging_files_2.rename(columns={'Kökssvinn (kg)_x': 'jan_20', 'Kökssvinn (kg)_y': 'feb_20',  'Kökssvinn (kg)': 'mars_20'})
merge2020= pd.merge(merging_files_2, ny_df4, on = 'Enhet', how = 'inner')
merge2020=merge2020.rename(columns={'Kökssvinn (kg)': 'apr_20'})
#print(merge2020)

'''columns = merge2020.columns
for column in columns:
     print(column) '''

matsvinn_2020_mean=merge2020[['jan_20','feb_20','mars_20', 'apr_20'] ].agg('mean')
matsvinn_2020_mean=matsvinn_2020_mean[['jan_20','feb_20','mars_20', 'apr_20']].round(2).astype(float)
matsvinn_2020_sum=merge2020[['jan_20','feb_20','mars_20', 'apr_20'] ].agg('sum')
matsvinn_2020_sum=matsvinn_2020_sum[['jan_20','feb_20','mars_20', 'apr_20']].astype(int)

print(matsvinn_2020_mean)
print(matsvinn_2020_sum)

#matsvinn_2020_mean.to_csv('Medel_matsvinn_2020.csv', index=False)
matsvinn_2020_sum.to_csv('Sum_matsvinn_2020.csv', index=False)

# df = pd.read_csv('2021 jan.csv')
# df2= pd.read_csv('2021 febr.csv')
# df3= pd.read_csv('2021 mars.csv')
# df4= pd.read_csv('2021 april.csv')

# #print(df, df2, df3, df4)

# df.columns = df.columns.str.strip()
# df2.columns = df2.columns.str.strip()
# df3.columns = df3.columns.str.strip()
# df4.columns = df4.columns.str.strip()


# ny_df=df.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn/gäst/dag'], axis=1)
# ny_df2=df2.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn/gäst/dag'], axis=1)
# ny_df3=df3.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn/gäst/dag'], axis=1)
# ny_df4=df4.drop(['Kategori', 'Månad', 'År', 'Antal dagar', 'Antal ätande på plats', 'Kökssvinn/gäst/dag'], axis=1)

# #print(ny_df, ny_df2, ny_df3, ny_df4)
# #print(ny_df.head(2), ny_df2.head(2))

# merging_files= pd.merge(ny_df, ny_df2, on = 'Enhet', how = 'inner')
# merging_files_2= pd.merge(merging_files, ny_df3, on = 'Enhet', how = 'inner')
# #print(merging_files_2)
# merging_files_2=merging_files_2.rename(columns={'Kökssvinn (i kg)_x': 'jan_21', 'Kökssvinn (i kg)_y': 'feb_21',  'Kökssvinn  (i kg)': 'mars_21'})
# merge2021= pd.merge(merging_files_2, ny_df4, on = 'Enhet', how = 'inner')
# merge2021=merge2021.rename(columns={'Kökssvinn  (i kg)': 'apr_21'})
# #print(merge2021)

# # columns = merge2021.columns
# # for column in columns:
# #      print(column) 

# matsvinn_2021_mean=merge2021[['jan_21','feb_21','mars_21', 'apr_21'] ].agg('mean')
# matsvinn_2021_mean=matsvinn_2021_mean[['jan_21','feb_21','mars_21', 'apr_21']].round(2).astype(float)
# matsvinn_2021_sum=merge2021[['jan_21','feb_21','mars_21', 'apr_21'] ].agg('sum')
# matsvinn_2021_sum=matsvinn_2021_sum[['jan_21','feb_21','mars_21', 'apr_21']].astype(int)


# print(matsvinn_2021_mean)
# print(matsvinn_2021_sum)

# matsvinn_2021_mean.to_csv('Medel_matsvinn_2021.csv', index=False)
#matsvinn_2021_sum.to_csv('Sum_matsvinn_2021.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#MATSVINN FORSKOLOR I SODERTALJE   - JMF MELLAN JANUARI - FEBRUARI 2024

#_________________________________LOAD________________________________________


df = pd.read_csv('Inlamning2\Rapportering svinn förskola januari.csv')
df2 =pd.read_csv('Inlamning2\Rapportering svinn förskola februari.csv')
df3= pd.read_csv('Inlamning2\Rapportering svinn förskola mars.csv')
ny_df = pd.DataFrame(data=df)
ny_df2= pd.DataFrame(data=df2)
ny_df3= pd.DataFrame(data=df3)
#print(ny_df.head(), ny_df2.head(), ny_df3.head())


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
ny_merging_files= pd.merge(merging_files, ny_df3, on = 'Enhet', how = 'outer')
'''print(ny_merging_files)'''

 #byta namn till kolumner och spara enbart de mest relevanta - drop allt annat
cleaned_data =ny_merging_files.drop(['Kategori_x', 'Kategori_y', 'Kategori' , 'Månad_x', 'Månad_y', 'Månad', 'År_x', 'År_y', 'År'], axis=1)
cleaned_data_2 = cleaned_data.rename(columns={'Kökssvinn(i kg)_x':'Kökssvinn(i kg) januari', 'Kökssvinn(i kg)_y':'Kökssvinn(i kg) februari', 
 'Kökssvinn(i kg)':'Kökssvinn(i kg) mars'})
print(cleaned_data_2)



#jag vill visa matsvinnstrend jamforelse over tid. Da tar jag bort de raderna dar den ena och bade varde ar NaN:

cleaning_data_3 = cleaned_data_2.dropna(subset=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari','Kökssvinn(i kg) mars'])
#print(cleaning_data_3.head(60))   

cleaning_data_3['Matsvinn forandring jan-feb i %']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])/cleaning_data_3['Kökssvinn(i kg) januari'] * 100
cleaning_data_3['Matsvinn forandring feb-mars i %']= (cleaning_data_3['Kökssvinn(i kg) mars'] - cleaning_data_3['Kökssvinn(i kg) februari'])/cleaning_data_3['Kökssvinn(i kg) februari'] * 100
cleaning_data_3['Matsvinn forandring jan-mars i %']= (cleaning_data_3['Kökssvinn(i kg) mars'] - cleaning_data_3['Kökssvinn(i kg) januari'])/cleaning_data_3['Kökssvinn(i kg) januari'] * 100
cleaning_data_3['Matsvinn forandring jan-feb i %'] = cleaning_data_3['Matsvinn forandring jan-feb i %'].astype(int) 
cleaning_data_3['Matsvinn forandring feb-mars i %'] = cleaning_data_3['Matsvinn forandring feb-mars i %'].astype(int) 
cleaning_data_3['Matsvinn forandring jan-mars i %'] = cleaning_data_3['Matsvinn forandring jan-mars i %'].astype(int) 

print(cleaning_data_3)
#selc= cleaning_data_3[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari', 'Kökssvinn(i kg) mars', 'Matsvinn forandring jan-mars i %', 'Matsvinn forandring jan-feb i %', 'Matsvinn forandring feb-mars i %']]
#print(selc)
#print(cleaning_data_3.dtypes)

# ny_dataset_for_graphs = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-mars i %'] > 0 & 
#                               cleaning_data_3['Matsvinn forandring jan-mars i %'] < 15]
# print(ny_dataset_for_graphs)

# cleaning_data_3['Medel_matsvinn_utveckl. %']= cleaning_data_3[['Matsvinn forandring jan-feb i %', 'Matsvinn forandring feb-mar i %']].agg('mean', axis =1)
# print(cleaning_data_3)
# filter_for_graphs = cleaning_data_3['Matsvinn forandring jan-mars i %']
# data_for_graphs = filter_for_graphs[(filter_for_graphs > 0) & (filter_for_graphs < 15)]
# print(data_for_graphs)
   
# # aggregation_februari= cleaning_data_3['Kökssvinn(i kg) februari'].agg(['sum', 'mean', 'min', 'max'])

# sns.barplot(data= cleaning_data_3, data_for_graphs, x='Enhet', y = data_for_graphs)
# plt.title('preliminar linjeplot')
# plt.show()

#filtering= cleaning_data_3['']
'''cleaning_data_3.sort_values(by='', ascending= FAlse/true)'''
'''df.agg(func, axis=1, *args, **kwargs)'''
# matsvinn_okning = cleaning_data_3['Matsvinn forandring feb-mar i %'] > cleaning_data_3['Matsvinn forandring jan-feb i %']
# matsvinn_minskning = cleaning_data_3['Matsvinn forandring feb-mar i %'] < cleaning_data_3['Matsvinn forandring jan-feb i %




# #skapar agg() fuktion for insikter om matsvinn hos Sodertalje forskolor i januari samt februari:

# aggregation_januari= cleaning_data_3['Kökssvinn(i kg) januari'].agg(['sum', 'mean', 'min', 'max'])
# aggregation_februari= cleaning_data_3['Kökssvinn(i kg) februari'].agg(['sum', 'mean', 'min', 'max'])

# print(aggregation_januari.round(1), aggregation_februari.round(1))
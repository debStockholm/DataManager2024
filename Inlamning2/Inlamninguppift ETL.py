import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#MATSVINN FORSKOLOR I SODERTALJE   - JMF MELLAN JANUARI - FEBRUARI 2024

#_________________________________LOAD________________________________________


df = pd.read_csv('Inlamning2\Rapportering svinn förskola januari.csv')
df2 =pd.read_csv('Inlamning2\Rapportering svinn förskola februari.csv')
#df3= pd.read_csv('Inlamning2\Rapportering svinn förskola mars.csv')
ny_df = pd.DataFrame(data=df)
ny_df2= pd.DataFrame(data=df2)
#ny_df3= pd.DataFrame(data=df3)
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
#ny_merging_files= pd.merge(merging_files, ny_df3, on = 'Enhet', how = 'outer')
'''print(ny_merging_files)'''

 #byta namn till kolumner och spara enbart de mest relevanta - drop allt annat
cleaned_data =merging_files.drop(['Kategori_x', 'Kategori_y', 'Månad_x', 'Månad_y', 'År_x', 'År_y'], axis=1)
cleaned_data_2 = cleaned_data.rename(columns={'Kökssvinn(i kg)_x':'Kökssvinn(i kg) januari', 'Kökssvinn(i kg)_y':'Kökssvinn(i kg) februari'})
#print(cleaned_data_2)


#jag vill visa matsvinnstrend jamforelse over tid. Da tar jag bort de raderna dar den ena och bade varde ar NaN:

cleaning_data_3 = cleaned_data_2.dropna(subset=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'])
#print(cleaning_data_3.head(60))   
cleaning_data_3['Kökssvinn(i kg) skillnad']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])
cleaning_data_3['Kökssvinn(i kg) skillnad']= cleaning_data_3['Kökssvinn(i kg) skillnad'].astype(int)
cleaning_data_3['Matsvinn forandring jan-feb i %']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])/cleaning_data_3['Kökssvinn(i kg) januari'] * 100
cleaning_data_3['Matsvinn forandring jan-feb i %'] = cleaning_data_3['Matsvinn forandring jan-feb i %'].astype(int) 

cleaning_data_3['Kökssvinn(i kg) januari'] = cleaning_data_3['Kökssvinn(i kg) januari'].astype(float)
cleaning_data_3['Kökssvinn(i kg) februari'] = cleaning_data_3['Kökssvinn(i kg) februari'].astype(float)
print(cleaning_data_3.head())

print(cleaning_data_3.dtypes)
#skapar agg() fuktion for insikter om matsvinn hos Sodertalje forskolor i januari och februari:

aggregation= cleaning_data_3[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']].agg('mean')
print(aggregation)
aggregation_2=cleaning_data_3[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']].agg('sum')
# Restructure the aggregation result to a DataFrame
aggregation_ny_df = (aggregation, aggregation_2).reset_index()
aggregation_ny_df.columns = ['M', 'Medelvarde']  

# Create the line plot
sns.scatterplot(data=aggregation_ny_df, x='M', y='Medelvarde')

# Display the plot
plt.show()


# def matsvinn_januari(cleaning_data_3):
#      for x in cleaning_data_3['Kökssvinn(i kg) januari']:
#       if 0 <= x <= 2:
#        print(x)
# print(matsvinn_januari)


# sorting_matsvinn_data= cleaning_data_3.sort_values(by='Kökssvinn(i kg) januari', ascending=True)
# print(sorting_matsvinn_data)
# print(cleaning_data_3['Kökssvinn(i kg) januari'].head(10))


# sns.lineplot(data= cleaning_data_3, x= 'Kökssvinn(i kg) januari', y = 'Kökssvinn(i kg) februari')
# plt.show()





#print(cleaning_data_3.dtypes)
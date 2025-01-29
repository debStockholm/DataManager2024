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
print(ny_df.head(), ny_df2.head())


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
#ny_merging_files= pd.merge(merging_files, n on = 'Enhet', how = 'outer')
#print(merging_files)


 #byta namn till kolumner och spara enbart de mest relevanta - drop allt annat:
cleaned_data =merging_files.drop(['Kategori_x', 'Kategori_y', 'Månad_x', 'Månad_y', 'År_x', 'År_y'], axis=1)
cleaned_data_2 = cleaned_data.rename(columns={'Kökssvinn(i kg)_x':'Kökssvinn(i kg) januari', 'Kökssvinn(i kg)_y':'Kökssvinn(i kg) februari'})
#print(cleaned_data_2)


# #jag vill visa matsvinnstrend jamforelse over tid. Da tar jag bort de raderna dar minst det ena vardet varde ar NaN:

cleaning_data_3 = cleaned_data_2.dropna(subset=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'])
print(cleaning_data_3.head(10))   

#skapar nya kolumner:
cleaning_data_3['Kökssvinn(i kg) skillnad']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])
cleaning_data_3['Kökssvinn(i kg) skillnad']= cleaning_data_3['Kökssvinn(i kg) skillnad'].astype(float)
cleaning_data_3['Matsvinn forandring jan-feb i %']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])/cleaning_data_3['Kökssvinn(i kg) januari'] * 100
cleaning_data_3['Matsvinn forandring jan-feb i %'] = cleaning_data_3['Matsvinn forandring jan-feb i %'].astype(int) 
#se till att samtliga kolumner ar i nagin numeric form:

cleaning_data_3['Kökssvinn(i kg) januari'] = cleaning_data_3['Kökssvinn(i kg) januari'].astype(float)
cleaning_data_3['Kökssvinn(i kg) februari'] = cleaning_data_3['Kökssvinn(i kg) februari'].astype(float)


#print(cleaning_data_3.head())

# # # filtrerar ut data for att skapa en mindre graf:
# # 1.stort negativt matsvinn forandring: skolor som slandge mer mat i februari jmt med januari:
# print('NEGATIV UTVECKLING')
# positive_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %'] > 0]
# neg_matsvinn_utv= positive_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending= False)
# print(neg_matsvinn_utv.head(5))  #funkar

# #--------------------------------------------------------------------------------------------
# #mest positiva matsvinn forandring: skolor som slandge mindre mat i februari jmt med januari
# print('POSITIV UTVECKLING')
# neg_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %']  < 0]
# pos_matsvinn_utv= neg_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending = True)
# print(pos_matsvinn_utv.head(5))


#skapar agg() fuktion for insikter om matsvinn hos Sodertalje forskolor i januari och februari:

matsvinn_januari=cleaning_data_3.groupby('Kökssvinn(i kg) januari').agg('mean', 'sum')
print(matsvinn_januari)
# #Skapa lineplot
# # 
# # sns.scatterplot(data=data_graph, x='Enhet', y='Kökssvinn(i kg) januari')
# # plt.title('Matsvinn for forskolor som hade liten matsvinn forandring mellan januari och februari')
# # plt.show()

# sns.scatterplot(x='Enhet', y='Kökssvinn(i kg) januari', data=data_graph, label='Januari', color='blue')
# sns.scatterplot(x='Enhet', y='Kökssvinn(i kg) februari', data=data_graph, label='Februari', color='orange')
# plt.title('Matsvinn forandring jan/feb')
# plt.show()

# # Samtliga skolor som hade en liten mandg matsvinn forandring (0-2kg kg) mellan jan-feb har registrerat en valdig lite 
# # okning i matsvinn i februari. Kan bero pa att i januari har forskolor varit stangda i nagra dagar? '''

# # # def matsvinn_januari(cleaning_data_3):
# #      for x in cleaning_data_3['Kökssvinn(i kg) januari']:
# #       if 0 <= x <= 2:
# #        print(x)
# # print(matsvinn_januari)


# # sorting_matsvinn_data= cleaning_data_3.sort_values(by='Kökssvinn(i kg) januari', ascending=True)
# # print(sorting_matsvinn_data)
# # print(cleaning_data_3['Kökssvinn(i kg) januari'].head(10))


# # sns.lineplot(data= cleaning_data_3, x= 'Kökssvinn(i kg) januari', y = 'Kökssvinn(i kg) februari')
# # plt.show()





# #print(cleaning_data_3.dtypes)
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
#print(ny_df.head(), ny_df2.head())


#Ta fram en lista av alla kolumner av bada dataset:

'''columns = ny_df.columns
for column in columns:
     print(column) '''

#_____________________________________TRANSFORM________________________________________

#merging de tva dataset
merging_files= pd.merge(ny_df, ny_df2, on = 'Enhet', how = 'outer')
ny_merging_files= pd.merge(merging_files, ny_df3, on = 'Enhet', how = 'outer')
#print(ny_merging_files)


#byta namn till kolumner och spara enbart de mest relevanta - drop allt annat:
cleaned_data =ny_merging_files.drop(['Kategori_x', 'Kategori_y', 'Kategori', 'Månad_x', 'Månad_y','Månad', 'År_x', 'År_y', 'År'], axis=1)
cleaned_data_2 = cleaned_data.rename(columns={'Kökssvinn(i kg)_x':'Januari (kg)', 'Kökssvinn(i kg)_y':'Februari (kg)', 'Kökssvinn(i kg)' : 'Mars (kg)'})
#print(cleaned_data_2)


#jag vill visa matsvinnstrend jamforelse over tid. Da tar jag bort de raderna dar minst det ena vardet varde ar NaN:

cleaning_data_3 = cleaned_data_2.dropna(subset=['Januari (kg)', 'Februari (kg)', 'Mars (kg)'])
#print(cleaning_data_3)   

number_rows = len(cleaning_data_3)
#print(f"Number of rows: {number_rows}")  #kollar hur manga rader har vi


#skapar nya kolumner:
cleaning_data_3['jan-feb matsvinn (kg)']= (cleaning_data_3['Februari (kg)'] - cleaning_data_3['Januari (kg)'])
cleaning_data_3['jan-feb matsvinn (kg)']= cleaning_data_3['jan-feb matsvinn (kg)'].astype(float)
cleaning_data_3['feb - mars matsvinn (kg)']= (cleaning_data_3['Mars (kg)'] - cleaning_data_3['Februari (kg)'])
cleaning_data_3['feb - mars matsvinn (kg)']= cleaning_data_3['feb - mars matsvinn (kg)'].astype(float)
cleaning_data_3['Matsvinn jan-feb i %']= (cleaning_data_3['Februari (kg)'] - cleaning_data_3['Januari (kg)'])/cleaning_data_3['Januari (kg)'] * 100
cleaning_data_3['Matsvinn jan-feb i %'] = cleaning_data_3['Matsvinn jan-feb i %'].astype(int) 
cleaning_data_3['Matsvinn feb - mars i %']= (cleaning_data_3['Februari (kg)'] - cleaning_data_3['Mars (kg)'])/cleaning_data_3['Februari (kg)'] * 100
cleaning_data_3['Matsvinn feb - mars i %'] = cleaning_data_3['Matsvinn feb - mars i %'].astype(int) 

# print('STATISTIK OVER KOKSVINN I KG HOS OLIKA SODERTALJE FORSKOLOR')
# print(cleaning_data_3.head(10))

# print(cleaning_data_3.dtypes)

#skapar en agg() sortering for 'key' insikter om matsvinn hos Sodertalje forskolor i januari, februari, mars:

matsvinn_keyvalues=cleaning_data_3.agg({'Januari (kg)':['sum','mean', 'max','min'], 'Februari (kg)': ['sum','mean', 'max', 'min'],'Mars (kg)': ['sum','mean','max', 'min']})
matsvinn_keyvalues[['Januari (kg)', 'Februari (kg)', 'Mars (kg)']] = matsvinn_keyvalues[['Januari (kg)', 'Februari (kg)', 'Mars (kg)']].round(2).astype(int)
#print(matsvinn_keyvalues)



# # Filtrerar ut data for att skapa en mindre graf, men det gar att kora pa samtliga 'Enheter'.

# 1.stort negativt matsvinn forandring: skolor som slandge 20% + mat i februari jmf med januari:
print('NEGATIV UTVECKLING ---> mer matsvinn mellan januari - februari')
positive_values = cleaning_data_3[cleaning_data_3['Matsvinn jan-feb i %']> 20]
neg_matsvinn_utv= positive_values.sort_values(by='Matsvinn jan-feb i %', ascending= False)
numberrows2 = len(neg_matsvinn_utv) 
print(f'row:{numberrows2}')
print(neg_matsvinn_utv)  #funkar
Ny_data_graph = neg_matsvinn_utv

# 1.stort negativt matsvinn forandring: skolor som slandge 20% + mat i mars jmf med februari:
print('NEGATIV UTVECKLING ---> mer matsvinn mellan februari - mars')
positive_values_1 = cleaning_data_3[cleaning_data_3['Matsvinn feb - mars i %']> 20]
neg_matsvinn_utv_1= positive_values_1.sort_values(by='Matsvinn feb - mars i %', ascending= False)
numberrows2_1 = len(neg_matsvinn_utv_1) 
print(f'row:{numberrows2_1}')
print(neg_matsvinn_utv_1)  #funkar

Ny_data_graph_1 = neg_matsvinn_utv_1


# # #--------------------------------------------------------------------------------------------
# # #mest positiva matsvinn forandring: skolor som slandge 30% + mindre mat i februari jmf med januari
# # print('POSITIV UTVECKLING ---> mindre matsvinn')
# # neg_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %']  < 0]
# # pos_matsvinn_utv= neg_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending = True)
# # Ny_data_graph_2 = pos_matsvinn_utv.head(5)
# # #print(pos_matsvinn_utv.head(10))



neg_utveckling = Ny_data_graph.melt(id_vars=['Enhet'], value_vars=['Januari (kg)', 'Februari (kg)'], 
var_name='Månad', value_name='Kökssvinn (i kg)')

sns.catplot(data=neg_utveckling, x='Enhet', y='Kökssvinn (i kg)', hue='Månad', kind='bar', dodge=True, height=6, aspect=2)

plt.title("Jämförelse av kökssvinn i januari och februari")
plt.suptitle('Top 5 forskolor som okade deras matsvinn fran januari till februari med en skillnad av + 20%')
plt.xlabel("Enhet")
plt.ylabel("Kökssvinn (i kg)")
plt.show()



# # sns.lineplot(data=Ny_data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) januari', color = 'orange', marker='o' , label = 'januari')
# # sns.lineplot(data=Ny_data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) februari', color = 'green', marker= 'o' , label = 'februari')
# # plt.title("Jämförelse av kökssvinn i januari och februari")
# # plt.suptitle('Top 5 forskolor som minskade deras matsvinn fran januari till februari med en skillnad pa +30%')
# # plt.xlabel("Enhet")
# # plt.ylabel("Kökssvinn (i kg)")

# # plt.show()


# # # sorting_matsvinn_data= cleaning_data_3.sort_values(by='Kökssvinn(i kg) januari', ascending=True)
# # # print(sorting_matsvinn_data)
# # # print(cleaning_data_3['Kökssvinn(i kg) januari'].head(10))


# # # sns.lineplot(data= cleaning_data_3, x= 'Kökssvinn(i kg) januari', y = 'Kökssvinn(i kg) februari')
# # # plt.show()





# # #print(cleaning_data_3.dtypes)

# '''time_series = dataFrame.groupby("Date").sum("Sales")
# plt.plot(time_series.index, time_series["Sales"])
# plt.title("Försäljning över tid")
# plt.xlabel("Datum")
# plt.ylabel("Försäljning")
# plt.show()'''

'''plt.hist(dataFrame["Quantity"], bins=10)'''

''''''
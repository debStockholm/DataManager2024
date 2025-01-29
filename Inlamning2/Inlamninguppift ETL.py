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

#skapar agg() fuktion for 'key' insikter om matsvinn hos Sodertalje forskolor i januari och februari:

# matsvinn_keyvalues=cleaning_data_3.agg({'Kökssvinn(i kg) januari':['sum','mean', 'max','min'], 'Kökssvinn(i kg) februari': ['sum','mean', 'max', 'min']})
# print(matsvinn_keyvalues)



# Filtrerar ut data for att skapa en mindre graf:
# 1.stort negativt matsvinn forandring: skolor som slandge mer mat i februari jmt med januari:
print('NEGATIV UTVECKLING')
positive_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %'] > 0]
neg_matsvinn_utv= positive_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending= False)
Ny_data_graph = neg_matsvinn_utv.head(5)
#print(neg_matsvinn_utv.head(5))  #funkar

#--------------------------------------------------------------------------------------------
#mest positiva matsvinn forandring: skolor som slandge mindre mat i februari jmt med januari
print('POSITIV UTVECKLING')
neg_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %']  < 0]
pos_matsvinn_utv= neg_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending = True)
Ny_data_graph_2 = pos_matsvinn_utv.head(5)
#print(pos_matsvinn_utv.head(10))


#Negativ utveckling= forskolor som slangde mer mat i februari jmf i januari
neg_utveckling = Ny_data_graph.melt(id_vars=['Enhet'], value_vars=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'], 
 var_name='Månad', value_name='Kökssvinn (i kg)')

sns.catplot(data=neg_utveckling, x='Enhet', y='Kökssvinn (i kg)', hue='Månad', kind='bar', dodge=True, height=8, aspect=1)

plt.title("Jämförelse av kökssvinn i januari och februari")
plt.suptitle('Top 5 forskolor som okade deras matsvinn fran januari till februari med en skillnad av +40%')
plt.xlabel("Enhet")
plt.ylabel("Kökssvinn (i kg)")
plt.show()



sns.lineplot(data=Ny_data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) januari', color = 'orange', label = 'januari')
sns.lineplot(data=Ny_data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) februari', color = 'green', label = 'februari')
plt.title("Jämförelse av kökssvinn i januari och februari")
plt.suptitle('Top 5 forskolor som minskade deras matsvinn fran januari till februari med en skillnad pa +30%')
plt.xlabel("Enhet")
plt.ylabel("Kökssvinn (i kg)")

plt.show()


# # sorting_matsvinn_data= cleaning_data_3.sort_values(by='Kökssvinn(i kg) januari', ascending=True)
# # print(sorting_matsvinn_data)
# # print(cleaning_data_3['Kökssvinn(i kg) januari'].head(10))


# # sns.lineplot(data= cleaning_data_3, x= 'Kökssvinn(i kg) januari', y = 'Kökssvinn(i kg) februari')
# # plt.show()





# #print(cleaning_data_3.dtypes)

'''time_series = dataFrame.groupby("Date").sum("Sales")
plt.plot(time_series.index, time_series["Sales"])
plt.title("Försäljning över tid")
plt.xlabel("Datum")
plt.ylabel("Försäljning")
plt.show()'''

'''plt.hist(dataFrame["Quantity"], bins=10)'''

''''''
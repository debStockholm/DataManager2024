import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#MATSVINN FORSKOLOR I SODERTALJE   - JMF MELLAN JANUARI - FEBRUARI 2024

#_________________________________LOAD________________________________________


df = pd.read_csv('Inlamning2\Rapportering svinn förskola januari.csv')
df2= pd.read_csv('Inlamning2\Rapportering svinn förskola februari.csv')
df3= pd.read_csv('Inlamning2\Rapportering svinn förskola mars.csv')
df4= pd.read_csv('')
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
#ny_merging_files= pd.merge(merging_files, ny_df3, on = 'Enhet', how = 'outer')
#print(merging_files)


#byta namn till kolumner och spara enbart de mest relevanta - drop allt annat:
cleaned_data =merging_files.drop(['Kategori_x', 'Kategori_y', 'Månad_x', 'Månad_y', 'År_x', 'År_y'], axis=1)
cleaned_data_2 = cleaned_data.rename(columns={'Kökssvinn(i kg)_x':'Kökssvinn(i kg) januari', 'Kökssvinn(i kg)_y':'Kökssvinn(i kg) februari'})
#print(cleaned_data_2)


# #jag vill visa matsvinnstrend jamforelse over tid. Da tar jag bort de raderna dar minst det ena vardet varde ar NaN:

cleaning_data_3 = cleaned_data_2.dropna(subset=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'])
#print(cleaning_data_3.head(10))   

#skapar nya kolumner:
cleaning_data_3['Kökssvinn(i kg) skillnad']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])
cleaning_data_3['Kökssvinn(i kg) skillnad']= cleaning_data_3['Kökssvinn(i kg) skillnad'].astype(float)
cleaning_data_3['Matsvinn forandring jan-feb i %']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])/cleaning_data_3['Kökssvinn(i kg) januari'] * 100
cleaning_data_3['Matsvinn forandring jan-feb i %'] = cleaning_data_3['Matsvinn forandring jan-feb i %'].astype(int) 

#print(cleaning_data_3.dtypes)
#print(cleaning_data_3.head())


#skapar en agg() sortering for 'key' insikter om matsvinn hos Sodertalje forskolor i januari och februari:

# matsvinn_keyvalues=cleaning_data_3.agg({'Kökssvinn(i kg) januari':['sum','mean', 'max','min'], 'Kökssvinn(i kg) februari': ['sum','mean', 'max', 'min']})
# matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']] = matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']].round(2).astype(int)
# print(matsvinn_keyvalues)


# # Filtrerar ut data for att skapa en mindre graf, men det gar att koraa pa samtliga 'Enheter'.

# # 1.stort negativt matsvinn forandring: skolor som slandge 40% + mat i februari jmf med januari:
# print('NEGATIV UTVECKLING ---> mer matsvinn')
# positive_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %'] > 40]
# neg_matsvinn_utv= positive_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending= False)
# Ny_data_graph = neg_matsvinn_utv
# print(Ny_data_graph)  #funkar

# # --------------------------------------------------------------------------------------------
# # 2. mest positiva matsvinn forandring: skolor som slandge 40% + mindre mat i februari jmf med januari

# print('POSITIV UTVECKLING ---> mindre matsvinn')
# neg_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %']  < -30 ]
# pos_matsvinn_utv= neg_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending = True)
# Ny_data_graph_2 = pos_matsvinn_utv
# print(Ny_data_graph_2)


# Max_= cleaning_data_3['Matsvinn forandring jan-feb i %'].max()
# #print(f'hogst matsvinn forandring:{Max_}')

# Minim_= cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %'] > 0]['Matsvinn forandring jan-feb i %'].min()
# #print(f'Lagst matsvinn forandring:{Minim_}')


# Ny_data_graph_3= pd.DataFrame({
#       'Typ av varde': ['Max % matsvinn', 'Min % matsvinn'],
#        'varde': [Max_, Minim_]
#  })
# #print(Ny_data_graph_3)
# #_-----------------------GRAPH

# neg_utveckling = Ny_data_graph.melt(id_vars=['Enhet'], value_vars=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'], 
# var_name='Månad', value_name='Kökssvinn (i kg)')
# sns.catplot(data=neg_utveckling, x='Enhet', y='Kökssvinn (i kg)', hue='Månad', kind='bar', dodge=True, height=8, aspect=1)
# plt.title("Jämförelse av kökssvinn i januari och februari")
# plt.suptitle('Top 5 forskolor som okade deras matsvinn fran januari till februari med en skillnad av + 40%')
# plt.xlabel("Enhet")
# plt.ylabel("Kökssvinn (i kg)")
# plt.show()



# sns.lineplot(data=Ny_data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) januari', color = 'orange', marker='o' , label = 'januari')
# sns.lineplot(data=Ny_data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) februari', color = 'green', marker= 'o' , label = 'februari')
# plt.title("Jämförelse av kökssvinn i januari och februari")
# plt.suptitle('Top 5 forskolor som minskade deras matsvinn fran januari till februari med en skillnad pa +30%')
# plt.xlabel("Enhet")
# plt.ylabel("Kökssvinn (i kg)")
# plt.show()


ny_merging_files= pd.merge(cleaning_data_3, ny_df3, on = 'Enhet', how = 'outer')
Merge_for_scatterplot =pd.merge(ny_merging_files)
#print(ny_merging_files)

merging =ny_merging_files.drop(['Kategori','Månad', 'År'], axis=1)
print(f'detta funkar:{merging}')
merging_ = merging.rename(columns={'Kökssvinn(i kg)':'Kökssvinn(i kg) mars'})
print(f'detta funkar OXA:{merging_}')
#merging_mars = merging_.dropna(subset=['Kökssvinn(i kg) mars', 'Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari', 'Kökssvinn(i kg) skillnad', 'Matsvinn forandring jan-feb i %']) 
print(merging_)

#skapar en agg() sortering for 'key' insikter om matsvinn hos Sodertalje forskolor i januari och februari:

matsvinn_keyvalues=cleaning_data_3.agg({'Kökssvinn(i kg) januari':['sum','mean', 'max','min'], 'Kökssvinn(i kg) februari': ['sum','mean', 'max', 'min']})
# matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']] = matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']].round(2).astype(int)
# print(matsvinn_keyvalues)
# sns.scatterplot(x='Enhet', y='Matsvinn forandring jan-feb i %', data=Ny_data_graph, palette='deep')
# sns.scatterplot(x='Enhet', y='Matsvinn forandring jan-feb i %', data=  Ny_data_graph_2, palette = 'light')
# sns.lineplot(x='Enhet', y='Matsvinn forandring jan-feb i %', data=Ny_data_graph, color= 'blue', linewidth = 3)
# sns.lineplot(x='Enhet', y='Matsvinn forandring jan-feb i %', data=Ny_data_graph_2, color= 'green', linewidth = 3)
# plt.title('Scatterexempel')
# plt.show()



# # Customizing labels and title
# plt.xlabel('X Axis Label')
# plt.ylabel('Y Axis Label')
# plt.title('Custom Scatter Plot')

# # Adding a grid
# plt.grid(True)

# # Show the plot
# plt.show()




# #print(cleaning_data_3.dtypes)

'''time_series = dataFrame.groupby("Date").sum("Sales")
plt.plot(time_series.index, time_series["Sales"])
plt.title("Försäljning över tid")
plt.xlabel("Datum")
plt.ylabel("Försäljning")
plt.show()'''

'''plt.hist(dataFrame["Quantity"], bins=10)'''

''''''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#MATSVINN(kokssvinn) FORSKOLOR I SODERTALJE   - JAMFORELSE MELLAN JANUARI - FEBRUARI - MARS - APRIL 2023



#_________________________________LOAD________________________________________


df = pd.read_csv('Inlamning2\Rapportering svinn förskola januari.csv')
df2= pd.read_csv('Inlamning2\Rapportering svinn förskola februari.csv')
df3= pd.read_csv('Inlamning2\Rapportering svinn förskola mars.csv')
df4= pd.read_csv('Inlamning2\Rapportering svinn förskola april.csv')
print(df,df2, df3, df4)


'''
# Ta fram en lista av alla kolumner om det behovs:

columns = ny_df.columns
for column in columns:
     print(column) 

'''

#_____________________________________TRANSFORM________________________________________

#merging de forsta tva dataset:
merging_files= pd.merge(df, df2, on = 'Enhet', how = 'outer')
'''#print(merging_files)'''


#byta namn till kolumner och spara enbart de mest relevanta - drop allt annat:
cleaned_data =merging_files.drop(['Kategori_x', 'Kategori_y', 'Månad_x', 'Månad_y', 'År_x', 'År_y'], axis=1)
cleaned_data_2 = cleaned_data.rename(columns={'Kökssvinn(i kg)_x':'Kökssvinn(i kg) januari', 'Kökssvinn(i kg)_y':'Kökssvinn(i kg) februari'})
#print(cleaned_data_2)


#jag vill visa jamforelse over tid under tva manader. Da tar jag bort de raderna dar minst det ena vardet varde ar 'NaN':

cleaning_data_3 = cleaned_data_2.dropna(subset=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'])
'''print(cleaning_data_3.head(10)) '''  


#skapar nya kolumner:

#1. raknar skillnad i kg av matsvinn fran januari till februari:
cleaning_data_3['Kökssvinn(i kg) skillnad']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])
cleaning_data_3['Kökssvinn(i kg) skillnad']= cleaning_data_3['Kökssvinn(i kg) skillnad'].astype(float)

#2. Kollar i % hur mycket andring blev det:
cleaning_data_3['Matsvinn forandring jan-feb i %']= (cleaning_data_3['Kökssvinn(i kg) februari'] - cleaning_data_3['Kökssvinn(i kg) januari'])/cleaning_data_3['Kökssvinn(i kg) januari'] * 100
cleaning_data_3['Matsvinn forandring jan-feb i %'] = cleaning_data_3['Matsvinn forandring jan-feb i %'].astype(int) 

'''
print(cleaning_data_3.dtypes)
print(cleaning_data_3)
'''

'''rad beraknare:
rows= len(cleaning_data_3)
print(rows)
'''
print(cleaning_data_3)
#skapar en agg() sortering for 'key' insikter om matsvinn hos forskolorna i januari och februari:

matsvinn_keyvalues=cleaning_data_3.agg({'Kökssvinn(i kg) januari':['sum','mean', 'max','min'], 'Kökssvinn(i kg) februari': ['sum','mean', 'max', 'min']})
matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']] = matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari']].round(2).astype(float)


# Filtrerar ut data for att skapa en mindre graf, men det gar att koras grafer pa samtliga 'Enheter' dvs forskolorna:

# 1.stort negativt matsvinn forandring: skolor som slandge 40% + mat i februari jmf med januari:
#print('NEGATIV UTVECKLING ---> mer matsvinn')
positive_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %'] >= 40]
neg_matsvinn_utv= positive_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending= True)
data_graph_1 = neg_matsvinn_utv             
 # -----------------5 skolor pa 40 okade deras matsvinn av mer an 40%
''' print(data_graph_1) '''


# 2. mest positiva matsvinn forandring: skolor som slandge 40% + mindre mat i februari jmf med januari

#print('POSITIV UTVECKLING ---> mindre matsvinn')
neg_values = cleaning_data_3[cleaning_data_3['Matsvinn forandring jan-feb i %']  <= -40 ]
pos_matsvinn_utv= neg_values.sort_values(by='Matsvinn forandring jan-feb i %', ascending = True)
data_graph_2 = pos_matsvinn_utv               
# ---------------4 skolor pa 40 minskade deras matsvinn av mer an 40%
'''print(data_graph_2)'''


# 3. forskolor som hade en liten forandring i matsvinn mangd mellan jan/feb:

#print('LAGOM OFORANDRAD MATSVINN')
lagom_utveck= cleaning_data_3.loc[(cleaning_data_3['Matsvinn forandring jan-feb i %'] >= -10) & (cleaning_data_3['Matsvinn forandring jan-feb i %'] <=10)]
# ---------------15 skolor pa 40 hade en matsvinnforandring av +/-10% mellan de tva manaderna

'''print(lagom_utveck)  '''

'''
Mer en 1/3 av de analyserade forskolor hade en nastan oforandrat matsvinn pa +\-10%. 
Ca 1/4 av de analyserade forskolor hade en krafting okning eller minskning av matsvinnet -ca 1/10 okning, och 1/10 minskning
Mindre en halften av de analyserad forskolor hade en okning eller minskning av matsvinnet med +/-39%
Samtliga kolumner kan fordelas vidare, men saknas viktigt data for att fordela saker rimligare- se analys
'''


#_________________________________grafer______________________________________

# #1. OVERSIKT ANTAL SKOLOR X KG MATSVINN UNDER JANUARI OCH FEBRUARI MANAD

# sns.histplot(cleaning_data_3['Kökssvinn(i kg) januari'], kde=True, color='cyan', bins=15)
# sns.histplot(cleaning_data_3['Kökssvinn(i kg) februari'], kde= True, color='yellow', bins=15)
# plt.title('Antal forskolor x atsvinn i kg - distribution')
# plt.ylabel('Antal_forskolor')
# plt.xlabel('Matsvinn i kg')
# plt.show()

# #overblick over skillnader mellan jan och febr: pa ca 40 enheter, finns enbart nagra stycken stora avvikelser mellan matsvinn

# # 2.MATSVINN OKNING: forskolor som okade matsvinn 40% + mellan i februari jmf med januari:

# neg_utveckling = data_graph_1.melt(id_vars=['Enhet'], value_vars=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari'], 
# var_name='Månad', value_name='Kökssvinn (i kg)')
# sns.catplot(data=neg_utveckling, x='Enhet', y='Kökssvinn (i kg)', hue='Månad', kind='bar', dodge=True, height=8, aspect=1)
# plt.title("Jämförelse av kökssvinn i januari och februari")
# plt.suptitle('Top 5 forskolor som okade deras matsvinn fran januari till februari')
# plt.xlabel("Forskole namn")
# plt.ylabel("Kökssvinn i kg")
# plt.show()


# # 3 MATSVINN MINSKNING: forskolor som minskade deras matsvinn av 40% + mellan janauri och februari:

# sns.lineplot(data=data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) januari', color = 'orange', marker='o' , label = 'januari')
# sns.lineplot(data=data_graph_2, x='Enhet', y= 'Kökssvinn(i kg) februari', color = 'green', marker= 'o' , label = 'februari')
# plt.title("Jämförelse av kökssvinn i januari och februari")
# plt.suptitle('Forskolor som minskade deras matsvinn fran januari till februari med en skillnad pa +30%')
# plt.xlabel("Forskola")
# plt.ylabel("Kökssvinn i kg")
# plt.show()


# # 4 MATSVINN UTAN STORRE FORANDRING: forskolor som hade ett +\-10% matsvinn forandring mellan januari och februari:
#     #a. matsvinnsforandring jmfr:
# sns.scatterplot(y='Kökssvinn(i kg) januari', x='Enhet' , data=lagom_utveck, color='darkblue', label='jan' , s=150)
# sns.scatterplot(y='Kökssvinn(i kg) februari', x='Enhet',  data=lagom_utveck, color='orange', label = 'feb', s=80)
# plt.title('Forskolor som upplevde +\-10% matsvinnsforandring')
# plt.legend(loc= 'upper right')
# plt.ylabel('Kökssvinn(i kg)')
# plt.xlabel('Forskola:')
# plt.show()


#  #eller
#       #b. matsvinnsforandring jmfr:

# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=lagom_utveck, x='Kökssvinn(i kg) januari', y='Kökssvinn(i kg) februari', color ='salmon', s=150)
# for i in range(lagom_utveck.shape[0]):
#     plt.text(lagom_utveck['Kökssvinn(i kg) januari'].iloc[i] + 0.5, 
#              lagom_utveck['Kökssvinn(i kg) februari'].iloc[i], 
#              lagom_utveck['Enhet'].iloc[i],
#              fontsize=10, ha='left', va='top')

# plt.title('Forskolor med +/-10% matsvinn forandring mellan januari och februari')
# plt.suptitle('Scatterplot jmfrs Januari/Februari')
# plt.xlabel('matsvinn januari i kg')
# plt.ylabel('matsvinn februari i kg')
# plt.show()



#______________________ny merging - joinar tva till dataset, bara for att gora mitt liv mer komplicerat

ny_merging_files= pd.merge(cleaning_data_3, df3, on = 'Enhet', how = 'outer')
ny_merge =pd.merge(ny_merging_files, df4, on = 'Enhet', how='outer')
#print(ny_merge)

merging =ny_merge.drop(['Matsvinn forandring jan-feb i %','Kökssvinn(i kg) skillnad', 'Kategori_x', 'År_x','Månad_x' ,'Månad_y','Kategori_y' , 'År_y'], axis=1)
#print(f'detta funkar:{merging}')
merging_ = merging.rename(columns={'Kökssvinn(i kg)':'Kökssvinn(i kg) mars'})
merging_2 =merging_.rename(columns={'Kökssvinn  (i kg)':'Kökssvinn(i kg) april'})
#print(merging_2)   
#59 rows inkl. kolumns titel

#Brunnsang - Grusasen omrade: forskolor som ligger i samma geografiska omrade(saknas en forskola, dar vi hade inget data!): 
forskole_namn= ['Algården',  'Grusåsen', 'Oxelgrenshagen', 'Trädgården']
forsk_omrade= merging_2[merging_2['Enhet'].isin(forskole_namn)]
print(forsk_omrade)


#Jag tar bort samtliga rader dar ALLA varde ar NaN da jag inte kan arbeta med dem anda (fast jag vet jag inte behover gora detta for att kora 'Aggregate'):

# merging_ma = merging_2.dropna(axis=0, how= 'all', subset=merging_2.columns[1:])
# #print(merging_ma)
# #52 rader kvar inkl. kolumns titel

# '''rowss=len(merging_ma)
# print(rowss)'''


# #skapar en agg() sortering for 'key' insikter om matsvinn hos Sodertalje forskolor i samtliga manader januari - april, inklusive kolumn med NaN varden:

# matsvinn_keys=merging_ma.agg({'Kökssvinn(i kg) januari':['sum','mean', 'max','min'], 'Kökssvinn(i kg) februari': ['sum','mean', 'max', 'min'], 
# 'Kökssvinn(i kg) mars':['sum','mean', 'max','min'], 'Kökssvinn(i kg) april':['sum','mean', 'max','min']})
# matsvinn_keys[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari', 'Kökssvinn(i kg) mars', 'Kökssvinn(i kg) april']] = matsvinn_keys[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari','Kökssvinn(i kg) mars','Kökssvinn(i kg) april']].round(2).astype(float)   #kor INT typ pa allt

# print(matsvinn_keys)  #tycker det ar bra med avrundning, men behovs ej egentligen


# #forbereder mina nya data for plotting enligt chatGPT visdom (skulle jag soka syntax sjalv skulle det ta 1 ar att gora detta):

# matsvinn_keys = matsvinn_keys.reset_index()

# merging_data = matsvinn_keys.melt(id_vars=['index'], 
# value_vars=['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari', 'Kökssvinn(i kg) mars', 'Kökssvinn(i kg) april'],
# var_name='Månad',
# value_name='Kökssvinn (kg)')
# merging_data.columns=['Aggregat_typ', 'Månad', 'Kökssvinn (kg)']
# print(merging_data)


# #______________________________BETTER SCATTERPLOT (BUBBLES)________________________________________
# sns.scatterplot(x='Månad', y='Kökssvinn (kg)', hue='Aggregat_typ', size='Kökssvinn (kg)', sizes=(30, 180), data=merging_data)

# plt.title('Matsvinn Sodertalje forskolor_better_scatterplot')
# plt.xlabel('Månad')
# plt.ylabel('Kökssvinn (i kg)')
# plt.show()

# #___________________________________HEATMAP____________________________________________________________
# Data_graph_3 = merging_data.pivot(index='Månad', columns='Aggregat_typ', values='Kökssvinn (kg)')

# sns.heatmap(Data_graph_3, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=1)
# plt.title('Matsvinn Sodertalje forskolor')
# plt.xlabel('Aggregat_typ')
# plt.ylabel('Månad')
# plt.show()



# # merging_data.to_csv('Arbete_med_flera_kolumner.csv', index=False) 
# data_graph_1.to_excel('Dataframe_1.xlsx', index=False)
# # #data_graph_2.to_excel('Dataframe 2.xlsx', index=False)
# # Data_graph_3.to_excel('Arbete_med_flera_kolumner_2.xlsx, index=False)
# # #lagom_utveck.to_excel('Dataframe_3.xlsx', index=False)



# #UTVARDERING:

# '''
# I had well ordered data to work with, which could result in nice graphs. 
# I downloaded and merged different files to allow a comparison over time, which was the easiest and most valuable operation to do with those data. 
# I had difficult to sort out the most important insights, reason being that data which would allow a more
# objective analysis was in fact missing -as exempel, amount of children/forskola, amount of days open each month, children presence each month, food catering or not:
# things which would have explained the  reason of the variation over time, but we did not have them
# '''
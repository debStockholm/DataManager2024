import numpy as np
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression



df = pd.read_excel('inlamning 3\Df for LR and Cluster.xlsx')
df_drop=df.dropna()
df_drop_1=df.rename(columns={'Kökssvinn(i kg) januari': 'jan_kg', 'Kökssvinn(i kg) februari': 'feb_kg' , 'Kökssvinn(i kg) mars': 'mars_kg', 'Kökssvinn(i kg) april':'apr_kg'})
print(df_drop_1)


#vill arbeta med MEDELVARDET som ser mer linjar ut, men kan arbeta med vad som helst av alla varde:
matsvinn_keyvalues=df_drop_1[['jan_kg','feb_kg','mars_kg', 'apr_kg'] ].agg('medel')
print(matsvinn_keyvalues)

x_idx = matsvinn_keyvalues.index.tolist()
x = [[i] for i in range(len(x_idx))]   
y = matsvinn_keyvalues.values.tolist()   
#print(x)

linear_data=linear_model.LinearRegression()
linear_data.fit(x,y)

x_axis = [[i] for i in range(-2, len(x) + 2)] #2 manader innan och 2 till

predic_on_y = linear_data.predict(x_axis)


months=('nov', 'dec','jan', 'feb', 'mars', 'apr', 'maj', 'juni')

plt.scatter(x, y, c ='purple')
plt.plot(x_axis, predic_on_y, c = 'orange')
plt.title('Matsvinn Sodertalje forskolor ar 2023')
plt.xlabel('manader')
plt.ylabel('summa matsvinn bland samtliga forskolor')
plt.xticks(range(-2, len(x) + 2), months)
plt.show()



#man kan arbeta med max varde ocksa,for att testa:

# months_1=('nov', 'dec','jan', 'feb', 'mars', 'apr', 'maj', 'juni')

# plt.scatter(x,y, c ='red')
# plt.plot(x_max, y_pred, c = 'cyan')
# plt.title('Matsvinn Sodertalje forskolor ar 2023')
# plt.xlabel('manader')
# plt.ylabel('sum matsvinn bland samtliga forskolor')
# plt.xticks(range(-2, len(x) + 2), months_1)
# plt.show()

#print(x)
                                                                


#jag har aktuell data fran maj, da jag kan kora en double check. Fragan ar: inner eller outer? 

df2_com= pd.read_csv('Inlamning2\Rapportering svinn förskola maj.csv')
#print(df2_com)
merge_check=pd.merge(df_drop_1, df2_com , on = 'Enhet', how ='inner' )
#print(merge_check)
mean_check= merge_check[['jan_kg','feb_kg','mars_kg', 'apr_kg', 'Kökssvinn  (i kg)'] ].agg('medel')
#mean_check= merge_check[['jan_kg','feb_kg','mars_kg', 'apr_kg', 'Kökssvinn  (i kg)'] ].agg('sum')
print(mean_check)

#enligt medel, ar medelsvinnet for MAJ ca 9.57kg - med dropna
#i LR grafen: ca 9.31kg
#enligt medel, ar medelsvinnet  i MAJ 10.40kg - utan dropna
#i LR grafen: 10.7kg

#enlig max varde, ar max varden i matsvinn for MAJ ca 31.5kg - med dropna ohch utan dropna
#i LR grafen: ca 38kg

#enlig min varde, ar min varden i matsvinn for MAJ ca 0.8kg - utan dropna och med dropna
#i LR grafen: ca 1.1kg

#enligt sum varde, ar sum varden i matsvinn for MAJ ca 258.5 kg  - med dropna
#i LR grafen: ca 270kg
#enligt sum varde, ar sum varden i matsvinn for MAJ ca 440 kg  - utan dropna
#i LR grafen: ca 456kg

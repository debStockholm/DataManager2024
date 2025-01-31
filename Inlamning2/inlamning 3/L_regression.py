import numpy as np
from sklearn import linear_model
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv('gen_feb_mar_apr.csv')
#print(df)

# matsvinn_keyvalues=df.agg({'Kökssvinn(i kg) januari':['sum','mean', 'max','min'], 'Kökssvinn(i kg) februari': ['sum','mean', 'max', 'min'], 
#                               'Kökssvinn(i kg) mars':['sum','mean', 'max','min'], 'Kökssvinn(i kg) april':['sum','mean', 'max','min']})
# matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari', 'Kökssvinn(i kg) mars', 'Kökssvinn(i kg) april']] = matsvinn_keyvalues[['Kökssvinn(i kg) januari', 'Kökssvinn(i kg) februari',
# 'Kökssvinn(i kg) mars','Kökssvinn(i kg) april']].round(2).astype(int)   #kor INT typ pa allt
# print(matsvinn_keyvalues)

matsvinn_keyvalues=df[['Kökssvinn(i kg) januari','Kökssvinn(i kg) februari','Kökssvinn(i kg) mars', 'Kökssvinn(i kg) april'] ].agg('mean')
#print(matsvinn_keyvalues)

x_idx = matsvinn_keyvalues.index.tolist()
print(x_idx)
x = [[i] for i in range(len(x_idx))]   #voglio sempre una lista per fare la regressione - check parentesi
y = matsvinn_keyvalues.values.tolist()  #voglio sempre una lista per fare la regressione
print(x)



#regression import

linear_data=linear_model.LinearRegression()
linear_data.fit(x,y)

x_axis = [[i] for i in range(-2, len(x) + 4)]
predic_on_y = linear_data.predict(x_axis)



plt.scatter(x,y, color ='')
plt.plot(x_axis, predic_on_y, color = 'green')
plt.title('regression example')
# plt.xlabel
# plt.ylabel
# plt.xticks(range)  #inserire manualmente mesi 
plt.show()
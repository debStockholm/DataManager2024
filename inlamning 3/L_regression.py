import numpy as np
from sklearn import linear_model
#from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

df = pd.read_excel('inlamning 3\Df for LR and Cluster.xlsx')
 #print(df)

df_drop=df.dropna()
df_drop_1=df_drop.rename(columns={'Kökssvinn(i kg) januari': 'jan_kg', 'Kökssvinn(i kg) februari': 'feb_kg' , 'Kökssvinn(i kg) mars': 'mars_kg', 'Kökssvinn(i kg) april':'apr_kg'})
print(df_drop_1)


df_drop_1[['%_jan_feb', '%_feb_mars', '%_mars_april']] = df_drop_1[['jan_kg', 'feb_kg', 'mars_kg', 'apr_kg']].pct_change(axis=1).iloc[:, 1:] * 100
#print(df_drop_1)
df_drop_1['Medel %'] = df_drop_1[['%_jan_feb', '%_feb_mars', '%_mars_april']].mean(axis=1)
df_drop_1[['%_jan_feb', '%_feb_mars', '%_mars_april', 'Medel %']] = df_drop_1[['%_jan_feb', '%_feb_mars', '%_mars_april', 'Medel %']].astype(int)
#print(df_drop_1)   #jag vill ha allt INT

ny_df= df_drop_1.sort_values(by ='Medel %', axis = 0, ascending= True)
#print(ny_df)

#ALTERNATIV 1: om jag kor en LR vill jag nog ha de varderna som tillater mig gora det mest akkurata prediction. Jag tycker det ar rimligt
#att valja de forskolor som had en totalt medelforandring mellan -/+ 10% som betyder att de har en nagorlunda linjar utveckling

#ALTERNATIV 2: anvander aggragat data som samlar info for samtliga forskolor och forsoker forutse utvecklingen  t.e. medelvarde av svinn



#______________________ALTERNATIV 1____________________________________
df_LR= ny_df.loc[(ny_df['Medel %'] >= -10) & (ny_df['Medel %'] <=10)]
print(df_LR)  #yep!

# df_LR['maj_kg'] = None #?


model_LR = linear_model.LinearRegression()

x=df_LR[['mars_kg']]
y=df_LR[['apr_kg']]
model_LR.fit(x, y)  #mitt mal har inga varden?
y_pred=model_LR.predict(x)


#df_LR['maj_kg']=y_pred
#print(model_LR)


plt.scatter(x, y, c ='blue')
plt.plot(x, y_pred, c = 'green')
plt.title('regression example')
plt.xlabel('matsvinn jan')
plt.ylabel('matsvinn feb')
plt.show()
# # plt.xticks(range)  #tillagg manader manuellt?

#vill arbeta med medelvarde som ser mer linjar ut, men kan arbeta med vad som helst av alla varde

# matsvinn_keyvalues=df_drop_1[['jan_kg','feb_kg','mars_kg', 'apr_kg'] ].round(2).agg('mean')
# matsvinn_keyvalues['Medel']=matsvinn_keyvalues.mean()
# print(matsvinn_keyvalues)

# x_idx = matsvinn_keyvalues.index.tolist()
# x = [[i] for i in range(len(x_idx))]   
# y = matsvinn_keyvalues.values.tolist()   
#jag har denna losning i varsta fall, men det galler medelvardet av alla rader... funkar dock.
# print(x)s


# #regression import

# # linear_data=linear_model.LinearRegression()
# # linear_data.fit(x,y)

# # x_axis = [[i] for i in range(len(x) + 3)] + 2: 2 manader till
# # predic_on_y = linear_data.predict(x_axis)



# plt.scatter(x,y, c ='blue')
# plt.plot(x_axis, predic_on_y, c = 'green')
# plt.title('regression example')
# # plt.xlabel
# # plt.ylabel
# # plt.xticks(range)  #tillagg manader manuellt?

# index_x = index()  #behover jag visserligen assign a index sa att programmet borjar rakna pa 'januari' och inte 'enhet'?
# X = np.array([[4.3], [4.5], [3.5], [3.0]])
# print(X)

# y = np.dot(X, np.array('jan_kg', 'feb_kg', 'mars_kg','apr_kg']))

# reg = LinearRegression().fit(X, y)
# reg.score(X, y)

# reg.predict(np.array([[5]]))


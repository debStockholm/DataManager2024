import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_excel('inlamning 3\Df for LR and Cluster.xlsx')

ny_df = df.dropna()
print(ny_df)

clustring= KMeans(n_clusters=5)
clustring.fit(ny_df[['Kökssvinn(i kg) januari','Kökssvinn(i kg) februari','Kökssvinn(i kg) mars','Kökssvinn(i kg) april']])
ny_df['n_cluster']= clustring.predict(ny_df[['Kökssvinn(i kg) januari','Kökssvinn(i kg) februari','Kökssvinn(i kg) mars','Kökssvinn(i kg) april']])

print(ny_df)


plt.scatter(ny_df['Kökssvinn(i kg) januari'], ny_df['Kökssvinn(i kg) februari'], c=ny_df['n_cluster'])
plt.show()
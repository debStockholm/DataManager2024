import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('gen_feb_mar_apr.csv')

ny_df = df.dropna()
print(ny_df)

columns = ny_df.columns
for column in columns:
     print(column) 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('Sum_matsvinn_2020.csv')
df2= pd.read_csv('Sum_matsvinn_2021.csv')
df3= pd.read_csv('Sum_matsvinn_2022.csv')
df4= pd.read_csv('Sum_matsvinn_2023.csv')

ny_df=pd.DataFrame(df)
ny_df2=pd.DataFrame(df2)
ny_df3=pd.DataFrame(df3)
ny_df4=pd.DataFrame(df4)
#print(ny_df, ny_df2, ny_df3, ny_df4)

merge1 = pd.merge(ny_df, ny_df2, on='Manad', how= 'inner')
merge2=pd.merge(merge1, ny_df3, on = 'Manad', how='inner')
merge_months=pd.merge(merge2, ny_df4, on='Manad', how='inner')
#print(merge_months)



#sns.scatterplot(x='Manad', y='')
df_graf = merge_months.melt(id_vars=['Manad'], value_vars=['Tot matsvinn 2020', 'Tot matsvinn 2021', 'Tot matsvinn 2022', 'Tot matsvinn 2023'],
                    var_name='Ar', value_name='Medel matsvinn per manad under aren')
#print(df_graf) 

sns.lineplot(x='Manad', y='Medel matsvinn per manad under aren', hue='Ar', data=df_graf)
sns.scatterplot(x='Manad', y='Medel matsvinn per manad under aren', hue='Ar', legend=False, data=df_graf)
plt.title('Tot matsvinn under aren')
plt.xlabel('Manad')
plt.ylabel('Total matsvinn i kg')
plt.legend(loc='center right')
plt.show()
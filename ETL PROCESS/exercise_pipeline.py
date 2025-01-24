import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    'Item' : ['Bread', 'Milk', 'Cereals', 'Jams', 'Apples'],
    'Price' : [2.8, 1.4, 2, 4.5, 1.5],
    'Import': ['no', 'no', 'no', 'no', 'yes'],
    'Expiring_date': [np.nan, '03.02.25', '12.25', '10.25', np.nan]
     
})


#print(df)

#print(df.head())   #riempie i vuoti con l'input dato
#ny_dataset= df.fillna(0.1)
#df['Update'].fillna(df['column'].mean(), inplace=True)  # Fill with column mean come lo uso?
print(df)

quantity = [35, 15, 12, 28, 13]  #create a variable to contain the values you wanna add
sold_items =[26, 14, 3, 7, 8]

df['Quantity'] = quantity
df['Sold items'] = sold_items
df['total_sales'] = df['Sold items']* df['Price']
print(df)

print(df['Expiring_date'])

elem= df.loc[df['Price']== 2.8, 'Expiring_date']  #trova location specifica riga

if elem.isna().bool():  #if vuole solo true o falso, non due valori
    df.loc[df['Price']== 2.8, 'Expiring_date'] = '06.23'  #riempie il NaN solo sotto Expiring date



print(df)



#PIE CHART O BAR CHART CIN I DATI PRECEDENTI- COME FARE?

df2 = pd.read_csv('exempel_transforming.csv')
print(df2)


price = df['Price']

# # Create a pie chart   #COSA DEVO FAR PER FARLO FUNZIONARE?
# item = df['Item']

# plt.pie(price, labels = item)   #labels è un'impostatzione di matplot
# plt.title('Total earning from sales') #ctrl + k  , ctrl + c per commentare tutto

# # Display the plot 
# 
price = df['Price']
item = df['Item']

np.random.seed(42)
gauss = np.random.normal(0,1,100)
print(gauss)

sns.histplot(gauss, kde=True)   #labels è un'impostatzione di matplot
plt.title('Total earning from sales') #ctrl + k  , ctrl + c per commentare tutto

# # Display the plot 
plt.show()





#df.to_csv('exempel_transforming.csv', index = False)
        
'''df.fillna(0)  # Fill missing values with 0
df['column'].fillna(df['column'].mean(), inplace=True)  # Fill with column mean'''

#df.dropna(subset=['Import'], inplace= True) #perche non mi cancella la riga?

#df.drop(columns='Import', inplace= True) #cosa vuol dire questo boolean? OK FUNZIONA!
#print(df)



'''df.dropna()  # Drop rows with any missing values
df.dropna(subset=['column_name'], inplace=True)  # DELETE ROWS

df['new_column'] = df['column1'] + df['column2']   #new column


df.rename(columns={'old_name': 'new_name'}, inplace=True)

df['column'] = df['column'].str.replace('old_value', 'new_value')  # String replacement
df['column'] = df['column'].str.lower()  # Convert strings to lowercase

df_merged = pd.merge(df1, df2, on='common_column', how='inner')  # Merge dataframes on a common column  #MERGE

df_grouped = df.groupby('category_column').agg({'value_column': 'sum'})  #GROUP 

df_pivot = df.pivot_table(index='category', columns='year', values='value')   #???

df.drop(columns=['column1', 'column2'], inplace=True)   #DELETE COLUMNS




'''


        


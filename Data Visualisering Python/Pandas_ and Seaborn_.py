import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open('Data Visualisering Python\Excel_blad_12.xlsx', 'r') as excel_pandas_ex:
    reading_as_DF= pd.read_excel('Data Visualisering Python\Excel_blad_12.xlsx')
    #print(reading_as_DF)

cleaning_file = reading_as_DF.dropna(how='all')       #clean empty rows
print(cleaning_file)
print(cleaning_file.tail())                           #visualize the head_datas (or tail) to understand the structure

'''cleaning_file = cleaning_file.sort_values(by= 'Quantity', ascending =True) #sorting data in a specific order
print(cleaning_file)'''


#data visualization: SEABORN

'''sns.scatterplot(data=cleaning_file, x = 'Name', y='Price')
plt.title('Exempel with Seaborn')
plt.show()'''


#DOMANDE: perche istogrammi sono 'sbagliati'
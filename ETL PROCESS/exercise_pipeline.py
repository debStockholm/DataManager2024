import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Item' : ['Bread', 'Milk', 'Cereals', 'Jams', 'Apples'],
    'Price' : [2.8, 1.4, 2, 4.5, 1.5],
    'Import': ['no', 'no', 'no', 'no', 'yes'],
    'Expiring_date': [np.nan, '03.02.25', '12.25', '10.25', np.nan]
     
})
print(df)
print(df.head(2))
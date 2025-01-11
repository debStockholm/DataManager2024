'''import pandas as pd

print(pd.__version__)'''

import pandas as pd

data ={
    'Name': ['Sofia','Bert','Anna'],
    'Age' : [23, 30, 27],
    'City' :['Stockholm','Goteborg','Malmo']
}

df = pd.DataFrame(data)
print(df)
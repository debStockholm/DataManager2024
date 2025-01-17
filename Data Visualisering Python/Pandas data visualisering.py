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
summa = df["Age"].sum()
# Räknar antal rader
antal = df["Age"].count()
print(summa)
print(antal)

# vi gör en beräkning:
print("Egen beräkning:")
print(summa/antal)

# eller vi använder inbyggda funktioner
print("Inbyggd beräkning för medelvärde:")
print(df["Age"].mean())

print("Eller median:")
print(df["Age"].median())




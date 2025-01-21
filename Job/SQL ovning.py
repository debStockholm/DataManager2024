import pandas as pd

with open ('Job\sales_data.csv') as sales_fil:

    df = pd.read_csv('Job\sales_data.csv')
    print(df)
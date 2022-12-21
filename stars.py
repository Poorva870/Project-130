import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')
print(df.shape)

df.to_csv('final.csv') 
print(df.shape)

del df['Unnamed: 0']
del df['Unnamed: 6']
del df['Star_name.1']
del df['Distance.1']
del df['Mass.1']
del df['Radius.1']

df.to_csv('main.csv') 

print(df.shape)
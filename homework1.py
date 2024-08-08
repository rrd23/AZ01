import pandas as pd

df = pd.read_csv('smartphone-cleaned.csv')

print(df.head())

print(df.info())

print(df.describe())
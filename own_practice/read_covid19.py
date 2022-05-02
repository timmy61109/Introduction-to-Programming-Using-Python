"""Read covid-19 data."""

import pandas as pd


COUNT = 0

df = pd.read_csv('covid19_free_rapid_antigen_test_clinics.csv')

print(df)

print(pd.DataFrame(df).head(5))

a = df.sample().sample(axis=1)

for i in a:
    for j in a[i]:
        b = j

for columns in df:
    for value in df[columns]:
        if value == b:
            COUNT += 1
print(COUNT)

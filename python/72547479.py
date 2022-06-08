"""
Tag : Python, DataFrame
URL : https://stackoverflow.com/questions/72546917/how-to-split-df-by-dates-based-on-another-df/72547479#72547479
"""



import pandas as pd

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")
df1['Sample Date'] = pd.to_datetime(df1['Sample Date'])
df2['Sample Date'] = pd.to_datetime(df2['Sample Date'])
df2_date_list = df2['Sample Date'].tolist()
df_list = []
for idx, val in enumerate(df2_date_list):
    if val != df2_date_list[-1]:
        df_list.append(df1[(df1['Sample Date'] >= val) & (df1['Sample Date'] <= df2_date_list[idx + 1])])
for idx, val in enumerate(df_list):
    val.to_csv(f'df{idx}.csv')

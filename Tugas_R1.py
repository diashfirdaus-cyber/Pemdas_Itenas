import pandas as pd
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'], 
'Usia': [25, 35, 30, 28],
'Gaji': [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data) 
df['Bonus'] = 0
for index, row in df.iterrows():
    df['Bonus'] = df.apply(lambda row: 0.05 * row['Gaji'], axis=1) 
    df['Gaji_setelah_bonus'] = df['Gaji'] + df['Bonus']
print(df)
print()
for index, row in df.iterrows():
    df.at[index, 'Tambahan_bonus'] = (lambda x: 0.02 * x if row['Usia'] > 30 
    else 0)(row['Gaji_setelah_bonus'])
    df['Gaji_setelah_tambahan_bonus'] = df['Gaji_setelah_bonus'] + df['Tambahan_bonus']
    pd.set_option('display.max_columns', None)
print(df)
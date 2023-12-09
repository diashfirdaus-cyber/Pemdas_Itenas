import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data)

df['Status Usia'] = df['Usia'].apply(lambda x: 'Muda' if x < 30 else 'Tua')
df['Bonus'] = df.apply(lambda x: x['Gaji'] * 1.1 if x['Status Usia'] == 'Tua' else x['Gaji'] * 1.05, axis=1)
df['Umur Diatas 30'] = df.apply(lambda x: x['Bonus'] * 2 if x['Status Usia'] == 'Tua' else x['Bonus'] * 1, axis=1)
print(df)

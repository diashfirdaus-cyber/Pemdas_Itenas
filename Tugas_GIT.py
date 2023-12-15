import pandas as pd

data = {'Nama': ['Dika', 'Juniar', 'Diash', 'Firdaus'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
# Pertanyaan 1:
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x * 1.05)(row['Gaji'])

# Pertanyaan 2:
print("Data Karyawan setelah peningkatan gaji 5%:")
print(df)
print("\nRingkasan perubahan:")
print(df['Gaji'].describe())

# Pertanyaan 3:
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x * 1.02)(row['Gaji'])

# Pertanyaan 4:
print("\nData Karyawan setelah peningkatan gaji untuk \nkaryawan dengan usia di atas 30 tahun:")
print(df)
print("\nRingkasan perubahan:")
print(df['Gaji'].describe())

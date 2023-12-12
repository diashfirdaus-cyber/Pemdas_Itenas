
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

df['Gaji'] = df['Gaji'].apply(lambda gaji: gaji * 1.05)

# Pertanyaan 2:

print("setelah peningkatan gaji 5%:")
print(df)

# Pertanyaan 3:

for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] *= 1.02

# Pertanyaan 4:

print("\nsetelah peningkatan gaji tambahan 2% untuk karyawan di atas 30 tahun:")
print(df)
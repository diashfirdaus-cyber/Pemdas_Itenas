import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
sesudah = lambda gaji: gaji * 0.05
for i, row in df.iterrows():
    df.at[i, 'Gaji Peningkatan'] = sesudah(row['Gaji']) + row['Gaji']

# Pertanyaan 2:
print("DataFrame Setelah di perbarui:")
print(df)

# Ringkasan
print("\nRingkasan Perubahan:")
for i, row in df.iterrows():
    print(f"Gaji {row['Nama']} sebelumnya: {row['Gaji']}, Gaji setelah peningkatan: {row['Gaji Peningkatan']}")

# Pertanyaan 3:
for i, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[i, 'Gaji Usia Senja'] = (lambda gaji: gaji * 1.02)(row['Gaji Peningkatan'])
    else:
        df.at[i, 'Gaji Usia Senja'] = row['Gaji Peningkatan']

# Pertanyaan 4:
print("DataFrame Setelah di perbarui:")
print(df)

# Ringkasan
print("\nRingkasan Perubahan:")
for i, row in df.iterrows():
    print(f"Gaji {row['Nama']} sebelumnya: {row['Gaji'] / 1.07:.2f}, Gaji peningkatan: {row['Gaji Usia Senja']:.2f}")

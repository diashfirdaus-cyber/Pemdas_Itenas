import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = row['Gaji'] * 1.05


# Pertanyaan 2
print("DataFrame setelah peningkatan gaji 5%:")
print(df)
print("\nRingkasan perubahan:")
print("Gaji semua karyawan telah ditingkatkan sebesar 5%.")


# Pertanyaan 3
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = row['Gaji'] * 1.02


# Pertanyaan 4
print("\nDataFrame setelah peningkatan tambahan:")
print(df)
print("\nRingkasan hasil:")
print("Karyawan di atas usia 30 tahun menerima peningkatan tambahan sebesar 2% dari gaji saat ini.")

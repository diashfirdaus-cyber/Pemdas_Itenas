import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data)
print("DataFrame Sebelum Perubahan:")
print(df)

KenaikanGaji5 = lambda gaji: gaji * 1.05
KenaikanGaji2 = lambda gaji: gaji * 1.02

for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = KenaikanGaji5(row['Gaji'])
    else:
        df.at[index, 'Gaji'] = KenaikanGaji2(row['Gaji'])
print("\nDataFrame Setelah Peningkatan Gaji:")
print(df)

print("\nRingkasan Perubahan:")
print("Gaji setiap karyawan ditingkatkan sebesar 5%. untuk karyawan yang usianya di atas 30 tahun ada tambahan 2%")

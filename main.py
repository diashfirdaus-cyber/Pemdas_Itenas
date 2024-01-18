import pandas as pd
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
 'Usia': [25, 35, 30, 28],
 'Gaji': [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data)
gaji_peningkatan = lambda gaji: gaji * 1.05
gaji_peningkatan_tambahan = lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji']
for index, row in df.iterrows():
 df.at[index, 'Gaji'] = gaji_peningkatan_tambahan(row)
print("Data Frame Setelah Peningkatan Gaji Tambahan: ")
print(df)
print("\nRingkasan Perubahan:")
for index, row in df.iterrows():
 print(f"{row['Nama']} - Sebelum: {row['Gaji']/1.05:.2f}, Setelah: {row['Gaji']:.2f}, Peningkatan: 
{row['Gaji']/1.05 - row['Gaji']:.2f}")
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
gaji_bonus = []
for gaji in df['Gaji']:
    gaji_bonus.append((lambda x: x * 1.05)(gaji))

df['Gaji Bonus'] = gaji_bonus

# Pertanyaan 2:
# tampilkan DataFrame yang sudah diperbarui
print("DataFrame gaji setelah bonus")
print(df[['Nama', 'Usia', 'Gaji', 'Gaji Bonus']])

#ringkasan perubahan
print("\nRingkasan Gaji:")
for index, row in df.iterrows():
    print(f"{row['Nama']}: Gaji awal {row['Gaji']:.2f}, Gaji setelah bonus {row['Gaji Bonus']:.2f}, Peningkatan sebesar {row['Gaji Bonus'] - row['Gaji']:.2f}")


# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun.
# Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

gaji_tambahan = []
for index, row in df.iterrows():
    if row['Usia'] > 30:
        gaji_tambahan.append(row['Gaji'] * 1.05 * 1.02)
    else:
        gaji_tambahan.append(row['Gaji Bonus'])

df['Tambahan untuk usia > 30'] = gaji_tambahan

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("DataFrame setalah peningkatan gaji")
print(df)

#ringkasan hasil
print("\n Ringkasan peningkatan")
for index, row in df.iterrows():
    print(f"{row['Nama']}: Gaji setelah tambahan {row['Tambahan untuk usia > 30']:.2f}, Peningkatan sebesar {row['Tambahan untuk usia > 30'] - row['Gaji Bonus']:.2f}")


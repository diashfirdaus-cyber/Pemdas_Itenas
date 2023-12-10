import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
bonus_5percen = 0.05
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x * (1 + bonus_5percen))(row['Gaji'])

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji 5%:")
print(df)

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
bonus_2percen = 0.02
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x * (1 + bonus_2percen))(row['Gaji'])

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nDataFrame setelah peningkatan gaji tambahan:")
print(df)

# Ringkasan
print("\nRingkasan Perubahan:")
for index, row in df.iterrows():
    gaji_awal = row['Gaji'] / (1 + bonus_5percen) if row['Usia'] <= 30 else row['Gaji'] / ((1 + bonus_5percen) * (1 + bonus_2percen))
    print(f"{row['Nama']} ({row['Usia']} tahun):", end=' ')
    print(f"Gaji awal Rp.{gaji_awal:.2f}", end=' ')
    print(f"Gaji setelah peningkatan Rp.{row['Gaji']:.2f}", end=' ')
    if row['Usia'] > 30:
        print("(mendapatkan bonus 2% karena usia > 30)")
    else:
        print()

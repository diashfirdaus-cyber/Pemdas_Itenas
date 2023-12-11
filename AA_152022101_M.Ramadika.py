import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

print("Berikut merupakan perubahan yang terjadi setelah peningkatan 5%")
print(df)

print("\nSebelum peningkatan gaji:")
for index, row in df.iterrows():
    print(f"{row['Nama']}: {row['Gaji'] / 1.05}")

print("\nSesudah peningkatan gaji:")
for index, row in df.iterrows():
    print(f"{row['Nama']}: {row['Gaji']}")


# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

df['Gaji'] = df.apply(lambda row: row['Gaji'] * 1.02 if row['Usia'] > 30 else row['Gaji'], axis=1)

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

print("\nBerikut merupakan perubahan yang terjadi setelah karyawan usia diatas 30 tahun mendapat peningkatan 2%")
print(df)

print("\nSebelum peningkatan gaji:")
for index, row in df.iterrows():
    gaji_sebelum = row['Gaji'] / 1.02 if row['Usia'] > 30 else row['Gaji']
    print(f"{row['Nama']}: {gaji_sebelum} (Usia: {row['Usia']})")

print("\nSesudah peningkatan gaji:")
for index, row in df.iterrows():
    print(f"{row['Nama']}: {row['Gaji']} (Usia: {row['Usia']})")
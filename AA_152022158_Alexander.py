import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
df['Gaji + 5%'] = df.apply(lambda x: x['Gaji'] * 1.05, axis=1)

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji 5%:")
print(df)
print("\nRingkasan perubahan:")
print(df[['Nama', 'Gaji']].describe())

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
df['Gaji Usia >30'] = df.apply(lambda x: x['Gaji'] * 1.02 if x['Usia'] > 30 else x['Gaji'], axis=1)

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nDataFrame setelah peningkatan gaji tambahan:")
print(df)
print("\nRingkasan hasil peningkatan gaji tambahan:")
print(df[['Nama', 'Gaji']].describe())

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.
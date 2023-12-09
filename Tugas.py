import pandas as pd
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'], 
'Usia': [25, 35, 30, 28],
'Gaji': [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data) 
df['Bonus_Karyawan'] = 0
for index, row in df.iterrows():
    df['Bonus_Karyawan'] = df.apply(lambda row: 0.05 * row['Gaji'], axis=1) 
    df['Gaji_Bonus'] = df['Gaji'] + df['Bonus_Karyawan']
print(df)
print()
for index, row in df.iterrows():
    df.at[index, 'Tambahan'] = (lambda x: 0.02 * x if row['Usia'] > 30 else 0) 
    (row['Gaji_Bonus'])
    df['Gaji_Akhir'] = df['Gaji_Bonus'] + df['Tambahan']
    pd.set_option('display.max_columns', None)
print(df)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.
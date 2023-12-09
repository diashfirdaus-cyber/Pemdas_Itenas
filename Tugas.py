import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)


# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
bonus_gaji = 0.05
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] += df.at[index, 'Gaji'] * bonus_gaji

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("\nDataFrame setelah diberikan peningkatan 5% gaji untuk karyawan di atas usia 30:")
print(df)

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
bonus_tambahan = 0.02
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] += df.at[index, 'Gaji'] * bonus_tambahan

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nDataFrame setelah diberikan peningkatan tambahan 2% gaji untuk karyawan di atas usia 30:")
print(df)

summary = f"\nRingkasan Perubahan:\n"
for index, row in df.iterrows():
    summary += f"{row['Nama']} ({row['Usia']} tahun): Gaji awal {row['Gaji'] / (1 + bonus_gaji + bonus_tambahan):,.2f}, Gaji setelah peningkatan {row['Gaji']:,.2f}\n"

print(summary)
# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1 dan 2:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
hitung_gaji = lambda gaji: gaji * 1.05

for index, row in df.iterrows():
    df.at[index, 'Gaji'] = hitung_gaji(row['Gaji'])

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("\nDataFrame Setelah Perubahan:")
print(df)

# Ringkasan perubahan
print("\nRingkasan Perubahan:")
for index, row in df.iterrows():
    print(f"{row['Nama']} - Gaji sebelum: ${row['Gaji']/1.05:.2f}, Gaji setelah: ${row['Gaji']:.2f}, Peningkatan: ${row['Gaji'] - row['Gaji']/1.05:.2f}")
# Pertanyaan 3 dan 4:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
peningkatan_tambahan = lambda gaji: gaji * 0.02 if row['Usia'] > 30 else 0

for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] += peningkatan_tambahan(row['Gaji'])

# Menampilkan DataFrame setelah peningkatan tambahan
print("\nDataFrame Setelah Peningkatan Tambahan:")
print(df)


# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.
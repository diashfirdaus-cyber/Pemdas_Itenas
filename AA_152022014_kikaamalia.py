#import library
import pandas as pd

#variabel data
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}
#variavel df
df = pd.DataFrame(data)

# Output data sebelum diubah
print("\nData Sebelum Diubah : ")
print(df)

#kolom persentase gaji tambahan 5%
df["Percentage"] = df["Gaji"].apply(lambda x: "5%")

# Fungsi lambda untuk menghitung kenaikan gaji
kenaikan_gaji = lambda x: x*1.05  # Peningkatan gaji sebesar 5%

#kolom kenaikan gaji 5% dari gaji sebelumnya
df["Salary Increase"] = [kenaikan_gaji(gaji) for gaji in df["Gaji"]] # iterasi untuk setiap nilai dalam kolom 'Gaji'

#menambahkan kolom additional untuk usia>30 tambahan gaji 2%
df["Additional"] = df["Usia"].apply(lambda x: "2%" if x > 30 else "0%")

# fungsi loop dan lambda pada kolom gaji
#iterasi indeks baris Dataframe df
for i in range(len(df)):
    # memeriksa apakah nilai pada kolom 'Usia' pada baris ke-i lebih dari 30.
    if df.loc[i, "Usia"] > 30:
        #jika kondisi diatas benar, maka nilai pada kolom 'Salary Increase' pada baris ke-i dikali dengan 1.02
        df.loc[i, 'Final Salary'] = (lambda x: x * 1.02)(df.loc[i, 'Salary Increase'])
    
    # jika kondisi if tidak memenuhi
    else:
        #kolom 'Final Salary' pada baris ke-i
        #kolom 'Final Salary' hasil dari nilai pada kolom 'Salary Increase' pada baris ke-i
        df.loc[i, "Final Salary"] = df.loc[i, "Salary Increase"] #tidak ada pertambahan gaji

# Output setelah data diubah
print("\nData Setelah Diubah : ")
print(df)

#Ringkasan perubahan :
    #1. menambahkan kolom 'Percentage' dengan nilai "5%"
    #2.  Fungsi lambda untuk menghitung kenaikan gaji
    #3.  menambahkan kolom 'Salary Increase' dan menghitung 'Salary Increase' dengan fungsi loop
    #4. menambahkan kolom additional sebagai informasi bahwa pertambahan gaji untuk usia>30 dengan tambahan 2% dari gaji saat ini
    #5. fungsi loop untuk menghitung 'Final Salary'
    #6. iterasi indeks baris Dataframe df
    #7. memeriksa apakah nilai pada kolom 'Usia' pada baris ke-i lebih dari 30.
    #8. jika benar, maka nilai pada kolom 'Salary Increase' pada baris ke-i dikali dengan 1.02
    #9. jika salah, kolom 'Final Salary' hasil dari nilai pada kolom 'Salary Increase' pada baris ke-i(tidak ada pertambahan gaji)
    #10. output data setelah diubah


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
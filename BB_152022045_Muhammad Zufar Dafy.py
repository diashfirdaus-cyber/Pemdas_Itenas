import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
# menggunakan for
for i in range(len(df)):
    df.at[i,"setelah peningkatan"] = df.at[i,"Gaji"] * 1.05

# menggunakan lambda    
df["setelah peningkatan"] = df["Gaji"].apply(lambda x: x * 1.05)


# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
df['nilai yang ditambahkan'] = df["Gaji"].apply(lambda x:x*0.05)
print(df)
# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for i,a in df.iterrows():
    df.at[i,"setelah bonus usia"] = (lambda x: x*1.02 if a["Usia"]>30 else x)(a["setelah peningkatan"])
# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
df['nilai dari usia yg ditambahkan'] = df.apply(lambda x: x['setelah bonus usia']-x['setelah peningkatan'],axis=1)
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

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

penghitung_peningkatan = lambda gaji: gaji * 1.05

df['Gaji Setelah Peningkatan'] = 0

for index, row in df.iterrows():
    gaji_sekarang = row['Gaji']
    gaji_setelah_peningkatan = penghitung_peningkatan(gaji_sekarang)
    df.at[index, 'Gaji Setelah Peningkatan'] = gaji_setelah_peningkatan

print(df)

# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

penghitung_peningkatan = lambda gaji: gaji * 1.05

df['Gaji Setelah Peningkatan'] = 0

for index, row in df.iterrows():
    gaji_sekarang = row['Gaji']
    gaji_setelah_peningkatan = penghitung_peningkatan(gaji_sekarang)
    df.at[index, 'Gaji Setelah Peningkatan'] = gaji_setelah_peningkatan

print("DataFrame setelah perubahan:")
print(df)

# Ringkasan perubahan
summary = df[['Nama', 'Gaji', 'Gaji Setelah Peningkatan']]
print("\nRingkasan Perubahan Gaji:")
print(summary)

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

penghitung_peningkatan = lambda gaji: gaji * 1.05

df['Gaji Setelah Peningkatan'] = 0.0

for index, row in df.iterrows():
    usia = row['Usia']
    gaji_sekarang = row['Gaji']
    
    if usia > 30:
        penghitung_peningkatan = lambda gaji: gaji * 1.07  
    else:
        penghitung_peningkatan = lambda gaji: gaji * 1.05 
    
    gaji_setelah_peningkatan = penghitung_peningkatan(gaji_sekarang)
    df.at[index, 'Gaji Setelah Peningkatan'] = gaji_setelah_peningkatan

print(df)

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

penghitung_peningkatan = lambda gaji: gaji * 1.05

df['Gaji Setelah Peningkatan'] = 0.0

for index, row in df.iterrows():
    usia = row['Usia']
    gaji_sekarang = row['Gaji']

    if usia > 30:
        penghitung_peningkatan = lambda gaji: gaji * 1.07  
    else:
        penghitung_peningkatan = lambda gaji: gaji * 1.05  
    
    gaji_setelah_peningkatan = penghitung_peningkatan(gaji_sekarang)
    df.at[index, 'Gaji Setelah Peningkatan'] = gaji_setelah_peningkatan

print("DataFrame setelah perubahan:")
print(df)

summary = df[['Nama', 'Usia', 'Gaji', 'Gaji Setelah Peningkatan']]
print("\nRingkasan Hasil Peningkatan Gaji:")
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
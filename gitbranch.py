#AmsaTarigan
#152023120
#TugasGitBranch
#PemdasCC

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1: Menggunakan loop for dan fungsi lambda untuk menghitung gaji setelah peningkatan 5%
df['Gaji Setelah Peningkatan 5%'] = df['Gaji'].apply(lambda x: x * 1.05)

# Pertanyaan 2: Menampilkan DataFrame yang sudah diperbarui
print("DataFrame setelah peningkatan 5%:")
print(df[['Nama', 'Gaji', 'Gaji Setelah Peningkatan 5%']])

# Menyusun ringkasan perubahan
df['Perubahan Gaji'] = df['Gaji Setelah Peningkatan 5%'] - df['Gaji']
df['Persentase Peningkatan'] = (df['Perubahan Gaji'] / df['Gaji']) * 100

print("\nRingkasan Perubahan Gaji:")
print(df[['Nama', 'Gaji', 'Gaji Setelah Peningkatan 5%', 'Perubahan Gaji', 'Persentase Peningkatan']])

# Pertanyaan 3: Loop for untuk meningkatkan gaji tambahan 2% jika usia lebih dari 30
df['Gaji Setelah Peningkatan Tambahan 2%'] = df.apply(
    lambda row: row['Gaji Setelah Peningkatan 5%'] * 1.02 if row['Usia'] > 30 else row['Gaji Setelah Peningkatan 5%'],
    axis=1
)

# Pertanyaan 4: Tampilkan DataFrame yang sudah diperbarui dan ringkasan hasilnya
print("\nDataFrame setelah peningkatan gaji tambahan 2% untuk usia di atas 30 tahun:")
print(df[['Nama', 'Usia', 'Gaji', 'Gaji Setelah Peningkatan 5%', 'Gaji Setelah Peningkatan Tambahan 2%']])

# Ringkasan hasil
ringkasan_hasil = df[['Nama', 'Usia', 'Gaji', 'Gaji Setelah Peningkatan 5%', 'Gaji Setelah Peningkatan Tambahan 2%']]
ringkasan_hasil['Perubahan Gaji Tambahan'] = ringkasan_hasil['Gaji Setelah Peningkatan Tambahan 2%'] - ringkasan_hasil['Gaji Setelah Peningkatan 5%']
print("\nRingkasan Hasil Perubahan Gaji Tambahan 2%:")
print(ringkasan_hasil)
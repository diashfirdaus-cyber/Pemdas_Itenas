import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
for index, row in df.iterrows():
    df.at[index, 'Peningkatan Gaji'] = (lambda x: x * 1.05)(row['Gaji'])

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame Setelah Peningkatan Gaji:")
print(df[['Nama', 'Gaji', 'Peningkatan Gaji']])

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun.
# Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
df['Usia > 30 Peningkatan Tambahan'] = df['Peningkatan Gaji']
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Usia > 30 Peningkatan Tambahan'] = (lambda x: x * 1.02)(row['Peningkatan Gaji'])

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("DataFrame Setelah Peningkatan Gaji Tambahan:")
print(df[['Nama', 'Usia', 'Peningkatan Gaji', 'Usia > 30 Peningkatan Tambahan']])
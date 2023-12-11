import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

data1 = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
print(data1)
for index in range(len(data1)):
    data1.at[index, 'Gaji'] = (lambda dio: dio * 1.05)(data1.at[index, 'Gaji'])

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji sebesar 5%:")
print(data1)

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun.
# Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for index in range(len(data1)):
    if data1.at[index, 'Usia'] > 30:
        data1.at[index, 'Gaji'] = (lambda dio: dio * 1.02)(data1.at[index, 'Gaji'])

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nDataFrame setelah peningkatan gaji tambahan 2%:")
print(data1)
print("\nHasil:")
print("- Peningkatan gaji sebesar 5% didapatkan untuk semua karyawan.")
print("- Peningkatan gaji tambahan sebesar 2% untuk karyawan yang usianya di atas 30 tahun.")
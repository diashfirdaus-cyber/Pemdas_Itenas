import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

DC = pd.DataFrame(data)

# Pertanyaan 1: Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
for i in range(len(DC['Gaji'])):
    DC['Gaji'][i] = (lambda x: x + 0.05 * x)(DC['Gaji'][i])

# Pertanyaan 2: Tampilkan DataFrame setelah peningkatan gaji 5%.
print("DataFrame setelah peningkatan gaji 5%:")
print(DC)

# Pertanyaan 3: Mengubah tipe data kolom 'Gaji' menjadi float
DC['Gaji'] = DC['Gaji']

# Fungsi lambda untuk menghitung naik gaji
gaji_baru = lambda usia, gaji: gaji * 1.07 if usia > 30 else gaji * 1.05

# Membuat kolom baru 'GajiBaru' dengan nilai yang sudah diperbarui
DC['GajiBaru'] = DC.apply(lambda row: gaji_baru(row['Usia'], row['Gaji']), axis=1)

# Pertanyaan 4: Tampilkan DataFrame dengan kolom 'GajiBaru'
print("\nDataFrame setelah peningkatan tambahan:")
print(DC[['Nama', 'Usia', 'Gaji', 'GajiBaru']])
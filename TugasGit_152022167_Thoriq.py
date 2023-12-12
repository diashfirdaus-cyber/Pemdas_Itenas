import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1: Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
kenaikan_gaji = lambda salary: salary * 1.05

gaji_sebelum = df['Gaji'].copy()

# Pertanyaan 3: Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for index, row in df.iterrows():
        df.at[index, 'Gaji'] = kenaikan_gaji(row['Gaji'])
        if row['Usia'] > 30:
                df.at[index, 'Gaji'] *= 1.02

print("DataFrame setelah perubahan:")
print(df)

# Pertanyaan 2: Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("\nRingkasan Perubahan Gaji:")
for i, (nama, gaji_awal, gaji_baru) in enumerate(zip(df['Nama'], gaji_sebelum, df['Gaji'])):
        print(f"{i+1}. {nama}: Gaji awal = {gaji_awal}, Gaji setelah perubahan = {gaji_baru}")


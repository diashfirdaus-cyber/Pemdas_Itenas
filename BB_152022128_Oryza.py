import pandas as pd

data = {
    "Nama": ["John", "Jane", "Bob", "Alice"],
    "Usia": [25, 35, 30, 28],
    "Gaji": [50000, 60000, 70000, 55000],
}

df = pd.DataFrame(data)
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
hitung_gaji_setelah_peningkatan = lambda gaji: gaji * 1.05

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
for index, row in df.iterrows():
    if row["Usia"] > 30:
        df.at[index, "Gaji"] = hitung_gaji_setelah_peningkatan(row["Gaji"]) * 1.02

print(df)

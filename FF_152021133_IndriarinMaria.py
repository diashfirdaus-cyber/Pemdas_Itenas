import pandas as pd
data = {'Nama' : ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25,35,30,28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

def hitungnaikgaji(Gaji):
    return Gaji*1.05

for i in range(len(df)):
    df['Gaji Peningkatan'] = df['Gaji'].apply (hitungnaikgaji)

print (df) 

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
# Gaji setiap karyawan telah dinaikkan sebesar 5% dari gaji awal.
# Kenaikan gaji bervariasi tergantung pada gaji awal karyawan.
# Karyawan dengan gaji awal yang lebih tinggi akan menerima kenaikan gaji yang lebih besar.

# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

for i in df.index:
    if df.loc[i, 'Usia'] >= 30:
        df.loc[i,'Gaji Peningkatan'] = df.loc[i, 'Gaji'] * 1.05 * 1.02
    else:
        df.loc[i, 'Gaji Peningkatan'] = df.loc[i, 'Gaji'] * 1.05

print (df) 

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
# Gaji setiap karyawan telah dinaikkan sebesar 5%, ditambah dengan peningkatan tambahan sebesar 2% jika usia karyawan di atas 30.
# Kenaikan gaji bervariasi tergantung pada gaji awal karyawan dan usia karyawan.
# Karyawan dengan gaji awal yang lebih tinggi dan usia yang lebih tua akan menerima kenaikan gaji yang lebih besar.

import pandas as pd

# Data
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
print("DataFrame awal:")
print(df)

# Pertanyaan 1: Implementasi peningkatan gaji 5%
df['Gaji'] = df['Gaji'].apply(lambda x: x * 1.05)

# Pertanyaan 2:
print("\nDataFrame setelah peningkatan gaji 5%:")
print(df)

# Ringkasan perubahan setelah peningkatan 5%
ringkasan_5_percent = df['Gaji'] - data['Gaji']
print("\nRingkasan perubahan setelah peningkatan 5%:")
print(ringkasan_5_percent)

# Pertanyaan 3: Implementasi peningkatan 2% untuk usia di atas 30 tahun
for i in range(len(df)):
    if df.at[i, 'Usia'] > 30:
        df.at[i, 'Gaji'] = df.at[i, 'Gaji'] * 1.02

# Pertanyaan 4:
print("\nDataFrame setelah peningkatan tambahan untuk usia di atas 30 tahun:")
print(df)

# Ringkasan hasil setelah peningkatan tambahan
ringkasan_total = df['Gaji'] - data['Gaji']
print("\nRingkasan hasil setelah peningkatan tambahan:")
print(ringkasan_total)


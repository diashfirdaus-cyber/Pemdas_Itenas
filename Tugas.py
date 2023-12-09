import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data)

#pertanyaan no 1
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x * 1.05)(row['Gaji'])

print("DataFrame setelah peningkatan 5%:")
print(df)
print()

#Pertanyaan no 2
ringkasan_data = []
for index, row in df.iterrows():
    ringkasan_data.append([row['Nama'], row['Gaji']/1.05, row['Gaji']])

ringkasan_data = pd.DataFrame(ringkasan_data, columns=['Nama', 'Gaji Sebelumnya', 'Gaji Setelah 5%'])

print("Ringkasan Perubahan:")
print(ringkasan_data)
print()

#pertanyaan no 3
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x * 1.02)(row['Gaji'])

print("DataFrame setelah peningkatan gaji tambahan:")
print(df)
print()

#pertanyaan no 4
hasil_ringkasan_data = []
for index, row in df.iterrows():
    hasil_ringkasan_data.append([row['Nama'], row['Gaji']])

hasil_ringkasan_data = pd.DataFrame(hasil_ringkasan_data, columns=['Nama', 'Gaji Setelah Peningkatan'])
print("Ringkasan Hasil:")
print(hasil_ringkasan_data)

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
bonus_gajih=0.05
for index, row in df.iterrows():
    df.at[index, 'Gaji Bonus'] = row['Gaji'] + (row['Gaji'] * bonus_gajih)
print("Pertanyaan 2:")
print("Gajih Bonus 5%")
print(df)

# Pertanyaan 3:
bonus_gajih_2 = 0.02
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji Bonus'] += row['Gaji'] * bonus_gajih_2
print("\nPertanyaan 4:")
print("Gajih Bonus 2%, untuk usia lebih dari 30 Tahun")
print(df)

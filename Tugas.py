import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
print("Data Awal:")
print(df)
print("\n")
# Pertanyaan 1:

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
df['Naik Gaji 5%'] = df.apply(lambda row: row['Gaji'] * 1.05, axis=1)
# Pertanyaan 2:

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("Data dengan Kolom Baru 'Naik Gaji 5%':")
print(df)

print("\nRingkasan Perubahan:")
print("Semua karyawan naik gaji sebesar 5%.")
print()
# Pertanyaan 3:

# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
df['Gaji Tambahan'] = df.apply(lambda row: row['Gaji'] * 0.02 if row['Usia'] > 30 else 0, axis=1)

# Pertanyaan 4:

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("Data dengan Kolom Baru 'Gaji Tambahan' untuk Usia > 30 Tahun:")
print(df)

print("\nRingkasan Hasil Peningkatan Gaji Tambahan:")
print("Karyawan di atas usia 30 tahun menerima gaji tambahan sebesar 2% dari gaji saat ini.")
print()
df['Total Gaji'] = df['Naik Gaji 5%'] + df['Gaji Tambahan']
print(df)
# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.
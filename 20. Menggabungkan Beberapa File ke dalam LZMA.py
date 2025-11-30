import lzma
import os

file_names = ['file1.txt', 'file2.txt']

with lzma.open('combined.xz', 'wb') as f_out:
    for file_name in file_names:
        with open(file_name, 'rb') as f_in:
            f_out.write(f_in.read())
print("Beberapa file berhasil dikompres menjadi 'combined.xz'.")
# Fungsi: Mengompres beberapa file ke dalam satu arsip LZMA.
# Kondisi: Ketika Anda ingin menggabungkan beberapa file ke dalam arsip yang lebih kecil.

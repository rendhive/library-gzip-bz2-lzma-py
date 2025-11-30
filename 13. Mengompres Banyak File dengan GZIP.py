import gzip
import os

file_names = ['file1.txt', 'file2.txt']

with gzip.open('multiple_files.tar.gz', 'wb') as f_out:
    for file_name in file_names:
        with open(file_name, 'rb') as f_in:
            f_out.write(f_in.read())
print("Beberapa file berhasil dikompres menjadi 'multiple_files.tar.gz'.")
# Fungsi: Mengompres beberapa file menjadi satu arsip GZIP.
# Kondisi: Ketika Anda ingin mengompres beberapa file menjadi satu arsip untuk kemudahan distribusi.

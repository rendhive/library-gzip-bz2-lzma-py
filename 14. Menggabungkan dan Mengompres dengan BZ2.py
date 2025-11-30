import bz2

file_names = ['file1.txt', 'file2.txt']
with bz2.BZ2File('combined.bz2', 'wb') as f_out:
    for file_name in file_names:
        with open(file_name, 'rb') as f_in:
            f_out.write(f_in.read())
print("Beberapa file berhasil dikompres menjadi 'combined.bz2'.")
# Fungsi: Mengompres beberapa file sekaligus dengan format BZ2.
# Kondisi: Ketika Anda ingin menggabungkan beberapa file menjadi satu arsip terkompresi.

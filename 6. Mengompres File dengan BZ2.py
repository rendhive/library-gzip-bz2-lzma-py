import bz2

# Mengompres file ke format BZ2
with open('file.txt', 'rb') as f_in:
    with bz2.open('file.txt.bz2', 'wb') as f_out:
        f_out.writelines(f_in)

print("File 'file.txt' berhasil dikompres menjadi 'file.txt.bz2'.")
# Fungsi: Mengompres file dengan format BZ2.
# Kondisi: Ketika Anda perlu menggunakan kompresi tingkat tinggi yang lebih efisien.

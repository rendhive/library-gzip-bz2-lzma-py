import lzma

# Mengompres file ke format LZMA
with open('file.txt', 'rb') as f_in:
    with lzma.open('file.txt.xz', 'wb') as f_out:
        f_out.writelines(f_in)

print("File 'file.txt' berhasil dikompres menjadi 'file.txt.xz'.")
# Fungsi: Mengompres file dengan format LZMA.
# Kondisi: Ketika Anda ingin menggunakan kompresi yang lebih efisien dan memiliki rasio kompresi yang tinggi.

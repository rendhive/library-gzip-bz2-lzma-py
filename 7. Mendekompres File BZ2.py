import bz2

# Mendekompres file BZ2
with bz2.open('file.txt.bz2', 'rb') as f_in:
    with open('file_decompressed_bz2.txt', 'wb') as f_out:
        f_out.write(f_in.read())

print("File 'file.txt.bz2' berhasil didekompres menjadi 'file_decompressed_bz2.txt'.")
# Fungsi: Mendekompresi file dengan format BZ2.
# Kondisi: Ketika Anda perlu mengambil versi asli dari file yang telah dikompres dengan BZ2.

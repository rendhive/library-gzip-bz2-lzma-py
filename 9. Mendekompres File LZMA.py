import lzma

# Mendekompres file LZMA
with lzma.open('file.txt.xz', 'rb') as f_in:
    with open('file_decompressed_lzma.txt', 'wb') as f_out:
        f_out.write(f_in.read())

print("File 'file.txt.xz' berhasil didekompres menjadi 'file_decompressed_lzma.txt'.")
# Fungsi: Mendekompresi file dengan format LZMA.
# Kondisi: Ketika Anda perlu mengambil versi asli dari file yang telah dikompres dengan LZMA.

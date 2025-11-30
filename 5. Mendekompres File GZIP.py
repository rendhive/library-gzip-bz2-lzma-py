import gzip
import shutil

# Mendekompres file GZIP
with gzip.open('file.txt.gz', 'rb') as f_in:
    with open('file_decompressed.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("File 'file.txt.gz' berhasil didekompres menjadi 'file_decompressed.txt'.")
# Fungsi: Mendekompresi file dengan format GZIP.
# Kondisi: Ketika Anda perlu mengambil versi asli dari file yang telah dikompres.

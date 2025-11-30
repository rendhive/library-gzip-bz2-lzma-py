import gzip
import shutil

# Mengompres file ke format GZIP
with open('file.txt', 'rb') as f_in:
    with gzip.open('file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("File 'file.txt' berhasil dikompres menjadi 'file.txt.gz'.")
# Fungsi: Mengompres file dengan format GZIP.
# Kondisi: Ketika Anda perlu mengurangi ukuran file untuk penyimpanan atau transmisi.

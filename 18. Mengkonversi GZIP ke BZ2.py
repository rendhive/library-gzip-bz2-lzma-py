import gzip
import bz2

# Membaca file GZIP dan menyimpannya sebagai BZ2
with gzip.open('file.txt.gz', 'rb') as f_in:
    with bz2.open('file.txt.bz2', 'wb') as f_out:
        f_out.writelines(f_in)
print("File GZIP berhasil dikonversi menjadi BZ2.")
# Fungsi: Mengonversi file dari format GZIP ke BZ2.
# Kondisi: Ketika Anda ingin mengonversi format kompresi untuk alasan penyimpanan atau distribusi.

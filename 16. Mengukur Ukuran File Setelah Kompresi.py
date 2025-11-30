import os

original_size = os.path.getsize('file.txt')
gzipped_size = os.path.getsize('file.txt.gz')
print(f"Ukuran asli: {original_size} bytes, Ukuran setelah GZIP: {gzipped_size} bytes")
# Fungsi: Mengukur ukuran file sebelum dan setelah kompresi.
# Kondisi: Ketika Anda ingin memverifikasi seberapa efektif kompresi yang dilakukan.

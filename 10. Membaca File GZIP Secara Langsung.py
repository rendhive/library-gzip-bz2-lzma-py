import gzip

# Membaca isi file GZIP
with gzip.open('file.txt.gz', 'rt') as f:
    content = f.read()
    print("Isi file:", content)
# Fungsi: Membaca isi file GZIP secara langsung.
# Kondisi: Ketika Anda hanya ingin membaca dari file GZIP tanpa mendekompresinya ke disk terlebih dahulu.

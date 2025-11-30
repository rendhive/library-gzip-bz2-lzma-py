import bz2

# Membaca isi file BZ2
with bz2.open('file.txt.bz2', 'rt') as f:
    content = f.read()
    print("Isi file:", content)
# Fungsi: Membaca isi file BZ2 secara langsung.
# Kondisi: Ketika Anda hanya ingin membaca dari file BZ2 tanpa mendekompresinya ke disk terlebih dahulu.

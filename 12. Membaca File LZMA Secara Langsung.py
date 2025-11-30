import lzma

# Membaca isi file LZMA
with lzma.open('file.txt.xz', 'rt') as f:
    content = f.read()
    print("Isi file:", content)
# Fungsi: Membaca isi file LZMA secara langsung.
# Kondisi: Ketika Anda hanya ingin membaca dari file LZMA tanpa mendekompresinya ke disk terlebih dahulu.

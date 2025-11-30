import lzma

# Simpan konten ke file LZMA dan baca kembali
content_to_compress = b"Ini adalah data yang akan dikompres."

# Mengompres data
with lzma.open('data.xz', 'wb') as f:
    f.write(content_to_compress)

# Membaca konten
with lzma.open('data.xz', 'rb') as f:
    compressed_content = f.read()
    print(compressed_content)
# Fungsi: Mengompres string dan membaca kembalinya.
# Kondisi: Ketika Anda bekerja dengan data dalam memori dan ingin menyimpannya dengan efisien.

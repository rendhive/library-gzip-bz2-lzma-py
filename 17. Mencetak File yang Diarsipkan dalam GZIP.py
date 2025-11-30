import gzip

with gzip.open('file.txt.gz', 'rb') as f:
    content = f.read()
    print("Isi file terkompresi:")
    print(content[:50])  # Hanya menampilkan karakter pertama
# Fungsi: Mencetak konten dari file GZIP.
# Kondisi: Ketika Anda ingin memastikan bahwa file terkompresi berisi data yang benar.

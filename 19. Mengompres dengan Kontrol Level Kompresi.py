import bz2

# Mengompres file dengan pengaturan level kompresi tertentu
with open('file.txt', 'rb') as f_in:
    with bz2.open('file_with_level.bz2', 'wb', compresslevel=9) as f_out:  # Level 9 untuk kompresi maksimum
        f_out.writelines(f_in)

print("File berhasil dikompres dengan level kompresi maksimum.")
# Fungsi: Mengompres file dengan kontrol atas tingkat kompresi.
# Kondisi: Ketika Anda memiliki kebutuhan spesifik terkait ukuran file hasil kompresi.

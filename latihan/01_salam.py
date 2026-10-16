# ==================================================
# LATIHAN 1: FUNGSI SALAM
# ==================================================

# LANGKAH 1: Membuat fungsi salam dengan parameter nama.
# NOTE: Parameter nama menerima data saat fungsi dipanggil.
def salam(nama):
    print(f"Halo, {nama}. Selamat belajar Python!")


# LANGKAH 2: Memanggil fungsi dengan dua nama berbeda.
# NOTE: Alya dan Bima adalah argumen yang dikirim ke fungsi.
salam("Alya")
salam("Bima")


# LANGKAH 3: Memodifikasi fungsi agar menerima nama dan kelas.
# NOTE: Dua parameter memungkinkan fungsi menerima dua data.
def salam_kelas(nama, kelas):
    print(f"Halo, {nama} dari kelas {kelas}. Selamat belajar Python!")


# LANGKAH 4: Menguji fungsi yang sudah dimodifikasi.
salam_kelas("Alya", "A")
salam_kelas("Bima", "B")

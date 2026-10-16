# ==================================================
# LATIHAN 2: LUAS PERSEGI PANJANG
# ==================================================

# LANGKAH 1: Membuat fungsi untuk menghitung luas.
# NOTE: Parameter p adalah panjang dan l adalah lebar.
# NOTE: return mengembalikan hasil agar dapat digunakan lagi.
def luas_persegi_panjang(p, l):
    return p * l


# LANGKAH 2: Menguji fungsi dengan tiga test case.
# NOTE: Hasil setiap pemanggilan ditampilkan dengan print().
print("Luas 8 x 5 =", luas_persegi_panjang(8, 5))
print("Luas 2.5 x 4 =", luas_persegi_panjang(2.5, 4))
print("Luas 0 x 7 =", luas_persegi_panjang(0, 7))

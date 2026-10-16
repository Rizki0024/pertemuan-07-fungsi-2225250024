# ==================================================
# LATIHAN 5: EKSPERIMEN SCOPE
# ==================================================

# LANGKAH 1: Membuat variabel x di luar fungsi.
# NOTE: Variabel ini berada pada global scope.
x = 10


# LANGKAH 2: Membuat fungsi dengan parameter x.
# NOTE: Parameter x di dalam fungsi berbeda dari variabel global x.
def demo(x):
    y = x + 5
    print("di dalam fungsi:", x, y)

    # LANGKAH 3: Mengembalikan nilai y.
    # NOTE: return digunakan agar hasil dapat dipakai di luar fungsi.
    return y


# LANGKAH 4: Memanggil fungsi dengan argumen 20.
hasil = demo(20)


# LANGKAH 5: Menampilkan variabel di luar fungsi.
print("di luar fungsi:", x, hasil)

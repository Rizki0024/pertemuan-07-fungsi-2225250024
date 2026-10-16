# ==================================================
# LATIHAN 3: JUMLAH 1 SAMPAI N
# ==================================================

# LANGKAH 1: Membuat fungsi untuk menjumlahkan bilangan.
# NOTE: Parameter n menentukan batas bilangan yang dijumlahkan.
def jumlah_n(n):
    total = 0

    # LANGKAH 2: Menjumlahkan bilangan dari 1 sampai n.
    # NOTE: n + 1 digunakan karena batas akhir range tidak disertakan.
    for i in range(1, n + 1):
        total += i

    # LANGKAH 3: Mengembalikan hasil penjumlahan.
    return total


# LANGKAH 4: Menguji fungsi dengan n = 1, 5, 10, dan 100.
# NOTE: Hasil juga dapat dibandingkan dengan rumus n(n+1)/2.
for n in [1, 5, 10, 100]:
    hasil = jumlah_n(n)
    rumus = n * (n + 1) / 2

    print(f"n = {n}, hasil = {hasil}, rumus = {rumus:.0f}")

# ==================================================
# LATIHAN 4: STATISTIK SEDERHANA
# ==================================================

# LANGKAH 1: Membuat fungsi statistik.
# NOTE: Parameter data menerima kumpulan bilangan.
def statistik(data):
    total = 0
    minimum = data[0]
    maksimum = data[0]

    # LANGKAH 2: Menghitung total serta mencari nilai minimum
    # dan maksimum dengan perulangan.
    for x in data:
        total += x

        if x < minimum:
            minimum = x

        if x > maksimum:
            maksimum = x

    # LANGKAH 3: Menghitung rata-rata.
    # NOTE: Data harus berisi setidaknya satu bilangan.
    rata = total / len(data)

    # LANGKAH 4: Mengembalikan tiga nilai sekaligus.
    return minimum, maksimum, rata


# LANGKAH 5: Menguji fungsi dengan data dari materi.
data_nilai = [70, 80, 65, 90, 75]
mn, mx, rt = statistik(data_nilai)

print("Data:", data_nilai)
print("Nilai minimum:", mn)
print("Nilai maksimum:", mx)
print("Rata-rata:", rt)

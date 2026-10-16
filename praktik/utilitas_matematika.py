# ==================================================
# PRAKTIK 2: UTILITAS MATEMATIKA MODULAR
# Pertemuan 07 - Fungsi Python
# ==================================================

# LANGKAH 1: Membuat fungsi luas persegi panjang.
# NOTE: Fungsi menerima panjang dan lebar,
# kemudian mengembalikan hasil perhitungan.
def luas_persegi_panjang(p, l):
    return p * l


# LANGKAH 2: Membuat fungsi luas segitiga.
# NOTE: Rumus luas segitiga adalah 0.5 x alas x tinggi.
def luas_segitiga(a, t):
    return 0.5 * a * t


# LANGKAH 3: Membuat fungsi jumlah 1 sampai n.
# NOTE: Perulangan digunakan untuk mengakumulasi jumlah.
def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


# LANGKAH 4: Membuat fungsi faktorial.
# NOTE: Faktorial n adalah hasil perkalian bilangan
# dari 1 sampai n. Nilai faktorial 0 adalah 1.
def faktorial(n):
    hasil = 1

    for i in range(2, n + 1):
        hasil *= i

    return hasil


# LANGKAH 5: Membuat fungsi untuk menampilkan menu.
# NOTE: Fungsi ini hanya menampilkan pilihan operasi.
def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")


# LANGKAH 6: Menampilkan menu dan membaca pilihan pengguna.
tampilkan_menu()
pilihan = input("Pilih operasi (1-4): ")


# LANGKAH 7: Menjalankan fungsi berdasarkan pilihan.
# NOTE: Pilihan dari input() berbentuk string.
if pilihan == "1":
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))

    hasil = luas_persegi_panjang(p, l)
    print("Luas persegi panjang =", hasil)

elif pilihan == "2":
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))

    hasil = luas_segitiga(a, t)
    print("Luas segitiga =", hasil)

elif pilihan == "3":
    n = int(input("Masukkan n: "))

    # NOTE: n harus bilangan bulat nonnegatif.
    if n >= 0:
        print("Jumlah 1 sampai", n, "=", jumlah_n(n))
    else:
        print("n harus nonnegatif.")

elif pilihan == "4":
    n = int(input("Masukkan n: "))

    # NOTE: Faktorial hanya dihitung untuk n nonnegatif.
    if n >= 0:
        print("Faktorial", n, "=", faktorial(n))
    else:
        print("n harus nonnegatif.")

else:
    print("Pilihan tidak valid.")

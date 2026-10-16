# Pertemuan 07 — Fungsi, Parameter, Return Value, dan Scope dalam Python

## 1. Identitas Mahasiswa

- **Nama:** [Isi nama lengkap]
- **NIM:** 2225250024
- **Program Studi:** S1 Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Pertemuan:** 07

## 2. Tujuan Pembelajaran

Kegiatan Pertemuan 07 bertujuan untuk mempelajari dan mempraktikkan:

1. Pembuatan fungsi menggunakan `def`.
2. Penggunaan parameter dan argumen dalam fungsi.
3. Penggunaan `return` untuk mengembalikan nilai.
4. Pemahaman scope variabel lokal dan global.
5. Pengujian fungsi dengan beberapa kasus.
6. Penyusunan program modular menggunakan Python.
7. Penggunaan VS Code dan GitHub untuk dokumentasi serta pengumpulan tugas.

## 3. Struktur Folder Proyek

```text
pertemuan-07-fungsi-2225250024/
├── README.md
├── .gitignore
├── latihan/
│   ├── 00_asesmen_diagnostik_scope.py
│   ├── 01_salam.py
│   ├── 02_luas_persegi_panjang.py
│   ├── 03_jumlah_n.py
│   ├── 04_statistik_sederhana.py
│   └── 05_scope.py
└── praktik/
    └── utilitas_matematika.py
```

**Keterangan:** Folder `latihan/` menyimpan kode asesmen diagnostik dan latihan fungsi. Folder `praktik/` menyimpan program utilitas matematika yang menggunakan beberapa fungsi.

## 4. Asesmen Diagnostik — Prediksi Scope

### Tujuan

Memprediksi output program dan memahami ruang lingkup (*scope*) variabel lokal dalam fungsi Python.

### Kode yang diuji

File: `latihan/00_asesmen_diagnostik_scope.py`

Program mendefinisikan fungsi `kuadrat(x)`, menghitung kuadrat dari nilai yang diberikan, lalu mencoba mengakses variabel `hasil` di luar fungsi.

### Prediksi output

Ketika `nilai = 5`, pemanggilan `kuadrat(nilai)` menghasilkan:

`5 × 5 = 25`

Dengan demikian, perintah `print(kuadrat(nilai))` menampilkan `25`.

Selanjutnya, perintah `print(hasil)` menimbulkan `NameError` karena variabel `hasil` didefinisikan di dalam fungsi dan tidak tersedia di ruang lingkup global.

### Hasil pengamatan

- Output pertama: `25`.
- Output berikutnya: `NameError` karena nama `hasil` tidak didefinisikan di luar fungsi.

Catatan: Hasil ini merupakan hasil yang diharapkan berdasarkan kode. Pastikan kembali dengan menjalankan program di VS Code.

### Penjelasan scope

Variabel `hasil` merupakan variabel lokal karena didefinisikan di dalam fungsi `kuadrat()`. Variabel lokal digunakan di dalam fungsi tempat variabel tersebut didefinisikan.

Pernyataan `return hasil` mengirimkan nilai perhitungan kepada bagian program yang memanggil fungsi. Nilai tersebut dapat digunakan tanpa perlu mengakses variabel lokal `hasil` secara langsung dari luar fungsi.

### Kesimpulan asesmen

Scope menentukan bagian program tempat suatu variabel dapat diakses. Pemahaman tentang scope membantu menghindari kesalahan `NameError` dan membuat program lebih terstruktur.

## 5. Latihan Fungsi Python

### Latihan 1 — Fungsi Salam

File: `latihan/01_salam.py`

Latihan ini membuat fungsi salam dengan parameter nama dan mengembangkan fungsi agar dapat menerima informasi kelas.

Konsep yang dipelajari:
- Mendefinisikan fungsi dengan `def`.
- Menggunakan parameter.
- Memanggil fungsi dengan argumen.

### Latihan 2 — Luas Persegi Panjang

File: `latihan/02_luas_persegi_panjang.py`

Latihan ini membuat fungsi untuk menghitung luas persegi panjang menggunakan rumus:

`Luas = panjang × lebar`

Fungsi menerima dua parameter dan mengembalikan hasil menggunakan `return`.

Kasus pengujian:

| Panjang | Lebar | Hasil yang diharapkan |
|---:|---:|---:|
| 8 | 5 | 40 |
| 2.5 | 4 | 10.0 |
| 0 | 7 | 0 |

### Latihan 3 — Jumlah Bilangan 1 sampai n

File: `latihan/03_jumlah_n.py`

Latihan ini menggunakan perulangan dan variabel akumulator untuk menghitung jumlah bilangan dari 1 sampai n.

Kasus pengujian:

| n | Hasil yang diharapkan |
|---:|---:|
| 1 | 1 |
| 5 | 15 |
| 10 | 55 |
| 100 | 5050 |

### Latihan 4 — Statistik Sederhana

File: `latihan/04_statistik_sederhana.py`

Latihan ini membuat fungsi untuk menghitung nilai minimum, maksimum, dan rata-rata dari sekumpulan data.

Contoh data: `[70, 80, 65, 90, 75]`

Hasil yang diharapkan:
- Minimum: `65`
- Maksimum: `90`
- Rata-rata: `76.0`

### Latihan 5 — Eksperimen Scope

File: `latihan/05_scope.py`

Latihan ini mengamati perbedaan variabel global dan variabel lokal atau parameter fungsi.

Program menggunakan variabel global `x = 10`, kemudian memanggil fungsi dengan argumen `20`. Pengamatan dilakukan terhadap nilai variabel di dalam dan di luar fungsi.

Hasil yang diharapkan:
- Nilai parameter `x` di dalam fungsi: `20`.
- Nilai variabel lokal `y`: `25`.
- Nilai global `x` di luar fungsi tetap `10`.
- Nilai `y` tidak dapat diakses langsung di luar fungsi karena merupakan variabel lokal.

## 6. Praktik — Program Utilitas Matematika

File: `praktik/utilitas_matematika.py`

### Deskripsi program

Program utilitas matematika merupakan program berbasis menu yang menggabungkan beberapa fungsi matematika dalam satu aplikasi terminal.

Fungsi yang digunakan:

| Fungsi | Kegunaan |
|---|---|
| `luas_persegi_panjang(p, l)` | Menghitung luas persegi panjang. |
| `luas_segitiga(a, t)` | Menghitung luas segitiga. |
| `jumlah_n(n)` | Menghitung jumlah bilangan dari 1 sampai n. |
| `faktorial(n)` | Menghitung faktorial bilangan n. |
| `tampilkan_menu()` | Menampilkan pilihan menu program. |

Program menggunakan fungsi terpisah agar setiap operasi lebih mudah dipahami, diuji, dan diperbaiki.

### Cara menjalankan

Dari folder utama proyek, jalankan:

```bash
python praktik/utilitas_matematika.py
```

Jika menggunakan Windows dan perintah `python` tidak tersedia, coba:

```bash
py praktik/utilitas_matematika.py
```

Ikuti menu yang ditampilkan, masukkan pilihan operasi, kemudian masukkan nilai yang diminta oleh program.

## 7. Pengujian Program

Tabel berikut berisi hasil yang diharapkan berdasarkan contoh kasus pengujian. Setelah menjalankan setiap program, isi kolom hasil aktual dan status sesuai pengamatanmu.

| Program atau fungsi | Kasus uji | Hasil yang diharapkan | Hasil aktual |
|---|---|---|---|
| Asesmen diagnostik | `kuadrat(5)` | `25`, kemudian `NameError` saat `hasil` diakses dari luar fungsi | [Isi setelah dijalankan] |
| Luas persegi panjang | Panjang 8, lebar 5 | `40` | [Isi setelah dijalankan] |
| Jumlah bilangan | n = 10 | `55` | [Isi setelah dijalankan] |
| Statistik sederhana | `[70, 80, 65, 90, 75]` | Min 65, maks 90, rata-rata 76.0 | [Isi setelah dijalankan] |
| Luas persegi panjang pada program praktik | p = 8, l = 5 | `40` | [Isi setelah dijalankan] |
| Luas segitiga pada program praktik | a = 10, t = 6 | `30.0` | [Isi setelah dijalankan] |
| Jumlah bilangan pada program praktik | n = 10 | `55` | [Isi setelah dijalankan] |
| Faktorial pada program praktik | n = 5 | `120` | [Isi setelah dijalankan] |
| Faktorial pada program praktik | n = 0 | `1` | [Isi setelah dijalankan] |

**Status pengujian:** [Isi setelah pengujian, misalnya seluruh kasus yang dicoba menghasilkan keluaran sesuai harapan.]

Catatan: Jangan menyatakan seluruh pengujian berhasil sebelum kamu menjalankan program dan memeriksa hasil aktualnya.

## 8. Refleksi Pembelajaran

### 1. Apa manfaat menggunakan fungsi?

Fungsi membantu membagi program menjadi bagian-bagian yang lebih kecil dan terstruktur. Kode dapat digunakan kembali sehingga mengurangi pengulangan dan memudahkan pengujian maupun perbaikan.

### 2. Apa perbedaan `print()` dan `return`?

`print()` menampilkan informasi ke layar, sedangkan `return` mengirimkan nilai dari fungsi kepada pemanggilnya. Nilai yang dikembalikan dapat disimpan dalam variabel atau digunakan dalam perhitungan lain.

### 3. Apa yang dipelajari tentang scope?

Scope menentukan bagian program tempat suatu variabel dapat diakses. Variabel lokal yang dibuat di dalam fungsi tidak dapat langsung diakses dari luar fungsi.

Catatan: Refleksi ini merupakan contoh jawaban. Sesuaikan dengan pemahaman dan pengalamanmu setelah mengerjakan latihan.

## 9. Dokumentasi Git dan GitHub

Proyek dikelola menggunakan Git untuk mencatat perubahan kode dan dokumentasi. Repositori GitHub digunakan untuk menyimpan serta mengumpulkan hasil pekerjaan.

Contoh pesan commit yang bermakna:

```text
feat: menambahkan struktur latihan fungsi pertemuan 07
feat: menyelesaikan latihan fungsi dan parameter
feat: menyelesaikan praktik utilitas matematika modular
docs: melengkapi hasil uji dan refleksi pertemuan 07
docs: menambahkan asesmen diagnostik scope
```

Pesan commit harus mencerminkan perubahan yang benar-benar dilakukan. Tidak perlu membuat commit untuk perubahan yang belum ada atau mengulang commit yang sama.

**URL repositori GitHub:** [Tempelkan URL repositori milikmu di sini]

## 10. Kesimpulan

Pada Pertemuan 07, saya mempelajari cara membuat dan menggunakan fungsi Python, memanfaatkan parameter dan `return`, serta memahami perbedaan variabel lokal dan global melalui konsep scope.

Melalui latihan dan praktik utilitas matematika, konsep fungsi diterapkan dalam program modular. Pengujian digunakan untuk memeriksa kebenaran hasil, sedangkan Git dan GitHub digunakan untuk mendokumentasikan serta mengumpulkan pekerjaan.

## 11. Referensi

1. Bahan Ajar Pertemuan 07 — Fungsi, Parameter, Return Value, dan Scope dalam Python di VS Code dan Pengumpulan melalui GitHub.
2. Dokumentasi resmi Python: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# Analisis Komparatif Insertion Sort pada Data Terurut dan Tidak Terurut

Muhammad Raffi - 231110211,
Fajar Ario Abdillah - 2311102114

Program ini berisi implementasi algoritma Insertion Sort dalam bentuk iteratif dan rekursif menggunakan Python. Program ini mengukur dan membandingkan waktu eksekusi kedua metode pada dua set data input: satu data yang tidak terurut dan satu data yang sudah terurut. Hasilnya ditampilkan dalam format tabel dan grafik.

## Fitur

- **Insertion Sort (Iteratif)**: Versi iteratif dari algoritma Insertion Sort.
- **Insertion Sort (Rekursif)**: Versi rekursif dari algoritma Insertion Sort.
- **Pengukuran Kinerja**: Mengukur dan membandingkan waktu eksekusi untuk kedua metode.
- **Tampilan Hasil**: Menampilkan output yang sudah diurutkan dan waktu eksekusinya dalam format tabel dan grafik.

## Persyaratan

Sebelum menjalankan skrip ini, Anda perlu menginstal dependensi berikut:

- `matplotlib` untuk menggambar grafik
- `prettytable` untuk menampilkan hasil dalam format tabel

Anda dapat menginstal dependensi tersebut menggunakan `pip`:

```bash
pip install matplotlib prettytable
```

## Penggunaan

### Langkah 1: Masukkan Data

Program akan meminta Anda untuk memasukkan dua dataset yang perlu diurutkan. Untuk setiap dataset, masukkan nilai yang dipisahkan dengan koma (misalnya, `5,2,9,1`).

### Langkah 2: Pengurutan dan Perbandingan Kinerja

Skrip ini akan menjalankan kedua versi **iteratif** dan **rekursif** dari Insertion Sort pada data input dan mengukur waktu eksekusinya. Hasilnya akan ditampilkan dalam dua tabel, satu untuk setiap dataset, yang menunjukkan array yang sudah diurutkan dan waktu eksekusi masing-masing.

### Langkah 3: Output Grafik

Dua grafik batang akan dihasilkan untuk membandingkan secara visual waktu eksekusi antara metode iteratif dan rekursif untuk kedua dataset.

## Contoh

```plaintext
Masukkan data pertama untuk diurutkan (pisahkan dengan koma, contoh: 5,2,9,1):
Data pertama: 5,1,2,4,3
Masukkan data kedua untuk diurutkan (pisahkan dengan koma, contoh: 8,3,7,4):
Data kedua: 1,2,3,4,5
```

**Output:**

### Data Pertama ([5, 1, 2, 4, 3]):
| Metode    | Output Terurut   | Waktu (detik) |
|-----------|------------------|---------------|
| Iteratif  | [1, 2, 3, 4, 5]  | 0.000010      |
| Rekursif  | [1, 2, 3, 4, 5]  | 0.000006      |

### Data Kedua ([1, 2, 3, 4, 5]):
| Metode    | Output Terurut   | Waktu (detik) |
|-----------|------------------|---------------|
| Iteratif  | [1, 2, 3, 4, 5]  | 0.000003      |
| Rekursif  | [1, 2, 3, 4, 5]  | 0.000002      |

**Perbandingan Grafik:**

Grafik batang yang menampilkan perbandingan waktu antara metode iteratif dan rekursif untuk kedua dataset.

## Kesimpulan

Data yang tidak terurut membutuhkan waktu lebih lama untuk diurutkan karena melibatkan lebih banyak operasi perbandingan dan pergeseran elemen. Sementara itu, data terurut lebih efisien dengan waktu eksekusi yang lebih cepat. Metode rekursif sedikit lebih cepat dibandingkan metode iteratif pada saat mengurutkan data.



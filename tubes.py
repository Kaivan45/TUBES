import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi Insertion Sort Iteratif
def insertion_sort_iterative(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Fungsi Insertion Sort Rekursif
def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
    insertion_sort_recursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

# Fungsi untuk mengukur waktu eksekusi
def measure_time(func, arr):
    start = time.time()
    func(arr)
    end = time.time()
    return end - start

# Input data untuk diurutkan (pertama)
print("Masukkan data pertama untuk diurutkan (pisahkan dengan koma, contoh: 5,2,9,1):")
try:
    input_data1 = list(map(int, input("Data pertama: ").split(",")))
except ValueError:
    print("Input tidak valid! Pastikan memasukkan angka yang dipisahkan dengan koma.")
    exit()

# Input data untuk diurutkan (kedua)
print("Masukkan data kedua untuk diurutkan (pisahkan dengan koma, contoh: 8,3,7,4):")
try:
    input_data2 = list(map(int, input("Data kedua: ").split(",")))
except ValueError:
    print("Input tidak valid! Pastikan memasukkan angka yang dipisahkan dengan koma.")
    exit()

# Proses data pertama
arr_iter1 = input_data1.copy()
arr_recur1 = input_data1.copy()

# Tabel hasil data pertama
detail_table1 = PrettyTable()
detail_table1.field_names = ["Method", "Sorted Output", "Time (s)"]

iter_time1 = measure_time(lambda x: insertion_sort_iterative(x), arr_iter1)
detail_table1.add_row(["Iterative", arr_iter1, f"{iter_time1:.6f}"])

recur_time1 = measure_time(lambda x: insertion_sort_recursive(x, len(x)), arr_recur1)
detail_table1.add_row(["Recursive", arr_recur1, f"{recur_time1:.6f}"])

# Proses data kedua
arr_iter2 = input_data2.copy()
arr_recur2 = input_data2.copy()

# Tabel hasil data kedua
detail_table2 = PrettyTable()
detail_table2.field_names = ["Method", "Sorted Output", "Time (s)"]

iter_time2 = measure_time(lambda x: insertion_sort_iterative(x), arr_iter2)
detail_table2.add_row(["Iterative", arr_iter2, f"{iter_time2:.6f}"])

recur_time2 = measure_time(lambda x: insertion_sort_recursive(x, len(x)), arr_recur2)
detail_table2.add_row(["Recursive", arr_recur2, f"{recur_time2:.6f}"])

# Menampilkan tabel hasil pengurutan
print("Hasil untuk data pertama:", input_data1.copy())
print(detail_table1)

print("\nHasil untuk data kedua:", input_data2.copy())
print(detail_table2)

# Membuat grafik perbandingan untuk kedua data
plt.figure(figsize=(12, 6))
methods = ["Iterative", "Recursive"]

# Grafik data pertama
plt.subplot(1, 2, 1)
plt.bar(methods, [iter_time1, recur_time1], color=['blue', 'red'])
plt.ylim(0, max(iter_time1, recur_time1, iter_time2, recur_time2) * 1.1)
plt.title("Data Pertama")
plt.ylabel("Time (s)")

# Grafik data kedua
plt.subplot(1, 2, 2)
plt.bar(methods, [iter_time2, recur_time2], color=['green', 'orange'])
plt.ylim(0, max(iter_time1, recur_time1, iter_time2, recur_time2) * 1.1)
plt.title("Data Kedua")

plt.suptitle("Time Comparison of Iterative and Recursive Insertion Sort")
plt.tight_layout()
plt.show()
# Contoh penggunaan variabel loop dengan nama yang sama dengan daftar
# buah = ["apel", "pisang", "ceri"]
# for buah in buah:
#     print(buah)

# kata = "python"
# for huruf in kata:
#     print(huruf)

# for i in range(5):
    # print(i)

# for i in range(2, 10, 2):
#     print(i)

# atas = int(input("Batas atas: "))
# bawah = int(input("Batas bawah: "))
# pilih = input("Pilih (ganjil/genap?): ")

# if pilih == "genap":
#     for c in range(bawah, atas + 1):
#         if c % 2 == 0:
#             print(c)
# elif pilih == "ganjil":
#     for c in range(bawah, atas + 1):
#         if c % 2 != 0:
#             print(c)
# else:
#     print("Pilihan tidak valid.")


# print("Program menentukan bilangan prima.")
# start = int(input("Masukkan angka awal: "))
# stop = int(input("Masukkan angka akhir: "))
# for a in range(start, stop + 1):
#     if a > 1:
#         for i in range(2, a):
#             if (a % i) == 0:
#                 break
#         else:
#             print(a, "adalah bilangan prima.")


# for char in "saya belajar":
#     print(char)

# vokal = "aiueo"
# kata = "Saya Belajar Python"
# jumlah_vokal = 0
# for char in kata.lower():
#     if char in vokal:
#         jumlah_vokal += 1
# print("Jumlah huruf vokal adalah", jumlah_vokal)

# teks = input("Masukkan teks: ").lower()
# cari = input("Masukkan huruf yang ingin dicari: ").lower()

# jumlah = 0
# for char in teks:
#     if char.lower() in cari:
#         jumlah += 1  

# if jumlah == 0:
#     print(f"Tidak ada huruf '{cari}' yang ditemukan dalam teks.")
# else:
#     print(f"Jumlah huruf '{cari}' dalam teks adalah: {jumlah}")

# kata = "Indonesia" 
# huruf = input("Masukkan huruf yang ingin dicari: ").lower()

# vokal = "aiueo"

# if huruf in kata.lower():
#     if huruf in vokal:
#         print(f"Huruf '{huruf}' ada di dalam kata '{kata}' dan termasuk huruf vokal.")
#     else:
#         print(f"Huruf '{huruf}' ada di dalam kata '{kata}' dan termasuk huruf konsonan.")
# else:
#     print(f"Huruf '{huruf}' tidak ada di dalam kata '{kata}'.")

# kata = "Indonesia"
# vokal = "aiueo"

# for huruf in kata.lower():
#     if huruf in vokal:
#         print(f"Huruf '{huruf}' adalah huruf vokal.")
#     elif huruf.isalpha():  # pastikan hanya huruf, bukan spasi/tanda baca
#         print(f"Huruf '{huruf}' adalah huruf konsonan.")



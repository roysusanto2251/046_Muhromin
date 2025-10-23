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


print("Program menentukan bilangan prima.")
start = int(input("Masukkan angka awal: "))
stop = int(input("Masukkan angka akhir: "))
for a in range(start, stop + 1):
    if a > 1:
        for i in range(2, a):
            if (a % i) == 0:
                break
        else:
            print(a, "adalah bilangan prima.")
            
# =============================================
# PROGRAM 1: PERULANGAN DENGAN VARIABEL SAMA
# =============================================
# Contoh penggunaan variabel loop dengan nama yang sama dengan daftar
buah = ["apel", "pisang", "ceri"]
for buah in buah:
    print(buah)

# =============================================
# PROGRAM 2: PERULANGAN PADA STRING
# =============================================
kata = "python"
for huruf in kata:
    print(huruf)

# =============================================
# PROGRAM 3: PERULANGAN DENGAN RANGE SEDERHANA
# =============================================
for i in range(5):
    print(i)

# =============================================
# PROGRAM 4: PERULANGAN DENGAN RANGE KOMPLEKS
# =============================================
for i in range(2, 10, 2):
    print(i)

# =============================================
# PROGRAM 5: FILTER BILANGAN GANJIL/GENAP
# =============================================
atas = int(input("Batas atas: "))
bawah = int(input("Batas bawah: "))
pilih = input("Pilih (ganjil/genap?): ")

if pilih == "genap":
    for c in range(bawah, atas + 1):
        if c % 2 == 0:
            print(c)
elif pilih == "ganjil":
    for c in range(bawah, atas + 1):
        if c % 2 != 0:
            print(c)
else:
    print("Pilihan tidak valid.")

# =============================================
# PROGRAM 6: MENENTUKAN BILANGAN PRIMA
# =============================================
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

# =============================================
# PROGRAM 7: PERULANGAN PADA KALIMAT
# =============================================
for char in "saya belajar":
    print(char)

# =============================================
# PROGRAM 8: MENGHITUNG HURUF VOKAL
# =============================================
vokal = "aiueo"
kata = "Saya Belajar Python"
jumlah_vokal = 0
for char in kata.lower():
    if char in vokal:
        jumlah_vokal += 1
print("Jumlah huruf vokal adalah", jumlah_vokal)

# =============================================
# PROGRAM 9: MENCARI HURUF TERTENTU DALAM TEKS
# =============================================
teks = input("Masukkan teks: ").lower()
cari = input("Masukkan huruf yang ingin dicari: ").lower()

jumlah = 0
for char in teks:
    if char.lower() in cari:
        jumlah += 1  

if jumlah == 0:
    print(f"Tidak ada huruf '{cari}' yang ditemukan dalam teks.")
else:
    print(f"Jumlah huruf '{cari}' dalam teks adalah: {jumlah}")

# =============================================
# PROGRAM 10: ANALISIS HURUF VOKAL/KONSONAN
# =============================================
kata = "Indonesia" 
huruf = input("Masukkan huruf yang ingin dicari: ").lower()

vokal = "aiueo"

if huruf in kata.lower():
    if huruf in vokal:
        print(f"Huruf '{huruf}' ada di dalam kata '{kata}' dan termasuk huruf vokal.")
    else:
        print(f"Huruf '{huruf}' ada di dalam kata '{kata}' dan termasuk huruf konsonan.")
else:
    print(f"Huruf '{huruf}' tidak ada di dalam kata '{kata}'.")

# =============================================
# PROGRAM 11: IDENTIFIKASI VOKAL DAN KONSONAN
# =============================================
kata = "Indonesia"
vokal = "aiueo"

for huruf in kata.lower():
    if huruf in vokal:
        print(f"Huruf '{huruf}' adalah huruf vokal.")
    elif huruf.isalpha():  # pastikan hanya huruf, bukan spasi/tanda baca
        print(f"Huruf '{huruf}' adalah huruf konsonan.")

# =============================================
# PROGRAM 12: PERULANGAN DENGAN LIST
# =============================================
angka = [1, 2, 3, 4, 5]
for a in angka:
    print(a)

# =============================================
# PROGRAM 13: MENGHITUNG TOTAL ANGKA DALAM LIST
# =============================================
angka = [1, 2, 3, 4, 5]
total = 0
for a in angka:
    total += a
print("Total jumlah angka adalah:", total)

# =============================================
# PROGRAM 14: FILTER ANGKA GANJIL/GENAP DALAM LIST
# =============================================
angka = [1, 2, 3, 4, 5]

# Meminta input dari pengguna
pilihan = input("Kamu ingin menampilkan angka 'ganjil' atau 'genap'? ").lower()

if pilihan == "genap":
    print("Angka genap:")
    for a in angka:
        if a % 2 == 0:
            print(a)

elif pilihan == "ganjil":
    print("Angka ganjil:")
    for a in angka:
        if a % 2 != 0:
            print(a)

else:
    print("Pilihan tidak valid! Silakan ketik 'ganjil' atau 'genap'.")
print("\n1. PERBANDINGAN ANGKA")
print("-" * 30)
a = 10
b = 10
c = 20

print(f"a = {a}, b = {b}, c = {c}")
print(f"a == b:", a == b)  # True
print(f"a != b: {a != b}")  # False
print(f"a == c: {a == c}")  # False
print(f"a != c: {a != c}")  # False

print("\n2. LOGIKA")
x = 10
y = 5

print(x > y)   # True, karena 10 lebih besar dari 5
print(x < y)   # False, karena 10 tidak lebih kecil dari 5

print("\n3. KONDISI")
umur = 17

if umur < 18:
    print("Anda masih di bawah umur.")
else:
    print("Anda sudah dewasa.") 
    
print("\n4. STUDI KASUS - DISKON LANSIA")
usia = int(input("Masukkan usia Anda: "))

if usia >= 60:
    print("Berhak mendapatkan diskon Lansia.")
else:
    print("Tidak berhak mendapatkan diskon Lansia.")
    
print("\n5. STUDI KASUS - CUACA")

suhu = 30
kelembapan = 70

if suhu > 28 and kelembapan > 60:
    print("Cuaca panas dan lembap.")
else:
    print("Cuaca cukup nyaman.")
    
print("\n6. STUDI KASUS - LOGIN")

username = input("Masukkan username: ")
password = input("Masukkan password: ") 
if username == "admin" and password == "password123":
    print("Login berhasil!")
else:
    print("Login gagal! Periksa username dan password Anda.")
    

print("\n7. STUDI KASUS - ANGIN KENCANG")

suhu = int(input("Masukkan suhu (dalam °C): "))
angin_kencang = bool(input("Apakah ada angin kencang? (True/False): "))

if suhu > 33 or angin_kencang:
    print("Peringatan: Cuaca ekstrem!")
else:
    print("Cuaca normal.")
    
print("\n8. FUNGSI LOGIKA NOT")
is_logged_in = False

if not is_logged_in:
    print("Silakan login terlebih dahulu.")
else:
    print("Selamat datang kembali!")
    
akses_ditolak = True

if not akses_ditolak:
    print("Akses diizinkan.")
else:
    print("Akses ditolak.")
    
print("\n9. OPERATOR KEANGGOTAAN")
kalimat = "Belajar Python itu menyenangkan"
print(f"Kalimat: '{kalimat}'")
cari = input("Masukkan kalimat yang ingin dicari: ")

if cari in kalimat:
    print(f"Kalimat '{cari}' ditemukan dalam teks.")
else:
    print(f"Kalimat '{cari}' tidak ditemukan dalam teks.")
    
daftar_belanja = ["beras", "minyak", "gula"]
cari_barang = input("Masukkan barang yang ingin dicari: ")

if cari_barang not in daftar_belanja:
    print(f"Barang '{cari_barang}' tidak ada dalam daftar belanja.")
else:
    print(f"Barang '{cari_barang}' ada dalam daftar belanja.")
    
print("\n10. OPERATOR IDENTITAS IS, IS NOT")

data = input("Masukkan data (biarkan kosong untuk None): ")
if data == "":
    data = None

if data is None:
    print("Data belum diisi.")
else:
    print("Data sudah diisi.")
    
    
a = [1, 2, 3]
b = [1, 2, 3]

if a is not b:
    print("a dan b adalah objek yang berbeda.")
else:
    print("a dan b adalah objek yang sama.")
    
print("\n11. OPERATOR PENUGASAN")

nama = "Dina"
umur = 21
print(f"Nama: {nama}, Umur: {umur}")

skor = 50
skor += 20
print(f"Skor akhir: {skor}")

stok_barang = 100
stok_barang -= 15
print(f"Stok tersisa: {stok_barang}")

pesan = "Halo"
pesan += ", selamat datang!"
print(pesan)


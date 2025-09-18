# ----------- Tipe Data Primitif -----------

# Integer
angka_bulat = 42
print("Integer:", angka_bulat, "| Tipe:", type(angka_bulat))

# Float
angka_desimal = 3.14159
print("Float:", angka_desimal, "| Tipe:", type(angka_desimal))

# Boolean
is_active = True
is_logged_in = False
print("Boolean 1:", is_active, "| Boolean 2:", is_logged_in)

# String
nama = "Python Programming"
print("String:", nama, "| Panjang:", len(nama))

# ----------- Operasi pada String -----------
print("\nOperasi String:")
print("Huruf besar:", nama.upper())
print("Huruf kecil:", nama.lower())
print("Potong kata pertama:", nama.split()[0])
print("Ganti kata:", nama.replace("Programming", "Language"))

# ----------- Tipe Data Kompleks -----------
bil_kompleks = 4 + 5j
print("\nBilangan Kompleks:", bil_kompleks)
print("Real:", bil_kompleks.real, "| Imaginer:", bil_kompleks.imag)

# NoneType
tidak_ada = None
print("NoneType:", tidak_ada, "| Tipe:", type(tidak_ada))

# ----------- Tipe Data Koleksi -----------

# List
daftar_buah = ["apel", "jeruk", "pisang"]
print("\nList:", daftar_buah)
daftar_buah.append("mangga")
print("Setelah ditambah:", daftar_buah)
print("Buah pertama:", daftar_buah[0])
print("Buah terakhir:", daftar_buah[-1])

# Tuple (tidak bisa diubah)
koordinat = (10.5, 20.7)
print("\nTuple:", koordinat)

# Set (tidak duplikat, tidak berurutan)
angka_unik = {1, 2, 2, 3, 4, 4}
print("\nSet:", angka_unik)

# Dictionary (key-value pair)
biodata = {
    "nama": "Andi",
    "umur": 25,
    "hobi": ["coding", "membaca"]
}
print("\nDictionary:", biodata)
print("Nama:", biodata["nama"])
print("Hobi ke-1:", biodata["hobi"][0])

# ----------- Operasi Matematika ----------
a = 10
b = 3
print("\nOperasi Matematika:")
print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Modulus:", a % b)
print("Pangkat:", a ** b)

# ----------- Konversi Tipe Data ----------
print("\nKonversi Tipe:")
angka_str = "123"
angka_int = int(angka_str)
print("String ke Int:", angka_int)

float_ke_int = int(3.99)
print("Float ke Int:", float_ke_int)

int_ke_str = str(999)
print("Int ke String:", int_ke_str)

list_str = list("Python")
print("String ke List:", list_str)

# ----------- Nested Tipe Data ----------
mahasiswa = {
    "nama": "Budi",
    "nilai": {
        "matematika": 85,
        "bahasa": 90
    },
    "lulus": True
}
print("\nNested Dictionary:")
print("Nilai Matematika:", mahasiswa["nilai"]["matematika"])

# ----------- Looping Koleksi ----------
print("\nLooping List:")
for buah in daftar_buah:
    print("-", buah)

print("\nLooping Dictionary:")
for k, v in biodata.items():
    print(f"{k.capitalize()}: {v}")

# ----------- Tipe Data Dinamis ----------
print("\nTipe Data Dinamis:")
variabel = 10
print("Tipe awal:", type(variabel))
variabel = "Sekarang string"
print("Tipe berubah:", type(variabel))

# ----------- Fungsi dengan Tipe Data -----------

def deskripsikan_buah(buah_list):
    print("\nDeskripsi Buah:")
    for i, buah in enumerate(buah_list):
        print(f"{i+1}. {buah.capitalize()}")

deskripsikan_buah(daftar_buah)

# ----------- Penanganan Tipe Data Error -----------

def bagi(a, b):
    try:
        hasil = a / b
        return hasil
    except ZeroDivisionError:
        return "Error: Pembagian dengan nol"
    except TypeError:
        return "Error: Tipe data tidak sesuai"

print("\nFungsi Bagi:")
print("10 / 2 =", bagi(10, 2))
print("10 / 0 =", bagi(10, 0))
print("10 / 'a' =", bagi(10, 'a'))

# ----------- Akhir Program -----------
print("\n=== Program Selesai ===")

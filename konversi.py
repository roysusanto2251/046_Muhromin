# ================================
# PROGRAM KONVERSI TIPE DATA DI PYTHON
# ================================

print("=== KONVERSI TIPE DATA PYTHON ===\n")

# ----------- Konversi Implisit (Automatic) -----------
print("1. Konversi Implisit (Otomatis):")

x = 10      # integer
y = 2.5     # float

z = x + y   # hasil otomatis jadi float
print("x =", x, "| Tipe:", type(x))
print("y =", y, "| Tipe:", type(y))
print("x + y =", z, "| Tipe:", type(z))

# ----------- Konversi Eksplisit (Manual) -----------
print("\n2. Konversi Eksplisit (Manual):")

angka_str = "123"
print("angka_str =", angka_str, "| Tipe awal:", type(angka_str))

# String ke Integer
angka_int = int(angka_str)
print("Konversi ke int:", angka_int, "| Tipe:", type(angka_int))

# Integer ke Float
angka_float = float(angka_int)
print("Konversi ke float:", angka_float)

# Float ke String
angka_str2 = str(angka_float)
print("Konversi ke string:", angka_str2, "| Tipe:", type(angka_str2))

# Integer ke Boolean
print("int(0) ->", bool(0))
print("int(5) ->", bool(5))

# ----------- Konversi String yang Tidak Valid -----------
print("\n3. Konversi Gagal:")

invalid_str = "abc"
try:
    hasil = int(invalid_str)
except ValueError:
    print(f"'{invalid_str}' tidak bisa dikonversi ke int.")

# ----------- Konversi List, Tuple, Set, Dict -----------
print("\n4. Konversi Koleksi Data:")

# List ke Tuple
buah_list = ["apel", "jeruk", "mangga"]
buah_tuple = tuple(buah_list)
print("List:", buah_list, "| Tipe:", type(buah_list))
print("Ke Tuple:", buah_tuple, "| Tipe:", type(buah_tuple))

# Tuple ke List
buah_list2 = list(buah_tuple)
print("Ke List lagi:", buah_list2)

# List ke Set
buah_set = set(buah_list)
print("Ke Set (hilangkan duplikat):", buah_set)

# Set ke List
buah_list3 = list(buah_set)
print("Set ke List lagi:", buah_list3)

# List of tuples ke Dictionary
pasangan = [("nama", "Rina"), ("umur", 21)]
data_dict = dict(pasangan)
print("List of Tuples:", pasangan)
print("Ke Dictionary:", data_dict)

# Dictionary ke List of keys
dict_keys = list(data_dict.keys())
dict_values = list(data_dict.values())
print("Keys:", dict_keys)
print("Values:", dict_values)

# ----------- Konversi Boolean ke Angka/String -----------
print("\n5. Konversi Boolean:")

print("True -> int:", int(True))
print("False -> int:", int(False))
print("True -> str:", str(True))
print("False -> str:", str(False))

# ----------- Input dan Konversi ----------
print("\n6. Input User dan Konversi:")

user_input = input("Masukkan angka: ")
try:
    angka_user = float(user_input)
    print("Dikonversi ke float:", angka_user)
    print("Dikonversi ke int:", int(angka_user))
except ValueError:
    print("Input tidak valid untuk konversi ke angka.")

# ----------- Konversi Karakter ke ASCII dan Sebaliknya ----------
print("\n7. Karakter dan ASCII:")

karakter = "A"
ascii_code = ord(karakter)
karakter_kembali = chr(ascii_code)
print("Karakter:", karakter, "-> ASCII:", ascii_code)
print("ASCII:", ascii_code, "-> Karakter:", karakter_kembali)

# ----------- Fungsi Umum Konversi ----------
print("\n8. Fungsi Konversi Umum:")

def coba_konversi(data):
    print(f"\nData: {data} | Tipe: {type(data)}")
    try:
        print("Ke int:", int(data))
    except:
        print("Gagal ke int.")
    try:
        print("Ke float:", float(data))
    except:
        print("Gagal ke float.")
    try:
        print("Ke str:", str(data))
    except:
        print("Gagal ke str.")
    try:
        print("Ke bool:", bool(data))
    except:
        print("Gagal ke bool.")

contoh_data = ["123", "3.14", "", "hello", 0, 1, None, True, False]
for item in contoh_data:
    coba_konversi(item)

# ----------- Akhir Program -----------
print("\n=== Selesai ===")

# Konversi tipe data
print("\nKONVERSI TIPE DATA")
print("-" * 30)

angka_string = "123"
angka_float = "45.67"

# Konversi string → integer dan float
konversi_int = int(angka_string)
konversi_float = float(angka_float)

print(f"String '{angka_string}' menjadi integer: {konversi_int}")
print(f"String '{angka_float}' menjadi float: {konversi_float}")
print(f"Integer {konversi_int} menjadi string: '{str(konversi_int)}'")
print("")
print(f"String '{angka_string}' (tipe: {type(konversi_int)})")
print(f"String '{angka_float}' (tipe: {type(konversi_float)})")
print(f"Integer '{konversi_int}' (tipe: {type(konversi_int)})")
print(f"Float '{konversi_float}' (tipe: {type(konversi_float)})")

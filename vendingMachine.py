# Program Vending Machine sederhana
print("=== Vending Machine ===")  # Judul program
print("*" * 30)  # Garis pembatas
print("Menu Pilihan:")  # Teks menu
print("-" * 30)  # Garis pembatas
print("\n1. Es Teh - 5000", "\n2. Jus Buah - 5000", "\n3. Soda - 7000")  # Daftar menu

# Meminta input dari user
pilihan = input("Masukkan pilihan (1-3): ")
# Mengecek apakah input berupa angka
if pilihan.isdigit():
    pilihan = int(pilihan)
    # Mengecek pilihan dan menampilkan hasil sesuai input
    if pilihan == 1:
        print("Anda memilih Es Teh, harga 5000.")
    elif pilihan == 2:
        print("Anda memilih Jus Buah, harga 5000.")
    elif pilihan == 3:
        print("Anda memilih Soda, harga 7000.") 
    else:
        print("Pilihan tidak valid.")
else:
    print("Input harus berupa angka!")
# Menghitung rata-rata dari sebuah daftar angka menggunakan loop while

# data = [2, 4, 6, 8, 10]

# sum = 0    
# i = 0

# if data[1] < 7:
#     sum += data[1]

# while i < len(data):
#     sum += data[i]
#     i += 1

# rata_rata = sum / len(data)
# print("Rata-rata:", rata_rata)

# while untuk mengontrol eksekusi berulang

# users = ["Ali", "Budi", "Citra", "Dodi", "Ella"]
# active_users = ["Ali", "Citra", "Ella"]
# admin = ["Dodi", "Ella"]

# # Cek status untuk users[1]
# user = users[1]

# if user in active_users:
#     if user in admin:
#         print(f"{user} is admin and active")
#     else:
#         print(f"{user} is active")
# else:
#     print(f"{user} is not active")

# # Cek status untuk seluruh user menggunakan while
# i = 0
# while i < len(users):
#     current_user = users[i]

#     if current_user in active_users:
#         print(f"{current_user} is active")
#     else:
#         print(f"{current_user} is not active")

#     i += 1
    
    
# penggunaan while loop dalam filter data
# data = [5, 12, 8, 20, 7, 14, 11]
# filtered_data = []  
# i = 0

# while i < len(data):
#     if data[i] > 10:
#         filtered_data.append(data[i])
#     i += 1
    
# print("Filtered data :", filtered_data)


# memisahkan bilangan ganjil dan genap menggunakan while loop
# data = [5, 12, 8, 20, 7, 14, 11]

# ganjil = []
# genap = []

# i = 0
# while i < len(data):
#     if data[i] % 2 == 0:      
#         genap.append(data[i])
#     else:                    
#         ganjil.append(data[i])
#     i += 1

# print("Bilangan genap :", genap)
# print("Bilangan ganjil:", ganjil)

# penggunaan while loop dalam transformasi data
harga = [10000, 25000, 15000, 30000]
i = 0

while i < len(harga):
    harga[i] = 'Rp ' + str(harga[i])
    i += 1
    
print("Harga setelah transformasi:", harga)
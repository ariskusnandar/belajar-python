# Program Memanggil Module Sendiri

import my_module

print("=== MENGGUNAKAN MODULE SENDIRI ===")

# Menggunakan fungsi dari module
nama = "Aris"
print(my_module.sapa(nama))

# Operasi matematika
a = 10
b = 5
print(f"{a} + {b} = {my_module.tambah(a, b)}")
print(f"{a} - {b} = {my_module.kurang(a, b)}")
print(f"{a} x {b} = {my_module.kali(a, b)}")
print(f"{a} / {b} = {my_module.bagi(a, b)}")

# Mengakses variabel dari module
print(f"Nilai PI: {my_module.PI}")
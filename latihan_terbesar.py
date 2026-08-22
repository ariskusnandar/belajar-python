# Program Menentukan bilangan Terbesar

print("=== Menentukan Bilangan Terbesar ===")

# Meminta input 3 angka
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

# Menentukan terbesar
if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print(f"Angka terbesar di antara {a}, {b}, dan {c} adalah {terbesar}")
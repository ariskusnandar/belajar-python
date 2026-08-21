# Latihan Operator dan Logika

print("=== CEK ANGKA ===")

angka = int(input("Masukkan sebuah angka: "))

# Cek positif/negatif/nol
if angka > 0:
    print(f"{angka} adalah angka POSITIF.")
elif angka < 0:
    print(f"{angka} adalah angka NEGATIF.")
else:
    print(f"{angka} adalah angka NOL.")

# Cek genap/ganjil (hanya untuk angka positif)
if angka > 0:
    if angka % 2 == 0:
        print(f"{angka} adalah angka GENAP.")
    else:
        print(f"{angka} adalah angka GANJIL.")

# Cek apakah angka ada di rentang 1-100
if 1 <= angka <= 100:
    print(f"{angka} berada di antara 1-100.")
else:
    print(f"{angka} TIDAK berada di antara 1-100.")
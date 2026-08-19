# Game Tebak Angka Menggunakan Module random

import random

print("=== GAME TEBAK ANGKA ===")
print()

# Menentukan angka rahasia (1-100)
angka_rahasia = random.randint(1, 100)
kesempatan = 5

print("Saya sudah memilih angka antara 1-100.")
print(f"Kamu memiliki {kesempatan} kesempatan untuk menebak.")
print()

while kesempatan > 0:
    try:
        tebakan = int(input(f"Masukkan tebakanmu ({kesempatan} kesempatan lagi): "))

        if tebakan < 1 or tebakan > 100:
            print("Angka harus antara 1-100!\n")
            continue

        if tebakan == angka_rahasia:
            print(f"Selamat! Kamu benar! Angkanya adalah {angka_rahasia}.")
            break
        elif tebakan < angka_rahasia:
            print("Terlalu rendah! Coba lagi.\n")
        else:
            print("Terlalu tinggi! Coba lagi.\n")

        kesempatan -= 1

    except ValueError:
        print("Masukkan angka yang valid!\n")

if kesempatan == 0:
    print(f"Maaf, kesempatan habis. Angka rahasianya adalah {angka_rahasia}.")
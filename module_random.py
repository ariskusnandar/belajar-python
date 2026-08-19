# Program Menggunakan Module random

import random

print("=== MODULE RANDOM ===")

# Angka acak antara 1-10
angka = random.randint(1, 10)
print(f"Angka acak 1-10: {angka}")

# Angka acak desimal antara 0-1
desimal = random.random()
print(f"Angka acak 0-1: {desimal}")

# Pilih acak dari list
buah = ["Apel", "Jeruk", "Mangga", "Pisang"]
pilihan = random.choice(buah)
print(f"Pilihan acak dari list buah: {pilihan}")

# Acak urutan list
random.shuffle(buah)
print(f"List setelah diacak: {buah}")
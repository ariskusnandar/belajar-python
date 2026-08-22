# Program Penjumlahan Berhenti

print("=== PROGRAM PENJUMLAHAN ===")
print("Masukkan 0 untuk berhenti.")

total = 0

while True:
    angka = float(input("Masukkan angka: "))

    if angka == 0:
        print("Program berhenti.")
        break

    total += angka
    print(f"Total sementara: {total}")

print(f"Total akhir: {total}")
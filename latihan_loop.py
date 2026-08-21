# Latihan Loop dan Operator

print("=== PENJUMLAHAN 5 ANGKA ===")

total = 0

for i in range(1, 6):
    angka = float(input(f"Masukkan angka ke-{i}: "))
    total += angka # total = total + angka

print(f"\nTotal penjumlahan: {total}")
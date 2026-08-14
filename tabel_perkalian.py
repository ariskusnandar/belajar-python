# Program Tabel Perkalian

print("=== TABEL PERKALIAN 1-10 ===")
print()

for i in range(1, 11):
    for j in range(1, 11):
        hasil = i * j
        print(f"{i} x {j} = {hasil}", end="\t")
    print()
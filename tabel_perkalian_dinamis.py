# Program Tabel Perkalian Dinamis

print("=== TABEL PERKALIAN DINAMIS ===")
n = int(input("Mau tabel perkalian sampai berapa? "))

print() # Baris kosong
for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i} x {j} = {i*j}", end="\t")
    print() # Baris kosong
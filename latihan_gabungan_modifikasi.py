# Latihan Gabungan Modifikasi (Loop + If-Else) + Total & Rata-rata

print("=== PROGRAM PREDIKAT NILAI ===")
print("Masukkan 0 untuk keluar.")

# Inisialisasi variabel
total = 0
jumlah = 0

while True:
    try:
        nilai = int(input("\nMasukkan nilai (0-100): "))

        if nilai == 0:
            print("\nTerima kasih!")
            break
        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0-100!")
            continue

        # Tambahkan nilai ke total dan hitung jumlah data
        total += nilai
        jumlah += 1

        # Menentkan predikat
        if nilai >= 80:
            predikat = "A"
        elif nilai >= 60:
            predikat = "B"
        elif nilai >= 40:
            predikat = "C"
        else:
            predikat = "D"

        print(f"Nilai {nilai} -> Predikat: {predikat}")

    except ValueError:
        print("Error: Masukkan angka yang valid!")

# Menampilkan total dan rata-rata setelah loop selesai
if jumlah > 0:
    rata_rata = total / jumlah
    print(f"\nTotal nilai yang dimasukkan: {total}")
    print(f"Jumlah data: {jumlah}")
    print(f"Rata-rata nilai: {rata_rata}")
else:
    print("\nTidak ada data yang dimasukkan.")
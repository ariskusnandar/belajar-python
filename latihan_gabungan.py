# Latihan Gabungan (Loop + If-Else)

print("=== PROGRAM PREDIKAT NILAI ===")
print("Masukkan 0 untuk keluar.")

while True:
    try:
        nilai = int(input("\nMasukkan nilai (1-100): "))

        if nilai == 0:
            print("Terima kasih!")
            break

        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0-100!")
            continue

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
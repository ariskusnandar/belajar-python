# Program Nilai Akhir

print("=== PROGRAM NILAI AKHIR ===")
print("Masukkan -1 untuk keluar.")

while True:
    try:
        nilai = float(input("\nMasukkan nilai (1-100): "))

        if nilai == -1:
            print("Terima kasih!")
            break

        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0-100! Silakan coba lagi.")
            continue

        if nilai >= 85:
            predikat = "A"
        elif nilai >= 70:
            predikat = "B"
        elif nilai >= 60:
            predikat = "C"
        else:
            predikat = "D"

        print(f"Nilai: {nilai} -> Predikat: {predikat}")

    except ValueError:
        print("Error: Masukkan angka yang valid!")
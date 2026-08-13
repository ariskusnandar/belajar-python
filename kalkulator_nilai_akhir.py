# Program Kalkulator Nilai Akhir

print("=== KALKULATOR NILAI AKHIR ===")
print()

# Memasukakan nilai
tugas = float(input("Masukkan nilai tugas (0-100): "))
uts = float(input("Masukkan nilai UTS (0-100): "))
uas = float(input("Masukkan nilai UAS (0-100): "))

# Menghitung nilai akhir
nilai_akhir = (tugas * 0.2) + (uts * 0.3) + (uas * 0.5)

# Menentukan predikat
if nilai_akhir >= 80:
    predikat = "A"
    status = "LULUS"
elif nilai_akhir >= 70:
    predikat = "B"
    status = "LULUS"
elif nilai_akhir >= 60:
    predikat = "C"
    status = "LULUS"
else:
    predikat = "D"
    status = "TIDAK LULUS"

# Menampilkan hasil
print("\n=== HASIL AKHIR ===")
print("Nilai Akhir:", round(nilai_akhir, 2))
print("Predikat:", predikat)
print("Status:", status)

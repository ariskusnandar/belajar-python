# Pogram Predikat Nilai

print("=== PROGRAM PREDIKAT NILAI ===")

nilai = int(input("Masukan nilai kamu (0-100): "))

if nilai >= 90:
    predikat = "A (sangat Baik)"
elif nilai >= 80:
    predikat = "B (Baik)"
elif nilai >= 70:
    predikat = "C (Cukup)"
elif nilai >= 60:
    predikat = "D (Kurang)"
else:
    predikat = "E (Sangat Kurang)"

print("Nilai kamu:", nilai)
print("Predikat:", predikat)


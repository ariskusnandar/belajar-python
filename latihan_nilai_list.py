# Program Nilai Akhir dengan List

print("=== PROGRAM NILAI AKHIR ===")
print("Masukkan nilai (-1 untuk selesai).")

nilai_list = []

while True:
    try:
        nilai = float(input("Masukkan nilai: "))

        if nilai == -1:
            break

        if 0 <= nilai <= 100:
            nilai_list.append(nilai)
            print(f"Nilai {nilai} berhasil ditambahkan.")
        else:
            print("Nilai harus antara 0-100!")

    except ValueError:
        print("Masukkan angka yang valid!")

# Menampilkan hasil
if len(nilai_list) > 0:
    print("\n=== HASIL ===")
    print(f"Semua nilai: {nilai_list}")
    print(f"Jumlah data: {len(nilai_list)}")
    print(f"Nilai tertinggi: {max(nilai_list)}")
    print(f"Nilai terendah: {min(nilai_list)}")
    print(f"Rata-rata: {sum(nilai_list)}")
else:
    print("\nTidak ada data yang dimasukkan.")
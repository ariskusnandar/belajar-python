# Program Mengelola Daftar Buah

print("=== MENGELOLA DAFTAR BUAH ===")

buah = ["Apel", "Jeruk", "Mangga"]
print("Daftar awal:", buah)

# 1. Menambah data
buah.append("Pisang")
print("Setelah tambah Pisang:", buah)

# 2. Menambah di posisi tertentu
buah.insert(1, "Stroberi")
print("Setelah insert stroberi di index 1:", buah)

# 3. Hapus Jeruk
buah.remove("Jeruk")
print("Setelah hapus Jeruk:", buah)

# 4. Mengubah data
buah[2] = "Melon"
print("Setelah ubah index 2 menjadi Melon:", buah)

# 5. Menghapus data terakhir
buah.pop()
print("Setelah hapus data terakhir:", buah)

# 6. Mengecek apakah ada data
if "Apel" in buah:
    print("Apel masih ada di daftar!")
else:
    print("Apel sudah tidak ada.")
print("Jumlah buah sekarang:", len(buah))
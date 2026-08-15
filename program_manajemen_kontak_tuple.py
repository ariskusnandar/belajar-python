# Program Manajemen Kontak

print("=== MANAJEMEN KONTAK ===")

kontak = []

while True:
    print("\n1. Tambah Kontak")
    print("2. Lihat Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

    pilihan = input("Pilihan menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        telepon = input("Masukkan nomor telepon: ")
        kontak.append({"nama": nama, "telepon": telepon})
        print(f"Kontak '{nama}' berhasil ditambahkan!")

    elif pilihan == "2":
        # Tampilkan semua kontak
        pass

    # ... dan seterusnya
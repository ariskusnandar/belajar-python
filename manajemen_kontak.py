# Program Manajemen Kontak dengan Fungsi
print("=== PROGRAM MANAJEMEN KONTAK ===")
print()

# Data Kontak (list of dictionary)
kontak = []

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nMENU:")
    print("1. Tambah Kontak")
    print("2. Lihat Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

# Fungsi untuk menambah kontak
def tambah_kontak():
    print("\n--- TAMBAH KONTAK ---")
    nama = input("Masukkan nama: ")
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")

    # Menyimpan data dalam dictionary
    data = {
        "nama": nama,
        "telepon": telepon,
        "email": email
    }
    kontak.append(data)
    print(f"Kontak '{nama}' berhasil ditambahkan!")

# Fungsi untuk melihat semua kontak
def lihat_kontak():
    print("\n--- DAFTAR KONTAK ---")
    if len(kontak) == 0:
        print("Belum ada kontak.")
    else:
        for i, data in enumerate(kontak, start=1):
            print(f"{i}. Nama: {data['nama']}")
            print(f"    Telepon: {data['telepon']}")
            print(f"    Email: {data['email']}")

# Fungsi untuk mencari kontak
def cari_kontak():
    print("\n--- CARI KONTAK ---")
    keyword = input("Masukkan nama yang dicari: ")

    ditemukan = []
    for data in kontak:
        if keyword.lower() in data["nama"].lower():
            ditemukan.append(data)

    if len(ditemukan) == 0:
        print(f"Kontak dengan nama '{keyword}' tidak ditemukan.")
    else:
        print(f"Ditemukan {len(ditemukan)} kontak:")
        for data in ditemukan:
            print(f"- Nama: {data['nama']}")
            print(f"  Telepon: {data['telepon']}")
            print(f" Email: {data['email']}")

# Fungsi untuk menghapus kontak
def hapus_kontak():
    print("\n--- HAPUS KONTAK ---")
    if len(kontak) == 0:
        print("Belum ada kontak.")
        return

    # Tampilkan daftar kontak
    for i, data in enumerate(kontak, start=1):
        print(f"{i}. {data['nama']}")

    try:
        nomor = int(input("Masukkan nomor kontak yang ingin dihapus: "))
        if 1 <= nomor <= len(kontak):
            hapus = kontak.pop(nomor - 1)
            print(f"Kontak '{hapus['nama']}' berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")

# Program utama (loop)
while True:
    tampilkan_menu()
    pilihan = input("Pilihan menu (1-5): ")

    if pilihan == "1":
        tambah_kontak()
    elif pilihan == "2":
        lihat_kontak()
    elif pilihan == "3":
        cari_kontak()
    elif pilihan == "4":
        hapus_kontak()
    elif pilihan == "5":
        print("\nTerima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")
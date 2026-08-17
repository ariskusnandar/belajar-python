# Program Manajemen Kontak dengan Penyimpanan File

print("=== PROGRAM MANAJEMEN KONTAK (DENGAN FILE) ===")
print()

# Nama file untuk menyimpan data
FILE_KONTAK = "kontak.txt"

# Fungsi untuk membuat data dari file
def muat_kontak():
    kontak = []
    try:
        with open(FILE_KONTAK, "r") as file:
            for baris in file:
                # Format: nama|telepon|email
                data = baris.strip().split("|")
                if len(data) == 3:
                    kontak.append({
                        "nama": data[0],
                        "telepon": data[1],
                        "email": data[2]
                    })
    except FileNotFoundError:
        # File belum ada, buat baru
        with open(FILE_KONTAK, "w") as file:
            pass # Buat file kosong
    return kontak

# Fungsi untuk menyimpan data ke file
def simpan_kontak(kontak):
    with open(FILE_KONTAK, "w") as file:
        for data in kontak:
            file.write(f"{data['nama']}|{data['telepon']}|{data['email']}\n")

# Muat data kontak dari file
kontak = muat_kontak()
print(f"Berhasil memuat {len(kontak)} kontak dari file.\n")

# --- FUNGSI MENU (sama seperti sebelumnya) ---
def tampilkan_menu():
    print("\nMENU:")
    print("1. Tambah Kontak")
    print("2. Lihat Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

def tambah_kontak():
    global kontak
    print("\n--- TAMBAH KONTAK ---")
    nama = input("Masukkan nama: ")
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")

    kontak.append({"nama": nama, "telepon": telepon, "email": email})
    simpan_kontak(kontak) # Simpan ke file
    print(f"Kontak '{nama}' berhasil ditambahkan!")

def lihat_kontak():
    print("\n--- DAFTAR KONTAK ---")
    if len(kontak) == 0:
        print("Belum ada kontak.")
    else:
        for i, data in enumerate(kontak, start=1):
            print(f"{i}. Nama: {data['nama']}")
            print(f"   Telepon: {data['telepon']}")
            print(f"   Email: {data['email']}")

def cari_kontak():
    print("\n--- CARI KONTAK ---")
    keyword = input("Masukkan nama yang dicari: ")

    ditemukan = [data for data in kontak if keyword.lower() in data["nama"].lower()]

    if len(ditemukan) == 0:
        print(f"Kontak dengan nama '{keyword}' tidak ditemukan.")
    else:
        print(f"Ditemukan {len(ditemukan)} kontak:")
        for data in ditemukan:
            print(f"- Nama: {data['nama']}")
            print(f"  Telepon: {data['telepon']}")
            print(f"  Email: {data['email']}")

def hapus_kontak():
    global kontak
    print("\n--- HAPUS KONTAK ---")
    if len(kontak) == 0:
        print("Belum ada kontak.")
        return

    for i, data in enumerate(kontak, start=1):
        print(f"{i}. {data['nama']}")

    try:
        nomor = int(input("Masukkan nomor kontak yang ingin dihapus: "))
        if 1 <= nomor <= len(kontak):
            hapus = kontak.pop(nomor -1)
            simpan_kontak(kontak) # Simpan perubahan ke file
            print(f"Kontak '{hapus['nama']}' berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")

# --- PROGRAM UTAMA ---
while True:
    tampilkan_menu()
    pilihan = input("Pilhan menu (1-5): ")

    if pilihan == "1":
        tambah_kontak()
    elif pilihan == "2":
        lihat_kontak()
    elif pilihan == "3":
        cari_kontak()
    elif pilihan == "4":
        hapus_kontak()
    elif pilihan == "5":
        simpan_kontak(kontak) # Simpan terakhir sebelum keluar
        print("\nTerima kasih! Data kontak telah disimpan.")
        break
    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")
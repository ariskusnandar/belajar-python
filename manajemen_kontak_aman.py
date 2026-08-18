# Program Manajemen Kontak dengan Error Handling

print("=== PROGRAM MANAJEMEN KONTAK (DENGAN ERROR HANDLING) ===")
print()

FILE_KONTAK = "kontak.txt"

def muat_kontak():
    kontak = []
    try:
        with open(FILE_KONTAK, "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 3:
                    kontak.append({
                        "nama": data[0],
                        "telepon": data[1],
                        "email": data[2]
                    })
        print(f"Berhasil memuat {len(kontak)} kontak dari file.")
    except FileNotFoundError:
        print("File kontak belum ada. Akan dibuat baru.")
        try:
            with open(FILE_KONTAK, "w") as file:
                pass
        except Exception as e:
            print(f"Error saat membuat file: {e}")
    except Exception as e:
        print(f"Error saat memuat kontak: {e}")
    return kontak

def simpan_kontak(kontak):
    try:
        with open(FILE_KONTAK, "w") as file:
            for data in kontak:
                file.write(f"{data['nama']}|{data['telepon']}|{data['email']}\n")
    except Exception as e:
        print(f"Error saat menyimpan kontak: {e}")

def tambah_kontak(kontak):
    print("\n--- TAMBAH KONTAK ---")

    # Validasi input nama
    while True:
        nama = input("Masukkan nama: ").strip()
        if nama:
            break
        print("Nama tidak boleh kosong! Silakan coba lagi.")

    # Validasi input telepon
    while True:
        telepon = input("Masukkan nomor telepon: ").strip()
        if telepon:
            break
        print("Nomor telepon tidak boleh kosong! Silakan coba lagi.")

    # Validasi input email
    while True:
        email = input("Masukkan email: ").strip()
        if email:
            break
        print("Email tidak boleh kosong! Silakan coba lagi.")

    kontak.append({"nama": nama, "telepon": telepon, "email": email})
    simpan_kontak(kontak)
    print(f"Kontak '{nama}' berhasil ditambahkan!")

def lihat_kontak(kontak):
    print("\n--- DAFTAR KONTAK ---")
    if len(kontak) == 0:
        print("Belum ada kontak.")
    else:
        for i, data in enumerate(kontak, start=1):
            print(f"{i}. Nama: {data['nama']}")
            print(f"   Telepon: {data['telepon']}")
            print(f"   Email: {data['email']}")
        print(f"\nTotal kontak: {len(kontak)}")

def cari_kontak(kontak):
    print("\n--- CARI KONTAK ---")
    keyword = input("Masukkan nama yang dicari: ").strip()

    if not keyword:
        print("Keyword tidak boleh kosong!")
        return

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
            print(f"  Email: {data['email']}")

def hapus_kontak(kontak):
    print("\n--- HAPUS KONTAK ---")
    if len(kontak) == 0:
        print("Belum ada kontak.")
        return

    for i, data in enumerate(kontak, start=1):
        print(f"{i}. {data['nama']}")

    try:
        nomor = input("Masukkan nomor kontak yang ingin dihapus: ").strip()
        if not nomor:
            print("Input tidak boleh kosong!")
            return

        nomor = int(nomor)
        if 1 <= nomor <= len(kontak):
            hapus = kontak.pop(nomor - 1)
            simpan_kontak(kontak)
            print(f"Kontak '{hapus['nama']}' berhasil dihapus!")
        else:
            print("Nomor tidak valid! Harus antara 1 sampai", len(kontak))
    except ValueError:
        print("Error: Kamu harus memasukkan angka!")
    except Exception as e:
        print(f"Error tak terduga: {e}")

def tampilkan_menu():
    print("\n" + "="*30)
    print("MENU:")
    print("1. Tambah Kontak")
    print("2. Lihat Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")
    print("="*30)

# --- PROGRAM UTAMA ---
kontak = muat_kontak()

while True:
    tampilkan_menu()
    pilihan = input("Pilihan menu (1-5): ").strip()

    if pilihan == "1":
        tambah_kontak(kontak)
    elif pilihan == "2":
        lihat_kontak(kontak)
    elif pilihan == "3":
        cari_kontak(kontak)
    elif pilihan == "4":
        hapus_kontak(kontak)
    elif pilihan == "5":
        simpan_kontak(kontak)
        print("\nTerima kasih! Data kontak telah disimpan.")
        break
    else:
        print("Pilihann tidak valid! Silakan pilih 1-5.")



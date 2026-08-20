# Program Daftar Belanja dengan Fungsi

belanja = []

def tambah_item():
    item = input("Masukkan nama item: ")
    belanja.append(item)
    print(f"'{item}' berhasil ditambahkan!")

def lihat_item():
    if len(belanja) == 0:
        print("Daftar belanja kosong.")
    else:
        print("\n=== DAFTAR BELANJA ===")
        for i, item in enumerate(belanja, start=1):
            print(f"{i}. {item}")

def hapus_item():
    if len(belanja) == 0:
        print("Daftar belanja kosong.")
        return

    lihat_item()
    try:
        nomor = int(input("Masukkan nomor item yang ingin dihapus: "))
        if 1 <= nomor <= len(belanja):
            hapus = belanja.pop(nomor - 1)
            print(f"'{hapus}' berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")

# Program Utama
while True:
    print("\n=== MENU DAFTAR BELANJA ===")
    print("1. Tambah item")
    print("2. Lihat item")
    print("3. Hapus item")
    print("4. Keluar")

    pilihan = input("Pilihan menu (1-4): ")

    if pilihan == "1":
        tambah_item()
    elif pilihan == "2":
        lihat_item()
    elif pilihan == "3":
        hapus_item()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
                    
# Program Daftar Belanja Interaktif

print("=== PROGRAM DAFTAR BELANJA ===")
print()

belanja = []

while True:
    print("1. Lihat daftar belanja")
    print("2. Tambah item")
    print("3. Hapus item")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        if len(belanja) == 0:
            print("\nDaftar belanja kosong.\n")
        else:
            print("\n=== DAFTAR BELANJA ===")
            for i, item in enumerate(belanja, start=1):
                print(f"{i}. {item}")
            print()

    elif pilihan == "2":
        item = input("Masukkan nama item: ")
        belanja.append(item)
        print(f"'{item}' berhasil ditambahkan!\n")

    elif pilihan == "3":
        if len(belanja) == 0:
            print("\nDaftar belanja kosong, tidak ada yang bisa dihapus.\n")
        else:
            print("\n=== DAFTAR BELANJA ===")
            for i, item in enumerate(belanja, start=1):
                print(f"{i}. {item}")
            print()

            try:
                nomor = int(input("Masukkan nomor item yang ingin dihapus: "))
                if 1 <= nomor <= len(belanja):
                    item_hapus = belanja.pop(nomor - 1)
                    print(f"'{item_hapus}' berhasil dihapus!\n")
                else:
                    print("Nomor tidak valid!\n")
            except ValueError:
                print("Masukka angka yang valid!\n")
    elif pilihan == "4":
        print("\nTerima kasih! Sampai jumpa.")
        break

    else:
        print("\nPilihan tidak valid! Silakan pilih 1-4. \n")
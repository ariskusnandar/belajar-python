# Program Membaca File dengan Error Handling

print("=== PROGRAM BACA FILE AMAN ===")

nama_file = input("Masukkan nama file yang ingin dibaca: ")

try:
    with open(nama_file, "r") as file:
        isi = file.read()
        print(f"\nIsi file '{nama_file}':")
        print(isi)

except FileNotFoundError:
    print(f"Error: File '{nama_file}' tidak ditemukan!")
except PermissionError:
    print(f"Error: Tidak memiliki izin untuk membaca file '{nama_file}'!")
except Exception as e:
    print(f"Error tak terduga: {e}")
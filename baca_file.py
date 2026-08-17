# Program Membaca Data dari File

print("=== MEMBACA FILE ===")

try:
    with open("data.txt", "r") as file:
        isi = file.read()
        print("Isi file 'data.txt':")
        print(isi)
except FileNotFoundError:
    print("File 'data.txt' tidak ditemukan!")
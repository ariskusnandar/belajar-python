# Program Menambahkan Data ke File

print("=== MENAMBAH DATA KE FILE ===")

with open("data.txt", "a") as file:
    file.write("Hobi: Coding\n")
    file.write("Pekerjaan: Programmer\n")

print("Data berhasil ditemukan ke 'data.txt'!")
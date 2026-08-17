# Program Menulis Data ke File

print("=== MENULIS FILE ===")

# Menulis data ke file (mode "w" = write)
with open("data.txt", "w") as file:
    file.write("Nama: Aris Kusnandar\n")
    file.write("Umur: 25 tahun\n")
    file.write("Kota: Jakarta\n")

print("Data berhasil disimpan ke file 'data.txt'!")
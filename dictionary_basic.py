# Program Dictionary Sederhana

print("=== DICTIONARY SEDERHANA ===")

# Membuat dictionary
data_diri = {
    "nama": "Aris Kusnandar",
    "umur": 25,
    "kota": "Jakarta",
    "pekerjaan": "Programmer"
}

print("Data Diri:", data_diri)

# Mengakses data berdasarkan key
print("Nama:", data_diri["nama"])
print("Umur:", data_diri["umur"])
print("Kota:", data_diri["kota"])

# Menambah data baru
data_diri["hobi"] = "Coding"
print("Setelah tambah hobi:", data_diri)

# Mengubah data
data_diri["umur"] = 26
print("Setelah ubah umur:", data_diri)

# Menghapus data
del data_diri["pekerjaan"]
print("Setelah hapus pekerjaan:", data_diri)

# Mengecek apakah key ada
if "nama" in data_diri:
    print("Key 'nama' ada di dictionary!")

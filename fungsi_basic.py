# Program Fungsi Dasar

print("=== FUNGSI DASAR ===")

# Fungsi tanpa parameter dan tanpa return
def sapa_pagi():
    print("Selamat pagi, semangat belajar!")

# Fungsi dengan parameter, tanpa return
def sapa_nama(nama):
    print(f"Halo {nama}, selamat datang!")

# Fungsi dengan parameter dan return
def luas_persegi(sisi):
    return sisi * sisi

# Memanggil fungsi
sapa_pagi()
sapa_nama("Aris")

hasil = luas_persegi(5)
print(f"Luas persegi dengan sisi 5 adalah: {hasil}")
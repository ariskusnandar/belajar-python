# Module Buatan Sendiri

def sapa(nama):
    """Fungsi untuk menyapa"""
    return f"Halo {nama}, selamat belajar!"

def tambah(a, b):
    """Fungsi untuk menjumlahkan dua angka"""
    return a + b

def kurang(a, b):
    """Fungsi untuk mengurangkan dua angka"""
    return a - b

def kali(a, b):
    """Fungsi untuk mengalikan dua angka"""
    return a * b

def bagi(a, b):
    """Fungsi untuk membagi dua angka"""
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b

PI = 3.14159
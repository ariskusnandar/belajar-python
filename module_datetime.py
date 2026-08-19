# Program Menggunakan Module datetime

import datetime

print("=== MODULE DATETIME ===")

# Waktu sekarang
sekarang = datetime.datetime.now()
print(f"Waktu sekarang: {sekarang}")

# Format waktu yang lebih rapi
print(f"Tanggal: {sekarang.day}/{sekarang.month}/{sekarang.year}")
print(f"Jam: {sekarang.hour}:{sekarang.minute}:{sekarang:second}")

# Format dengan strftime
print(f"Format rapi: {sekarang.strftime('%A, %d %B %Y %H:%M:%S')}")

# Membuat tanggal sendiri
tanggal_lahir = datetime.datetime(1995, 8, 15)
print(f"Tanggal lahir: {tanggal_lahir.strftime('%d %B %Y')}")

# Menghitung selisih waktu
selisih = sekarang - tanggal_lahir
print(f"Usia dalam hari: {selisih.days} hari")
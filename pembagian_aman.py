# Program Pembagian dengan Error Handling

print("=== PROGRAM PEMBAGIAN AMAN ===")

while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        hasil = angka1 / angka2
        print(f"{angka1} / {angka2} = {hasil}")
        break # Keluar dari loop jika berhasil

    except ValueError:
        print("Error: Kamu harus memasukkan angka! Silakan coba lagi.\n")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol! Silakan coba lagi!\n")
    except Exception as e:
        print(f"Error tak terduga: {e}\n")
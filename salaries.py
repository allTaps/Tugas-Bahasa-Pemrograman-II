nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Apa status Anda? (Pegawai Tetap/Pegawai Honor) " )
golongan = input("Anda termasuk golongan apa? (A/B/C) " )

if status == "Tetap" or status == "tetap":
    gaji = 1000000
    if golongan == "A" or golongan == "a":
        bonus = 200000
    elif golongan == "B" or golongan == "b":
        bonus = 400000
    elif golongan == "C" or golongan == "c":
        bonus = 550000
    else:
        print("Golongan tidak tersedia.")
        exit()
elif status == "Honor" or status == "honor":
    gaji = 750000
    if golongan == "A" or golongan == "a":
        bonus = 150000
    elif golongan == "B" or golongan == "b":
        bonus = 275000
    elif golongan == "C" or golongan == "c":
        bonus = 480000
    else:
        print("Golongan tidak tersedia.")
        exit()
else:
    print("Status tidak tersedia.")
    exit()

gajiTotal = gaji + bonus

print("=== Slip Gaji ===")
print(f"Nama: {nama}")
print(f"NIK: {nik}")
print(f"Gaji Pokok: {gaji}")
print(f"Bonus: {bonus}")
print(f"Gaji Total: {gajiTotal}")

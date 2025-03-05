print("VOLUME TABUNG\n")

radius = float(input("Masukkan nilai jari-jari tabung (dalam cm): "))
tinggi = float(input("Masukkan nilai tinggi tabung (dalam cm): "))
pi = 3.14

volumeTabung = pi * pow(radius, 2) * tinggi

print("Nilai volume tabung dengan jari-jari", radius, "cm dan tinggi", tinggi, "cm =", volumeTabung, "cm")
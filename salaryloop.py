gajiKaryawan = {
    "Tetap": 1000000, 
    "Honor": 750000
    }

bonusGaji = {
    "Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000}
}

statusKaryawan = ["Tetap", "Honor"]
golonganKaryawan = ["A", "B", "C"]

for s in statusKaryawan:
    print("Status:", s)

    for gol in golonganKaryawan:
        tambahanGaji = bonusGaji[s][gol]
        gajiTotal = gajiKaryawan[s] + tambahanGaji

        print("Golongan:", gol)
        print("Bonus:", tambahanGaji)
        print("Gaji Total:", gajiTotal)
        print()

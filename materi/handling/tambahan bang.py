import csv

file_path = r"C:\Users\rieee\Documents\python\handling\jajan.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("SEMUA DATA")
    print("-" * 20)
    for baris in list_read:
        nomor = baris[0]
        nama = baris[1]
        uang_jajan = baris[2]

        print(f"{nomor} | {nama} | {uang_jajan}")

#tambah data
with open(file_path, 'a', newline="") as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["7","fadhil", "18500" ])

import csv

file_path = r"C:\Users\rieee\Documents\python\handling\keuangan.csv"

with open(file_path, 'a', newline="")as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["2025-08-22", "pisang", "makan sore", "5000" ])
with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)
    

    print("- DATA KEUANGAN -")
    print("-"*50)
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori = baris[2]
        jumlah = baris[3]

        print(f"{tanggal} | {keterangan} | {kategori} | {jumlah}")
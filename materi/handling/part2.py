import csv
#tambahkan module "csv" dengan import
print("-------- update csv ---------")
#baca semua file -> ekstrak data -> buat data baru
# tulis ulang semua isi barisnya dengan mode 'w'
# 1. baca seluruh data
file_path_csv = r"C:\Users\rieee\Documents\python\handling\jajan.csv"
# siapkan data jajan kosong untuk menampung data dari csv ke list
data_jajan = []
with open(file_path_csv, "r", newline="") as file_jajan:
    isi_table_jajan = csv.reader(file_jajan)
    #ekstrak semua data dengan for loop
    for item_jajan in isi_table_jajan:
       data_jajan.append(item_jajan)

# 2. mengubah atau membuat data baru
for items in data_jajan:
    print(f"proses item no => {items[0]}")
    print(items)
    #jika kolom nama adalah "x nama"
    if items[1] == "thufail":
        uang_jajan_baru = 15000
        #ganti kolom uang jajan dengan nilai baru
        items[2] = uang_jajan_baru
        print(f"data ditemukan, ganti uang jajan {uang_jajan_baru}")
    print("loop end")

print(f"data jajan terkini: {data_jajan}")

#hapus data di list by index
del data_jajan[2]

print(data_jajan)
# 4. tulis ulang data dengan mode 'w' -> write
with open(file_path_csv, "w", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    # .writerows() -> tulis sekali banyak
    writer.writerows(data_jajan)

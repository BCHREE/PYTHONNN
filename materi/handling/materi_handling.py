import csv


print("materi 10 - File Handling")
print("-------------------------")
# buka file
file_path = r"C:\Users\rieee\Documents\python\handling\pesan.txt"
# baca file
file_pesan = open(file_path, "r")
# baca isi pesan
isi_pesan = file_pesan.read()
# tampilan output isi pesan 
print(f"ISI PESAN => {isi_pesan}")
#tutup file
file_pesan.close()

print('------ READ CSV FILE ------')
print('---------------------------')
file_path_csv = r"C:\Users\rieee\Documents\python\handling\jajan.csv"
file_jajan = open(file_path_csv, "r")
isi_table_jajan = file_jajan.read()
print(f"TABLE JAJAN => {isi_table_jajan}")
file_jajan.close()

print('----- APPEND CSV FILE -----')
print("-------------------------")
jajan_baru = [6,"syahid", 100000]
print(f"jajan baru: {jajan_baru}")
with open(file_path_csv, "a", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    writer.writerow(jajan_baru)

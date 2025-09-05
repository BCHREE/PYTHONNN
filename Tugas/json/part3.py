import json
#tambahkan module "csv" dengan import
print("-------- OPEN JSON FILE ---------")
file_path_json = r"C:\Users\rieee\Documents\python\handling\materi.json"

with open(file_path_json, "r") as file_materi:
    #json load()--> membaca isi file json
    data_materi=json.load(file_materi)
    #akses data json denga 'key' nya
    print(f"judul berkas: {data_materi['title']}")
    print(f"total kelas A: {data_materi['total']}")
    print(f"status santri: {data_materi['status_santri']}")
    print(f"status kelulusan: {data_materi['status_lulus']}")
    #ekstrak data list dengan for loop
    for pelajaran in data_materi['pelajaran']:
        print(f"--> {pelajaran}")

    print("-" * 50)
    print("| NO | Nama Surat | Ayat | Tempat Turun")
    print("-" * 50)
    for surah in data_materi['surah']:
        print(f"| {surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']} |")        
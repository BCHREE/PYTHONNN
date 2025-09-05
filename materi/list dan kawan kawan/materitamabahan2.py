# apa itu Dictionary

harun = {
    'umur': 15,
    'asal': 'bogor',
    'kelas': '10 A'
}
print(harun)

# Operasi pada Dictionary

# 1. mengakses nilainya

print(harun["asal"])

# 2. menambahkan nilai (value)

harun["berat badan"] =  75
print(harun['berat badan'])

# 3. mengubah nilai
harun["berat_badan"] = 65
print(harun)

# 5. mengecek key

print("umur" in harun)

# 6. mendapatkan semua key dan value nya

# cara ngecek ada key apa aja
print(harun.keys())

# cara ngecek ada value apa aja
print(harun.values())

# Looping

for key in harun:
    print(key)

for value in harun.values():
    print(value)

for key, value in harun.items():
    print(f"{key} -> {value}")

# Nested Dictionary

kelas = {
    "siswa1" : {
        'nama' : 'harun',
        'umur' : 24,
        'asal' : 'bogor',
        'hobi' : {
            'hobi1' : 'makan',
            'hobi2' : 'tidur',
            'hobi3' : 'marah marah',
            'hobi4' : {
                'bola1' : 'bola sepak',
                'bola2' : 'bola basket',
                'bola3' : 'bola voli'
            }
        }
    },
    "siswa2" : {
        'nama' : 'junet',
        'umur' : 20,
        'asal' : 'bekasi'
    },
    "siswa3" : {
        'nama' : 'wildan kautsar',
        'umur' : 16,
        'asal' : 'wonosobo'
    }
}
print(kelas, siswa1)
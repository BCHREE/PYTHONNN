#list manipulasi lanjutan
#menggabungkan list dengan +
jajan_ujang = ["pentol", "cireng"]
jajan_asep = ["pempek", "siomay"]
jajan_ujang_dan_asep = jajan_ujang + jajan_asep
print(jajan_ujang_dan_asep)
#list multi dimensi
list_minuman = [
    ["kopi", "susu", "teh"], #baris/index 0
    ["es dawet", "es jeruk", "kelapa"], #baris/index 1
    ["jus apel", "jus alpukat", "cincau"],#baris/index 2
]
print(list_minuman)
print(list_minuman[2][2])

#operasi dasar pada list

# 1. mengakses elemen
list_minuman = ["es duren", "esteh", "jus apel",]
print(list_minuman[2])

# 2. mengubah nilainya
list_minuman[1] = "es jeruk"    
print(list_minuman)

# 3. menambah elemen
# menambah elemen di akhir
list_minuman.append("es coklat",)
print(list_minuman)

# menambah elemen di terserah
list_minuman.insert(0, "es dawet",)
print(list_minuman)
list_minuman.insert(2, "air putih",)

# 4. menghapus elemen
# menghapus berdasarkan isi
list_minuman.remove ("es duren")
print(list_minuman)

# menghapus berdasarkan index
list_minuman.pop(0)
print(list_minuman)

# 5. panjang list
print(len(list_minuman))

# 6. mencetak seluruh isi list menggunakan looping
for item in list_minuman:
    print(item)

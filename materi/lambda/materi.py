#materi function lambada
print("--------===---------")

def say_hello(name):
    #print("halo mr.", name)
    #lasih f di awal string untuk menyisipkan variable/parameter
    print(f"halo mr. {name}")
    print("baek baek ae")

#lambda untuk menulis fungsi yang ringkas dengan 1 baris saja
#string disebut juga fungsi anonim(tanpa nama)

say_hello_mini = lambda name: print(f"halo mr. {name}")

say_hello("azzam")
say_hello("syahid")
print("-------->")
say_hello_mini("wildan")
say_hello_mini("azka")

#contoh penerapan lambda dengan higher-order function
#map() -- sorted() -- filter()
jajan_mingguan = [50000, 30000, 15000, 20000, 40000]
urutkan_uang = sorted(jajan_mingguan)
urutkan_uang_terbalik = sorted(jajan_mingguan, reverse=True)
print(f"urutan uang: {urutkan_uang}")
print(f"urutan uang terbalik: {urutkan_uang_terbalik}")
# map() --> mentranformasi data
kurangin_uang = map(lambda uang: uang - 5000, jajan_mingguan)
#list(mengubah data objek map menjadi bentuk list)
list_kurangin_uang = list(kurangin_uang)
print(f"map uang berkurang: {list_kurangin_uang}")

#filter() menyaring / memfilter data
filter_jajan_banyak = filter(lambda uang: uang > 30000, jajan_mingguan)
list_jajan_banyak = list(filter_jajan_banyak)
print (f"filter jajan di atas 30 ribu: {list_jajan_banyak}") 

#return untuk mengembalikan nilai
def doa_sebelum_makan():
    return"bismillah"

def doa_setelah_makan():
    return"alhamdulillah"

def doa_mandi_wajib():
    return"bismillah waduh kasur basah"
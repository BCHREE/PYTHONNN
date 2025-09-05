#set ---> {} ---> tidak berurutan, berubah, tidak duplikat

game_azka = {"valorant", "roblox", "delta"}
game_zaky = {"minecraft", "roblox"}
game_gabungan = game_azka | game_zaky

print ("daftar game", game_gabungan)
print(game_azka)
print(game_zaky)
game_azka.add("point blank")
print(game_azka)
game_azka.remove("delta")
print(game_azka)

#for (loop) untuk mengeluarkan isi item dari set
for game in game_gabungan:
    print(game)
    print("-----> transfer data", game, "ps 5")

#dictionary (dict) -> {key : value} / {kunci : nilai} -> berurutan, berubah, tidak berurutan
kamus_anime = {
    "one_piece": "Monkey D Luffy",
    "blue_lock": "Isagi ren",
    "demon_slayer":  "Tanjiro",
    "waifu": {
        "one_piece": "big mom",
        "demon_slayer": "nezuko",
    }
}
print("kamus anime : ", kamus_anime)
print("MC demon slayer : ", kamus_anime["demon_slayer"])
print("waifu one piece : ", kamus_anime["waifu"]["one_piece"]) 

# nambah item baru ke dictionary
kamus_anime["naruto"] = "shikamaru"
print("MC naruto:", kamus_anime["naruto"])
# mengubah item dari dictionary
kamus_anime["demon_slayer"] = "zenitsu"
# menghapus item dari dictionary
del(kamus_anime['blue_lock'])
print("kamus anime terbaru: ", kamus_anime)
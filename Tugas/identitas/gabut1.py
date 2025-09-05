("===== PROFIL DIGITAL GW =====")
nama = input("Nama:azka")
umur = int(input("Umur:"))
hitung_umur = 2025 - umur
print("tahun", hitung_umur)
kelas = input("Kelas:1 smp")
hobi = input("Hobi:nonton konser jkt48")
citacita = input("Cita-cita: menjadi wota sukses")
belajar = input("Belajar paling enak pas: malem sih ")

print("\n===== PILIH TIPE GAYA DIGITAL KAMU =====")
print("1. Wibu ")
print("2. Gamer ")
print("3. K-Popers ")
print("4. Anak konten ")
print("5. Anak nongki ")
tipe = input("Pilih tipe digital kamu (1-5): ")
if tipe == "1":
    pertanyaan_tambahan = "Siapa waifu atau husbando kamu?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
elif tipe == "2":
    pertanyaan_tambahan = "Game favorit kamu apa?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
elif tipe == "3":
    pertanyaan_tambahan = "Siapa bias kamu?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
elif tipe == "4":
    pertanyaan_tambahan = "Platform favorit kamu? TikTok? YouTube?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
elif tipe == "5":
    pertanyaan_tambahan = "Nongkrong paling sering di mana?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
else:

    jawaban_tambahan = "Tidak ada jawaban"

pertanyaan = input( "Jawab pertanyaan bonus ini 🤭: ")
print(pertanyaan)
soal = input("apakah teman di sebelah kamu bau?, (iya atau tidak) :")
print(soal)
if soal == "iya":
    print("suruh mandi dulu!!!")
else :
    print("tumben ituu, percaya dah")

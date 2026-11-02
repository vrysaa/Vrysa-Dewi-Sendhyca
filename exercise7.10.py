liburan = {}

while True:
    nama = input("\nSiapa nama Anda? ")

    tempat = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")

    liburan[nama] = tempat

    ulangi = input("Apakah ada orang lain yang ingin mengikuti survei? (ya/tidak): ")

    if ulangi == 'tidak':
        break

print("\n=== HASIL SURVEI LIBURAN IMPIAN ===")

for nama, tempat in liburan.items():
    print(f"{nama.title()} ingin berlibur ke {tempat.title()}.")
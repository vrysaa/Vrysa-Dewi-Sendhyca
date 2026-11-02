tamu = ["lyodra", "iqbal ramadhan", "vanesha", "bunda", "adik"]

for nama in tamu:
    print(f"Halo {nama}, saya ingin mengundang Anda untuk makan malam bersama saya.")

# Tamu yang tidak bisa hadir
tidak_hadir = "lyodra"
print(f"\n{tidak_hadir} tidak bisa hadir untuk makan malam.\n")

# Ganti dengan tamu baru
indeks = tamu.index(tidak_hadir)
tamu[indeks] = "Soekarno"

for nama in tamu:
    print(f"Halo {nama}, saya ingin mengundang Anda untuk makan malam bersama saya.")

#menemukan meja yang lebih besar
print("\nSaya menemukan meja makan yang lebih besar!\n")

tamu.insert(0, "ziva")                # di awal
tamu.insert(2, "hanin")      # di tengah
tamu.append("lana")                # di akhir

for nama in tamu:
    print(f"Halo {nama}, saya ingin mengundang Anda untuk makan malam bersama saya.")

# Meja baru tidak tiba tepat waktu
print("\nMaaf, meja makan baru tidak tiba tepat waktu. Saya hanya bisa mengundang dua orang.\n")

while len(tamu) > 2:
    dihapus = tamu.pop()
    print(f"Maaf {dihapus}, saya tidak bisa mengundang Anda makan malam.")

print()
for nama in tamu:
    print(f"Halo {nama}, Anda tetap diundang untuk makan malam bersama saya.")

# Kosongkan daftar dengan del
del tamu[0]
del tamu[0]

print(f"\nIsi daftar sekarang: {tamu}")
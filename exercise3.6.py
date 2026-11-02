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
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
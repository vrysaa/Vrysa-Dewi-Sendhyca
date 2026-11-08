#menghasilkan angka acak

import random

angka = random.randint(1, 100)

print("Angka acak:", angka)

#memilih nama secara acak

import random

nama = ["vrysa", "lana", "kala", "ren", "windi"]

pilihan = random.choice(nama)

print("Nama yang terpilih:", pilihan)

#mengacak urutan daftar
import random

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(angka)

print("Urutan setelah diacak:", angka)
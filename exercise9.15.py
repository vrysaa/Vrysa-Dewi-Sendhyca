
import random

# Daftar angka dan huruf
lottery_items = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
    "A", "B", "C", "D", "E"
]

# Membuat tiket milik kita
my_ticket = random.sample(lottery_items, 4)

# Membuat tiket pemenang
winning_ticket = random.sample(lottery_items, 4)

# Menghitung jumlah percobaan
attempts = 0

# Mengulang sampai tiket menang
while sorted(my_ticket, key=str) != sorted(winning_ticket, key=str):
    attempts += 1
    winning_ticket = random.sample(lottery_items, 4)

# Menampilkan hasil
print("Tiket saya:", my_ticket)
print("Tiket pemenang:", winning_ticket)
print("Jumlah percobaan sampai menang:", attempts + 1)
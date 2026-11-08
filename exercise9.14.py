
import random

# Membuat daftar angka dan huruf
lottery_items = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
    "A", "B", "C", "D", "E"
]

# Memilih 4 angka atau huruf secara acak
winning_ticket = random.sample(lottery_items, 4)

print("Tiket yang memenangkan hadiah adalah:")
print(winning_ticket)

print("Tiket apa pun yang cocok dengan 4 karakter tersebut akan memenangkan hadiah!")
mountains = ['Mount Everest', 'Mount Fuji', 'Kilimanjaro', 'Mount Elbrus']

# Cetak daftar asli
print(mountains)

# Mengakses elemen dalam daftar
print(mountains[0])
print(mountains[-1])

# Mengubah elemen dalam daftar
mountains[1] = 'K2'
print(mountains)

# Menambahkan elemen di akhir daftar
mountains.append('Mount Fuji')
print(mountains)

# Menambahkan elemen pada posisi tertentu
mountains.insert(1, 'Denali')
print(mountains)

# Menghapus elemen menggunakan del
del mountains[1]
print(mountains)

# Menghapus elemen menggunakan pop()
popped_mountain = mountains.pop()
print(popped_mountain)
print(mountains)

# Menghapus elemen berdasarkan nilainya
mountains.remove('K2')
print(mountains)

# Mengurutkan daftar berdasarkan abjad
mountains.sort()
print(mountains)

# Mengurutkan daftar berdasarkan abjad terbalik
mountains.sort(reverse=True)
print(mountains)

# Menggunakan sorted() tanpa mengubah daftar asli
print(sorted(mountains))
print(mountains)

# Membalik urutan daftar
mountains.reverse()
print(mountains)

# Menghitung jumlah elemen dalam daftar
print(len(mountains))
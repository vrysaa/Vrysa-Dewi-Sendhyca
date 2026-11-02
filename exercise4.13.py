# Membuat tuple berisi lima jenis makanan
foods = ('nasi goreng', 'ayam bakar', 'sate', 'soto', 'gado-gado')

# Mencetak menu awal
print("Menu awal restoran:")

for food in foods:
    print(food)

# Mencoba mengubah salah satu item tuple
# Python akan menghasilkan TypeError
# foods[0] = 'mie goreng'

# Mengubah menu restoran dengan membuat tuple baru
foods = ('mie goreng', 'ayam bakar', 'sate', 'bakso', 'gado-gado')

# Mencetak menu yang telah diperbarui
print("\nMenu restoran yang telah diperbarui:")

for food in foods:
    print(food)
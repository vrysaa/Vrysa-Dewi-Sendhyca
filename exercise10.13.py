import json

# Membuat dictionary
user_info = {}

# Meminta informasi pengguna
user_info['nama'] = input("Siapa namamu? ")
user_info['warna'] = input("Apa warna favoritmu? ")
user_info['makanan'] = input("Apa makanan favoritmu? ")

# Mengubah dictionary menjadi JSON
json_data = json.dumps(user_info)

# Menyimpan JSON ke dalam file
filename = 'user_info.json'

with open(filename, 'w') as file_object:
    file_object.write(json_data)

# Membaca kembali isi file
with open(filename) as file_object:
    contents = file_object.read()

# Mengubah JSON menjadi dictionary
stored_info = json.loads(contents)

# Menampilkan informasi pengguna
print("\nInformasi yang berhasil diingat:")

print(f"Namamu adalah {stored_info['nama']}.")
print(f"Warna favoritmu adalah {stored_info['warna']}.")
print(f"Makanan favoritmu adalah {stored_info['makanan']}.")
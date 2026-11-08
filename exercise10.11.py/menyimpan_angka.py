import json

number = input("Berapa angka favoritmu? ")

filename = 'favorite_number.json'

with open(filename, 'w') as file_object:
    json.dump(number, file_object)

print("Angka favoritmu berhasil disimpan!")
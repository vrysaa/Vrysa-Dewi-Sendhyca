import json

filename = 'favorite_number.json'

with open(filename) as file_object:
    number = json.load(file_object)

print(f"Aku tahu angka favoritmu! Angkanya adalah {number}.")
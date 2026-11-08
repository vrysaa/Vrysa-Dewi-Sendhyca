import json

filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        number = json.load(file_object)

except FileNotFoundError:
    number = input("Berapa angka favoritmu? ")

    with open(filename, 'w') as file_object:
        json.dump(number, file_object)

    print("Kami akan mengingat angka favoritmu!")

else:
    print(f"Aku tahu angka favoritmu! Angkanya adalah {number}.")
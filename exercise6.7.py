orang1 = {
    'first_name': 'Vrysa',
    'last_name': 'Sendhyca',
    'age': 17,
    'city': 'Boyolali'
}

orang2 = {
    'first_name': 'Fazyalana',
    'last_name': 'Titananda',
    'age': 19,
    'city': 'Boyolali'
}

orang3 = {
    'first_name': 'Hanin',
    'last_name': 'Tsakila',
    'age': 18,
    'city': 'Semarang'
}

people = [orang1, orang2, orang3]

for orang in people:
    print("\nInformasi Orang:")
    print("Nama depan:", orang['first_name'])
    print("Nama belakang:", orang['last_name'])
    print("Usia:", orang['age'])
    print("Kota:", orang['city'])
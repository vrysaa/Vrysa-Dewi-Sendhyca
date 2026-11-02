angka_favorit = {
    'vrysa': [1, 5, 7],
    'lana': [3, 8],
    'arsa': [2, 4, 9],
    'hanin': [7, 10],
    'mareta': [11, 15, 20]
}

for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama.title()}:")
    for nomor in angka:
        print(nomor)
tempat_favorit = {
    'Vrysa' : ['bali', 'bandung', 'raja ampat'],
    'Lana' : ['swis', 'yogyakarta'],
    'Yelsa' : ['lombok', 'surakarta', 'malang']
}

for nama, tempat in tempat_favorit.items():
    print(f"\nTempat favorite {nama.title()}:")
    for lokasi in tempat:
        print("-", lokasi)
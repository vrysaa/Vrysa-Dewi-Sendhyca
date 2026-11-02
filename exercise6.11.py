kota = {
    'surakarta': {
        'negara': 'Indonesia',
        'populasi': '522.364 jiwa',
        'fact': 'Dikenal sebagai Kota Batik.'
    },

    'tokyo': {
        'negara': 'Jepang',
        'populasi': 'Sekitar 14 juta jiwa',
        'fact': 'Memiliki menara Tokyo Tower.'
    },

    'paris': {
        'negara': 'Prancis',
        'populasi': 'Sekitar 2 juta jiwa',
        'fact': 'Terkenal dengan Menara Eiffel.'
    }
}

for nama_kota, informasi in kota.items():
    print(f"\nNama Kota: {nama_kota.title()}")
    print("Negara:", informasi['negara'])
    print("Populasi:", informasi['populasi'])
    print("Fakta:", informasi['fact'])
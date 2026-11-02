bahasa_favorit = {
    'vrysa': 'python',
    'lana': 'java',
    'arsa': 'c++',
    'hanin': 'python',
    'mareta': 'javascript'
}

orang = ['vrysa', 'lana', 'budi', 'andi', 'mareta', 'rudi']

for nama in orang:
    if nama in bahasa_favorit:
        print(f"Terima kasih, {nama.title()}, sudah mengikuti survei")
    else:
        print(f"{nama.title()}, silakan ikuti survei kami")
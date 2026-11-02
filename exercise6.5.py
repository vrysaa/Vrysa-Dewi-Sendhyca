sungai = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'yangtze': 'china'
}

#menampilkan sungai dan negara yang dilalui
for nama_sungai, negara in sungai.items():
    print(f"Sungai {nama_sungai.title()} mengalir melalui {negara.title()}.")

#menampilkan nama tiap sungai
print("\nDaftar sungai:")
for nama_sungai in sungai.keys():
    print(nama_sungai.title())

#menamilkan nama tiap negara
print("\nDaftar negara:")
for negara in sungai.keys():
    print(negara.title())
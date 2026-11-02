hewan1 = {
    'jenis': 'kucing',
    'pemilik': 'Vrysa'
}

hewan2 = {
    'jenis': 'anjing',
    'pemilik': 'Lana'
}

hewan3 = {
    'jenis': 'kelinci',
    'pemilik': 'Arsa'
}

pets = [hewan1, hewan2, hewan3]

for hewan in pets:
    print("\nInformasi Hewan Peliharaan:")
    print("Jenis hewan:", hewan['jenis'])
    print("Nama pemilik:", hewan['pemilik'])
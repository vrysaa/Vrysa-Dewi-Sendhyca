hewan1 = {
    'jenis': 'kucing',
    'pemilik': 'Vrysa',
    'umur': 2,
    'makanan': 'ikan'
}

hewan2 = {
    'jenis': 'anjing',
    'pemilik': 'Lana',
    'umur': 3,
    'makanan': 'daging'
}

hewan3 = {
    'jenis': 'kelinci',
    'pemilik': 'Arsa',
    'umur': 1,
    'makanan': 'wortel'
}

pets = [hewan1, hewan2, hewan3]

for hewan in pets:
    print("\n=== DATA HEWAN PELIHARAAN ===")
    print("Jenis hewan:", hewan['jenis'].title())
    print("Nama pemilik:", hewan['pemilik'])
    print("Umur:", hewan['umur'], "tahun")
    print("Makanan favorit:", hewan['makanan'])
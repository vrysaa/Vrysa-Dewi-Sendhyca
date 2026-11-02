sandwich_orders = [
    'tuna',
    'pastrami',
    'ayam',
    'pastrami',
    'keju',
    'pastrami',
    'telur'
]

finished_sandwiches = []

print("Maaf, stok pastrami di deli sudah habis.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Saya telah membuat roti lapis {sandwich} Anda.")

    finished_sandwiches.append(sandwich)

print("\nSemua roti lapis yang telah dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich.title())
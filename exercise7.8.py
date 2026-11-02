sandwich_orders = ['tuna', 'ayam', 'keju', 'telur']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Saya telah membuat roti lapis {sandwich} Anda.")

    finished_sandwiches.append(sandwich)

print("\nSemua roti lapis telah selesai dibuat:")

for sandwich in finished_sandwiches:
    print(sandwich.title())
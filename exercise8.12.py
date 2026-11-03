def make_sandwich(*ingredients):
    print("\nSandwich yang dipesan berisi:")
    for ingredient in ingredients:
        print("- " + ingredient)


# Memanggil fungsi sebanyak tiga kali
make_sandwich("Roti", "Keju", "Selada")

make_sandwich("Roti", "Daging", "Keju", "Tomat", "Saus")

make_sandwich("Roti", "Telur", "Mayones", "Selada", "Timun", "Keju")
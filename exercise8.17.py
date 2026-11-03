#program city names

def city_country(city, country):
    """Mengembalikan nama kota dan negara."""
    return f"{city}, {country}"


print(city_country("Santiago", "Chile"))
print(city_country("Jakarta", "Indonesia"))
print(city_country("Tokyo", "Japan"))

#Program album

def make_album(artist, title, songs=None):
    """Membuat dictionary yang berisi informasi album."""
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


album1 = make_album("Taylor Swift", "Midnights")
album2 = make_album("Adele", "25")
album3 = make_album("Bruno Mars", "24K Magic", 9)

print(album1)
print(album2)
print(album3)

#program sandwich

def make_sandwich(*ingredients):
    """Menampilkan daftar bahan sandwich yang dipesan."""
    print("\nSandwich yang dipesan berisi:")

    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich("Roti", "Keju", "Selada")

make_sandwich(
    "Roti",
    "Daging",
    "Keju",
    "Tomat"
)

make_sandwich(
    "Roti",
    "Telur",
    "Mayones",
    "Selada",
    "Timun"
)
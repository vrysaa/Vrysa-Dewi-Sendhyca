
def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


# Membuat tiga album berbeda
album1 = make_album("Taylor Swift", "Midnights")
album2 = make_album("Adele", "25")
album3 = make_album("Ed Sheeran", "Divide")

# Membuat album dengan jumlah lagu
album4 = make_album("Bruno Mars", "24K Magic", 9)

# Mencetak hasil
print(album1)
print(album2)
print(album3)
print(album4)

def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


while True:
    print("\nMasukkan informasi album:")
    print("(Ketik 'quit' untuk keluar)")

    artist = input("Nama artis: ")

    if artist == "quit":
        break

    title = input("Judul album: ")

    if title == "quit":
        break

    album = make_album(artist, title)

    print(album)

print("Terima kasih!")
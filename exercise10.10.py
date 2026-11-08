filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()

except FileNotFoundError:
    print(f"File {filename} tidak ditemukan.")

else:
    word = 'the'
    count = contents.lower().count(word)

    print(f"Kata '{word}' muncul sebanyak {count} kali.")

    word = 'the '
    count = contents.lower().count(word)

    print(f"Kata '{word}' muncul sebanyak {count} kali.")
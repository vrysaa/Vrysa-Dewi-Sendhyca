#menggunakan pengujian kondisional dalam while
pesan = ""

while pesan != 'quit':
    pesan = input("Masukkan topping pizza (quit untuk keluar): ")

    if pesan != 'quit':
        print(f"Topping {pesan} ditambahkan ke pizza!")

#menggunakan variabel penanda(flag)
aktif = True

while aktif:
    topping = input("Masukkan topping pizza (quit untuk keluar): ")

    if topping == 'quit':
        aktif = False
    else:
        print(f"Topping {topping} ditambahkan ke pizza!")

#menggunakan break 
while True:
    topping = input("Masukkan topping pizza (quit untuk keluar): ")

    if topping == 'quit':
        break

    print(f"Topping {topping} ditambahkan ke pizza!")
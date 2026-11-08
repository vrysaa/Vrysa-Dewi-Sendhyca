while True:
    try:
        number1 = input("Masukkan angka pertama (atau 'q' untuk keluar): ")

        if number1 == 'q':
            break

        number2 = input("Masukkan angka kedua: ")

        number1 = int(number1)
        number2 = int(number2)

        result = number1 + number2
        print(f"Hasil penjumlahan: {result}")

    except ValueError:
        print("Maaf, kamu harus memasukkan angka!")
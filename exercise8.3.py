def make_shirt(size, message):
    print(f"Ukuran kaos : {size}")
    print(f"Tulisan pada kaos : {message}")

# Memanggil fungsi menggunakan positional arguments(argumen berdasar urutan)
make_shirt("L", "Tetap Semangat!")

#memanggil fungsi menggunakan keyword arguments(argumen berdasar nama parameter)
make_shirt(size="M", message="Jangan Menyerah!")
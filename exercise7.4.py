while True:
    topping = input("Masukkan topping yang diinginkan:")

    if topping == 'quit':
        break
    else:
        print(f"Topping {topping} akan ditambahkan ke pizza Anda!")

print("Terima kasih sudah memesan pizza!")
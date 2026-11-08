filename = 'guest_book.txt'

while True:
    name = input("Please enter your name: ")

    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")

            print(f"Hello, {name}!")
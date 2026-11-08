import json

def get_stored_username():
    filename = 'username.json'

    try:
        with open(filename) as file_object:
            username = json.load(file_object)

    except FileNotFoundError:
        return None

    else:
        return username


def get_new_username():
    username = input("Siapa namamu? ")

    filename = 'username.json'

    with open(filename, 'w') as file_object:
        json.dump(username, file_object)

    return username


def greet_user():
    username = get_stored_username()

    if username:
        correct = input(
            f"Apakah nama pengguna ini benar, {username}? (ya/tidak): "
        )

        if correct.lower() == 'ya':
            print(f"Selamat datang kembali, {username}!")

        else:
            username = get_new_username()
            print(f"Kami akan mengingatmu, {username}!")

    else:
        username = get_new_username()
        print(f"Kami akan mengingatmu, {username}!")


greet_user()
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin! Apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {username}! Terima kasih telah masuk kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")
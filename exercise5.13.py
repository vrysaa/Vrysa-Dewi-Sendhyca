#APLIKASI DAFTAR TUGAS (TO-DO-LIST)
tasks = []

while True:
    print("\n=== APLIKASI TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Lihat Daftar Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        tugas = input("Masukkan tugas baru: ")
        tasks.append(tugas)
        print("Tugas berhasil ditambahkan!")

    elif pilihan == '2':
        if tasks:
            print("\nDaftar Tugas:")
            for i, tugas in enumerate(tasks, start=1):
                print(f"{i}. {tugas}")
        else:
            print("Belum ada tugas.")

    elif pilihan == '3':
        if tasks:
            for i, tugas in enumerate(tasks, start=1):
                print(f"{i}. {tugas}")

            nomor = int(input("Nomor tugas yang selesai: "))

            if 1 <= nomor <= len(tasks):
                print(f"Tugas '{tasks[nomor - 1]}' selesai!")
                tasks[nomor - 1] += " (Selesai)"
            else:
                print("Nomor tugas tidak ditemukan.")
        else:
            print("Belum ada tugas.")

    elif pilihan == '4':
        if tasks:
            for i, tugas in enumerate(tasks, start=1):
                print(f"{i}. {tugas}")

            nomor = int(input("Nomor tugas yang ingin dihapus: "))

            if 1 <= nomor <= len(tasks):
                tugas_dihapus = tasks.pop(nomor - 1)
                print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")
            else:
                print("Nomor tugas tidak ditemukan.")
        else:
            print("Belum ada tugas.")

    elif pilihan == '5':
        print("Terima kasih telah menggunakan To-Do List!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
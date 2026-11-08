
class User:
    def __init__(self, first_name, last_name, age, address, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.job = job

    def describe_user(self):
        print("Informasi Pengguna:")
        print(f"Nama depan: {self.first_name}")
        print(f"Nama belakang: {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Alamat: {self.address}")
        print(f"Pekerjaan: {self.job}")

    def greet_user(self):
        print(f"Halo, {self.first_name} {self.last_name}!")
        print("Selamat datang kembali!")


# Membuat beberapa instans pengguna
user1 = User("Andi", "Saputra", 20, "Surakarta", "Mahasiswa")
user2 = User("Budi", "Santoso", 25, "Yogyakarta", "Programmer")
user3 = User("Siti", "Aminah", 22, "Semarang", "Guru")

# Pengguna pertama
user1.describe_user()
user1.greet_user()

print()

# Pengguna kedua
user2.describe_user()
user2.greet_user()

print()

# Pengguna ketiga
user3.describe_user()
user3.greet_user()
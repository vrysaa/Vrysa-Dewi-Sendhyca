class User:
    def __init__(self, first_name, last_name, age, address, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.job = job
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Membuat instans pengguna
user = User("Andi", "Saputra", 20, "Surakarta", "Mahasiswa")

# Menampilkan jumlah login awal
print("Jumlah ercobaan login awal:", user.login_attempts)

# Menambah percobaan login beberapa kali
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Menampilkan jumlah percobaan login
print("Jumlah percobaan login sekarang:", user.login_attempts)

# Mengatur ulang jumlah percobaan login
user.reset_login_attempts()

# Menampilkan hasil setelah direset
print("Jumlah percobaan login setelah reset:", user.login_attempts)
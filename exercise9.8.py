
class User:
    def __init__(self, first_name, last_name, age, address, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.job = job

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Alamat: {self.address}")
        print(f"Pekerjaan: {self.job}")


class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can edit user"
        ]

    def show_privileges(self):
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, address, job):
        super().__init__(first_name, last_name, age, address, job)
        self.privileges = Privileges()


# Membuat instans Admin
admin = Admin("Andi", "Saputra", 25, "Surakarta", "Administrator")

# Menampilkan informasi pengguna
admin.describe_user()

# Menampilkan hak akses
admin.privileges.show_privileges()
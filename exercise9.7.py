
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


class Admin(User):
    def __init__(self, first_name, last_name, age, address, job):
        super().__init__(first_name, last_name, age, address, job)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Membuat instans Admin
admin = Admin("Andi", "Saputra", 25, "Surakarta", "Administrator")

# Menampilkan informasi dan hak akses
admin.describe_user()
admin.show_privileges()

from admin import Admin

# Membuat instans Admin
admin = Admin("Andi", "Saputra", 25, "Surakarta", "Administrator")

# Menampilkan informasi pengguna
admin.describe_user()

# Menampilkan hak akses administrator
admin.privileges.show_privileges()
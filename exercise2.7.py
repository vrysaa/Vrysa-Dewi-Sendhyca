#menghapus karakter spasi dari nama
nama = "\t\n Vrysa Dewi Sendhyca \t\n"

print("=== Nama Asli (dengan spasi, tab, dan newline) ===")
print(nama)

print("=== menggunakan lstrip() (menghapus spasi/karakter kosong di kiri) ===")
print(nama.lstrip())

print("=== menggunakan rsrtip() (menghapus spasi/karakter kosong di kanan) ===")
print(nama.rstrip())

print("=== menggunakan strip() (menghapus spasi/karakter kosong di kedua sisi) ===")
print(nama.strip())
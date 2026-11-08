class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

#membuat instans restoran
restaurant = Restaurant("warung padang", "masakan padang")

#mecetak jml pelanggan awal
print("Jumlah pelanggan awal:", restaurant.number_served)

#mengubah jml pelanggan secara langsung
restaurant.set_number_served(25)
print("Jumlah pelanggan setelah menggunakan metode set:", restaurant.number_served)

#menambah jml pelanggan
restaurant.increment_number_served(50)
print("Jumlah pelannggan setelah ditambah:", restaurant.number_served)